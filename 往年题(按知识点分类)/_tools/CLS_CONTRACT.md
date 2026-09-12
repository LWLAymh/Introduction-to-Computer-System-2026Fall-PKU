# 题目分类任务 · 输出契约

## 你的任务

读一份**已经转成 Markdown 的往年试卷**，把它按知识点归类。你**不抄写任何题目原文**——只输出
**行号区间**。后面有脚本按你给的行号去原文里切，所以只要你行号给对，归档出来的文字就是
逐字原文，不会因为你转述而出错。

## 9 个知识点模块（只能从这 9 个里选，名字必须逐字一致）

| 模块名 | 覆盖内容 |
|---|---|
| `Data Representation` | 补码/无符号、移位、符号扩展、字节序、IEEE 浮点、整数与浮点转换与舍入 |
| `Machine Prog` | x86-64 汇编、寄存器、寻址方式、过程调用与栈帧、控制流（cmp/test/jmp）、lea vs mov、gdb/objdump 读汇编、Y86 |
| `Processor Arch` | Y86/SEQ 流水线、数据通路、冒险与旁路、流水线寄存器、CPI/延迟/吞吐、组合逻辑与时序、指令集设计 |
| `Memory Hierarchy` | Cache 映射/组相联/替换与写策略、局部性、AMAT、存储设备（SRAM/DRAM/磁盘/SSD）、可靠性 |
| `Compilation (Program optimization and linking)` | 编译器优化、代码移动、CPE/性能下限、可重定位目标文件、符号表、静态/动态链接、重定位、共享库/PIC、ELF 结构 |
| `ECF and System IO` | 异常与中断、进程控制 fork/execve/wait、信号、非本地跳转、Unix I/O（open/read/write/dup2）、RIO、文件与目录、文件描述符表 |
| `Virtual Memory and Dynamic Memory Allocation` | 地址翻译、页表/TLB/多级页表、缺页、内存映射 mmap、堆分配器（隐式/显式空闲链表、分离空闲链表）、碎片、GC |
| `Network` | 协议分层、IP/子网、TCP/UDP、套接字接口、字节序转换、HTTP/Web 服务器、客户端-服务器模型 |
| `Concurrent Programming and Synchronization` | 线程与进程、共享变量、竞态、互斥锁/信号量/条件变量、死锁、生产者-消费者、读者-写者、线程安全与可重入、并行加速比 |

**判断要点**：按「这道题在考什么」归类，不要按「它出现在哪一章」。一道题若同时涉及多个，
选**主导**的那个；实在难分就在 `note` 里写「兼 xx」。

## 粒度要求（很重要）

区间要切到**小题**级别，不要整道大题一刀切。原因：一道大题里的各个小题常常分属不同模块。
例如 2024 期末第一题是 14 道选择题，分别考了 Data Representation / Machine Prog /
Processor Arch / Memory Hierarchy / Compilation / ECF / VM / Network / Concurrency —— 
这就要切成 14 个区间，各归各的模块。

反过来，如果一道大题的所有小题都属于同一个模块，切成一个区间即可。

## 输出格式

写一个 JSON 文件到指定路径，UTF-8，结构如下：

```json
{
  "file": "期末/2024期末-带答案.md",
  "total_lines": 1115,
  "items": [
    {
      "start": 45,
      "end": 78,
      "module": "Data Representation",
      "qno": "第一题 1",
      "note": "半字节数 int4/float4 的范围与表示"
    }
  ],
  "answer_sections": [
    {
      "start": 900,
      "end": 1115,
      "note": "全卷参考答案与解析"
    }
  ]
}
```

字段说明：

- `start` / `end`：**闭区间**，1-based，指 `原文/<file>` 的行号。必须与 Read 工具显示的
  行号一致。`start` 行和 `end` 行都包含在区间内。
- `module`：上表 9 个模块名之一，逐字一致（含括号和大小写）。
- `qno`：题号的人话标识，如 `"第一题 3"`、`"第二题 (2)"`、`"Problem A 7"`、
  `"选择题 12"`。用于生成清单表格。
- `note`：一句话说明这题考什么（≤ 30 字）。
- `answer_sections`：把散落在卷末的「参考答案/解析」整块标出来。它可以与 `items`
  **重叠**（因为答案常常在题目区间之外，但若重叠也没关系）。若卷子没有独立答案块，
  就写空数组 `[]`。

## 硬性约束

1. `items` 必须按 `start` 升序，且**互不重叠**。
2. 所有行号必须落在 `1 .. total_lines` 之内。
3. 试卷封面、考试须知、诚信承诺书、得分表、`<!-- ===== page N ===== -->` 注释行，
   **不要**单独成项；忽略它们即可（不必覆盖全文的每一行）。
4. 代码块、表格、图片引用（`![图](...)`）都要包含在它们所属题目的区间内，不要切开。
5. 若某题你实在无法判断模块，用 `Machine Prog` 以外的选择请谨慎；宁可写 `note` 说明存疑。

## 自检（交之前必须做一遍）

- `items` 里每个 `module` 都逐字出现在上面 9 个模块名中。
- `start <= end`，且区间递增不重叠。
- 区间覆盖了你认为属于题目正文的行；没有把两道不同模块的题塞进同一个区间。
