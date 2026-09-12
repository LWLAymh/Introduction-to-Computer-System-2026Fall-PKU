# -*- coding: utf-8 -*-
"""把某个 PDF 的每一页都渲染成 PNG，放进 assets/<同结构目录>/<文件名>/。

convert.py 只在「疑似插图/扫描」的页面才渲染；对于需要人工誊写的整卷扫描件，
这里强制全卷渲染。

用法: python render_all.py 期中/2012期中-带答案.pdf [更多...]
"""
import os
import sys
import glob
import shutil
import tempfile
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
REPO = os.path.dirname(BASE)
SRC = os.path.join(REPO, "往年题")
ASSETS = os.path.join(BASE, "assets")
DPI = 130


def render(rel):
    src = os.path.join(SRC, rel)
    if not os.path.exists(src):
        print("missing:", rel)
        return
    stem = os.path.splitext(os.path.basename(rel))[0]
    out = os.path.join(ASSETS, os.path.dirname(rel), stem)
    os.makedirs(out, exist_ok=True)

    # pdftoppm 是原生程序，读不了非 ASCII 路径（中文路径会 I/O Error），
    # 所以先复制成 ASCII 临时名再渲染。
    tmpd = tempfile.mkdtemp()
    ascii_pdf = os.path.join(tmpd, "src.pdf")
    shutil.copyfile(src, ascii_pdf)

    n = 0
    for pg in range(1, 200):
        dst = os.path.join(out, "page-%02d.png" % pg)
        if os.path.exists(dst):
            continue
        subprocess.run(["pdftoppm", "-f", str(pg), "-l", str(pg), "-r", str(DPI),
                        "-png", ascii_pdf, os.path.join(tmpd, "pg")],
                       capture_output=True)
        got = sorted(glob.glob(os.path.join(tmpd, "pg*.png")))
        if not got:
            break
        shutil.move(got[0], dst)
        n += 1
    shutil.rmtree(tmpd, ignore_errors=True)
    total = len(glob.glob(os.path.join(out, "page-*.png")))
    print("%-40s 新渲染 %-3d 共 %d 页 -> %s" % (rel, n, total, out))


if __name__ == "__main__":
    for r in sys.argv[1:]:
        render(r.replace("/", os.sep))
