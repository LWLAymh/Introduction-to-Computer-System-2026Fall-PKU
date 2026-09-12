# -*- coding: utf-8 -*-
"""回查：模块文件里的每道题，是否真的逐字等于 原文/ 里对应的行区间。

这是 README「题目正文是逐字原文」这个说法的可执行证据。做法是把 _cls/ 里的每个
行号区间重新从 原文/ 切一遍，再检查这段文字是否原样出现在对应的模块文件里。
若切片环节有任何增删改（或行号错位），这里就会报未命中。

预期未命中只有一种情况：被去重的别名卷子。例如 2015期末-20151109 与 2015期中
正文相同，只保留一份，因此前者的切片不会出现在模块文件里——脚本会把它单独列出来。
"""
import io
import os
import json
import glob
import hashlib

import build_modules as bm          # 复用同一份去重指纹与模块名表

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
MOD = os.path.join(BASE, "模块")

BYNAME = bm.BYNAME
IMG = bm.IMG


def body_hash(lines):
    t = "\n".join(l for l in lines
                  if not l.startswith("# ") and not l.startswith("> 来源"))
    return hashlib.md5(IMG.sub("IMG", t).encode("utf-8")).hexdigest()


def main():
    # 先把「哪些卷子被去重了」算出来，这些卷子的未命中是预期的
    allp = []
    for p in sorted(glob.glob(os.path.join(BASE, "_cls", "*.json"))):
        d = json.load(io.open(p, encoding="utf-8"))
        rel = d.get("file")
        if not rel:
            continue
        src = os.path.join(BASE, "原文", rel.replace("/", os.sep))
        if os.path.exists(src):
            allp.append((rel, d, io.open(src, encoding="utf-8").read().splitlines()))
    allp.sort(key=lambda t: t[0])
    seen, dup_of = {}, {}
    for rel, d, lines in allp:
        h = body_hash(lines)
        if h in seen:
            dup_of[rel] = seen[h]
        else:
            seen[h] = rel

    bodies = {os.path.basename(m): io.open(os.path.join(MOD, m), encoding="utf-8").read()
              for m in os.listdir(MOD) if m.endswith(".md")}
    ok = empty = 0
    missed, expected = [], []

    for rel, d, lines in allp:
        if (d.get("kind") or "questions") != "questions":
            continue
        for it in d.get("items") or []:
            s, e = it.get("start"), it.get("end")
            if not isinstance(s, int) or not isinstance(e, int):
                continue
            frag = "\n".join(lines[s - 1:e]).strip("\n")
            if not frag:
                empty += 1
                continue
            m = BYNAME.get(it.get("module"))
            if not m:
                continue
            if frag in bodies[m[1] + ".md"]:
                ok += 1
            elif rel in dup_of:
                expected.append("%s %s [%d,%d]（同 %s，已去重）"
                                % (rel, it.get("qno"), s, e, dup_of[rel]))
            else:
                missed.append("%s %s [%d,%d] -> %s" % (rel, it.get("qno"), s, e, m[0]))

    L = ["逐字切片回查：命中 %d，未命中 %d，空片 %d" % (ok, len(missed), empty), ""]
    if missed:
        L.append("!! 不应出现的未命中（切片被改动或行号错位）:")
        L += ["   " + x for x in missed]
    else:
        L.append("所有非去重题目均逐字命中，未发现改动或错位。")
    if expected:
        L.append("")
        L.append("预期未命中（去重别名，正文已由另一份卷子承载）%d 条:" % len(expected))
        L += ["   " + x for x in expected[:20]]

    io.open(os.path.join(HERE, "_verify.txt"), "w", encoding="utf-8").write("\n".join(L))
    print("hit %d  missed %d  expected-miss %d  empty %d"
          % (ok, len(missed), len(expected), empty))


if __name__ == "__main__":
    main()
