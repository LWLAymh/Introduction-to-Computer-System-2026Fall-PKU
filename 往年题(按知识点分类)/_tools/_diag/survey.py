# -*- coding: utf-8 -*-
"""摸底：各年份试卷里的『大题/知识点』标注长什么样，用来设计分类器。"""
import io
import os
import re
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
MD = os.path.join(BASE, "原文")

PAT_SECTION = re.compile(r"^\s*[（(][^）)]{2,24}[）)]\s*$")          # （链接）
PAT_BIG = re.compile(r"^\s*[一二三四五六七八九十]+\s*[、.．]")        # 一、
PAT_Q = re.compile(r"^\s*(\d{1,2})\s*[.．、]\s*\S")                  # 12. 题干

out = []
for f in sorted(glob.glob(os.path.join(MD, "**", "*.md"), recursive=True)):
    rel = os.path.relpath(f, MD).replace(os.sep, "/")
    if rel.startswith("期末往年题勘误"):
        continue
    lines = io.open(f, encoding="utf-8").read().splitlines()
    secs = [l.strip() for l in lines if PAT_SECTION.match(l)]
    bigs = [l.strip()[:34] for l in lines if PAT_BIG.match(l)]
    nq = sum(1 for l in lines if PAT_Q.match(l))
    out.append("### %s   (题号行 %d)" % (rel, nq))
    if secs:
        out.append("    知识点标注(%d): %s" % (len(secs), " | ".join(secs[:14])))
    if bigs:
        out.append("    大题(%d): %s" % (len(bigs), " / ".join(bigs[:10])))
    if not secs and not bigs:
        out.append("    (无标注)")

io.open(os.path.join(HERE, "_survey.txt"), "w", encoding="utf-8").write("\n".join(out))
print("files:", len(out))
