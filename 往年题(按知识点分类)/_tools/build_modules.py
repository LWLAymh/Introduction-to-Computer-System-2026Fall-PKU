# -*- coding: utf-8 -*-
"""按 _cls/*.json 里的行号区间，从 原文/ 切出逐字原文，生成 9 个知识点模块文件。

设计要点：分类结果只记录「行号区间 -> 模块」，真正落到模块文件里的题目文字是
本脚本从 原文/ 里**按行号切出来的**，因此是逐字原文，不存在转述失真。

产出：
    模块/1-Data-Representation.md ... 模块/9-Concurrent-Programming.md
    00-总览.md
    _tools/_build_report.txt
"""
import io
import os
import re
import json
import glob
import hashlib
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
MD = os.path.join(BASE, "原文")
CLS = os.path.join(BASE, "_cls")
OUT = os.path.join(BASE, "模块")

MODULES = [
    ("Data Representation", "1-Data-Representation",
     "数据的表示"),
    ("Machine Prog", "2-Machine-Prog",
     "程序的机器级表示"),
    ("Processor Arch", "3-Processor-Arch",
     "处理器体系结构"),
    ("Memory Hierarchy", "4-Memory-Hierarchy",
     "存储层次"),
    ("Compilation (Program optimization and linking)", "5-Compilation-Linking",
     "编译系统（程序优化与链接）"),
    ("ECF and System IO", "6-ECF-and-System-IO",
     "异常控制流与系统级 I/O"),
    ("Virtual Memory and Dynamic Memory Allocation", "7-Virtual-Memory-and-Malloc",
     "虚拟内存与动态内存分配"),
    ("Network", "8-Network",
     "网络编程"),
    ("Concurrent Programming and Synchronization", "9-Concurrent-Programming",
     "并发编程与同步"),
]
BYNAME = {m[0]: m for m in MODULES}

# 试卷类别排序：期中 -> 期末 -> 阶段测验 -> Lab测验
CAT_ORDER = {"期中": 0, "期末": 1, "阶段测验": 2, "Lab测验": 3, "补充": 4}

YEAR = re.compile(r"(\d{4})")
IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")


def body_hash(lines):
    """正文指纹，忽略标题行、来源行和图片路径。

    同一份卷子可能被放在两个目录下（例：`期中/2015期中-带答案.pdf` 与
    `期末/2015期末-20151109-带答案.pdf` 是同一张卷子，正文逐行相同）。
    在模块清单里只保留一份，避免同题出现两次。
    """
    t = "\n".join(l for l in lines
                  if not l.startswith("# ") and not l.startswith("> 来源"))
    return hashlib.md5(IMG.sub("IMG", t).encode("utf-8")).hexdigest()


def load():
    """读所有分类结果，产出 [{file, cat, year, label, items, answer_sections}]"""
    out = []
    for p in sorted(glob.glob(os.path.join(CLS, "*.json"))):
        try:
            d = json.load(io.open(p, encoding="utf-8"))
        except Exception:
            continue
        rel = d.get("file")
        if not rel:
            continue
        src = os.path.join(MD, rel.replace("/", os.sep))
        if not os.path.exists(src):
            continue
        cat = rel.split("/")[0]
        stem = os.path.splitext(os.path.basename(rel))[0]
        ym = YEAR.search(rel)
        out.append({
            "file": rel, "json": os.path.basename(p), "cat": cat,
            "year": int(ym.group(1)) if ym else 0,
            "label": stem, "rel": rel,
            "items": d.get("items") or [],
            "ans": d.get("answer_sections") or [],
            # kind 缺省为 questions；勘误/评分说明类材料没有题目，但可能通过
            # applies_to 指名它注解的是哪几份卷子，从而挂进对应模块。
            "kind": d.get("kind") or "questions",
            "applies_to": d.get("applies_to") or [],
            "lines": io.open(src, encoding="utf-8").read().splitlines(),
        })
    # 先按 (类别, 年份, 名称) 排出稳定顺序，再让指纹相同的卷子只保留一份。
    # 年份解析不出来的（如「期末往年题勘误、详解 by Arthals」）排到最后。
    out.sort(key=lambda d: (CAT_ORDER.get(d["cat"], 9), d["year"] or 9999, d["label"]))
    seen = {}
    for d in out:
        h = body_hash(d["lines"])
        if h in seen:
            d["dup_of"] = seen[h]          # 与哪一份重复
        else:
            seen[h] = d["rel"]
    return out


def ydisplay(d):
    """年份列：解析不出年份时显示破折号，不显示 0。"""
    return str(d["year"]) if d["year"] else "—"


def slice_of(d, a, b):
    return "\n".join(d["lines"][a - 1:b]).strip("\n")


