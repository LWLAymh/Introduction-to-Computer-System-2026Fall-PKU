# -*- coding: utf-8 -*-
"""把转换后的 md 切成「题目单元」，供后续做知识点分类。

单元定义：每道大题下的一个编号小题（选择题则是每个编号选项）。
切分要点：
  - 用「编号连续」判定新单元，避免把正文里的数字、表格数字误判成新题；
  - 进入「参考答案/答案/解析」块后不再切新单元，整块作为该大题的答案；
  - 代码围栏内的行不参与切分。
"""
import io
import os
import re
import json
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
MD = os.path.join(BASE, "原文")
OUT = os.path.join(BASE, "_units")

BIG = re.compile(r"^\s*(第\s*([一二三四五六七八九十]+)\s*题|[一二三四五六七八九十]+\s*[、.．])\s*(.*)$")
SUBQ = re.compile(r"^\s*(\d{1,2})\s*[.．、]\s*(\S.*)$")
TOPIC = re.compile(r"^\s*[（(]\s*([^）)]{2,26})\s*[）)]\s*$")
ANSBLOCK = re.compile(r"^\s*(参考答案|答案|解析|解答)\s*[:：]?\s*$")
PAGEMARK = re.compile(r"^\s*<!--\s*=+\s*page\s+(\d+)\s*=+\s*-->\s*$")


def split(path):
    lines = io.open(path, encoding="utf-8").read().splitlines()
    units = []
    big = big_title = topic = None
    cur = None
    ans_mode = False
    ans_buf = []
    fence = False
    expect = None
    page = 0

    def flush():
        nonlocal cur
        if cur is not None:
            cur["text"] = "\n".join(cur["_buf"]).strip()
            cur.pop("_buf", None)
            if cur["text"]:
                units.append(cur)
        cur = None

    for ln in lines:
        s = ln.strip()

        m = PAGEMARK.match(ln)
        if m:
            page = int(m.group(1))
            if cur is not None:
                cur["_buf"].append(ln)
            elif ans_mode:
                ans_buf.append(ln)
            continue

        if s.startswith("```"):
            fence = not fence
            if cur is not None:
                cur["_buf"].append(ln)
            elif ans_mode:
                ans_buf.append(ln)
            continue

        if fence:
            if cur is not None:
                cur["_buf"].append(ln)
            elif ans_mode:
                ans_buf.append(ln)
            continue

        # 新大题
        mb = BIG.match(s)
        if mb and len(s) < 60 and (mb.group(2) or mb.group(3)):
            flush()
            if ans_buf:
                flush_answers(units, big, ans_buf)
                ans_buf = []
            big = mb.group(1).strip()
            big_title = (mb.group(3) or "").strip()
            topic = None
            ans_mode = False
            expect = None
            continue

        # 知识点标注（2024/2025）
        mt = TOPIC.match(s)
        if mt:
            cand = mt.group(1).strip()
            if any(k in cand for k in ("表示", "机器级", "体系结构", "存储", "性能",
                                       "链接", "异常", "系统级", "虚拟", "网络",
                                       "并发", "内存", "I/O", "高速缓存")):
                topic = cand
            if cur is not None:
                cur["_buf"].append(ln)
            continue

        # 答案块开始
        if ANSBLOCK.match(s):
            flush()
            ans_mode = True
            ans_buf.append(ln)
            continue

        # 编号小题
        ms = SUBQ.match(s)
        if ms and not ans_mode:
            n = int(ms.group(1))
            if expect is None or n == expect or n == 1:
                flush()
                cur = {"big": big, "big_title": big_title, "topic": topic,
                       "no": str(n), "page": page, "text": "",
                       "_buf": [ln]}
                expect = n + 1
                continue

        if cur is not None:
            cur["_buf"].append(ln)
        elif ans_mode:
            ans_buf.append(ln)

    flush()
    if ans_buf:
        flush_answers(units, big, ans_buf)
    return units


def flush_answers(units, big, buf):
    """把参考答案块并回同一大题的各单元。"""
    txt = "\n".join(buf).strip()
    if not txt:
        return
    for u in units:
        if u["big"] == big:
            u["answers"] = (u.get("answers", "") + "\n" + txt).strip()


def main():
    os.makedirs(OUT, exist_ok=True)
    index = {}
    for f in sorted(glob.glob(os.path.join(MD, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(f, MD).replace(os.sep, "/")
        if rel.startswith("期末往年题勘误"):
            continue
        key = os.path.splitext(rel)[0].replace("/", "__")
        units = split(f)
        io.open(os.path.join(OUT, key + ".json"), "w", encoding="utf-8").write(
            json.dumps(units, ensure_ascii=False, indent=1))
        index[rel] = {"key": key, "n": len(units),
                      "bigs": sorted({u["big"] for u in units if u["big"]})}
        print("%-46s units=%-4d bigs=%s" % (rel, len(units),
                                            ",".join(index[rel]["bigs"])[:40]))
    io.open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8").write(
        json.dumps(index, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
