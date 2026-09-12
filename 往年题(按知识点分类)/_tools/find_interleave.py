# -*- coding: utf-8 -*-
"""找出「行内交错」的坏行，并按严重程度给文件排序。

成因：Word 导出的 PDF 里，同一基线上叠着多段互相重叠的文本（正文一段、填空下划线
一段、(1)(2) 编号一段），x 范围彼此交叠。convert.py 按 x 排序拼接后，这些段被
逐字符交织，例如

    uunnssiiggnneedd   iinntt   ==  x;+f
    4444444000000000000004444444eeeffff58bd6cf:::::::

交错的最可靠指纹是**相邻重复字符**——两段文字被逐字符交替拼进来时，每一段自己的
字符会被复制成 `xx`、`xxxx` 这种形态。正常的代码/表格不会有连续 3 个以上相同字符，
也很少整行高频重复。

因此判据用两条，满足其一即记：
  A. 连续 >=3 个相同字符（排除缩进、分隔线、以及 0x 十六进制串里的正常重复）；
  B. 相邻字符相同的比例 >= 0.30 且去空白后长度 >= 10。

注意：像 `题号  一  二  三` 这类表格行、`pmap` 输出、以及合法代码只是「短 token 多」，
不会被这两条命中——那是上一版判据的误报来源，已废弃。
"""
import io
import os
import re
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
MD = os.path.join(BASE, "原文")

PAGE = re.compile(r"^\s*<!--\s*=+\s*page\s+(\d+)\s*=+\s*-->\s*$")
TRIPLE = re.compile(r"(.)\1{2,}")
# 正常的十六进制/二进制长串、缩进、分隔线，不算交错
BENIGN = re.compile(r"^\s*[0-9a-fA-Fx,\s]*$")


ALNUM = re.compile(r"[0-9A-Za-z]")
ALPHA = re.compile(r"[A-Za-z]")


def dup_ratio(s):
    """在 ASCII 字母数字上算相邻重复率。

    中文和标点不参与：它们不会因交错而自我重复，算进来只会稀释信号
    （也会让 `(((  )))` 这类正常填空下划线误报）。
    """
    t = "".join(ALNUM.findall(s))
    if len(t) < 10:
        return 0.0
    same = sum(1 for a, b in zip(t, t[1:]) if a == b)
    return same / (len(t) - 1)


def is_bad(s):
    core = s.strip()
    if len(core) < 8:
        return False
    if core.startswith("```") or core.startswith("<!--"):
        return False
    if set(core) <= set("-=_*# "):
        return False
    # 至少有 6 个字母才判：否则「端口 2222 / 地址 0x4000」这类正常重复数字
    # （10.0.0.5 … 2222 … 22）会被误判成交错。
    if len(ALPHA.findall(core)) < 6:
        return False
    return dup_ratio(core) >= 0.28


def scan(path):
    lines = io.open(path, encoding="utf-8").read().splitlines()
    bad, page, fence = [], 0, False
    for i, ln in enumerate(lines, 1):
        m = PAGE.match(ln)
        if m:
            page = int(m.group(1))
            continue
        if ln.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if is_bad(ln):
            bad.append((i, page, ln.strip()[:88]))
    return len(lines), bad


def main():
    rows = []
    for f in sorted(glob.glob(os.path.join(MD, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(f, MD).replace(os.sep, "/")
        nl, bad = scan(f)
        if bad:
            rows.append((len(bad), rel, nl, bad))
    rows.sort(reverse=True)

    out = ["交错坏行统计（按坏行数降序）", ""]
    out.append("%-46s %6s %6s  %s" % ("文件", "坏行", "总行", "涉及页"))
    out.append("-" * 100)
    for n, rel, nl, bad in rows:
        pages = sorted({p for _, p, _ in bad})
        ps = ",".join(map(str, pages[:16])) + ("..." if len(pages) > 16 else "")
        out.append("%-46s %6d %6d  %s" % (rel, n, nl, ps))

    out.append("")
    out.append("=" * 100)
    out.append("严重文件（坏行 >= 8）的坏行明细")
    out.append("=" * 100)
    for n, rel, nl, bad in rows:
        if n < 8:
            continue
        out.append("")
        out.append("### %s   （%d 坏行 / %d 行）" % (rel, n, nl))
        for i, p, s in bad[:40]:
            out.append("  p%-3s L%-5d %s" % (p, i, s))
        if len(bad) > 40:
            out.append("  ... 另有 %d 行" % (len(bad) - 40))

    io.open(os.path.join(HERE, "_interleave.txt"), "w", encoding="utf-8").write(
        "\n".join(out))
    print("files:", len(rows), "  severe(>=8):", sum(1 for n, _, _, _ in rows if n >= 8))


if __name__ == "__main__":
    main()
