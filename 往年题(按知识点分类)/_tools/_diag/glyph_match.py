# -*- coding: utf-8 -*-
"""用字形轮廓反查 Unicode。

某些 PDF 内嵌的 SimSun 子集字体既没有 ToUnicode（或只有残缺的），也没有 cmap
表，但保留了原始 glyf 轮廓。拿系统里的 simsun.ttc 做参照，把轮廓归一化后比对，
即可反推出每个 GID 对应的字符。

只处理简单轮廓（numberOfContours > 0）；复合字形跳过。
"""
import io
import os
import sys
import struct
import hashlib
import warnings

warnings.filterwarnings("ignore")
from fontTools.ttLib import TTFont, TTCollection

SYS_FONTS = [
    r"C:\Windows\Fonts\simsun.ttc",
    r"C:\Windows\Fonts\simsunb.ttf",
    r"C:\Windows\Fonts\msyh.ttc",
]


def sig(glyph, upem):
    """归一化轮廓签名：点数 + 起点平移后的坐标序列（量化）。"""
    if glyph is None or glyph.numberOfContours is None or glyph.numberOfContours <= 0:
        return None
    try:
        coords, endPts, flags = glyph.getCoordinates(None)
    except Exception:
        try:
            coords = glyph.coordinates
        except Exception:
            return None
    if not coords:
        return None
    pts = [(x, y) for x, y in coords]
    x0, y0 = pts[0]
    norm = [((x - x0) * 1000 // upem, (y - y0) * 1000 // upem) for x, y in pts]
    return "%d:%s" % (len(norm), hashlib.md5(
        (";".join("%d,%d" % p for p in norm)).encode()).hexdigest())


def build_reference():
    """{签名: 字符}，来自系统字体。"""
    ref = {}
    for path in SYS_FONTS:
        if not os.path.exists(path):
            continue
        try:
            fonts = (TTCollection(path).fonts if path.lower().endswith(".ttc")
                     else [TTFont(path, lazy=True)])
        except Exception:
            continue
        for f in fonts:
            if "glyf" not in f or "cmap" not in f:
                continue
            upem = f["head"].unitsPerEm
            gl = f["glyf"]
            best = None
            for t in f["cmap"].tables:
                if t.isUnicode():
                    best = t
                    break
            if best is None:
                continue
            for cp, gname in best.cmap.items():
                if cp < 0x20:
                    continue
                s = sig(gl[gname], upem)
                if s:
                    ref.setdefault(s, chr(cp))
        if ref:
            break
    return ref


def recover(pdf_path, ref):
    """{gid: char}，来自 PDF 内嵌子集字体。"""
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage

    out = {}
    fp = open(pdf_path, "rb")
    doc = PDFDocument(PDFParser(fp))
    seen = set()
    for page in PDFPage.create_pages(doc):
        for _k, v in (page.resources.get("Font") or {}).items():
            f = v.resolve()
            bf = str(f.get("BaseFont") or "")
            if bf in seen or "SimSun" not in bf:
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
                data = ff.resolve().get_data()
                t = TTFont(io.BytesIO(data), lazy=True)
            except Exception as e:
                print("   font load fail:", e)
                continue
            if "glyf" not in t:
                continue
            upem = t["head"].unitsPerEm
            gl = t["glyf"]
            n = t["maxp"].numGlyphs
            hit = 0
            for gid in range(n):
                try:
                    s = sig(gl[t.getGlyphName(gid)], upem)
                except Exception:
                    continue
                if s and s in ref:
                    out[gid] = ref[s]
                    hit += 1
            print("   %s: GID %d, 匹配上 %d" % (bf, n, hit))
    return out


if __name__ == "__main__":
    ref = build_reference()
    print("参考字体签名:", len(ref))
    if not ref:
        sys.exit("没有可用的系统字体参照")
    pdf = sys.argv[1] if len(sys.argv) > 1 else None
    if pdf:
        m = recover(pdf, ref)
        print("还原出", len(m), "个字形")
        for gid in sorted(m)[:40]:
            print("  ", gid, m[gid])
