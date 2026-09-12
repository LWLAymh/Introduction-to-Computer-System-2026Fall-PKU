# -*- coding: utf-8 -*-
"""诊断：每页各字体的字符数，以及按“主字体”聚出的锚行是否合理。"""
import io
import os
import warnings
from collections import Counter

warnings.filterwarnings("ignore")
import pdfplumber

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(REPO, "往年题")
OUT = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(SRC, "期中", "2019期中-带答案.pdf")


def cluster_lines(cs, tol):
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


with pdfplumber.open(PDF) as pdf:
    for pno in (2, 3):
        pg = pdf.pages[pno - 1]
        chars = list(pg.chars)
        cnt = Counter(c["fontname"].split("+")[-1] for c in chars)
        buf = ["===== page %d  (%d chars) =====" % (pno, len(chars))]
        for f, n in cnt.most_common():
            fc = [c for c in chars if c["fontname"].split("+")[-1] == f]
            buf.append("  font %-18s chars=%4d  ->  %2d lines"
                       % (f, n, len(cluster_lines(fc, 1.0))))
        # 主字体锚行
        dom = Counter(c["fontname"] for c in chars).most_common(1)[0][0]
        buf.append("  DOMINANT = %s" % dom)
        for ln in cluster_lines([c for c in chars if c["fontname"] == dom], 1.0):
            ln.sort(key=lambda c: c["x0"])
            buf.append("    bottom=%8.2f n=%3d | %s"
                       % (ln[0]["bottom"], len(ln),
                          "".join(c["text"] for c in ln)[:55]))
        io.open(os.path.join(OUT, "_diag_%d.txt" % pno), "w",
                encoding="utf-8").write("\n".join(buf))
        print("wrote page", pno)
