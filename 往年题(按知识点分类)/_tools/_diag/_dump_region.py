# -*- coding: utf-8 -*-
"""临时诊断：打印指定文件里含关键词的行及其上下文。"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(BASE, "原文")

targets = [
    ("期末/2014期末-带答案.md", r"第二题"),
    ("期末/2015期末-20160104-带答案.md", r"第二题"),
    ("期中/2012期中-带答案.md", r"Problem A"),
]
out = []
for rel, pat in targets:
    p = os.path.join(MD, rel.replace("/", os.sep))
    lines = io.open(p, encoding="utf-8").read().splitlines()
    hits = [i for i, l in enumerate(lines) if re.search(pat, l)]
    out.append("=" * 70)
    out.append("%s  共 %d 行，命中 %s 于 %s" % (rel, len(lines), pat, hits[:6]))
    out.append("=" * 70)
    if hits:
        a = hits[0]
        for i in range(max(0, a - 2), min(len(lines), a + 55)):
            out.append("%5d| %s" % (i + 1, lines[i][:110]))
    out.append("")
io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_region.txt"),
        "w", encoding="utf-8").write("\n".join(out))
print("ok")
