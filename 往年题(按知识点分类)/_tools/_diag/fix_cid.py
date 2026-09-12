# -*- coding: utf-8 -*-
"""修补 (cid:N) 残留。

个别 PDF（如 2014期中）的 SimSun 子集字体 ToUnicode 缺失，抽取后中文变成
(cid:NNN)。这类字体是 Identity-H 编码，CID 即 GID；字体本身嵌在 PDF 里，
把它的 cmap（unicode -> GID）反过来就能还原。

用法: python fix_cid.py            # 就地修补 原文/ 下所有 md
"""
import io
import os
import re
import glob
import warnings

warnings.filterwarnings("ignore")

from fontTools.ttLib import TTFont
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
REPO = os.path.dirname(BASE)
SRC = os.path.join(REPO, "往年题")
MD = os.path.join(BASE, "原文")

CID = re.compile(r"\(cid:(\d+)\)")


def cmap_inverted(data):
    """TTF 字节 -> {gid: char}"""
    try:
        f = TTFont(io.BytesIO(data), fontNumber=0, lazy=True)
    except Exception:
        return {}
    best = None
    for t in f["cmap"].tables:
        if t.isUnicode():
            best = t
            if t.platformID == 3:
                break
    if best is None:
        return {}
    inv = {}
    for cp, gid in best.cmap.items():
        inv.setdefault(gid, chr(cp))
    return inv


def font_maps(pdf_path):
    """{字体全名: {gid: char}}，含去掉子集前缀的短名。"""
    maps = {}
    try:
        fp = open(pdf_path, "rb")
        doc = PDFDocument(PDFParser(fp))
    except Exception:
        return maps
    seen = set()
    for page in PDFPage.create_pages(doc):
        for _k, v in (page.resources.get("Font") or {}).items():
            try:
                f = v.resolve()
            except Exception:
                continue
            bf = str(f.get("BaseFont") or "")
            if bf in seen:
                continue
            seen.add(bf)
            df = f.get("DescendantFonts")
            if df is None:
                continue
            try:
                d = (df[0].resolve() if hasattr(df, "__getitem__")
                     else df.resolve()[0].resolve())
                fd = d.get("FontDescriptor")
                fd = fd.resolve() if fd else {}
                ff = fd.get("FontFile2")
                if not ff:
                    continue
                inv = cmap_inverted(ff.resolve().get_data())
            except Exception:
                continue
            if inv:
                maps[bf] = inv
                maps[bf.split("+")[-1]] = inv
    return maps


def main():
    total = 0
    for f in sorted(glob.glob(os.path.join(MD, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(f, MD).replace(os.sep, "/")
        text = io.open(f, encoding="utf-8").read()
        n = len(CID.findall(text))
        if not n:
            continue
        # 找对应的源 PDF
        pdf = os.path.join(SRC, os.path.splitext(rel)[0] + ".pdf")
        if not os.path.exists(pdf):
            print("  no pdf for", rel)
            continue
        maps = font_maps(pdf)
        # 合并所有字体的映射（同 GID 冲突时先到先得）
        merged = {}
        for m in maps.values():
            for g, ch in m.items():
                merged.setdefault(g, ch)

        def sub(mo):
            return merged.get(int(mo.group(1)), mo.group(0))

        fixed = CID.sub(sub, text)
        left = len(CID.findall(fixed))
        io.open(f, "w", encoding="utf-8").write(fixed)
        print("%-46s cid %5d -> %5d  (字体表 %d)" % (rel, n, left, len(maps)))
        total += n - left
    print("\n共还原", total, "处")


if __name__ == "__main__":
    main()