def main():
    os.makedirs(OUT, exist_ok=True)
    allp = load()
    aliases = collections.defaultdict(list)
    papers = []
    for d in allp:
        if d.get("dup_of"):
            aliases[d["dup_of"]].append(d["rel"])
        else:
            papers.append(d)

    buckets = collections.defaultdict(list)
    for d in papers:
        for it in d["items"]:
            m = it.get("module")
            if m not in BYNAME:
                continue
            s, e = it.get("start"), it.get("end")
            if not isinstance(s, int) or not isinstance(e, int) or s > e:
                continue
            if s < 1 or e > len(d["lines"]):
                continue
            buckets[m].append((d, it))

    # 无题目的勘误/评分说明，挂到它所注解的卷子所触及的模块上。
    # 例：2024期中勘误说明了哪几道小题改判满分，对它涉及的每个模块都有用。
    mods_of = collections.defaultdict(set)
    for d in papers:
        for it in d["items"]:
            if it.get("module") in BYNAME:
                mods_of[d["rel"]].add(it["module"])
    errata_by_mod = collections.defaultdict(list)
    for d in allp:
        if d["kind"] == "questions" or not d["ans"]:
            continue
        targets = set()
        for t in d["applies_to"]:
            targets |= mods_of.get(t, set())
        for m in targets:
            errata_by_mod[m].append(d)

    report = []
    cross = collections.defaultdict(lambda: collections.defaultdict(int))

    for mname, slug, zh in MODULES:
        rows = buckets.get(mname, [])
        L = []
        L.append("# %s\n" % zh)
        L.append("> **英文模块名**：`%s`  \n" % mname)
        L.append("> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，")
        L.append("> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。\n")

        if not rows:
            L.append("（本模块暂未归入题目。）\n")
            io.open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8").write("\n".join(L))
            report.append("%-46s items=0" % mname)
            continue

        # ---- 清单 ----
        L.append("## 一、清单\n")
        L.append("共 %d 道题，来自 %d 份材料。\n" % (len(rows), len({d["rel"] for d, _ in rows})))
        L.append("| 年份 | 试卷 | 类别 | 题号 | 考什么 |")
        L.append("|---|---|---|---|---|")
        for d, it in rows:
            cross[d["rel"]][mname] += 1
            lab = d["label"]
            if aliases.get(d["rel"]):
                lab += "（同 %s）" % "、".join(
                    os.path.splitext(os.path.basename(a))[0] for a in aliases[d["rel"]])
            L.append("| %s | %s | %s | %s | %s |" % (
                ydisplay(d), lab, d["cat"],
                str(it.get("qno", "")).replace("|", "/"),
                str(it.get("note", "")).replace("|", "/")))
        L.append("")

        # ---- 原文 ----
        L.append("## 二、题目原文\n")
        for d, it in rows:
            L.append("### %s · %s" % (d["label"], it.get("qno", "")))
            L.append("")
            if aliases.get(d["rel"]):
                L.append("> ⚠️ 同一份卷子也存在于：%s（正文等同，已去重）" % "、".join(
                    "`原文/%s`" % a for a in aliases[d["rel"]]))
            L.append("> 出处：`原文/%s` 第 %d–%d 行　·　模块判定：%s" % (
                d["rel"], it["start"], it["end"], mname))
            if it.get("note"):
                L.append("> 考什么：%s" % it["note"])
            L.append("")
            L.append(slice_of(d, it["start"], it["end"]))
            L.append("")
            L.append("---")
            L.append("")

        # ---- 相关答案 ----
        ans_papers = [d for d, _ in rows if d["ans"]]
        group = []
        seen = set()
        for d in ans_papers + errata_by_mod.get(mname, []):
            if d["rel"] not in seen:
                seen.add(d["rel"])
                group.append(d)
        if group:
            L.append("## 三、相关试卷的参考答案 / 解析原文\n")
            for d in group:
                for a in d["ans"]:
                    s, e = a.get("start"), a.get("end")
                    if not isinstance(s, int) or not isinstance(e, int) or s > e:
                        continue
                    if s < 1 or e > len(d["lines"]):
                        continue
                    L.append("### %s · %s" % (d["label"], a.get("note", "参考答案")))
                    L.append("")
                    L.append("> 出处：`原文/%s` 第 %d–%d 行" % (d["rel"], s, e))
                    L.append("")
                    L.append(slice_of(d, s, e))
                    L.append("")
                    L.append("---")
                    L.append("")

        io.open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8").write("\n".join(L))
        report.append("%-46s items=%-4d papers=%d" % (
            mname, len(rows), len({d["rel"] for d, _ in rows})))

    # ---- 总览 ----
    T = []
    T.append("# 总览：历年试卷 × 知识点 交叉表\n")
    T.append("> 由 `_tools/build_modules.py` 生成。单元格是「该试卷归入该模块的题目数」。\n")
    short = [m[1].split("-", 1)[1].replace("-", " ") for m in MODULES]
    T.append("| 试卷 | 类别 | 年份 | " + " | ".join(
        "%d" % (i + 1) for i in range(len(MODULES))) + " | 合计 |")
    T.append("|---" * (len(MODULES) + 4) + "|")
    grand = collections.Counter()
    for d in papers:
        if d["rel"] not in cross:
            continue
        vals = [cross[d["rel"]].get(m[0], 0) for m in MODULES]
        tot = sum(vals)
        for m in MODULES:
            grand[m[0]] += cross[d["rel"]].get(m[0], 0)
        T.append("| %s | %s | %s | %s | %d |" % (
            d["label"], d["cat"], ydisplay(d),
            " | ".join(str(v) if v else "·" for v in vals), tot))
    T.append("| **合计** | | | " + " | ".join(
        str(grand[m[0]]) for m in MODULES) + " | %d |" % sum(grand.values()))
    T.append("")
    T.append("列编号对应：\n")
    for i, (mname, slug, zh) in enumerate(MODULES):
        T.append("%d. [%s](模块/%s.md) — `%s`" % (i + 1, zh, slug, mname))
    T.append("")
    io.open(os.path.join(BASE, "00-总览.md"), "w", encoding="utf-8").write("\n".join(T))

    io.open(os.path.join(HERE, "_build_report.txt"), "w", encoding="utf-8").write(
        "\n".join(report) + "\n\ntotal items: %d\n" % sum(grand.values()))
    print("built", len(MODULES), "modules; total items", sum(grand.values()))


if __name__ == "__main__":
    main()
