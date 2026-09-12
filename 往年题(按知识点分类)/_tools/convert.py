#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""往年题 PDF/DOCX -> Markdown 批量转换。

为什么不用 pdftotext：这批 PDF 内嵌 CID 子集字体、ToUnicode 不规范，
pdftotext 抽不出中文；pdfplumber/pdfminer 可以，但要自己重建阅读顺序。

阅读顺序重建（anchor 法）：
  这批 Word 导出的 PDF 里，中文和拉丁文字是两个独立的文字层，同一视觉行的
  baseline 相差约 5.7pt，而行距约 15.6pt——所以任何固定容差都不安全。
  做法是：取“承载中文最多的字体”的中文行作为锚行，再把其它字符按 baseline
  就近归行；离所有锚行都远的碎片（纯拉丁的选项行、代码行）自成一锚。
"""
import os
import re
import json
import glob
import shutil
import tempfile
import warnings
import subprocess
from collections import Counter

warnings.filterwarnings("ignore")

import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)                 # 往年题(按知识点分类)
REPO = os.path.dirname(BASE)
SRC = os.path.join(REPO, "往年题")
MD = os.path.join(BASE, "原文")
ASSETS = os.path.join(BASE, "assets")

DPI = 130
SCAN_CPP = 80            # 每页字符数低于此值 -> 视为扫描件，整本渲染
CJK = re.compile(r"[　-鿿＀-￯]")

manifest = {}


def cluster_lines(cs, tol=1.0):
    """按 baseline 聚成行（leader 聚类，足够应付等宽中文）。"""
    cs = sorted(cs, key=lambda c: c["bottom"])
    lines, cur, last = [], [], None
    for c in cs:
        b = c["bottom"]
        if last is None or abs(b - last) <= tol:
            cur.append(c)
            if last is None:
                last = b
        else:
            lines.append(cur)
            cur = [c]
            last = b
    if cur:
        lines.append(cur)
    return lines


def rep(ln):
    return sorted(c["bottom"] for c in ln)[len(ln) // 2]


def page_text(pg, gap_k=0.35):
    chars = list(pg.chars)
    if not chars:
        return ""

    cjk_cnt, tot_cnt = Counter(), Counter()
    for c in chars:
        tot_cnt[c["fontname"]] += 1
        if CJK.match(c["text"]):
            cjk_cnt[c["fontname"]] += 1
    af = (max(cjk_cnt, key=lambda f: (cjk_cnt[f], tot_cnt[f]))
          if cjk_cnt else max(tot_cnt, key=tot_cnt.get))

    anchors = cluster_lines([c for c in chars if c["fontname"] == af])
    if not anchors:
        anchors = cluster_lines(chars)
    reps = sorted(rep(ln) for ln in anchors)

    gaps = [b - a for a, b in zip(reps, reps[1:]) if b - a > 2]
    pitch = sorted(gaps)[len(gaps) // 2] if gaps else 12.0
    thr = 0.5 * pitch

    for ln in cluster_lines([c for c in chars if c["fontname"] != af]):
        r = rep(ln)
        if min(abs(r - x) for x in reps) > thr:
            reps.append(r)
    reps.sort()

    buckets = [[] for _ in reps]
    for c in chars:
        buckets[min(range(len(reps)),
                    key=lambda k: abs(c["bottom"] - reps[k]))].append(c)

    frag = []
    for ln in buckets:
        ln.sort(key=lambda c: c["x0"])
        s, prev = "", None
        for c in ln:
            if prev is not None and (c["x0"] - prev["x1"]) > gap_k * c["size"]:
                s += " "
            s += c["text"]
            prev = c
        if s.strip():
            frag.append(s.rstrip())
    return "\n".join(frag)


def save_jpeg(stream, path):
    f = stream.get("Filter")
    if isinstance(f, list):
        f = f[-1]
    name = getattr(f, "name", str(f) if f else "").lstrip("/")
    if name != "DCTDecode":
        return None
    try:
        with open(path, "wb") as fh:
            fh.write(stream.get_rawdata())
        return path
    except Exception:
        return None


def render_page(pdf, page_no, out_png):
    tmp = tempfile.mkdtemp()
    try:
        subprocess.run(
            ["pdftoppm", "-f", str(page_no), "-l", str(page_no),
             "-r", str(DPI), "-png", pdf, os.path.join(tmp, "pg")],
            check=True, capture_output=True)
        got = glob.glob(os.path.join(tmp, "pg*.png"))
        if not got:
            return None
        shutil.move(got[0], out_png)
        return out_png
    except Exception:
        return None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def convert_pdf(rel):
    src = os.path.join(SRC, rel)
    dst = os.path.join(MD, os.path.splitext(rel)[0] + ".md")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    stem = os.path.splitext(os.path.basename(rel))[0]
    adir = os.path.join(ASSETS, os.path.dirname(rel), stem)

    pages, fig_pages = [], []

    with pdfplumber.open(src) as pdf:
        npages = len(pdf.pages)
        for i, pg in enumerate(pdf.pages, 1):
            txt = page_text(pg)
            if pg.images:
                fig_pages.append(i)
                os.makedirs(adir, exist_ok=True)
                imgs = sorted(pg.images,
                              key=lambda im: (round(im["top"], 1), round(im["x0"], 1)))
                links = []
                for n, im in enumerate(imgs, 1):
                    p = os.path.join(adir, "p%d-img%d.jpg" % (i, n))
                    if save_jpeg(im["stream"], p):
                        links.append(os.path.relpath(p, os.path.dirname(dst))
                                     .replace(os.sep, "/"))
                if links:
                    txt += "\n\n" + "\n".join("![图](%s)" % l for l in links)
            pages.append((i, txt))

    scanned = npages and (sum(len(p[1]) for p in pages) / npages) < SCAN_CPP
    render_pages = list(range(1, npages + 1)) if scanned else fig_pages
    if render_pages:
        os.makedirs(adir, exist_ok=True)
        for pno in render_pages:
            render_page(src, pno, os.path.join(adir, "page-%02d.png" % pno))

    buf = ["# %s" % stem, "",
           "> 来源：`往年题/%s`　共 %d 页%s"
           % (rel, npages, "　**扫描件**，正文需人工誊写" if scanned else ""), ""]
    for pno, txt in pages:
        buf += ["<!-- ===== page %d ===== -->" % pno, "", txt, ""]
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write("\n".join(buf))

    manifest[rel] = {"md": os.path.relpath(dst, BASE).replace(os.sep, "/"),
                     "pages": npages,
                     "chars": sum(len(p[1]) for p in pages),
                     "scanned": bool(scanned),
                     "figure_pages": fig_pages}
    return manifest[rel]


def convert_docx(rel):
    src = os.path.join(SRC, rel)
    dst = os.path.join(MD, os.path.splitext(rel)[0] + ".md")
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    # 用源目录当 cwd，让 --extract-media 产生相对路径，再整体搬到 assets
    tmp_media = os.path.join(os.path.dirname(src), "_media_tmp")
    cmd = ["pandoc", "-f", "docx", "-t", "gfm", "--wrap=none",
           "--extract-media=" + os.path.basename(tmp_media),
           os.path.basename(src), "-o", dst]
    r = subprocess.run(cmd, cwd=os.path.dirname(src), capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[:300])

    body = open(dst, encoding="utf-8").read()
    if os.path.isdir(tmp_media):
        tgt = os.path.join(ASSETS, os.path.dirname(rel),
                           os.path.splitext(os.path.basename(rel))[0])
        if os.path.exists(tgt):
            shutil.rmtree(tgt, ignore_errors=True)
        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        shutil.move(tmp_media, tgt)
        rel_media = os.path.relpath(tgt, os.path.dirname(dst)).replace(os.sep, "/")
        body = body.replace(os.path.basename(tmp_media) + "/", rel_media + "/")
        open(dst, "w", encoding="utf-8").write(body)
        # pandoc 会在源目录留下空目录或 media 目录，清掉
        leftover = os.path.join(os.path.dirname(src), "media")
        if os.path.isdir(leftover):
            shutil.rmtree(leftover, ignore_errors=True)

    manifest[rel] = {"md": os.path.relpath(dst, BASE).replace(os.sep, "/"),
                     "chars": len(body), "kind": "docx"}
    return manifest[rel]


def main():
    os.makedirs(MD, exist_ok=True)
    os.makedirs(ASSETS, exist_ok=True)

    for p in sorted(glob.glob(os.path.join(SRC, "**", "*.pdf"), recursive=True)):
        rel = os.path.relpath(p, SRC).replace(os.sep, "/")
        if os.path.basename(rel) == "期末往年题勘误、详解 by Arthals.pdf":
            continue                       # 已有 .md 源
        try:
            info = convert_pdf(rel)
            print("PDF  %3dp %6dch%s %s"
                  % (info["pages"], info["chars"],
                     "  [SCAN]" if info["scanned"] else "", rel), flush=True)
        except Exception as e:
            print("FAIL", rel, type(e).__name__, str(e)[:150], flush=True)

    for d in sorted(glob.glob(os.path.join(SRC, "**", "*.docx"), recursive=True)):
        rel = os.path.relpath(d, SRC).replace(os.sep, "/")
        try:
            convert_docx(rel)
            print("DOCX %s" % rel, flush=True)
        except Exception as e:
            print("FAIL", rel, type(e).__name__, str(e)[:150], flush=True)

    for pat in ("**/*.c", "**/*.h", "**/*.sh", "**/*.md"):
        for f in glob.glob(os.path.join(SRC, pat), recursive=True):
            dst = os.path.join(MD, os.path.relpath(f, SRC))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(f, dst)

    with open(os.path.join(MD, "_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    print("\nDONE", len(manifest), "files")


if __name__ == "__main__":
    main()
