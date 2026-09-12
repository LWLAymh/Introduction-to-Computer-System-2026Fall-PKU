# -*- coding: utf-8 -*-
"""抽取策略：中文正文定锚行 + 远离锚行的碎片自成一行的兜底。"""
import io
import os
import re
import warnings
from collections import Counter

warnings.filterwarnings("ignore")
import pdfplumber

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(REPO, "往年题")
OUT = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(SRC, "期中", "2019期中-带答案.pdf")
PAGES = [2, 3, 4]

CJK = re.compile(r"[　-鿿＀-￯]")


def cluster_lines(cs, tol=1.0):
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


def anchor_text(pg, gap_k=0.35):
    chars = list(pg.chars)
    if not chars:
        return ""

    # 1) 锚定字体 = 承载中文最多的字体
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

    # 2) 行距估计
    gaps = [b - a for a, b in zip(reps, reps[1:]) if b - a > 2]
    pitch = sorted(gaps)[len(gaps) // 2] if gaps else 12.0
    thr = 0.5 * pitch

    # 3) 其它字体的碎片，离任何锚行都远 -> 自成一锚
    others = [c for c in chars if c["fontname"] != af]
    for ln in cluster_lines(others):
        r = rep(ln)
        if min(abs(r - x) for x in reps) > thr:
            reps.append(r)
    reps.sort()

    # 4) 全部字符就近归行
    buckets = [[] for _ in reps]
    for c in chars:
        i = min(range(len(reps)), key=lambda k: abs(c["bottom"] - reps[k]))
        buckets[i].append(c)

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


if __name__ == "__main__":
    with pdfplumber.open(PDF) as pdf:
        buf = []
        for pno in PAGES:
            buf.append("<!-- page %d -->" % pno)
            buf.append(anchor_text(pdf.pages[pno - 1]))
        io.open(os.path.join(OUT, "_probe_anchor3.txt"), "w",
                encoding="utf-8").write("\n".join(buf))
        print("ok")
