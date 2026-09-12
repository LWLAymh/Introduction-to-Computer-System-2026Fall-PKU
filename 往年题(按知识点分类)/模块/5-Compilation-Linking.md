# 编译系统（程序优化与链接）

> **英文模块名**：`Compilation (Program optimization and linking)`  

> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，
> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。

## 一、清单

共 105 道题，来自 33 份材料。

| 年份 | 试卷 | 类别 | 题号 | 考什么 |
|---|---|---|---|---|
| 2012 | 2012期中-带答案 | 期中 | Problem A 14 | 已初始化变量所在的 ELF 段（.data） |
| 2012 | 2012期中-带答案 | 期中 | Problem F A | 链接：全局符号强弱、作用域与 ELF 段归属 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 14 | 程序优化与分支预测的正确性 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 15 | 编译器可自动进行的优化变换 |
| 2013 | 2013期中-带答案 | 期中 | 第七题 2)3) | CPE 下限与循环展开优化填空 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 13 | 程序性能说法辨析、循环展开代价（兼 Processor Arch） |
| 2014 | 2014期中-带答案 | 期中 | 第一题 14 | 编译器总是自动进行的代码优化 |
| 2014 | 2014期中-带答案 | 期中 | 第七题 1） | 循环条件中重复调用 length 的效率问题与修改 |
| 2014 | 2014期中-带答案 | 期中 | 第七题 2） | 删除循环变量以消除函数调用 |
| 2014 | 2014期中-带答案 | 期中 | 第七题 3） | 给定访存延时求内层循环 CPE 下限 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 20 | 编译器自动优化变换（别名/精度） |
| 2016 | 2016期中-带答案 | 期中 | 第三题 (2) | 链表循环 CPE 与关键路径，填 C 代码 |
| 2016 | 2016期中-带答案 | 期中 | 第三题 (2) 答案 | CPE 与关键路径参考答案 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 12 | 编译器不会做的程序优化 |
| 2018 | 2018期中-带答案 | 期中 | 第一题 11 | 编译器总是可行的优化（别名/副作用） |
| 2019 | 2019期中-带答案 | 期中 | 第一题 12 | 程序优化相关陈述的正误 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 13 | loop unrolling 的原理与代价 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 8 | 编译器可行优化与别名/副作用限制 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 14 | 编译器总能进行的优化与别名/副作用/浮点 |
| 2021 | 2021期中-带答案 | 期中 | 第六题 4 | 2x2 循环展开的两个累积变量改写 |
| 2021 | 2021期中-带答案 | 期中 | 第六题 5 | 浮点加法不满足结合律导致的错误 |
| 2021 | 2021期中-带答案 | 期中 | 第六题 6 | k*k 展开中 k 过大导致寄存器溢出 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 15 | 循环展开与编译优化的限制 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 20 | 程序优化：循环展开与编译器优化限制 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 15 | 代码优化等价性判断（别名、副作用、strlen） |
| 2013 | 2013期末-带答案 | 期末 | 第一题 7 | 同名全局变量导致的链接错误 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 8 | 哪些符号一定不需要重定位 |
| 2013 | 2013期末-带答案 | 期末 | 第四题 | 弱/强符号属性、ELF section 与链接解析 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 5 | 编译器安全优化策略 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 8 | 静态库链接与命令行顺序 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 9 | static 全局变量影响的 ELF 节 |
| 2014 | 2014期末-带答案 | 期末 | 第四题 | 符号强弱属性、静态库链接顺序与重定位 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 4 | 静态库链接的规则与命令行顺序 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 5 | 字符串常量被放入哪个 ELF 节 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 12 | 编译器安全优化策略 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第四题 | 符号强弱属性、类型声明冲突与数据布局 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 5 | strlen 外提优化与程序局部性 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 7 | 同名全局变量的符号解析与 extern |
| 2016 | 2016期末-带答案 | 期末 | 第一题 8 | .data/.bss 布局与变量地址顺序 |
| 2016 | 2016期末-带答案 | 期末 | 第四题 | 强/弱符号属性表与多文件链接运行输出 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 7 | 跨文件符号类型不一致的链接结果 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 8 | 符号解析规则与静态库链接 |
| 2017 | 2017期末-无答案 | 期末 | 第四题 | 强弱符号多重定义与链接成功原因（兼 GC 根指针） |
| 2018 | 2018期末-带答案 | 期末 | 第一题 4 | 链接、打桩与符号解析与重定位 |
| 2018 | 2018期末-带答案 | 期末 | 第三题 1 | 各符号的 .symtab 条目、类型与所在节 |
| 2018 | 2018期末-带答案 | 期末 | 第三题 2 | 反汇编中的重定位条目与引用值计算 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 7 | 编译期打桩、ABS 节与 -fPIC |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 8 | 跨模块同名符号类型不一致 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 解答题二 1 | 符号表与各符号所属节 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 解答题二 2 | 重定位地址计算与小端立即数 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 6 | 对引用而非符号谈重定位 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 解答题一 1-2 | CPE 与循环执行周期数 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 解答题一 4-5 | 循环展开与指令重排降低周期 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 解答题二 | 符号表、强弱符号与重定位计算 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 6 | 链接时哪些符号需要重定位 |
| 2019 | 2019期末-无答案 | 期末 | 第三题 | 符号表、强弱符号与重定位引用值 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 7 | 链接、打桩、共享库与程序入口点 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 8 | 跨文件符号类型冲突与链接结果 |
| 2020 | 2020期末-无答案 | 期末 | 第三题 | 符号表条目、节归属与重定位引用值 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 6 | 循环展开、累积变量与浮点合并顺序 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 9 | objdump/readelf/gdb 等可执行文件工具（兼 Machine Prog） |
| 2021 | 2021期末-无答案 | 期末 | 第一题 10 | 静态局部符号与 COMMON 伪节 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 11 | 动态链接、PLT/GOT 与 -ldl |
| 2021 | 2021期末-无答案 | 期末 | 第三题 | 符号表节归属、重定位与程序入口点（Part C 兼 ECF） |
| 2021 | chap 2-6 解析 | 期末 | 第一题 8 | 程序优化：循环展开、累积变量、浮点结合律 |
| 2021 | chap 7 解析 | 期末 | 第 1 题 | objdump/readelf/ls/gdb 处理目标文件与可执行文件的作用 |
| 2021 | chap 7 解析 | 期末 | 第 2 题 | 静态链接：未初始化全局变量在 COM/.bss 的归属与地址偏移 |
| 2021 | chap 7 解析 | 期末 | 第 3 题 | 动态链接：dlopen 与 PLT/GOT、库的符号解析顺序 |
| 2021 | chap 7 解析 | 期末 | 第 4 题 题干+Part A | 符号表中的符号及其定义所在节（.bss/.rodata/UNDEF 等） |
| 2021 | chap 7 解析 | 期末 | 第 4 题 Part B | 重定位条目 R_X86_64_PLT32/PC32 与符号地址推算 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 4 | 静态链接器的两大主要任务 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 5 | 延迟绑定依赖的两个数据结构 PLT/GOT |
| 2022 | 2022期末-无答案 | 期末 | 第一题 6 | 静态库命令行最小排列顺序以解析全部符号 |
| 2022 | 2022期末-无答案 | 期末 | 第三题 (1) | main.o 的 .symtab 条目、符号类型与所在节（含 main.c/addvec.c） |
| 2022 | 2022期末-无答案 | 期末 | 第三题 (2) | 依 objdump 反汇编片段填写重定位条目与引用值 |
| 2022 | 2022期末-无答案 | 期末 | 第三题 (3) | 动态链接器 ld-linux 的路径选择 |
| 2022 | 2022期末-无答案 | 期末 | 第三题 (4) | printf 对应的 PLT 与 GOT 表条目下标 |
| 2022 | 2022期末-答案 | 期末 | 第一题 4 | 符号解析与重定位 |
| 2022 | 2022期末-答案 | 期末 | 第一题 5 | GOT 与 PLT |
| 2022 | 2022期末-答案 | 期末 | 第一题 6 | 静态库链接顺序 gcc 命令行 |
| 2022 | 2022期末-答案 | 期末 | 第三题 | 符号表、重定位、.interp 与 PLT |
| 2024 | 2024期末-带答案 | 期末 | 第一题 5 | gcc 编译链接过程、ld 报错与重定位 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 6 | 符号表条目与 .data/.bss/UND 节 |
| 2025 | 2025期末-带答案 | 期末 | 二 14 | 全局符号强/弱定义与类型检查 |
| 2025 | 2025期末-带答案 | 期末 | 三 1 | 符号表条目、符号类型与所在节（含答案） |
| 2025 | 2025期末-带答案 | 期末 | 三 2 | 重定位条目与 32 位小端机器码（含答案） |
| 2025 | 2025期末-带答案 | 期末 | 三 3 | 链接顺序影响的答案选项 |
| 2025 | 2025期末-无答案 | 期末 | 二 14 | 全局符号强/弱定义与重复定义 |
| 2025 | 2025期末-无答案 | 期末 | 三 1 | main.o 的 .symtab 符号表条目与所在节 |
| 2025 | 2025期末-无答案 | 期末 | 三 2 | 重定位条目与 32 位小端机器码 |
| 2025 | 2025期末-无答案 | 期末 | 三 3 | 链接顺序对可执行文件的影响 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2015 第四题 | 重复定义全局变量的理解（union 验证） |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2020 第一题 第7问 | ABS 节在静态/部分链接文件中的存在性 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2020 第三题 ④ | 重定位符号应为 count（答案勘误） |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2021 第三题 Part A | 局部静态变量重命名加 .x 后缀 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2021 第三题 Part B | 相对重定位偏移与 addend 含义 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2022 第三题 第3问 | .interp 节内容为动态链接器路径 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2022 第三题 第4问 | 识别 PLT0 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第14/15讲 19 | 编译优化的过程调用限制与存储器别名限制 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第14/15讲 20 | 不定项：链接器需要解析的符号 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第14/15讲 21 | 目标文件反汇编中 0 填充与重定位、callq 偏移 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 7 | Makefile 模式规则 %.o: %.c |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 8 | make 默认目标与执行过程 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 9 | gcc -c 生成目标文件与 objdump -d 反汇编（兼 Machine Prog） |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 10 | binutils 中 ldd 查看共享库依赖 |

## 二、题目原文

### 2012期中-带答案 · Problem A 14

> 出处：`原文/期中/2012期中-带答案.md` 第 119–123 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：已初始化变量所在的 ELF 段（.data）

14. In what section of an ELF binary are initialized variables located? **(2pts) (e2b-s11)**　**答案：B**
   a) .symtab
   b) .data
   c) .bss
   d) .text

---

### 2012期中-带答案 · Problem F A

> 出处：`原文/期中/2012期中-带答案.md` 第 637–683 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链接：全局符号强弱、作用域与 ELF 段归属

**Problem F – Linking (12 pts)**

For each of the following code snippets, write down all symbols in the resulting object files from
compilation. Write whether it is a weak global, strong global, or local variable, and what section
of the final compiled ELF binary the variable will go into. Fill in the value if you have enough
information to determine the value.

   **A.**

![图](assets/期中/2012期中-带答案/page-13.png)

> 上图为本页的作答表格（符号强度/作用域、取值、所在 ELF 段），红色为参考答案；foo.o 最后两行为空白行。

```c
/* main.c */
#include <stdio.h>

int x;
int y;
int z = 0;

int main() {
  printf("%x\n", x);
  printf("%x\n", y);
  x = 0xdeadbeef;
  printf("%x\n", x);
  printf("%x\n", y);
  return 0;
}
```

```c
/* foo.c */
short x = 5;
short y = 2;
```

| File | Symbol | Strength / scope | Value | ELF Section |
| --- | --- | --- | --- | --- |
| Main.o | **X** | **Weak global** | **-** | **.data** |
| Main.o | **Y** | **Weak global** | **-** | **.data** |
| Main.o | **Z** | **Strong global** | **0** | **.data** |
| Main.o | **Main** | **Strong global** | **-** | **.text** |
| foo.o | **X** | **Strong global** | **5** | **.data** |
| foo.o | **Y** | **Strong global** | **2** | **.data** |
| foo.o | | | | |
| foo.o | | | | |

---

### 2013期中-带答案 · 选择题 14

> 出处：`原文/期中/2013期中-带答案.md` 第 130–140 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：程序优化与分支预测的正确性

14、下面哪些选项是错误的？答：（      ）
A. 同一个任务采用时间复杂度为O(logN)算法一定比采用复杂度为O(N)算法的执行时间短
3

<!-- ===== page 4 ===== -->

B. 编译器进行程序优化时，总是可以使用算数结合律来减少计算量
C. 增大循环展开（loop unrolling）的级数，有可能降低程序的执行性能（即增加执行时间）
D. 分支预测时，“总是预测不跳转”（branch not taken）一定比“总是预测跳转”（branch taken）
预测准确率高
答案：ABD

---

### 2013期中-带答案 · 选择题 15

> 出处：`原文/期中/2013期中-带答案.md` 第 141–156 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器可自动进行的优化变换

15、以下哪些程序优化编译器总是可以自动进行？（假设int i, int j, int A[N], int B[N], int m
都是局部变量，N是一个整数型常量，int foo(int) 是一个函数）答：（      ）
  优化前  优化后
A.  for (j = 0 ; j < N ; j ++)  int temp = i*N;
   m + = i*N*j;  for (j= 0 ; j < N ; j ++)
   m + = temp * j;
B.  for (j = 0 ; j < N ; j ++)  int temp = B[i];
   B[i] *= A[j];  for (j= 0 ; j < N ; j ++)
   temp *= A[j];
B[i] = temp;
C.  for (j = 0 ; j < N ; j ++)  for (j = 0 ; j < N ; j ++)
   m = (m + A[j]) + B[j];     m = m + (A[j] + B[j]);
D.  for (j = 0 ; j < foo(N) ; j ++)  int temp = foo(N);
   m ++;  for (j= 0 ; j < temp ; j ++)
   m ++;
答案：AC

---

### 2013期中-带答案 · 第七题 2)3)

> 出处：`原文/期中/2013期中-带答案.md` 第 414–438 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：CPE 下限与循环展开优化填空

2）假设读写访存指令延迟为20个时钟周期，其他指令延迟为2个时钟周期，所有分支预测都成功。同时
CPU包含足够多的部件来实现指令集并行，那么在最理想情况下CPE最低应该是多少（2分）？为什么（2
分）？
3）已知src对应字符串中每个字符c都满足0<c<=80且0<=delta<=5。通过下面的改写，可以把transform
程序CPE的理论下限降低一半，请填空。假设程序运行在小端法机器上。（每空1分）
void transform(char* src, char* tgt, char delta) {
  short x = ______________;
  while(*src && ____________) {
    *(short*)tgt = *(short*)src + x;
    src += 2;
    tgt += 2;
  }
  *(short*)tgt = __________ ? *(short*)src + delta : *(short*)tgt &_____________;
}
答案：
（1）  {while(*src) *tgt++ = *src++ + delta; *tgt = 0;}
（2）  42
每次循环的关键路径为 读内存、做加法、写内存，该路径需要42个时钟周期。
本题陷阱：同学可能会受书上的例子误导认为做加法可以和下一个时钟周期的读内存并行，使得
CPE降到40，但实际上因为src和tgt指向的位置可能重叠，我们不能把下一次迭代的读操作移动
到这一次的写操作之前。
（3）  (((short) delta) << 8) + delta
*(src+1)
0xFF00
*src

---

### 2014期中-带答案 · 第一题 13

> 出处：`原文/期中/2014期中-带答案.md` 第 230–239 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：程序性能说法辨析、循环展开代价（兼 Processor Arch）

13、下面关于程序性能的说法中，哪种是正确的？

A. 处理器内部只要有多个功能部件空闲，就能实现指令并行，从而提高程序性能。
B. 同一个任务采用时间复杂度为 O(logN) 算法一定比采用复杂度为 O(N) 算法的执行时间短
C. 转移预测总是能带来好处，不会产生额外代价，对提高程序性能有帮助。
D. 增大循环展开（loop unrolling）的级数，有可能降低程序的性能（即增加执行时间）

答：（　　　）

答案：D

---

### 2014期中-带答案 · 第一题 14

> 出处：`原文/期中/2014期中-带答案.md` 第 241–260 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器总是自动进行的代码优化

14、仅考虑以下代码，哪些程序优化总是被编译器自动进行？（假设 int i, int

<!-- ===== page 7 ===== -->

j, int A[N], int B[N], int m, int *p 都是局部变量，N 是一个整数型常量，int foo(int) 是一个函数）

![图](assets/期中/2014期中-带答案/page-07.png)

（图：第14题的"优化前 / 优化后"对照表，含 A、B、C、D 四组代码变换）

| | 优化前 | 优化后 |
| --- | --- | --- |
| A. | `for (j = 0 ; j < N ; j ++)`<br>`    B[i] *= A[j];` | `int temp = B[i];`<br>`for (j = 0 ; j < N ; j ++)`<br>`    temp *= A[j];`<br>`B[i] = temp;` |
| B. | `for (j = 0 ; j < N ; j ++)`<br>`    m += i*N*j;` | `int temp = i*N;`<br>`for (j = 0 ; j < N ; j ++)`<br>`    m += temp * j;` |
| C. | `i = foo(N);`<br>`j = foo(N);`<br>`if (*p != 0)`<br>`    m = j ;` | `j = foo(N);`<br>`if (*p != 0)`<br>`    m = j ;` |
| D. | `for (j = 0 ; j < foo(N) ; j ++)`<br>`    m ++;` | `int temp = foo(N);`<br>`for (j= 0 ; j < temp ; j ++)`<br>`    m ++;` |

答：（　　　）

答案：B

---

### 2014期中-带答案 · 第七题 1）

> 出处：`原文/期中/2014期中-带答案.md` 第 587–609 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：循环条件中重复调用 length 的效率问题与修改

第七题（10 分）

如下是使用 C 语言描述的链表结构的声明，链表的结尾使用空指针来表示。同时使用函数 int length (List *p) 来计算链表的长度。为简化起见，假设该链表是非循环的。

```c
typedef struct LIST {
    struct LIST *next;
    int data;
} List;
```

1）函数 count_pos1 用来计算链表中 data 为正数的元素个数，并将结果存放在地址 k。以下的程序可能存在问题导致效率很低或程序出错，请指出并修改。（4 分）

```c
void count_pos1 (List *p, int *k) {
    int i;
    for (i = 0; i < length(p); i++) {
        if (p->data > 0)
            *k++;
        p = p->next;
    }
}
```

---

### 2014期中-带答案 · 第七题 2）

> 出处：`原文/期中/2014期中-带答案.md` 第 611–611 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：删除循环变量以消除函数调用

2）为提高程序性能，可以考虑删除变量 i 以消除函数调用。请修改上述程序达到该目的。（2 分）

---

### 2014期中-带答案 · 第七题 3）

> 出处：`原文/期中/2014期中-带答案.md` 第 613–630 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：给定访存延时求内层循环 CPE 下限

3）上述程序内层循环的汇编片段如下所示。假设该链表不为空且大部分数据都为正数，转移预测全部正确，设计中有足够多的部件来实现指令并行。其中访存操作全部 cache 命中，时延为 3 cycle，其他指令时延为 1cycle。请计算以下程序的 CPE 下限，并给出文字说明。（4 分）

```
.L1:
    movl   4(%eax), %ecx
    testl      %ecx, %ecx
    jle    .L2
    incl       %edx
.L2:
```

<!-- ===== page 17 ===== -->

```
    movl   (%eax), %eax
    testl  %eax, %eax
    jne    .L1
```

---

### 2015期中-带答案 · 选择题 20

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 235–256 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器自动优化变换（别名/精度）

20. 以下哪些程序优化编译器总是可以自动进行？（假设int i, int j, int
A[N], int B[N], float m都是局部变量，N是一个整数型常量，int
foo(int) 是一个函数）
  优化前  优化后
A.  for (j = 0 ; j < N ; j ++)  int temp = i*N;
   m + = i*N*j;  for (j= 0 ; j < N ; j ++)
   m + = temp * j;
7

<!-- ===== page 8 ===== -->

B.  for (j = 0 ; j < N ; j ++)  int temp = B[i];
   B[i] *= A[j];  for (j= 0 ; j < N ; j ++)
   temp *= A[j];
B[i] = temp;
C.  for (j = 0 ; j < N ; j ++)  for (j = 0 ; j < N ; j ++)
   m = (m + A[j]) + B[j];     m = m + (A[j] + B[j]);
D.  for (j = 0 ; j < foo(N) ; j  int temp = foo(N);
++)  for (j= 0 ; j < temp ; j ++)
   m++;     m++;
答案：A
说明：考察procedure, memory aliasing，和floating 的精度问题

---

### 2016期中-带答案 · 第三题 (2)

> 出处：`原文/期中/2016期中-带答案.md` 第 318–345 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链表循环 CPE 与关键路径，填 C 代码

(2) 右边的汇编代码是由左边程序中的m函数编译而成。回答如下问题。
t  yspterduecft  s_tlriusctt*  _nleixstt;  {  m : testq  %rdi, %rdi
  int value;    je .L6
} i nlti smt(;l ist* p) {      mmtooevvsqlt  q  %($r%1dr0xd0,i, ) %,%r ed%axrx  dx
    iwnhti lre  =( _1_○010_;_ ) {     jjnmep  ..LL43
    r = __○2__;  .L14:
    p = __○3__;     mtoevsqt q  %(r%drxd,i )%,r d%xr dx
      }ir fe t(upr n! =r ; 0) r = __○4__;   .L4:j e .L3
}     m_o_○v5l_ _ 88((%%rrddxi)),,  %%rr88dd
  __○5__ %r8d, %eax
   mtoevsqt q  %(r%drid,x )%,r d%ir di
   jrneet  .L14
. L3:_ _○5__ 8(%rdi), %eax
 . L6:rm eotv l  $100, %eax
已知访存延迟1个指令周期。不访存的时候  adrdelt 延迟4个指令周期，imull延
10

<!-- ===== page 11 ===== -->

迟 8 个指令周期，其他指令延迟 1个指令周期。指令访存时延迟的执行周期为不
访存的时候延迟的指令周期和访存延迟的周期之和。函数m中的循环在处理链表p
的时候CPE为4个指令周期。○5处的指令为movl, addl, imull中的一个。请
填写○1-○5处的代码（○5空2分，其他3分）。
○1
○2
○3
○4
○5

---

### 2016期中-带答案 · 第三题 (2) 答案

> 出处：`原文/期中/2016期中-带答案.md` 第 351–360 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：CPE 与关键路径参考答案

(2) ○5空2分，其他3分
○1p != 0 && p->next != 0
○2r * (p->value * p->next->value) 注意：答案中运算可以交换，但不可
结合
○3p->next->next
○4r * p->value
○5imull （因为每次处理两个元素，所以关键路径的时间周期为 8。关键路径要
么为两次访存和两次 mov，要么为○5处的运算。前者不可能达到 8，所以只能是
imull。）
给分说明：如果○2○4的答案和○5一致，但是○5答错了就○2○4各给2分。

---

### 2017期中-带答案 · 第一题 12

> 出处：`原文/期中/2017期中-带答案.md` 第 153–168 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器不会做的程序优化

12. 假设已有声明int i, int j, const int n, int r, int a[n], int
b[n], int mul(int, int)以下程序优化编译器一般不会进行的是:
  优化前  优化后
A.  for (j = 0; j < n; ++j)  int tmp = (n << 3);
    a[n * 8] += b[j];  for (j = 0; j < n; ++j)
    a[tmp] += b[j];
B.  for (j = 0; j < n; ++j)  for (j = 0; j < n; ++j)
    r = (r * a[j]) * b[j];      r = r * (a[j] * b[j]);
C.  for (j = 0; j < n; ++j)  int ni = mul(n, i);
    a[mul(n, i) + j] = b[j];  for (j = 0; j < n; ++j)
    a[ni + j] = b[j];
D.  for (j = 1; j < n; ++j)  int tmp = 0;
    a[0] += a[j];  for (j = 1; j < n; ++j)
tmp += a[j];
a[0] += tmp;
答案: C

---

### 2018期中-带答案 · 第一题 11

> 出处：`原文/期中/2018期中-带答案.md` 第 178–208 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器总是可行的优化（别名/副作用）

11. 假设已有声明int i, int sum, int *p, int *q, int *r，const int n =
100, float a[n], float b[n], float c[n], int foo(int), void bar(),
以下哪项程序优化编译器总是可以进行？
float tmp;
for(i = 0; i < n; ++i) {
for(i = 0; i < n; ++i) {
  a[i] += b[i];
A    tmp = b[i] + c[i];
  a[i] += c[i];
  a[i] += tmp;
}
}
int tmp;
*p += *q;
B  tmp = *q + *r;
*p += *r;
*p += tmp;
int N = n * 4;
for(i = 0; i < n; ++i)
C  for(i = 0; i < N; i += 4)
    sum += i * 4;
    sum += i;
int tmp = foo(n);
for(i = 0; i < foo(n); ++i)
D  for(i = 0; i < tmp; ++i)
    bar();
    bar();
答案：C
A 浮点数不满足结合律
B p,q,r可能指向同一个地址
D foo函数可能有副作用

---

### 2019期中-带答案 · 第一题 12

> 出处：`原文/期中/2019期中-带答案.md` 第 212–223 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：程序优化相关陈述的正误

12. 针对程序优化，请挑出下面唯一正确的陈述：
A.  用add/sub和shift替代multiply/divide永远能提高程序的运行
速度。
B.  最有效的提高程序运行效率的方法是提高compiler的优化级别。
C.  跨procedure优化的障碍之一是因为使用了全局变量。
D.  程序中，*a += *b; *a += *b;永远可以用*a +=2*(*b);代替。
答案：C
解析：  A错因为如果cpu支持硬件乘除，则用add/sub来模拟乘除通常并不划
算。
B错因为优化算法更能提高运行效率。
C对
D错因为a和b可能指向同一数据。

---

### 2019期中-带答案 · 第一题 13

> 出处：`原文/期中/2019期中-带答案.md` 第 224–238 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：loop unrolling 的原理与代价

13. 对于loop-unrolling这种优化技巧，请指出下面哪一个陈述是错误的（一
个）：
A.  Loop-unrolling的原理是将尽量多的循环操作去掉相关性并重组，从
而提高循环操作的并行性。
B.  Loop-unrolling是一种将循环操作拆散的技术。
C.  Loop-unrolling可以利用目标处理器的并行处理能力。
D.  支持Loop-unrolling是有代价的，没有限制地增加并行支路数反而会
降低运算速度。
答案：B
解析：B是错误的因为简单地拆散loop并不能提高运行速度，只有拆散后做并行
6

<!-- ===== page 7 ===== -->

合并才能提高运行速度。

---

### 2020期中-带答案 · 第一题 8

> 出处：`原文/期中/2020期中-带答案.md` 第 125–149 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器可行优化与别名/副作用限制

8、仅考虑以下代码，哪个或哪些代码片段在当前主流编译器的标准优化选项下一
定会被优化？（假设int i, int j, int A[N], int B[N], int *p都是局
部变量，int foo(int) 是一个函数）B
  优化前  优化后
A.  for (j = 0 ; j < N ; j++)  int temp = B[i];
   B[i] *= A[j];  for (j= 0 ; j < N ; j++)
   temp *= A[j];
B[i] = temp;
B.  for (j = 0 ; j < N ; j++)  temp = i*N;
   m + = i*N*j;  for (j= 0 ; j < N ; j++)
   m + = temp * j;
C.  i = foo(N);
j = foo(N)+1;     m = j ;
if (i != j)
  m = j ;
D.  if(m==1){
   i=3;j=4;    m = 7;
}else{
   i=4;j=3;
}
m=i+j;
选项A中数组A和B可能存在别名
选项C中的函数可能会有副作用
选项D中i和j可能会被使用，原则上不应该删除i和j的定值
4

---

### 2021期中-带答案 · 第一题 14

> 出处：`原文/期中/2021期中-带答案.md` 第 240–260 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器总能进行的优化与别名/副作用/浮点

14. 假设已有声明int i, int j, float x, int y, const int n,
int a[n], int b[n], int *p, int *q int *r, int foo(int), 以
下哪项程序优化编译器总是可以进行：D
8

<!-- ===== page 9 ===== -->

A  for (i = 0; i < n; i++)  for (i = 0; i < n; i++)
    x = (x+ a[j]) + b[j]      x= x + (a[j] + b[j])
B  *p += *q  int tmp;
*p += *r  tmp = *q + *r
*p += tmp
C  for(i = 0; i < foo(n);  int tmp = foo(n)
i++)  for(i = 0; i < tmp; i++)
    sum += i;      sum += i;
D  for (i = 0; i < n; i++)  for (i = 0; i < n; i++)
    y = (y * a[j]) *      y = y * (a[j] *
b[j]  b[j])
A. 浮点数运算不具有结合性
B. pqr内存别名引用
C. 函数foo可能具有副作用

---

### 2021期中-带答案 · 第六题 4

> 出处：`原文/期中/2021期中-带答案.md` 第 670–688 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：2x2 循环展开的两个累积变量改写

4. 在学习了循环展开后，同学I想对func函数进行优化。他决定尝试模仿书上
2*2循环展开的方法，使用两个累积变量以提高代码并行性，请补全他改进后的函
数func1的代码。（1*4=4分）
float func1(s_element* p){
    float ans1 = 0, ans2 = 0;      //line 1
    while( p && ____①____){      //line 2
        ans1 += p->u1.f;            //line 3
        ans2 += _____②_____;      //line 4
        p = _____③______;        //line 5
    }
    if(_____④______)          //line 6
        ans1 += p->u1.f;       //line 7
    return ans1 + ans2;       //line 8
}
将要补全的代码填在下面：
① ________________
② ________________
③ ________________
④ ________________

---

### 2021期中-带答案 · 第六题 5

> 出处：`原文/期中/2021期中-带答案.md` 第 689–690 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：浮点加法不满足结合律导致的错误

5. 此时，同学C指出同学I的做法会导致新的错误，原因是_______________。
（2分）

---

### 2021期中-带答案 · 第六题 6

> 出处：`原文/期中/2021期中-带答案.md` 第 691–692 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：k*k 展开中 k 过大导致寄存器溢出

6. 同学S从书上读到，k * k循环展开在k很大时反而可能获得较差的效果，
这是因为k很大时会导致___________________。（2分）

---

### 2022期中-带答案 · 第一题 15

> 出处：`原文/期中/2022期中-带答案.md` 第 222–233 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：循环展开与编译优化的限制

15. 下面说法正确的是（    ）。
A. 随着循环展开次数越多，分支预测次数更少，指令调度空间更大，代码性能更
好。
B. 编译优化无法跨越函数调用和内存别名的阻碍。
C. 算法的渐进复杂度对于程序优化十分重要。
D. 由于处理器硬件带来的延迟界限（latency bound）是程序性能的终极限制。
答案：C
A循环展开次数增加会导致代码膨胀、增大寄存器压力，影响性能（课本5.11.1）。
B编译器能处理函数调用和内存别名，只是代价很高；（课本章节5.1用词“限制
了可能的优化”“大多数编译器不会”。此外，函数内联优化就是一个很好的反例）。
C很直白的正确的话，用来在这里坑一下喜欢猜答案的同学。
D吞吐量界限才是程序性能的终极限制（课本章节5.6最后一句话）。

---

### 2023期中-带答案 · 第一题 20

> 出处：`原文/期中/2023期中-带答案.md` 第 363–387 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：程序优化：循环展开与编译器优化限制

20.针对程序优化，下面说法正确的是:
A. 当处理器内部存在多个功能部件空闲时，就可以通过指令并行提高程序性能。
B. 循环展开的原理是将尽量多的循环操作去掉相关性并重组，展开次数越多，代
码性能更好。
C. a和b都是int*，*a+=*b;*a+=*b; 这段代码总是可以用 *a+=(*b)<<1;
代替。
D. 编译器不会将下面的代码自动优化
double ans;
double a[100][100];
for(int j=0;j<100;j++)
   for(int i=0;i<100;i++)
       ans+=a[i][j];
优化成:
double ans;
double a[100][100];
for(int i=0;i<100;i++)
   for(int j=0;j<100;j++)
       ans+=a[i][j];
答案：D
解析：
A. 错误。需要看具体的关键路径
B.  循环展开次数增加会导致代码膨胀、增大寄存器压力，影响性能（课本
5.11.1）。
C. a,b如果指向同一地址则出错
D. 正确，double没有结合律

---

### 2024期中-带答案 · 第一题 15

> 出处：`原文/期中/2024期中-带答案.md` 第 272–296 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：代码优化等价性判断（别名、副作用、strlen）

15.假设已有声明int a, int b, int i, int* pa, int* pb, float
fa, float fb, float fc, char s[100], int f(),以及
#include<string.h>，以下优化正确的是：
  原程序  优化程序
A  int c = *pa;  *pb ^= *pa;
8

<!-- ===== page 9 ===== -->

*pa = *pb;  *pa ^= *pb;
*pb = c;  *pb ^= *pa;
B  a = f();  a = f();
b = f();  int sum = a+a;
int sum = a+b;
C  int sum = 0;  int sum = 0;
for(i = 0; i <  int len = strlen(s);
strlen(s); ++i)  for(i = 0; i < len; ++i)
sum += s[i] - 'a';  sum += s[i] - 'a';
D  float ret =   float ret = (fa+fb)*fc;
fa*fc + fb*fc;
答案：C
A. pa和pb可能指向同一内存位置
B. f可能产生副作用
C. 正确，string.h中strlen无副作用
D. 浮点数运算不满足分配律

---

### 2013期末-带答案 · 第一题 7

> 出处：`原文/期末/2013期末-带答案.md` 第 94–117 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：同名全局变量导致的链接错误

7、下列程序运行的结果是什么？答：（       ）
/* main.c */
int i=0;
int main()
{
  foo();
  return 0;
}
3

![图](../../assets/期末/2013期末-带答案/p3-img1.jpg)

<!-- ===== page 4 ===== -->

/* foo.c */
int i=1;
void foo()
{
  printf(“%d”, i);
}
A. 编译错误                B. 链接错误
C. 段错误                  D. 有时打印输出1，有时打印输出0；
答案：B考点：链接的基本概念，符号解析的原则；
注：由于印刷版中引号的问题（现已修正），本题选A也算对

---

### 2013期末-带答案 · 第一题 8

> 出处：`原文/期末/2013期末-带答案.md` 第 118–125 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：哪些符号一定不需要重定位

8、在链接时，对于什么样的符号一定不需要进行重定位？答：（      ）
A．不同C语言源文件中定义的函数
B．同一C语言源文件中定义的全局变量
C．同一函数中定义时不带static的变量
D．同一函数中定义时带有static的变量
答案：C
说明：考察需要进行重定位的条件。A 在链接前不在同一目标文件中，BD 都位
于.data段中，这些都需要重定位。C位于栈中或者寄存器中，不需要重定位。

---

### 2013期末-带答案 · 第四题

> 出处：`原文/期末/2013期末-带答案.md` 第 371–423 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：弱/强符号属性、ELF section 与链接解析

 第四题（10分）
 考 虑如下两个程序（fact1.c和fact2.c）：
 /* fact1.c */
#idnetf itnaeb lMeA[XMNAUXMN U1M2] ;
iinntt  fmaacitn((iinntt  na)r;g c , char **argv) {
        ittnaatbb llnee;[[ 01]]  ==  01;;
i f (parrignct f=(=" E1r)r o{r :  missing argument\n");
 }  exit (0);
argv++;
i{ f (sscanf(*argv, "%d", &n) != 1 || n < 0 || n >= MAXNUM)
 *   a  r  gpevrx)ii;nt t f( 0()"; Error: %s not an int or out of range\n",
}p rintf("fact(%d) = %d\n", n, fact(n));
}
 /i*n tf*a ctta2b.lce ; */
i  n t  sftaactti(ci nitn tn )n u{m  = 2;
         i f   (inn t> =i  n=u mn)u m{;
                 w h i ltea b(lie [<i=]  n=)  t{a ble[i-1] * i;
            i++;
12

<!-- ===== page 13 ===== -->

        }
        num = i;
    }
    return table[n];
}
（1）对于每个程序中的相应符号，给出它的属性（局部变量、强全局变量或弱全
局变量），以及它在链接后位于ELF文件中的什么位置？（提示：如果某表项中的
内容无法确定，请画X）（6分）
fact1.c
变量  类型  ELF Section
table  weak global  .bss
fact  weak global  X（或.bss）
num  X  X
fact2.c
变量  类型  ELF Section
table  weak global  .bss
fact  strong global  .text
num  local  .data
（2）对上述两个文件进行链接之后，会对每个符号进行解析。请给出链接后下列
符号被定义的模块（fact1 or fact2）。（2分）
  定义模块
table  不确定
fact  fact2
num  fact2
（3）使用gcc（命令：gcc -o fact fact1.c fact2.c）来编译之后得到的
可执行文件是否能够正确执行？为什么？（2分）
不一定能正确执行。因为 table 在两个文件中都是 weak global，因此链
接器会任选一个定义来解析 table。而因为在 fact2 模块中只给 table 预留了
一个单字（4 字节）空间，因此如果选择了 fact2 来解析 table 的话，会出现
segmentation fault。【该问题已经过编译检查确认。】
考察知识点：linking的基本概念、符号属性、链接的过程、符号的解析等。

---

### 2014期末-带答案 · 第一题 5

> 出处：`原文/期末/2014期末-带答案.md` 第 93–100 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器安全优化策略

5.  根据编译器安全优化的策略，如下手工程序代码的优化，哪个达不到优化效果？
（    ）
A.  循环展开，以减少循环的迭代次数
B.  将函数调用移到循环内，以提高程序的模块性
C.  消除不必要的存储器引用，减少访存开销
D.  分离多个累计变量，以提高并行性
答案：B
（第五章）考察安全优化策略

---

### 2014期末-带答案 · 第一题 8

> 出处：`原文/期末/2014期末-带答案.md` 第 126–132 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态库链接与命令行顺序

8.  下列关于静态库链接的描述中，错误的是(      )
A.  链接时，链接器只拷贝静态库中被程序引用的目标模块
B.  使用库的一般准则是将它们放在命令行的结尾
C.  如果库不是相互独立的，那么它们必须排序
D.  每个库在命令行只须出现一次即可
【答案】D
【说明】如果相互调用的库，在命令行必须重复出现。

---

### 2014期末-带答案 · 第一题 9

> 出处：`原文/期末/2014期末-带答案.md` 第 133–148 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：static 全局变量影响的 ELF 节

9.  在foo.c文件中的函数外，如果添加如下一条语句：
       static int count = 0xdeadbeef;
  那么它在编译为foo.o后，会影响到ELF可重定位目标文件中的除.text以外
的那些字段？(      )
A. .rodata
B. .data,.symtab,
C. .data,.symtab,.rel.data
D. .rodata,.symtab,.rel.data
4

<!-- ===== page 5 ===== -->

【答案】B
【说明】这是一个本地静态全局变量，它在.data中占有位置，它不需要重定位，
因为它的初始值是确定的，但是它在符号表中占有一个位置。
考察ELF文件格式。

---

### 2014期末-带答案 · 第四题

> 出处：`原文/期末/2014期末-带答案.md` 第 455–533 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号强弱属性、静态库链接顺序与重定位

 第  四题（10分） 链接
  考虑如下3个文件：main.c, fib.c和bignat.c：
  /v*o imda ifni.bc  (*i/n t n);
int imnati nn  (=i n0t;  argc, char** argv) {
sfsicba(nnf)(; argv[1], "%d", &n);
}
  /* fib.c */
# define N 16
s tatic unsigned int ring[3][N];
statifinoctr   vi(o;ii  d=  pNr-i1n;t _ib i>g=n a0t;( uin-s-i)g ned int* a) {
p*r/ intf("%u ", a[i]); /* print a[i] as unsigned int
}  printf("\n");
voidi nfti bi ,( icnatr rny);  {
from_int(N, 0, ring[0]); /* fib(0) = 0 */
ffroorm _(iin t=( N0,;  1i,  <r=i nn-g2[;1 ]i)+;+ )/ *{  fib(1) = 1 */
crairnrgy[ (i+2=) %3]p)l;u s(N,  ring[i%3],  ring[(i+1)%3],
if ({c arrpyr)i n tf("Overflow  at  fib(%d)\n",  i+2);
}p rinetx_ibti(g0n)a;t (}r ing[n%3]);
  }
另外，假设在文件bignat.c中定义了如下两个函数plus和from_int（具体
定  义略）：
14

<!-- ===== page 15 ===== -->

int plus (int n, unsigned int* a, unsigned int* b, unsigned
int* c);
void from_int (int n, unsigned int k, unsigned int* a);
1. （5分）对于每个程序中的相应符号，给出它的属性（局部或全局，强符号或
弱符号）（提示：如果某表项中的内容无法确定，请画X。）
    main.c
  局部或全局？  强或弱？
fib
main
    fib.c
  局部或全局？  强或弱？
ring
fib
plus
2. （3分） 假设文件bignat.c被编译为一个静态库bignat.a，对于如下的
gcc调用，会得到什么样的结果（请选择）？
（A） 编译和链接都正确
（B） 链接失败（原因是包含未定义的引用）
（C） 链接失败（原因是包含重复定义）
命令  结果（A，B或C）
gcc -o fib main.c fib.c bignat.a
gcc -o fib bignat.a main.c fib.c
gcc -o fib fib.c main.c bignat.a
3. （2分）如果在文件fib.c中，程序员在声明变量ring时，不小心把它写成
了：
static int ring[3][N];
会不会影响这些文件的编译、链接和运行结果？为什么？
答案：
1. （5分）对于每个程序中的相应符号，给出它的属性（局部或全局，强符号或
弱符号）（提示：如果某表项中的内容无法确定，请画X。）
15

<!-- ===== page 16 ===== -->

main.c
  局部或全局？  强或弱？
fib  全局  弱
main  全局  强
fib.c
  局部或全局？  强或弱？
ring  局部  X
fib  全局  强
plus  全局  弱
2. （3分） 假设文件bignat.c被编译为一个静态库bignat.a，对于如下的
gcc调用，会得到什么样的结果（请选择）？
（A） 编译和链接都正确
（B） 链接失败（原因是包含未定义的引用）
（C） 链接失败（原因是包含重复定义）
命令  结果（A，B或C）
gcc -o fib main.c fib.c bignat.a  A
gcc -o fib bignat.a main.c fib.c  B
gcc -o fib fib.c main.c bignat.a  A
3. 对编译、链接和执行结果都没有影响。因为signed和unsigned之间的转换
不会改变整数的表示形式，因此函数调用会正常进行。

---

### 2015期末-20160104-带答案 · 第一题 4

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 66–73 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态库链接的规则与命令行顺序

4.  以下关于静态库链接的描述中，正确的是：
A. 链接时，链接器会拷贝静态库中的所有目标模块。
B. 使用库的时候必须把它们放在命令行的结尾处。
C. 如果库不是相互独立的，那么它们必须排序。
D. 每个库在命令行只须出现一次即可。
【答案】C。
解释：A: 链接时只需拷贝用到的目标模块；B：静态库也可以放在目标文件的前
面；C: 正确；D：如果相互调用的库，在命令行必须重复出现。

---

### 2015期末-20160104-带答案 · 第一题 5

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 74–85 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：字符串常量被放入哪个 ELF 节

5.  在foo.c文件中包含如下代码：
int foo(void) {
int error = printf("You ran into a problem!\n");
return error;
}
经过编译和链接之后，字符串"You ran into a problem!\n"会出现在哪个
段中？
A. .bss
B. .data
C. .rodata
D. .text
【答案】C.

---

### 2015期末-20160104-带答案 · 第一题 12

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 184–190 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译器安全优化策略

12. 根据编译器安全优化的策略，如下手工程序代码的优化，哪个达不到优化效
果？
A.  循环展开，以减少循环的迭代次数
B.  消除不必要的存储器引用，减少访存开销
C.  将函数调用移到循环内，以提高程序的模块性
D.  分离多个累计变量，以提高并行性
答案：C

---

### 2015期末-20160104-带答案 · 第四题

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 459–518 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号强弱属性、类型声明冲突与数据布局

 第四题（10分）链接
   在x86_64环境下，考虑如下2个文件：main.c和foo.c：
  /* main.c */
# lionncglluodneg  <_s_t_d_i_o_._h_>__ ______________;
c onst char* foo(int);
i nt imnati nn( i=n t0a;r gc, char **argv){
  sscanf(argv[1], "%d", &n);
   pprriinnttff((f"o%ol(lnx)\)n;",  a);
  }/*  foo.c */
# include <stdio.h>
  int a[2];
s tatiinct  vsowiadp psewra;p per(intnum){
   i f (snwuamp p%e r2 )={  a[0];
      aa[[01]]  ==  as[w1a]p;pe r;
 }  }
c onsssttw aactphipacer r*c( hnfauormo )(o;iu ntt_nbuumf)[{5 0];
16

<!-- ===== page 17 ===== -->

   srpertiunrtnfo(uotu_tb_ubfu;f , "%x\n", ________________________);
}
 1. 对于每个程序中的相应符号，给出它的属性（局部或全局，强符号或弱符号）
（提示：如果某表项中的内容无法确定，请画X。）
main.c    局部或全局？  强或弱？
af oo
foo.c    局部或全局？  强或弱？
afo ouot _buf
 2. 根据如下的程序运行结果，补全程序【在程序空白处填空即可】。
$$b  fg.fc/ectd ee-saotd   t1 est main.cfoo.c
cafebffedeadbeef
 $ ./test 2
bdeeeafdcbaefeef cafebffe
 3. 现在有一位程序员要为这个程序编写头文件。假设新的头文件名称为 foo.h，
内ex容te如r下n ：lo ng long a;
e然x后te在rnm acihna.rc *和fofoo(oi.nct中);分 别引用该头文件，请问编译链接能通过吗？请
说明理由。
17

<!-- ===== page 18 ===== -->

答案：
1. （5分）对于每个程序中的相应符号，给出它的属性（局部或全局，强符号或
弱符号）（提示：如果某表项中的内容无法确定，请画X。）
（每格0.5分）
main.c
  局部或全局？  强或弱？
A  全局  强
foo  全局  弱
foo.c
  局部或全局？  强或弱？
A  全局  弱
foo  全局  强
out_buf  局部  X
2. （3分）根据程序运行结果，补全程序
long longa = 0xdeadbeefcafebffe; （1分）
*(int*)((unsigned long long)a + 2) （2分）
3. 请问编译链接能通过吗？请说明理由。
不能。无论如何声明a的类型都会造成在至少一个文件内引起声明和定义冲突。
结论1分，理由2分。（结论错不得分）

---

### 2016期末-带答案 · 第一题 5

> 出处：`原文/期末/2016期末-带答案.md` 第 90–103 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：strlen 外提优化与程序局部性

5.  对于下面这段程序，哪个描述是正确的：_________
void upper(char *s)
{
  for(int i=0; i<strlen(s); i++)
    if(s[i]>=’a’ && s[i]<=’z’)
s[i] +=(‘A’-‘a’);
}
A．假设s的长度为N，该程序的时间复杂度为O(NlogN)
B．将“for(int i=0; i<strlen(s); i++){}”修改为:
  “int len = strlen(s); for(int i=0; i<len; i++){}”
可以使程序运行时间与S的长度线性相关
C．B选项中的修改策略不影响程序的空间局部性与时间局部性
D．B选项中的修改策略仅影响程序的空间局部性，不影响时间局部性
答案： B （考察程序性能优化与程序局部性原理）

---

### 2016期末-带答案 · 第一题 7

> 出处：`原文/期末/2016期末-带答案.md` 第 119–129 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：同名全局变量的符号解析与 extern

7.  C源文件f1.c 和 f2.c的代码分别如下所示，编译链接生成可执行文件后
执行，输出结果为（ ）
A. 100     B. 200
C//.  f210.1c      D. 链接错误  //f2.c
#sitnactliucd ei n<ts tvdairo .=h >10 0;  i nt var = 200;
i{n t main(void)  v{o id f()
        eexxtteerrnn  ivnoti dv afr( ); ;    }    var++;
        fp(r)i n;tf ("%d\n", var) ;
 }    return 0;
答案：A（f1.c中的extern int var, 会搜索f1.c之前定义过的全局变量, 因
为  之前已经已经有了var的定义，所以printf会打印该var的值100）

---

### 2016期末-带答案 · 第一题 8

> 出处：`原文/期末/2016期末-带答案.md` 第 130–149 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：.data/.bss 布局与变量地址顺序

8.  C 源文件 m1.c 和 m2.c 的代码分别如下所示，编译链接生成可执行文件后
执行，结果最可能为 (  )
$ gcc –o a.out m2.c m1.c ; ./a.out
0x1083020
A. 0x1083018, 0x108301c     B. 0x1083028, 0x1083024
C. 0x1083024, 0x1083028     D. 0x108301c, 0x1083018
/# /i nmc1l.ucd e <stdio.h>  /i /nmt2 .ac4  = 10 ;
iinntt  aa12  ;=  2 ;  i{n t main()
extern int a4 ;      extern void hello() ;
 v{ oid hello()           hreeltluor(n)  0; ;
    printf("%p ", &a1);  }
4

<!-- ===== page 5 ===== -->

    printf("%p ", &a2);
    printf("%p\n", &a4);
}
答案：D（a2和a4在.data中, a1在.bss中, 按照布局, .data地址比.bss
要小, 又由于m2.c的编译先于m1.c, 故选D不选A ）

---

### 2016期末-带答案 · 第四题

> 出处：`原文/期末/2016期末-带答案.md` 第 405–469 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：强/弱符号属性表与多文件链接运行输出

 第四题（10分）
在/* xm8a6i_n.6c4 环*/境  下，考虑如下4个文件（main.c, value.c, f1.c, f2.c）：
# eixntcelrund ev o<isdt dfi_ov.ohi>d_ void();
ev xotiedr n* fi; nt f_int_void();
i{  n  t  imnati na( )=  1, b, c;
      f = (void *)f_void_void;
            (bp( rv=io ni(td(f i((n"*tb)  ((=i* n)%t(d))\))nff")),(( a)b););;
      f = (void *)f_int_void;
  p  r  i  n(ct( fv=(o "i(cd(  i=(n *t%) d((\)*n))"f(,)i (ncat)));;) f )(a);
  }    return 0;
 /i*n tv aBlIuGe; .c */
 /#*i nfc1l.ucd e* /< stdio.h>
 eixntte rsnm ailnlt  =B I1G; ;
 v  o i ds mfa_lvlo i+d=_ v1o;i d() {
  }       BpIrGi n+t=f (1";sm all = %d, BIG = %d\n", small, BIG);
12

<!-- ===== page 13 ===== -->

 /* f2.c*/
# include <stdio.h>
esxttaetrinc  iinntt  BsImGa;l l;
 int f_int_void() {
        sBmIaGl l+ =+ =1 ;1 ;
        prreitnutrfn( "ssmmaallll  +=  1%;d , BIG = %d\n", small, BIG);
}
使gc用c 命-o令  main main.c f1.c f2.c value.c
编  译这四个文件。
使./用ma in
运  行编译好的程序。
1. 对于程序中的相应符号，请给出它的属性（局部或全局，强符号或弱符号），不
确定的请画X。
源ma文in件.c        符f 号名      局部或全局？    强符号或弱符号？
vfa1l.uc e.c        BsmIaGl l
f2.c       small
2sm. a请ll补 全= 程__序_运__行, 的B输IG出 =， 不__确__定_的 请画X。
small = _____, BIG = _____
b = _____
small = _____, BIG = _____
small = _____, BIG = _____
c = _____
！！！！答案
13

<!-- ===== page 14 ===== -->

1. （4 分）对于程序中的相应符号，请给出它的属性（局部或全局，强符号或弱
符号），不确定的请填X。
源文件      符号名      局部或全局？    强符号或弱符号？
main.c     f        全局        弱符号
value.c     BIG       全局        弱符号
f1.c       small      全局        强符号
f2.c       small      局部        X
评分标准：每空0.5分
2. （6分）请补全程序运行的输出，不确定的请填X。
small = 2, BIG = 1
small = 3, BIG = 2
b = X
small = 1, BIG = 3
small = 2, BIG = 4
c = 3
评分标准：small和BIG的值每空0.5分【取整，错1-2个扣1分，错3-4个
扣2分，以此类推】，b和c的值每空1分
b值无法确定，是因为传入参数无法确定。
！！！！答案结束

---

### 2017期末-无答案 · 第一题 7

> 出处：`原文/期末/2017期末-无答案.md` 第 92–107 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：跨文件符号类型不一致的链接结果

7.  C源文件f1.c 和 f2.c的代码分别如下所示：
// f1.c  //f2.c
#include <stdio.h>  float x ;
void f();  void f()
int x ;  {
int main(void)      x = 2 ;
{  }
x = 1;
f() ;
    printf("%x\n", x) ;
    return 0;
}
运行下面的命令后得到的结果是:
$ gcc f1.c f2.c
$ ./a.out
A. 1    B. 2    C. 3f800000    D. 40000000

---

### 2017期末-无答案 · 第一题 8

> 出处：`原文/期末/2017期末-无答案.md` 第 108–112 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号解析规则与静态库链接

8.  下面关于链接的说法，正确的是：
A. Linux链接器在处理多重定义的同名弱符号时，选择链接时遇到的第一个符号
B. 链接发生在源代码编译之后、可执行目标程序运行之前
C. C程序静态局部变量和静态全局变量都在ELF可重定位目标文件的.data段
D. 链接器构造可执行目标文件时，只复制静态库里被应用程序引用的目标模块

---

### 2017期末-无答案 · 第四题

> 出处：`原文/期末/2017期末-无答案.md` 第 321–348 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：强弱符号多重定义与链接成功原因（兼 GC 根指针）

 第四题（10分）
考虑以下三个文件：
 polygon.h                            main.c（函数中部分内容折叠）
strufclto aNto dpeo s{[ 2];  #niondcel*u dreo o"tp_opltyrg o;n .h"
issntttrr uumccattr  kNNeooddd;ee**   pnreexvt;;   int nimonadiietn*(( ))p;{;
};  p=alloc();
t ypedef struct Node node;  r.o.o.t _ptr =p;
nvvooodiiedd*   igancli(lt)o(;c) (;) ;  g.rc.e(.t)u  ;rn  0;
      }
 gc.c（函数体被折叠）
##idnecfliundee  N" p(o1l<y<g2o0n). h"
ssttaattiicc  nnooddee *p oflryegeo_np t[rN ];;
svtoaitdi cm anrokd(en*o dreo*o tv_)p{t.r. .;}
vvvoooiiiddd   sgiwcne(ie)tp (({)).  .{{...}.. ..}}
node* alloc() {...}
 使  用命令gcc –o polygon main.c gc.c得到可执行文件polygon。
  11

<!-- ===== page 12 ===== -->

1. 对于每个程序中的相应符号，给出它 的属性（局部或全局，强符号或弱符号）
mai提n.示c ：如果某表项中的内容无法确定，请画X。
 rooitn_iptt r     局部或全局？     强或弱？
gc.c    maiNn       局部或全局？     强或弱？
  poallylgoocn
 2  . 解释为何其中一些符号被定义了多次，链接器仍然可以成功创建可执行文件。
 3. gc.c 的功能是实现一个垃圾收集器。解释为何前面的命令能够编译、链接成
   功，但得到的执行文件中却存在潜在错误。并试提出如何修复这一bug。

---

### 2018期末-带答案 · 第一题 4

> 出处：`原文/期末/2018期末-带答案.md` 第 105–122 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链接、打桩与符号解析与重定位

4.  下列关于链接技术的描述，错误的是（  ）
A． 在 Linux 系统中，对程序中全局符号的不恰当定义，会在链接时刻进行报告。
B． 在使用Linux的默认链接器时，如果有多个弱符号同名，那么会从这些弱符号
中任意选择一个占用空间最大的符号。
3

<!-- ===== page 4 ===== -->

C． 编译时打桩（interpositioning）需要能够访问程序的源代码，链接时打桩需
要能够访问程序的可重定位对象文件，运行时打桩只需要能够访问可执行目标
文件。
D． 链接器的两个主要任务是符号解析和重定位。符号解析将目标文件中的全局符
号都绑定到唯一的定义，重定位确定每个符号的最终内存地址，并修改对那些
目标的引用。
答案：选A。参考机械工业出版社第三版中文教材，四个选项分别对应P464第5自
然段、P471页文末、P494页文末、P496文末的文字。其中选项B略有调整，增加
了“占用空间最大的”，是Linux binutils中链接器实现的原则，仍是正确选项。
A错误是因为全局符号的不恰当定义并不总会报警（甚至不报告warning）。

---

### 2018期末-带答案 · 第三题 1

> 出处：`原文/期末/2018期末-带答案.md` 第 295–323 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：各符号的 .symtab 条目、类型与所在节

第三题（10分）
本题基于下列m.c及foo.c文件所编译生成的m.o和foo.o，编译过程未加优化选
项。
//m.c  //foo.c
void foo();  extern int buf[];
int buf[2] = {1, 2};  int *bufp0 = &buf[0];
int main(){  int *bufp1;
    foo();  void foo(){
    return 0;  static int count = 0;
}  int temp;
  bufp1 = &buf[1];
temp = *bufp0;
*bufp0 = *bufp1;
*bufp1 = temp;
count++;
}
对于每个foo.o中定义和引用的符号，请用“是”或“否”指出它是否在模块foo.o
的.symtab节中有符号表条目。如果存在条目，则请指出定义该符号的模块（foo.o
或m.o）、符号类型（局部、全局或外部）以及它在模块中所处的节；如果不存在条
目，则请将该行后继空白处标记为“/”。
第一问每行1分，该行全部答对才给分数，节名如果漏了“.”可以算对。
用英文回答的，如果正确也可以给分。
符号  .symtab条目?  符号类型  定义符号的模块  节
bufp0  是  全局  foo.o  .data
buf  是  外部  m.o  .data
bufp1  是  全局  foo.o  COMMON
foo  是  全局  foo.o  .text
temp  否  /  /  /
cnt  是  局部  foo.o  .bss

---

### 2018期末-带答案 · 第三题 2

> 出处：`原文/期末/2018期末-带答案.md` 第 324–392 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：反汇编中的重定位条目与引用值计算

下图左边给出了m.o和foo.o的反汇编文件，右边给出了采用某个配置链接成可执
行程序后再反汇编出来的文件。根据答题需要，其中的信息略有删减。
0000000000......<main>:  0000000000000fe8 <main>:
55                    push    %rbp  fe8:  55                    push   %rbp
10

<!-- ===== page 11 ===== -->

48 89 e5                mov      %rsp,%rbp  fe9:  48 89 e5             mov    %rsp,%rbp
b8 00 00 00 00      mov      $0x0,%eax  fec:  b8 00 00 00 00      mov    $0x0,%eax
e8 00 00 00 00      callq   e <main+0xe>           ①  ff1:  e8       ①            callq   1000 <foo>
b8 00 00 00 00      mov      $0x0,%eax  ff6:  b8 00 00 00 00      mov    $0x0,%eax
5d                          pop      %rbp  ffb:  5d                     pop    %rbp
c3                          req  ffc:  c3                     retq
  ......略去部分和答题无关的信息......
0000000000......<foo>:  0000000000001000 <foo>:
55                            push    %rbp  1000:  55                    push   %rbp
48 89 e5                   mov      %rsp,%rbp  1001:  48 89 e5             mov    %rsp,%rbp
48 c7 05 00 00 00 00 00 00 00 00  1004:  48 c7 05 ?? ?? ?? ?? ?? ?? ?? ??
                        movq      $0x0,0x0(%rip)         movq      ②  ,  ③
③②  (%rip)
48 8b 05 00 00 00 00 mov      0x0(%rip),%rax       ④  100f:  48 8b
8b 00                     mov      (%rax),%eax  05 ?? ?? ?? ??  mov      0x????(%rip),%rax
89 45 fc                    mov      %eax,-0x4(%rbp)  1016:  8b 00                  mov    (%rax),%eax
48 8b 05 00 00 00 00 mov      0x0(%rip),%rax       ⑤  1018:  89 45 fc              mov    %eax,-0x4(%rbp)
48 8b 15 00 00 00 00 mov      0x0(%rip),%rdx       ⑥  101b:  48 8b 05 ?? ?? ?? ?? mov      ⑤  (%rip),%rax
8b 12                         mov      (%rdx),%edx  1022:  48 8b 15 ?? ?? ?? ??  mov    0x????(%rip),%rdx
89 10                         mov      %edx,(%rax)  1029:  8b 12                  mov    (%rdx),%edx
48 8b 05 00 00 00 00 mov      0x0(%rip),%rax       ⑦  102b:  89 10                  mov    %edx,(%rax)
8b 55 fc                     mov      -0x4(%rbp),%edx  102d:  48 8b 05 ?? ?? ?? ?? mov    0x????(%rip),%rax
89 10                         mov      %edx,(%rax)  1034:  8b 55 fc               mov    -0x4(%rbp),%edx
8b  05  00  00  00  00        mov        0x0(%rip),%eax      1 037:  89 10                  mov    %edx,(%rax)
⑧  1039:  8b 05 ?? ?? ?? ??      mov
83 c0 01                     add      $0x1,%eax  0x????(%rip),%eax
89  05  00  00  00  00        mov        %eax,0x0(%rip)      1 03f:  83 c0 01               add    $0x1,%eax
⑨  1042:  89 05 ?? ?? ?? ??    mov    %eax,  ⑨  (%rip)
90                               nop  1048:  90                      nop
5d                               pop      %rbp  1049:  5d                      pop    %rbp
c3                               retq 104a:  c3                      retq
  ......略去部分和答题无关的信息......
0000000000002330 <buf>:
......略去部分和答题无关的信息......
0000000000002338 <bufp0>:
......略去部分和答题无关的信息......
0000000000003024 <count.1837>:
......略去部分和答题无关的信息......
0000000000003028 <bufp1>:
在上图中对所涉及到的重定位条目进行用数字①至⑨进行了标记，请根据下表中所
提供的重定位条目信息，计算相应的重定位引用值并填写下表。
编号  重定位条目信息  应填入的重定位引用值
r.offset = 0xa              r.symbol = 本题不提供
①  0a 00 00 00
r.type = R_X86_64_PC32     r.addend = -4
r.offset = 0xb              r.symbol = buf
②  0x2334
r.type = R_X86_64_32       r.addend = +4
③  r.offset = 0x7              r.symbol = bufp1
0x2019
11

<!-- ===== page 12 ===== -->

r.type = R_X86_64_PC32     r.addend = -8
r.offset = 0x1e             r.symbol = bufp0
⑤  0x1316
r.type = R_X86_64_PC32     r.addend = -4
r.offset = 0x44             r.symbol = 本题不提供
⑨  0x1fdc
r.type = R_X86_64_PC32     r.addend = -4

---

### 2019、2020期末-答案解析 · 2020 选择题 7

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 27–29 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译期打桩、ABS 节与 -fPIC

7. D。只有编译时打桩需要访问源代码，A错误。B，可执行目标文件中仍然会有ABS节（文件
名）。程序的入口是_start，后者跳到题干所说的位置，C错误。D是正确的（书P489原
话），但是-fPIC（大写）选项更好。

---

### 2019、2020期末-答案解析 · 2020 选择题 8

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 30–32 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：跨模块同名符号类型不一致

8. B。请注意编译器看不到两边x类型的不同，因此不会报错。链接器会将x初始化为0，在
f1.c中编译器生成的代码视其为浮点而在另一边视其为整数，所以自增结果是一个很小的
浮点数，转为整数是0。

---

### 2019、2020期末-答案解析 · 2020 解答题二 1

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 93–101 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表与各符号所属节

解答题二
1. 答案如下：
符号 .symtab 有条目？ 符号类型 定义符号的模块 节
buf 有 外部 m.o .data
bufp0 有 全局 swap.o COMMON
count 有 局部 swap.o .bss
func 有 全局 swap.o .text
temp 无 / / /
送分题。注意外部符号要填定义的模块中的节。

---

### 2019、2020期末-答案解析 · 2020 解答题二 2

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 106–112 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：重定位地址计算与小端立即数

2. 0x00002020, 0x000000be, 0x0000a000, 0x0000900d, 0x00decade。
1处，ADDR=1000, offset=a, addend=-4，结果为302e-1000-a-4=0x00002020。3
处类似，结果为10e4-1000-22-4=0x000000be。4处结合汇编代码知道目标符号是buf
的地址移入，所以是0x0000a000（绝对重定位）。9处对应bufp1，下一条指令地址是知道
的，可以不用重定位算法，所以是a250-1243=0x0000900d。11处对应count，下一条指
令地址也是知道的，所以是dedd38-125a=0x00decade。具体填要注意小端法和立即数格
式。

---

### 2019、2020期末-答案解析 · 2019 选择题 6

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 164–166 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：对引用而非符号谈重定位

6. C。实际上对符号谈重定位是不正确的，应当对引用谈重定位，例如全局变量如果初始化为
值且不使用，则不需要重定位。需要留意，如果是同一C语言源文件中定义的函数则一般不
需要重定位。

---

### 2019、2020期末-答案解析 · 2019 解答题一 1-2

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 196–197 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：CPE 与循环执行周期数

1. 8，送分题。
2. 48周期，即8×6。

---

### 2019、2020期末-答案解析 · 2019 解答题一 4-5

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 200–215 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：循环展开与指令重排降低周期

4. 42周期。因为只有前两个addq可以一次执行完，这样能节省8周期的时间。
5. 26周期。指令顺序可重新安排为
.L2:
movq (%rdi), %rbx
movq 8(%rdi), %rdx
addq %rbx, %rax
addq $16, %rdi
addq $2, %rcx
addq %rdx, %rax
第6页,共8页

<!-- ===== page 7 ===== -->

cmpq $8, %rcx
jl .L2
此时每次循环只需要6周期，一共4次循环，即24周期，补上两次miss的惩罚得到26周期。

---

### 2019、2020期末-答案解析 · 2019 解答题二

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 216–232 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表、强弱符号与重定位计算

解答题二
1. 答案如下：
符号 .symtab 有条目？ 符号类型 节 强弱符号
bufp1 有 全局 .data 强
buf 有 外部 UNDEF 弱
bufp0 有 全局 COMMON 弱
temp 无 / / /
count 有 局部 .bss 非强非弱
送分题。注意外部符号要填foo.o中的节，extern的变量严格说不能区分强弱，但是如果
要问则回答“弱”。
2. 未知；bufp1.foo。弱弱选弱，强弱选强。
3. 0x000000be, 0x0000a000, 0x0000900d, 0x0000babe。
1处，ADDR=f28, offset=16, addend=-4，结果为1000-f28-16-4=0x000000be。2处
结合汇编代码知道目标符号是buf的地址移入，所以是0x0000a000（绝对重定位）。6处对应
bufp1，下一条指令地址是知道的，可以不用重定位算法，所以是a050-1043=0x0000900d。
9处对应count，下一条指令地址也是知道的，所以是cb24-1066=0x0000babe。具体填
要注意小端法和立即数格式。

---

### 2019期末-无答案 · 第一题 6

> 出处：`原文/期末/2019期末-无答案.md` 第 88–93 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链接时哪些符号需要重定位

6.  在链接时，对于下列哪些符号需要进行重定位？
(1) 不同C语言源文件中定义的函数
(2) 同一C语言源文件中定义的全局变量
(3) 同一函数中定义时不带static的变量
(4) 同一函数中定义时带有static的变量
A. (1)(3)    B. (2)(4)    C. (1)(2)(4)    D. (1)(2)(3)(4)

---

### 2019期末-无答案 · 第三题

> 出处：`原文/期末/2019期末-无答案.md` 第 290–378 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表、强弱符号与重定位引用值

第三题（10分）
本题基于下列m.c及foo.c文件所编译生成的m.o和foo.o，编译和运行
在x86-64/Linux下完成，编译过程未加优化选项。
//m.c  //foo.c
void myswap();  extern int buf[];
char buf[2] = {1, 2};  char *bufp0;
void *bufp0;  ......//略去题目无关代码
void *bufp1;  char *bufp1 = &buf[1];
char temp;  void myswap(char temp){
int main(){  static int count = 0;
......//略去题目无关代码
......//略去题目无关代码
myswap(temp);  bufp0 = &buf[0];
......//略去题目无关代码  temp = *bufp0;
    return 0;  ......//略去题目无关代码
}  *bufp0 = *bufp1;
  *bufp1 = temp;
......//略去题目无关代码
count++;
}
（1）  对于每个foo.o中定义和引用的符号，请用“是”或“否”指出它是
否在模块foo.o的.symtab节中有符号表条目。如果存在条目，则请指出在
模块foo.o中的符号类型（局部、全局或外部）、它在foo.o模块中所处的
节（.data、.text、.bss 或 COMMON）以及其强弱信息（强、弱、非强非
弱）；如果不存在条目，则请将该行后继空白处标记为“/”（请将下表画到答
题纸上）。
符号  .symtab条目?  符号类型  节  强弱
bufp1  是  全局  .data  强
buf
bufp0
temp
count
（2）  我们使用 REF(myswap.m)->DEF(myswap.foo)表示链接器将把
模块m中对符号myswap的任意引用与模块foo中对swap的定义关联起来。
对于下面的示例，用这种方法来说明链接器如何解析每个模块对多重定义符号
的引用。如果有链接时错误，请标记“错误”。如果链接器从定义中任意选择一
个，请标记“未知”。
a) REF(bufp0.m)  ->DEF(________________)
b) REF(bufp1.m)  ->DEF(________________)
（3）  下图左边给出了m.o和foo.o的反汇编文件，右边给出了采用某个
配置链接成可执行程序后再反汇编出来的文件。根据答题需要，其中的信息略
有删减。
9

<!-- ===== page 10 ===== -->

0000000000......<main>:  0000000000000f28 <main>:
5458   8 9   e 5                          mpouvs h      %%rrbspp, %rbp  ff2289::    5458   8 9   e 5                           pmuosvh       %%rrsbpp, %rbp
4.8. .8.3. .e c 10         sub     $0x10,%rsp  f.2.c.:. . .4略8去 8部3 分ec和 答10题  无  关  的  信 s息u.b.  . . . .$ 0x10,%rsp
be88  0000  0000  0000  0000           m ocva l l q  $ 01xa0 ,<%meaaixn +0x1a>    ff 33 8d ::        be88  00   0 0  0 0  ①00           m o v       $ 0cxa0l,l%qe a x1 000
①  <myswap>
......  ......略去部分和答题无关的信息......
c9                   leaveq  ffd:  c9                     leaveq
c 3                   req  f.f.e.:. . .c略3去   部 分  和  答  题  无   关 的  信  息 r.e.t.q. ..
0000000000......<myswap>:  0000000000001000 <myswap>:
55                   push   %rbp  1000:  55                    push   %rbp
4.8. .8.9. .e 5             mov    %rsp,%rbp  1.0.0.1.:. . 略4去8 部89分 e和5答  题  无  关  的  信  息 m.o.v. . .  .% rsp,%rbp
4  8   c 7    0 5   0  0   0 0   0  0   0 0  00 00 00 00  1m0o0vdq :    4  8② c 7  ,005x ????? ??(?% r?i?p )? ? ?? ?? ?? ??
movq   $0x0,0x0(%rip)        ③②  10051 8?:?  ?? ?? ?? mo v    0x????(4%8r ip),%rax  8b
4④08f   8bb6  0050  0 0    0 0   0 0   0 0   mmoovv z b l  0(x%0r(a%xr)i,p%)e,a%xr ax    11 00 11 f8::    08f8  b465  00f c                       m o v z bmlo v( % r a x%)e,a%xe,ax-
8.8. .4.5. .f c              mov    %al,-0x4(%rbp)  0.x.4.(.%.r.略bp去) 部分和答题无关的信息......
4⑤8  8b 05 00 00 00 00 mov    0x0(%rip),%rax    10 0x 3? 5?:? ?(% ri4p8) ,%r8abx   05  ??  ??  ??  ??  mov
48 8b 15 00 00 00 00 mov    0x0(%rip),%rdx    1 0 3 c:  48 8b 15 ?? ?? ?? ?? mov     ⑥
⑥  (%rip),%rdx
08f8  b160   1 2                             mmoovv z b l  %(d%lr,d(x%)r,a%xe)d x  1(0%4r3d:x ), %0efd x b6 12               movzbl
4⑦8  8b 05 00 00 00 00 mov    0x0(%rip),%rax    11 00 44 68::   8 8 1408     8 b     0 5     ?  ?   m?o?v    ? ?% dl,?(?% ramxo)v
0f b6 55 fc           movzbl -0x4(%rbp),%edx  0x????(%rip),%rax
8.8. .1.0. .                 mov    %dl,(%rax)  100x44f(:% rb p0)f, %ebd6x  55 fc           movzbl -
8⑧b  05 00 00 00 00    mov    0x0(%rip),%eax    1. 0. 5. 3.:. . 略8去8 部10分  和  答  题  无  关  的  信  息  .m.o.v. . .   %dl,(%rax)
83 c0 01              add    $0x1,%eax  100x5?7?:? ?( %r8ibp ),0%5e ax? ?  ??  ??  ??            mov
8⑨9  05 00 00 00 00    mov    %eax,0x0(%rip)    1 0 5 d:  83 c0 01               add    $0x1,%eax
90                     nop  1060:  89 05 ?? ?? ?? ??    mov    %eax,  ⑨
5d                     pop    %rbp  (1%0r6i6p:)   90                      nop
c 3                     retq  1067:  5d                      pop    %rbp
1.0.6.8.:. . 略c去3 部  分  和  答  题  无  关  的  信  息  . r.e.t.q..
0.0.0.0.0.0.略00去00部00分a和00答0题 <无bu关f>的:信 息......
0.0.0.0.0.0.略00去00部00分a和05答0题 <无bu关fp的1信>:息 ......
0.0.0.0.0.0.略00去00部00分c和b2答4题 <无co关un的t信.1息83.7.>.:.. .
0.0.0.0.0.0.略00去00部00分c和b2答8题 <无bu关fp的0信>:息 ......
在上图中对所涉及到的重定位条目进行用数字①至⑨进行了标记，请根据下表
中所提供的重定位条目信息，计算相应的重定位引用值并填写下表。（请将下
表的第1列和第3列画到答题纸上）
编号  重定位条目信息  应填入的重定位引用值
r.offset = 0x16             r.symbol = 本题不提供
①  r.type = R_X86_64_PC32     r.addend = -4
②  rr..otfyfpsee t=  =R _0Xx8164_ 6 4 _ 3 2               rr..asdydmebnodl  ==  +b0u f
⑥  rr..otfyfpsee t=  =R _0Xx836f_ 6 4 _ P C  3 2          rr..saydmdbeonld  ==  b-u4f p1
r.offset = 0x62             r.symbol = 本题不提供
⑨  r.type = R_X86_64_PC32     r.addend = -4

---

### 2020期末-无答案 · 第一题 7

> 出处：`原文/期末/2020期末-无答案.md` 第 101–105 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链接、打桩、共享库与程序入口点

7.  下列关于链接的描述，正确的是：
A．打桩（interpositioning)机制需要能够访问程序的源代码。
B. 链接器生成的文件不再有ABS、UNDEF 和COMMON 伪节。
C. 对于GlibC和GCC生成的程序，其入口点位于__libc_start_main函数的第一条指令处。
D．用户使用GCC进行共享库的编译必须使用-fpic选项指示生成位置无关代码。

---

### 2020期末-无答案 · 第一题 8

> 出处：`原文/期末/2020期末-无答案.md` 第 110–126 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：跨文件符号类型冲突与链接结果

8.  文件f1.c和f2.c的C源代码如下图所示：
//f1.c  //f2.c
#include<stdio.h>  int x = 0;
extern float x;  void f()
extern void f();  {
int main()    x++;
{  }
  f();
  printf("%d\n",(int)x);
  return 0;
}
已知这两个文件在同一个目录下，在该目录下用“gcc -Og -o f f1.c f2.c”编译，然后用“./f”运
行，这个过程中会出现的情况是：
A. 编译错误
B. 输出0
C. 输出1
D. 链接错误

---

### 2020期末-无答案 · 第三题

> 出处：`原文/期末/2020期末-无答案.md` 第 292–406 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表条目、节归属与重定位引用值

第三题（10分）
本题基于下列m.c及swap.c文件所编译生成的m.o和swap.o，编译和运行在Linux/
X86-64下使用GCC完成，编译过程未加优化选项。
//m.c  //swap.c
void myswap();  extern int buf[];
vcohiadr  fbuunfc[(2)];  = {1, 2};  c.h.a.r. ..*/b/u略fp去0;题 目无关代码
void *bufp0;  char *bufp1 = &buf[1];
void *bufp1;  void myswap(char temp){
icnhta rm atienm(p); {  s.t.a.t.i.c. //i略nt去 c题o目un无t 关=代 0码;
f.u.n.c.(.).;// 略去题目无关代码  bteumfpp 0=  =* b&ubfupf0[;0 ];
myswap(temp);  ......//略去题目无关代码
......//略去题目无关代码  *bufp0 = *bufp1;
}     return 0;  *.b.u.f.p.1. //=略 t去em题p目; 无关代码
  count++;
}
void. .f.u.n.c.(/)/{略 去题目无关代码
}
1） 对于每个 swap.o 中定义和引用的符号，请用“是”或“否”指出它是否在模块 swap.o
的.symtab节中存在符号表条目。如果存在条目，则请指出定义该符号的模块（swap.o
或m.o）、符号类型（局部、全局或外部）以及该符号在所属的模块（“即该符号在该模
块中被定义”）中所处的节；如果不存在条目，则请将该行后继空白处标记为“/”。
符号  .symtab有条目?  符号类型  定义符号的模块  节
buf
bufp0
count
func
temp
 2） 下 图左边给出了 m.o 和swap.o 的反汇编文件，右边给出了采用某个配置链接成可执
行程序后再反汇编出来的文件。根据答题需要，其中的信息略有删减。
  9

<!-- ===== page 10 ===== -->

0000000000......<main>:  0000000000001000 <main>:
55                          push   %rbp  1000: 55                     push  %rbp
48 89 e5                  mov    %rsp,%rbp  1001: 48 89 e5            mov   %rsp,%rbp
b8 00 00 00 00           mov    $0x0,%eax  1004: b8 00 00 00 00       mov   $0x0,%eax
e8 00 00 00 00           callq  e <main+0xe>     ①  1009: e8       ①            callq 302e <func>
......  ......
0f b6 05 00 00 00 00    movzbl 0x0(%rip),%eax  ②  1010:  0f  b6  05              ②              movzbl
0f be c0                  movsbl %al,%eax  0x??????(%rip),%eax
89 c7                      mov    %eax,%edi  1017: 0f be c0              movsbl %al,%eax
b8 00 00 00 00           mov    $0x0,%eax  101a: 89 c7                  mov    %eax,%edi
e8 00 00 00 00           callq  26 <main+0x26>  ③  101c: b8 00 00 00 00       mov    $0x0,%eax
......  1021: e8       ③            callq  10e4 <myswap>
b8 00 00 00 00           mov    $0x0,%eax  ......
5d                         pop    %rbp  10db: b8 00 00 00 00        mov    $0x0,%eax
c3                         retq  10e0: 5d                       pop   %rbp
  10e1: c3                       retq
0000000000......<myswap>:
55                   push   %rbp  00000000000010e4<myswap>:
48 89 e5             mov    %rsp,%rbp  10e4: 55                       push   %rbp
89 f8                mov    %edi,%eax  10e5: 48 89 e5                mov    %rsp,%rbp
88 45 fc             mov    %al,-0x4(%rbp)  10e8: 89 f8                    mov    %edi,%eax
......  10ea: 88 45 fc                 mov    %al,-0x4(%rbp)
48 c7 05 00 00 00 00 00 00 00 00               ⑤④  ......
movq   $0x0,0x0(%rip)     10f4: 48 c7 05       ⑤             ④
......  movq     ④  ,  ⑤  (%rip)
48 8b 05 00 00 00 00  mov    0x0(%rip),%rax    ⑥  ......
0f b6 00                movzbl (%rax),%eax  1104: 48 8b 05       ⑥       mov    ⑥  (%rip),%rax
88 45 fc                mov    %al,-0x4(%rbp)  110b: 0f b6 00                movzbl (%rax),%eax
......  110e: 88 45 fc                mov    %al,-0x4(%rbp)
48 8b 05 00 00 00 00 mov    0x0(%rip),%rax     ⑦  ......
48 8b 15 00 00 00 00 mov    0x0(%rip),%rdx     ⑧  1229: 48 8b 05       ⑦       mov    ⑦  (%rip),%rax
0f b6 12               movzbl (%rdx),%edx  1230：48 8b 15       ⑧       mov    ⑧  (%rip),%rdx
88 10                   mov    %dl,(%rax)  1237：0f b6 12                movzbl (%rdx),%edx
48 8b 05 00 00 00 00 mov    0x0(%rip),%rax     ⑨  123a: 88 10                   mov    %dl,(%rax)
0f b6 55 fc           movzbl -0x4(%rbp),%edx  123c: 48 8b 05       ⑨       mov     ⑨  (%rip),%rax
88 10                   mov    %dl,(%rax)  1243: 0f b6 55 fc            movzbl -0x4(%rbp),%edx
......  1247: 88 10                   mov    %dl,(%rax)
8b 05 00 00 00 00     mov    0x0(%rip),%eax     ⑩  ......
83 c0 01                add    $0x1,%eax  124b: 8b 05       ⑩          mov      ⑩  (%rip),%eax
89 05 00 00 00 00     mov    %eax,0x0(%rip)        1251：83 c0 01                add    $0x1,%eax
1254：89 05                  mov    %eax,     (%rip)
90                       nop  ⑪
5d                       pop    %rbp  125a: 90           ⑪            nop  ⑪
c3                       retq  125b: 5d                       pop    %rbp
  125c: c3                       retq
0000000000......<func>:
......  000000000000302e<func>:
......
......略去部分和答题无关的信息......
000000000000a000 <buf>:
......略去部分和答题无关的信息......
000000000000a250 <bufp1>:
......略去部分和答题无关的信息......
0000000000dedd38 <count.1837>:
......略去部分和答题无关的信息......
0000000000dedd40 <bufp0>:
......略去部分和答题无关的信息......
10

<!-- ===== page 11 ===== -->

在上图中对所涉及到的重定位条目进行用数字①至 进行了标记，请根据下表中所提供的
重定位条目信息，计算相应的重定位引用值并填写下表。
⑪
应填入的重定位引用值
编号 重定位条目信息
    一律填写32位16进制数
本题不提供
①  r.offset = 0x0a             r.symbol =
r.type = R_X86_64_PC32     r.addend = -4
本题不提供
③  r.offset = 0x22             r.symbol =
r.type = R_X86_64_PC32     r.addend = -4
本题不提供
④  r.offset = 0x17             r.symbol =
r.type = R_X86_64_32       r.addend = 0
本题不提供
⑨  r.offset = 0x15b            r.symbol =
r.type = R_X86_64_PC32     r.addend = -4
r.offset = 0x172            r.symbol = 本题不提供
  r.type = R_X86_64_PC32     r.addend = -4
  ⑪

---

### 2021期末-无答案 · 第一题 6

> 出处：`原文/期末/2021期末-无答案.md` 第 101–106 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：循环展开、累积变量与浮点合并顺序

6. 以下关于程序设计优化的说法，错误的是：
A.循环展开有助于进一步变换代码，减少关键路径上的操作数量。
B.分离多个累积变量计算可以提高并行性。
C.大多数编译器会改变浮点数的合并运算（如加法和乘法）顺序以提高程序
性能。
D.循环展开的程度增加并不一定能改善程序运行效率，反而会变差。

---

### 2021期末-无答案 · 第一题 9

> 出处：`原文/期末/2021期末-无答案.md` 第 126–131 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：objdump/readelf/gdb 等可执行文件工具（兼 Machine Prog）

9. 以下关于Linux系统上处理可执行文件的工具的说法错误的是：
A  使用objdump反汇编 .text 节的机器码。
B 使用readelf读取文件的节头部表(section header)和程序头部表
(program header)。
C 使用ls查询文件是文本文件还是二进制文件。
D 使用gdb加载可执行文件、设置断点，然后单步调试运行。

---

### 2021期末-无答案 · 第一题 10

> 出处：`原文/期末/2021期末-无答案.md` 第 132–145 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态局部符号与 COMMON 伪节

10.  对如下两个C程序，用gcc 生成对应的.o模块，链接在一起得到a.out
可执行程序。则下列说法正确的是：
// main.c  // util.c
#include <stdio.h>  int a = 0;
static int a;  int *func() {
int main() {  return &a;
int *func();  }
printf("%ld\n", func() - &a);
return 0;
}
A 在 main.o 中，符号 a 位于.COMMON 伪节。
B 在 util.o 中，符号 a 位于.COMMON 伪节。
C 无论怎样链接和运行 a.out，输出的结果都一样，但必不为 0。
D 以上说法都不正确。

---

### 2021期末-无答案 · 第一题 11

> 出处：`原文/期末/2021期末-无答案.md` 第 146–175 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：动态链接、PLT/GOT 与 -ldl

11.  在标准Linux系统中，以下程序可以使用 gcc dl.c -ldl 编译生成
a.out 可执行文件并正常运行。如果缺少了 -ldl 选项，链接时会报错
undefined reference to 'dlopen'等信息。基于对动态链接的正确
理解，请分析出以下说法中错误的一项是：
（libc.so 和 libdl.so 在实际系统中会带上版本号，路径名一般也更
复杂。在本题中认为此处的libdl.so和libc.so是二进制文件而非符号
链接。）
// dl.c
#include <dlfcn.h>
const char *path = "/lib/libc.so";
int (*printf)(const char *x);
int main() {
  // 加载共享库
  void *handle = dlopen(path, RTLD_NOW);
  5

<!-- ===== page 6 ===== -->

  // 解析符号 "printf" 并返回地址
  printf = dlsym(handle, "printf");
  // 调用
  printf("2022 is just around the corner.\n");
  // 关闭共享库
  dlclose(handle);
}
A 该机器上libdl.so模块中包含符号名为dlopen 的动态链接符号表条
目。
B 在a.out 文件中包含printf 的PLT 条目和相应的GOT 条目。
C 在a.out 文件中包含dlopen 的PLT 条目和相应的GOT 条目。
D 如果使用gcc -ldl dl.c编译程序，会在链接时发生错误。

---

### 2021期末-无答案 · 第三题

> 出处：`原文/期末/2021期末-无答案.md` 第 329–405 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表节归属、重定位与程序入口点（Part C 兼 ECF）

第三题. 请结合教材第七章“链接”的有关知识回答问题(10分)
有以下三个 c 文件 hd.h f1.c f2.c。使用gcc -c f1.c f2.c; gcc
f1.o f2.o 编译后得到可执行文件a.out。回答以下问题。Part A 中涉及
的符号所对应的变量已在代码中加粗。本大题无需理解代码的含义。
f1.c  #include "hd.h"
#include <stdio.h>
const int total = 1 << 30;
static int count = 0;
static Point pnt;
int iter;
int main() {
for (iter = 0; iter < total; ++iter) {
rand_point(&pnt);
count += if_inside(&pnt);
}
printf("Integral on [0,1] is %lf.\n",
1.0 * count / total);
}
hd.h  typedef struct {
double x;
double y;
} Point;
void rand_point(Point *);
int if_inside(Point *);
f2.c  #include "hd.h"
#include <stdlib.h>
#include <time.h>
void rand_point(Point *ptr) {
static int seed = 0;
if (!seed) {
srand((unsigned)time(NULL));
seed = 1;
}
ptr->x = 1.0 * rand() / RAND_MAX;
ptr->y = 1.0 * rand() / RAND_MAX;
}
int if_inside(Point *p) {
return 1 / (1 + p->x) >= p->y;
}
Part A. (每个符号1分，共5分) 请说明以下符号是否在a.out的符号表
中。如果是，请进一步指出符号定义所在的节，可能的选择
有.text、.data、.bss、.rodata、COM、UNDEF、ABS。
  10

<!-- ===== page 11 ===== -->

符号名  iter  pnt  Point  total  seed
在符号表中？（填是/否）
定义所在节
Part B. (每空1分，共3分) 使用objdump -dx f1.o f2.o 看到如下
几条代码。这里可以将重定位类型 R_X86_64_PLT32和 R_X86_64_PC32 同
等看待。
# objdump 重定位条目格式：
##  e . g .             O  FF S E1T8::  TRY_PXE86 _ 6 4 _ P L T 3 2         VrAaLnUdE_p oint-0x4
# 所有数值均以十六进制表示
#0 0f010.0o0 0000000000 <main>:
... # 省略无关代码
  11 7c ::    e4 88    08 0d1  803:0d   R00_00X  800600_. 6 04 0_  P 0 L0 T  3  2      lcea  al  l 0qx ra0 n(1d%c_r pi<opmi)an,it%nr-+d00ixx41  c>
  2 3 :   e 8   0 01 f0:0  R0_0X 8060_ 6 4 _  P C 3 2     c a l l q  . b2s8s +<0mxaci n+0x28>
  2 8 :   8 9   c 22 4 :    R _ X 8 6  _ 6 4 _ P L  T 3 2    mo  v   %eifa_xi,n%seiddxe -0x4
... # 省略无关代码
#0 0f020.0o0 0000000000 <rand_point>:
.0.0.0 0#0 0省00略00无0关00代07码4  <if_inside>:
... # 省略无关代码
据 此 可 以 确 定  <main+0x1f>  处 的 重 定 位 条 目 是 针 对 符 号
_______________(填写符号名，不要填写.bss这个节名)的重定位。同时该
符 号 定 义 的 位 置 在 f1.o 中 相 对 于 .bss 节 的 偏 移 量 是
0x__________________。
现已知 a.out 文件中 <main+0x17> 行变成
11a1: e8 69 00 00 00          callq  <rand_point>
那么 a.out 中 <main+0x23> 行将变成
11ad: e8 ___________          callq  <if_inside>
Part C. (每空1分，共2分) 使用execve加载a.out并执行时，其中第
一个被执行的语句默认是_______(单选)函数的开头。已知 gcc -e 可以修
改该默认行为到一个程序指定的函数，据此推断该函数执行在_______态下
(填 用户/内核)。
A. _init     B.main     C.__libc_start_main    D._start

---

### chap 2-6 解析 · 第一题 8

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 185–193 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：程序优化：循环展开、累积变量、浮点结合律

8.以下关于程序设计优化的说法，错误的是：

A.循环展开有助于进一步变换代码，减少关键路径上的操作数量。

B.分离多个累积变量计算可以提高并行性。

C.大多数编译器会改变浮点数的合并运算（如加法和乘法）顺序以提高程序性能。

D.循环展开的程度增加并不一定能改善程序运行效率，反而会变差。

---

### chap 7 解析 · 第 1 题

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 1–13 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：objdump/readelf/ls/gdb 处理目标文件与可执行文件的作用

（Linux工具链）简单，基础  1-2 min

1.  以下关于Linux系统上处理可执行文件的工具的说法**<u>不正确</u>**的是

<!-- -->

1.  使用 objdump 反汇编 .text 节的机器码

2.  使用 readelf 读取文件的节头部头(section header)和程序头部表(program header)

3.  使用 ls 查询文件是文本文件还是二进制文件

4.  使用 gdb 加载可执行文件、设断点，然后单步调试运行

---

### chap 7 解析 · 第 2 题

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 27–63 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态链接：未初始化全局变量在 COM/.bss 的归属与地址偏移

（静态链接）中等，需要2-4min

2.  对如下两个C程序，用gcc 生成对应的.o模块，再链接在一起得到a.out。则下列说法正确的是：

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th><p>// main.c</p>
<p>#include &lt;stdio.h&gt;</p>
<p>static int a;</p>
<p>int main() {</p>
<p>int *func();</p>
<p>printf("%ld\n", func() - &amp;a);</p>
<p>return 0;</p>
<p>}</p></th>
<th><p>// util.c</p>
<p>int a = 0;</p>
<p>int *func() {</p>
<p>return &amp;a;</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  在 main.o 中，符号 a 位于 COM 伪节

2.  在 util. o 中，符号 a 位于 COM 伪节

3.  无论怎样链接和运行 a.out， a.out 输出的结果都一样，但必不为 0

4.  以上说法都不正确

---

### chap 7 解析 · 第 3 题

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 75–111 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：动态链接：dlopen 与 PLT/GOT、库的符号解析顺序

（动态链接）困难，需要理解并分析 需要2-4min

3.  以下程序可以使用 gcc dl.c -ldl 编译并正常运行。如果缺少了 -ldl 标志，链接时会报错 undefined reference to \`dlopen'。基于你对于动态链接的理解，请分析出以下说法中**<u>不正确</u>**的一项。

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>// dl.c</p>
<p>#include &lt;dlfcn.h&gt;</p>
<p>const char *path = "/lib/libc.so";</p>
<p>int (*printf)(const char *x);</p>
<p>int main() {</p>
<p>  // 加载共享库</p>
<p>  void *handle = dlopen(path, RTLD_NOW);</p>
<p>  // 解析符号 "printf" 并返回地址</p>
<p>  printf = dlsym(handle, "printf");</p>
<p>  // 调用</p>
<p>  printf("2022 is coming!\n");</p>
<p>  // 关闭共享库</p>
<p>  dlclose(handle);</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  该机器上libdl.so模块中包含符号名为dlopen 的动态链接符号表条目

2.  在a.out 文件中包含printf 的PLT 条目和相应的GOT 条目

3.  在a.out 文件中包含dlopen 的PLT 条目和相应的GOT 条目

4.  如果使用gcc -ldl dl.c编译程序，则会在链接时发生同样错误

---

### chap 7 解析 · 第 4 题 题干+Part A

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 136–202 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表中的符号及其定义所在节（.bss/.rodata/UNDEF 等）

4.  **(本大题共三问，共10分)** 有以下三个 c 文件 hd.h f1.c f2.c。使用

gcc -c f1.c f2.c; gcc f1.o f2.o 

编译后得到可执行文件a.out。回答以下问题。Part A 中涉及的符号所对应的变量已在代码中加粗。**<u>本大题无需理解代码的含义。</u>**

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr>
<th>f1.c</th>
<th><p>#include "hd.h"</p>
<p>#include &lt;stdio.h&gt;</p>
<p>const int <strong><u>total</u></strong> = 1 &lt;&lt; 30;</p>
<p>static int count = 0;</p>
<p>static Point <strong><u>pnt</u></strong>;</p>
<p>int <strong><u>iter</u></strong>;</p>
<p>int main() {</p>
<p>for (iter = 0; iter &lt; total; ++iter) {</p>
<p>rand_point(&amp;pnt);</p>
<p>count += if_inside(&amp;pnt);</p>
<p>}</p>
<p>printf("Integral on [0,1] is %lf.\n",</p>
<p>1.0 * count / total);</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>hd.h</td>
<td><p>typedef struct {</p>
<p>double x;</p>
<p>double y;</p>
<p>} <strong><u>Point</u></strong>;</p>
<p>void rand_point(Point *);</p>
<p>int if_inside(Point *);</p></td>
</tr>
<tr>
<td>f2.c</td>
<td><p>#include "hd.h"</p>
<p>#include &lt;stdlib.h&gt;</p>
<p>#include &lt;time.h&gt;</p>
<p>void rand_point(Point *ptr) {</p>
<p>static int <strong><u>seed</u></strong> = 0;</p>
<p>if (!seed) {</p>
<p>srand((unsigned)time(NULL));</p>
<p>seed = 1;</p>
<p>}</p>
<p>ptr-&gt;x = 1.0 * rand() / RAND_MAX;</p>
<p>ptr-&gt;y = 1.0 * rand() / RAND_MAX;</p>
<p>}</p>
<p>int if_inside(Point *p) {</p>
<p>return 1 / (1 + p-&gt;x) &gt;= p-&gt;y;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

Part A. **(每个符号1分，共5分)** 请说明以下符号是否在a.out的符号表中。如果是，请进一步指出符号定义所在的节，可能的选择有.text、.data、.bss、.rodata、COM、UNDEF、ABS。

| 符号名                             | iter | pnt | Point | total | seed |
|------------------------------------|------|-----|-------|-------|------|
| 在符号表中？**<u>（填是/否）</u>** |      |     |       |       |      |
| 定义所在节                         |      |     |       |       |      |

---

### chap 7 解析 · 第 4 题 Part B

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 204–248 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：重定位条目 R_X86_64_PLT32/PC32 与符号地址推算

Part B.** (每空1分，共3分)** 使用objdump -dx f1.o f2.o 看到如下几条代码。**<u>这里你可以将重定位类型R_X86_64_PLT32和R_X86_64_PC32同等看待。</u>**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p># objdump 重定位条目格式：</p>
<p>#           OFFSET: TYPE              VALUE</p>
<p># e.g.          18: R_X86_64_PLT32    rand_point-0x4</p>
<p># 所有数值均以十六进制表示</p>
<p><strong># f1.o</strong></p>
<p>0000000000000000 &lt;main&gt;:</p>
<p>... # 省略无关代码</p>
<p>17: e8 00 00 00 00. callq  1c &lt;main+0x1c&gt;</p>
<p>          18: R_X86_64_PLT32      rand_point-0x4</p>
<p>1c: 48 8d 3d 00 00 00 00 lea 0x0(%rip),%rdi</p>
<p>          1f: R_X86_64_PC32       .bss+0xc</p>
<p>23: e8 00 00 00 00 callq  28 &lt;main+0x28&gt;</p>
<p>          24: R_X86_64_PLT32      if_inside-0x4</p>
<p>28: 89 c2 mov %eax,%edx</p>
<p>... # 省略无关代码</p>
<p><strong># f2.o</strong></p>
<p>0000000000000000 &lt;rand_point&gt;:</p>
<p>... # 省略无关代码</p>
<p>0000000000000074 &lt;if_inside&gt;:</p>
<p>... # 省略无关代码</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

据此你可以确定 \<main+0x1f\> 处的重定位条目是针对符号\_\_\_\_\_\_\_\_(**<u>填写符号名，不要填写.bss这个节名</u>**)的重定位，同时该符号定义的位置在 f1.o 中相对于 .bss 节的偏移量是 0x\_\_\_\_\_\_\_\_\_。

现已知 a.out 文件中 \<main+0x17\> 行变成

| 11a1: e8 69 00 00 00          callq  \<rand_point\> |
|-----------------------------------------------------|

那么 a.out 中 \<main+0x23\> 行将变成

| 11ad: e8 \_\_\_\_\_\_\_\_\_\_\_          callq  \<if_inside\> |
|---------------------------------------------------------------|

---

### 2022期末-无答案 · 第一题 4

> 出处：`原文/期末/2022期末-无答案.md` 第 46–46 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态链接器的两大主要任务

4. 为了构造可执行文件，静态链接器必须完成________________和________________这两个主要任务。

---

### 2022期末-无答案 · 第一题 5

> 出处：`原文/期末/2022期末-无答案.md` 第 48–48 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：延迟绑定依赖的两个数据结构 PLT/GOT

5. 在当前的 Linux 系统中，延迟绑定是通过两个数据结构之间的交互来实现的，这两个重要的数据结构分别是________________和________________。

---

### 2022期末-无答案 · 第一题 6

> 出处：`原文/期末/2022期末-无答案.md` 第 50–58 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态库命令行最小排列顺序以解析全部符号

6. a 和 b 表示当前目录中的目标模块或者静态库，而 a—>b 表示 a 依赖于 b，也就是说 b 定义了一个被 a 占用的符号。对于下面的每种场景，请给出最小的命令行（即一个含有最少数量 的目标文件和库参数的命令），使得静态链接器能解析所有的符号引用。

   ① p.o —>libx.a —> liby.a

   ________________________________________________________________________________

   ② p.o —>libx.a —>liby.a 且 liby.a —> libx.a —> p.o

   ________________________________________________________________________________

---

### 2022期末-无答案 · 第三题 (1)

> 出处：`原文/期末/2022期末-无答案.md` 第 167–202 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：main.o 的 .symtab 条目、符号类型与所在节（含 main.c/addvec.c）

本题基于下列 c 语言文件所编译生成的 main.o 和 addvec.o，编译和运行在 X86-64/Linux 下完成，编译过程未加优化选项。

```c
//main.c
#include <stdio.h>
#include "vector.h"
int x[2] = {1, 2};
int z[2];
int main(int argc, char** argv){
  int y[2] = {3, 4};
  int n=2;
  addvec(x,y,z,n);
  printf("z=[%d %d]\n", z[0], z[1]);
  return 0;
}
```

```c
//addvec.c
void addvec(int *x, int *y,
            int *z, int n) {
    int i;
    for (i = 0; i < n; i++)
        z[i] = x[i] + y[i];
}
```

(1) 对于每个下表中给出的符号，请用"是"或"否"指出它是否在模块 main.o 的 .symtab 节中有符号表条目。如果存在条目，则请指出该符号的符号类型（局部、全局或外部）。并进一步指出定义该符号的模块（main.o 或 addvec.o）、以及此符号在该模块中所处的节名或伪节名；如果不存在条目，则请将该行后继空白处标记为"/"。

| 符号 | .symtab 条目？ | 符号类型 | 定义符号的模块 | 节或伪节名 |
| --- | --- | --- | --- | --- |
| x |  |  |  |  |
| y |  |  |  |  |
| z |  |  |  |  |
| n |  |  |  |  |
| addvec |  |  |  |  |

---

### 2022期末-无答案 · 第三题 (2)

> 出处：`原文/期末/2022期末-无答案.md` 第 204–313 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：依 objdump 反汇编片段填写重定位条目与引用值

(2) 基于 main.o 和 addvec.o 生成可执行程序 m 的时候，会进行若干重定位。下述代码是对可执行程序 m 执行 objdump -D m 以后的片段结果，请根据相关信息进行填空。

```asm
0000000000400228 <.interp>:
  400228:	2f                   	(bad)
  400229:	6c                   	insb   (%dx),%es:(%rdi)
  40022a:	69 62 36 34 2f 6c 64 	imul   $0x646c2f34,0x36(%rdx),%esp
  400231:	2d 6c 69 6e 75       	sub    $0x756e692c,%eax
  400236:	78 2d                	js     400265 <_init-0x153>
  400238:	78 38                	js     400272 <_init-0x146>
  40023a:	36                   	ss
  40023b:	2d 36 34 2e 73       	sub    $0x732e342d,%eax
  400240:	6f                   	outsl  %ds:(%rsi),(%dx)
  400241:	2e 32 00             	xor    %cs:(%rax),%al
  ...

00000000004003e0 <printf@plt-0x10>:
  4003e0:	ff 35 0a 0c 20 00    	pushq  0x200c0a(%rip)        # 600ff0 <_GLOBAL_OFFSET_TABLE_+0x8>
  4003e6:	ff 25 0c 0c 20 00    	jmpq   *0x200c0c(%rip)        # 600ff8 <_GLOBAL_OFFSET_TABLE_+0x10>
  4003ec:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004003f0 <printf@plt>:
  4003f0:	ff 25 0a 0c 20 00    	jmpq   *0x200c0a(%rip)        # 601000 <_GLOBAL_OFFSET_TABLE_+0x18>
  4003f6:	68 00 00 00 00       	pushq  $0x0
  4003fb:	e9 e0 ff ff ff       	jmpq   4003e0 <_init+0x18>

0000000000400400 <__libc_start_main@plt>:
  400400:	ff 25 02 0c 20 00    	jmpq   *0x200c02(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x20>
  400406:	68 01 00 00 00       	pushq  $0x1
  40040b:	e9 d0 ff ff ff       	jmpq   4003e0 <_init+0x18>
  ...

0000000000400528 <main>:
  400528:	55                   	push   %rbp
  400529:	48 89 e5             	mov    %rsp,%rbp
  40052c:	48 83 ec 20          	sub    $0x20,%rsp
  400530:	89 7d ec             	mov    %edi,-0x14(%rbp)
```

<!-- ===== page 06 ===== -->

```asm
  400533:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
  400537:	c7 45 fc 02 00 00 00 	movl   $0x2,-0x4(%rbp)
  40053e:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400541:	89 c1                	mov    %eax,%ecx
  400543:	ba （1）______________	mov    $__________,%edx
  400548:	be （2）______________	mov    $__________,%esi
  40054d:	bf （3）______________	mov    $__________,%edi
  400552:	e8 （4）______________	callq  __________________
  400557:	8b 15 （5）____________	mov    __________(%rip),%edx
  40055d:	8b 05 （6）____________	mov    __________(%rip),%eax
  400563:	89 c6                	mov    %eax,%esi
  400565:	bf （7）______________	mov    $__________,%edi
  40056a:	b8 00 00 00 00       	mov    $0x0,%eax
  40056f:	e8 （8）______________	callq  __________________ <printf@plt>
  400574:	b8 00 00 00 00       	mov    $0x0,%eax
  400579:	c9                   	leaveq
  40057a:	c3                   	retq
  40057b:	90                   	nop

000000000040057c <addvec>:
  40057c:	55                   	push   %rbp
  40057d:	48 89 e5             	mov    %rsp,%rbp
  400580:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
  400584:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
  400588:	48 89 55 d8          	mov    %rdx,-0x28(%rbp)
  40058c:	89 4d d4             	mov    %ecx,-0x2c(%rbp)
  40058f:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
  400596:	eb 4a                	jmp    4005e2 <addvec+0x66>
  400598:	8b 45 fc             	mov    -0x4(%rbp),%eax
  40059b:	48 98                	cltq
  40059d:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
  4005a4:	00
  ...

0000000000600fe0 <.got>:
  ...

0000000000600fe8 <_GLOBAL_OFFSET_TABLE_>:
  600fe8:	10 0e                	adc    %cl,(%rsi)
  600fea:	60                   	(bad)
  ...
  600fff:	00 f6                	add    %dh,%dh
  601001:	03 40 00             	add    0x0(%rax),%eax
  601004:	00 00                	add    %al,(%rax)
  601006:	00 00                	add    %al,(%rax)
  601008:	06                   	(bad)
  601009:	04 40                	add    $0x40,%al
  60100b:	00 00                	add    %al,(%rax)
  60100d:	00 00                	add    %al,(%rax)
  ...
0000000000601020 <x>:
  601020:	01 00                	add    %eax,(%rax)
  601022:	00 00                	add    %al,(%rax)
  601024:	02 00                	add    (%rax),%al
  ...
0000000000601028 <y.2304>:
  601028:	03 00                	add    (%rax),%eax
  60102a:	00 00                	add    %al,(%rax)
  60102c:	04 00                	add    $0x0,%al
  ...
0000000000601038 <z>:
  ...
```

| 编号 | 重定位条目信息 | 应填入的重定位引用值 |
| --- | --- | --- |
| ③ | r.offset = 0x26　　　　r.symbol = x<br>r.type = R_X86_64_32　　r.addend = 0 |  |
| ① | r.offset = 0x2b　　　　r.symbol = addvec<br>r.type = R_X86_64_PC32　　r.addend = -4 |  |

---

### 2022期末-无答案 · 第三题 (3)

> 出处：`原文/期末/2022期末-无答案.md` 第 317–325 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：动态链接器 ld-linux 的路径选择

(3) 基于你对代码的分析，生成该可执行程序的操作系统的动态链接器的路径是（　　）

　　A) /lib64/ld-linux-x86-64.so.2

　　B) /lib/ld-linux-x86-64.so.2

　　C) /lib/ld-x86-64-linux.so.2

　　D) /lib64/ld-x86-64-linux.so.2

---

### 2022期末-无答案 · 第三题 (4)

> 出处：`原文/期末/2022期末-无答案.md` 第 327–327 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：printf 对应的 PLT 与 GOT 表条目下标

(4) 程序中 printf 的 PLT 表条目是 PLT[______]，GOT 表条目是 GOT[______]。（填写数字即可）

---

### 2022期末-答案 · 第一题 4

> 出处：`原文/期末/2022期末-答案.md` 第 13–13 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号解析与重定位

4、符号解析 重定位

---

### 2022期末-答案 · 第一题 5

> 出处：`原文/期末/2022期末-答案.md` 第 14–14 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：GOT 与 PLT

5、GOT PLT

---

### 2022期末-答案 · 第一题 6

> 出处：`原文/期末/2022期末-答案.md` 第 15–15 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：静态库链接顺序 gcc 命令行

6、① gcc p.o libx.a liby.a  ②gcc p.o libx.a liby.a libx.a

---

### 2022期末-答案 · 第三题

> 出处：`原文/期末/2022期末-答案.md` 第 35–50 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表、重定位、.interp 与 PLT

第三题 链接
(1) 注意，最后一列填的是“此符号在定义该符号的模块中的节”。addvec在addvec.o中
是在.text，在main.o中是在UND中
符号  .symtab条目？  符号类型  定义符号的模块  节或伪节名
x  是  全局  main.o  .data
y  否  /  /  /
z  是  全局  main.o  COMMON
n  否  /  /  /
addvec  是  外部  addvec.o  .text
(2) 20 10 60 00
      25 00 00 00
(3) A
.interp节的内容其实就是一个字符串，为动态链接器的路径。把.interp节的所有字节一个
一个地翻译成字符，就得到/lib64/ld-linux-x86-64.so.2。（大家可以特别记一下，’0’的
ascii的16进制是0x30）
(4) 1 3

---

### 2024期末-带答案 · 第一题 5

> 出处：`原文/期末/2024期末-带答案.md` 第 145–182 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：gcc 编译链接过程、ld 报错与重定位

5. 针对如下代码，假定编译器不做任何编译优化，同时编译系统在预处理a.c和
b.c时可以顺利找到common.h。运行gcc a.c b.c命令，发现报错。已知报
错信息中含有如下内容：
4

<!-- ===== page 5 ===== -->

collect2: error: ld returned 1 exit status
// a.c  // b.c  // common.h
#include <stdio.h>  #include "common.h"
#include "common.h"    int x = 1;
  int funcB(void) {
int main() {    x++;  int funcB(void);
  scanf("%d\n", &x);  }
  funcB();
  printf("%d\n", x);
}
则下列说法正确的是：
A. 在编译系统及二进制工具链对本题所涉源代码进行处理过程中，会产生名为
a.o、b.o的中间临时文件，并将其链接到一起。
B. 根据题目中的报错信息描述进行推断，报错信息是由编译系统及二进制工具链
中的预处理器输出的。
C. 报错原因是a.c、b.c、common.h其中之一含有语法错误。这个错误可以通
过调整编译顺序来解决，即gcc b.c a.c。
D. 在编译系统及二进制工具链对本题所涉源代码进行处理过程中，所产生的中间
目标文件的.text节中，对于变量x的引用都需要在链接时重定位。
答案：D
本题考察编译和链接的相关知识。
A. 用该命令编译时，common.h只被预处理器复制到a.c与b.c中，而不参与
之后的编译阶段。产生的中间临时文件名是随机的，并非一定为a.o和b.o。
B. 报错原因是int x=1; 会被预处理器分别复制到a.c与b.c中，从而导致强
符号a重定义，链接时报错，类似
/usr/bin/ld:  /tmp/cckR3OM5.o:(.data+0x0):  multiple
definition  of  `a';  /tmp/ccSDjtQc.o:(.data+0x0):  first
defined here
collect2: error: ld returned 1 exit status
C. 各种信息都说明这是链接器报错；最明显的是：ld是GNU 链接器的简称。
D. 确实，任何在编译时无法确定地址的数据引用需要重定位

---

### 2024期末-带答案 · 第一题 6

> 出处：`原文/期末/2024期末-带答案.md` 第 183–228 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表条目与 .data/.bss/UND 节

6. 本题基于下面c语言文件编译生成的可重定位目标文件main.o。该文件的生
成过程在x86-64 Linux下完成，其中编译过程未加优化选项。已知本题不涉及
COMMON节，不涉及重定位相关节。下面有关符号及其所在节说法错误的是：
5

<!-- ===== page 6 ===== -->

//main.c
extern int extern_var;
void global_used_func();
int init_var = 1;
int init_func() {
    return 1145;
}
void f() {
    static int x = 2;
    int local_var = 1;
    local_var++;
    x++;
}
int main() {
    extern_var++;
    global_used_func();
    return 0;
}
A. extern_var 和 global_used_func 在符号表中，且位于 UND 节；而
extern_unused_var不会出现在符号表中。
B. init_var在符号表中，且位于.data节。
C. init_func不会出现在符号表中，因为main.c没有调用它。
D. f函数中的局部静态变量x以某种形式出现在符号表中，且位于.data节；而
f函数中的local_var不会出现在符号表中，它存在栈上。
答案：C
本题考察链接与符号表的相关知识。
A. 正确，函数声明默认为extern。extern_var和global_used_func都在
main 函数中被使用，因此在符号表中。 两个符号没有定义，在 UND 节。
extern_unused_var没有被使用且没有定义，因此不在符号表中。
B. 正确。初值不为0的全局静态变量被放在.data节；未初始化全局静态变量放
在.bss。
C. 错误。含有定义的函数即使没有被使用也会存放在符号表中，可供其他.o文
件使用。
6

<!-- ===== page 7 ===== -->

D. 正确。初值非0的局部静态变量被存放在.data节。后半句包含解释。
可以使用objdump -t main.o 验证答案：

---

### 2025期末-带答案 · 二 14

> 出处：`原文/期末/2025期末-带答案.md` 第 86–92 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：全局符号强/弱定义与类型检查

二 不定项选择题（下）（36分）
（链接）
14.三个C程序文件，下面仅观察其中的全局符号g：
答案：ACD
解析： intg=1 是强定义；intg; 是“弱/共同（common）”风格，强胜弱，因此 A 对、
B 错。两个强定义会报错（D 对）。链接器通常不做类型一致性检查，E 错（但运行行为会
出问题）。

---

### 2025期末-带答案 · 三 1

> 出处：`原文/期末/2025期末-带答案.md` 第 147–156 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：符号表条目、符号类型与所在节（含答案）

三 链接相关主题（10分）
1.符号表分析（7分）每行1分
符号 .symtab有条目? 符号类型 定义符号的模块 节或伪节名
1 arr 是 全局 main.o .data
2 result 是 全局 main.o .bss
3 fix 是 局部 main.o .data
4 sum_array 是 外部 sum.o .text
5 i 否 / / /
6 sum 否 / / /
7 printf 是 外部 libc.so .text

---

### 2025期末-带答案 · 三 2

> 出处：`原文/期末/2025期末-带答案.md` 第 161–170 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：重定位条目与 32 位小端机器码（含答案）

2.重定位分析（2分）
已知以下重定位条目信息。请根据重定位信息填写空白处的机器码（32位小端编码）。
（注：在答题纸上画出下面表格的第1列和第3列）
重定位引用值32位编码（参
编号 重定位条目信息
照代码中的16进制形式）
① r.offset = 0x09 r.symbol = arr 10 20 40 00
r.type = R_X86_64_32 r.addend = 0
② r.offset = 0x0e r.symbol = sum_array 25 00 00 00
r.type = R_X86_64_PC32 r.addend = -4

---

### 2025期末-带答案 · 三 3

> 出处：`原文/期末/2025期末-带答案.md` 第 171–174 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链接顺序影响的答案选项

3.链接顺序影响（1分）
……以下说法正确的是（ B ）
A) 两者大小相同，内容相同 B) 两者大小相同，内容不同
C) 两者大小不同，内容相同 D) 两者大小不同，内容不同

---

### 2025期末-无答案 · 二 14

> 出处：`原文/期末/2025期末-无答案.md` 第 193–204 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：全局符号强/弱定义与重复定义

二 不定项选择题（下）（36分）
14.三个C程序文件，下面仅观察其中的全局符号g：
a.c：int g = 1;
b.c：int g;
main.c：extern int g; int main(){ return g; }
关于链接行为，下列说法哪些正确？
A. 链接成功，main 中引用的 g 解析到 a.c 的定义
B. 链接失败，因为 g 在 a.c 与 b.c 中被“重复定义”
C. 若把 a.c 改为 int g;，与 b.c 一样，则链接仍可成功，最终只分配一个 g
D. 若把 b.c 改为 int g = 2;，则链接失败
E. 若把 a.c 中 g 定义改成 double g = 1.0;，main.c中声明 extern int g; 并
使用，链接器会报“类型不匹配”错误

---

### 2025期末-无答案 · 三 1

> 出处：`原文/期末/2025期末-无答案.md` 第 340–366 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：main.o 的 .symtab 符号表条目与所在节

三 链接相关主题（10分）
本题基于下列两个 C 语言文件编译生成的 main.o 和 sum.o，编译和运行
在 x86-64/Linux 环境下完成，未开启优化选项。
// main.c // sum.c
#include <stdio.h> int sum_array(int *arr, int n) {
extern int sum_array(int *arr, int n); int sum = 0;
int arr[5] = {1, 2, 3, 4, 5}, result; for (int i = 0; i < n; i++) {
static int fix = 2010; sum += arr[i];
int main() { }
result = sum_array(arr, 5)+fix; return sum;
printf("sum = %d\n", res1); }
return 0;
}
1.符号表分析（7分）
对于下表中给出的每个符号，用“是”或“否”指出它是否在模块 main.o 的 .symtab 节
中有符号表条目。如果存在条目，请指出符号类型（局部、全局、外部）以及定义该符号的
模块（main.o、sum.o、libc.so或“无”）和所在节名（或伪节名）。如果不存在条目，
则填写“/”。
（注：在答题纸上画出下面完整表格）
符号 .symtab有条目? 符号类型 定义符号的模块 节或伪节名
1 arr
2 result
3 fix
4 sum_array
5 i
6 sum
7 printf

---

### 2025期末-无答案 · 三 2

> 出处：`原文/期末/2025期末-无答案.md` 第 367–386 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：重定位条目与 32 位小端机器码

2.重定位分析（2分）
下面是链接后生成的可执行文件 m 使用 objdump -D 反汇编的片段
（部分地址和内容为示意）
0000000000001149 <main>:
1149: 55 push %rbp
114a: 48 89 e5 mov %rsp, %rbp
114d: be 05 00 00 00 mov $0x5, %esi
1152: bf __ __ __ __ mov $_______, %edi ; arr的地址
1157: e8 __ __ __ __ callq _____________ ; sum_array
已知以下重定位条目信息。请根据重定位信息填写空白处的机器码（32位小端编码）。
（注：在答题纸上画出下面表格的第1列和第3列）
重定位引用值32位编码（参
编号 重定位条目信息
照代码中的16进制形式）
① r.offset = 0x09 r.symbol = arr
r.type = R_X86_64_32 r.addend = 0
② r.offset = 0x0e r.symbol = sum_array
r.type = R_X86_64_PC32 r.addend = -4
此处假设arr 在可执行文件中的地址为 0x402010，sum_array 的地址为 0x1180
result 的地址为 0x404018，main 中 call 指令的下一指令地址为 0x115c

---

### 2025期末-无答案 · 三 3

> 出处：`原文/期末/2025期末-无答案.md` 第 391–396 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：链接顺序对可执行文件的影响

3.链接顺序影响（1分）
执行以下两条命令
①gcc -o m1 main.c sum.c ②gcc -o m2 sum.c main.c
关于生成的两个可执行文件 m1 和 m2，以下说法正确的是（ ）
A.两者大小相同，内容相同 B.两者大小相同，内容不同
C.两者大小不同，内容相同 D.两者大小不同，内容不同

---

### 期末往年题勘误、详解 by Arthals · 2015 第四题

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 23–27 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：重复定义全局变量的理解（union 验证）

### 第四题

如果你认为 a[0] 应当是 \*(0xdeadbeefcafebffe)，那么你的理解有误。

你可以使用 union 结构体来验证这个重复定义的全局变量。

---

### 期末往年题勘误、详解 by Arthals · 2020 第一题 第7问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 186–188 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：ABS 节在静态/部分链接文件中的存在性

### 第一题

第 7 问，关于 D 选项，可能有些同学读书认为此时 ABS 节应当也不存在，但是书上说的是静态链接后的情况。你可以认为，在默认的编译选项下得到的可执行文件是会有这些伪节的。或者参考我的理解，我觉得书上说的是完全连接的可执行文件，你搞出来的是部分链接的可执行文件，其中还有一些共享库的条目？

---

### 期末往年题勘误、详解 by Arthals · 2020 第三题 ④

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 194–196 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：重定位符号应为 count（答案勘误）

### 第三题

④ 处怀疑是答案给错了，根据汇编看似乎应该是 count 才对，也就是 0x00dedd38（count 的地址，初始化置零）

---

### 期末往年题勘误、详解 by Arthals · 2021 第三题 Part A

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 212–214 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：局部静态变量重命名加 .x 后缀

### 第三题

Part A，seed。老师想考的是非全局的局部静态变量（函数内的 static）会被重命名，加一个.x 的后缀，所以是否，后来讨论了之后还是认为有。

---

### 期末往年题勘误、详解 by Arthals · 2021 第三题 Part B

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 216–220 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：相对重定位偏移与 addend 含义

Part B，`<main+0x1f>` 处的偏移量计算：

一个简单的计算是，设 `pnt` 的地址是 `addr(pnt)`，那么我们要求的相当于是 `addr(pnt) - addr(.bss)`，你需要深入理解这个相对重定位的含义，为什么要有一个 addent？你考虑读完 1c 这条指令（即其进入 D 译码阶段时），PC 已经到下一条指令（23）处了，所以要加一个 addent = -4 字节来抵消这个偏移（也即 23 - 1f），使得读入“指针”的位置是正确的。

于是，有：addr(.bss) + 0xc = addr(pnt) - 4，所以偏移量是 0xc + 4 = 0x10。

---

### 期末往年题勘误、详解 by Arthals · 2022 第三题 第3问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 244–246 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：.interp 节内容为动态链接器路径

### 第三题

第 3 问，interp（最前面的一节）放路径，也就是 ascii 码，解读出来就是动态链接器的路径。

---

### 期末往年题勘误、详解 by Arthals · 2022 第三题 第4问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 248–248 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：识别 PLT0

第 4 问，lt 其实给出了 plt0 了，就是 printf 前面那个，那个 push 和 jmp 明显是 plt0，所以是 1

---

### 2025第2次阶段测验-带答案 · 第14/15讲 19

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 215–222 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：编译优化的过程调用限制与存储器别名限制

19.（4分）编译优化时会有两种限制情况，分别解释说明原因。
答：
（1）为什么有“过程调用”限制：
过程调用可能存在“边带效应”的操作，例如改变某些全局变量或静态变量的值（1分）；
即使给定相同参数，过程调用的返回值可能会不同，如受全局变量影响等（1分）。
（2）为什么有“存储器别名”限制：
两个看起来不同的内存引用，可能指向相同的内存位置（1分）；一些编程语言（如C
语言）允许这样的操作存在或者不检查这样的问题（1分）。

---

### 2025第2次阶段测验-带答案 · 第14/15讲 20

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 223–238 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：不定项：链接器需要解析的符号

20.（不定项选择，2分）下面这段代码中，属于链接器要解析的符号包括：ADEG
8

<!-- ===== page 9 ===== -->

A.include B.stdio.h C.int D.cnt
E.print_value F.x G.main H.val
----------------------------------------------
#include <stdio.h>
int cnt = 10;
extern void print_value(int x);
int main() {
int val = 5;
print_value(val + cnt);
return 0;
}

---

### 2025第2次阶段测验-带答案 · 第14/15讲 21

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 239–277 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：目标文件反汇编中 0 填充与重定位、callq 偏移

21.（8分）下面是一段C代码main.c和对应目标文件main.o反汇编得到的代码。
----------------------------------------------
int array[2] = {1, 2};
int main(int argc, char** argv){
int val = sum(array, 2);
return val;
}
----------------------------------------------
0000000000000000 <main>:
0: 55 push %rbp
1: 48 89 e5 mov %rsp,%rbp
4: 48 83 ec 20 sub $0x20,%rsp
8: 89 7d ec mov %edi,-0x14(%rbp)
b: 48 89 75 e0 mov %rsi,-0x20(%rbp)
f: be 02 00 00 00 mov $0x2,%esi
14: bf 00 00 00 00 mov $0x0,%edi
19: e8 00 00 00 00 callq 1e <main+0x1e>
1e: 89 45 fc mov %eax,-0x4(%rbp)
21: 8b 45 fc mov -0x4(%rbp),%eax
24: c9 leaveq
25: c3 retq
----------------------------------------------
（1）地址14对应的mov指令，为什么要把0放到edi寄存器中?按源代码看，应该
是要放什么数，这里为什么是0，后续还会有什么操作？
答：要放到edi中的数据是数组array的首地址（1分）；编译成目标文件时，array
9

<!-- ===== page 10 ===== -->

数组在内存中的位置还不确定，所以用0代替（1分）；后续由链接器（1分）进行重
定位（1分），填上正确的数值。注：描述不用一模一样，按上述标记分数的关键点给
分。
（2）地址19对应的callq指令，看起来会转到地址1e，即下一条指令，这不合常
理，为什么？
答：callq指令要跳转到sum函数的起始地址（1分）；编译成目标文件时，sum函
数在内存中的位置还不确定，所以用0代替（1分）；按照callq指令的编码规则，
指令中保存的是callq下一条指令和要跳转的目标地址的差值，因为现在用0填充，
所以反汇编显示成下一条指令的地址，即1e（2分）。注：描述不用一模一样，按上
述标记分数的关键点给分。

---

### 2025Lab测验-无答案 · Lab 任务 7

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 101–105 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：Makefile 模式规则 %.o: %.c

7.  （2分）在Makefile模式规则中，%.o: %.c表示：
A. 任一.c文件修改后，所有的.o文件都需要重新编译
B. 每个.o文件依赖对应的同名.c文件
C. 当前目录中，需要存在一个名为 %.c 文件，否则make会报错
D. 当前目录中，如果存在一个名为 %.c 文件，会编译生成 %.o 文件

---

### 2025Lab测验-无答案 · Lab 任务 8

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 106–110 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：make 默认目标与执行过程

8.  （2分）关于make的执行过程，以下说法正确的是：
A. make默认会执行Makefile中定义的所有规则
B. 如果没有指定目标，make会执行第一个规则
C. make会按照规则的书写顺序依次执行
D. Makefile中规则的顺序是任意的，make会自行决定执行顺序

---

### 2025Lab测验-无答案 · Lab 任务 9

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 111–118 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：gcc -c 生成目标文件与 objdump -d 反汇编（兼 Machine Prog）

9.  （2分）关于汇编和反汇编的说法。下列哪个选项是正确的？
A. 反汇编得到的指令与原来的汇编文件的指令只需保证功能相同，并非一一对应
B. 必须先将汇编代码转换为 C 源文件，然后使用 gcc 编译得到目标文件，最后使用
objdump反汇编
C. 可以使用gcc -c命令将汇编代码直接生成目标文件，然后使用objdump -d命
令进行反汇编
D. 可以直接使用 objdump直接从汇编代码生成指令的字节编码，gcc在这个过程中
没有作用

---

### 2025Lab测验-无答案 · Lab 任务 10

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 119–123 行　·　模块判定：Compilation (Program optimization and linking)
> 考什么：binutils 中 ldd 查看共享库依赖

10. （2分）在binutils中，哪个工具可以用于查看共享库的依赖关系？
A. ldd
B. readelf
C. nm
D. objdump

---

## 三、相关试卷的参考答案 / 解析原文

### 2014期中-带答案 · 第七题参考答案（1）~3）），本卷其余答案随题内嵌

> 出处：`原文/期中/2014期中-带答案.md` 第 632–655 行

答案：

1）

```c
void count_pos1 (List *p, int *k) {
    int l, num=0, len;
    len = length(p)
    for (i = 0; i <len; i++) {
        if ( p->data > 0)
            num++;
        p = p->next;
    }
    *k = num
}
```

（4 分）

2） while(p) 或其他相同功能的语句　（2 分）

3） L1 和 L2 的代码没有数据依赖，完全可以并行。（2 分）

　　CPE 的下限为 3+1=4。（2 分）

---

### 2019期中-带答案 · 第二题（整数、浮点数）参考答案

> 出处：`原文/期中/2019期中-带答案.md` 第 270–289 行

 答案：
1类. 型   最大的整数+1  39+(-127)  39+(-127)是否溢出?
Unsigned   二进制：0000  十进制：168  是
Two’s Complement  0二0进00制  ：1000  十进制：-88  否
  0000
2浮.点  数  Decimal
0x80000000  v-a0 lues
0表x达41式18 0000  +是9否.5正 确
8

<!-- ===== page 9 ===== -->

(22  + +( 22505 0)– 2–502)5 0  !=  是
 225 +2 51 + 1 + 1 + 1  否
= = 2  + 4
Associative: Only 23 bits of mantissa (M), so 2 + 250 = 250
( 2 gets rounded off). So LHS = 0, RHS = 2.
Cumulative: 1 is 25 powers of 2 away from 225, so 225 + 1 =
i2t2 5d,o ebsunt’ 4t  igse t2 3r opuonwdeerds  oofff .2  away from 225, so
9

---

### 2019期中-带答案 · 第三题（机器级编程）参考答案，含已填答案的题目重排

> 出处：`原文/期中/2019期中-带答案.md` 第 388–486 行

答案：
机器级编程（15分，每空1分）
下面的C程序包含main(), caller(), callee()三个函数。本题给出了该程序的部分C代码和
X86-64汇编与机器代码。请分析给出的代码，补全空白处的内容，并回答问题。
注：汇编与机器码中的数字用16进制数填写
X86-64汇编与机器代码：                  答案填写处：
00000000004006cd <caller>:
  4006cd: 55                   push     %rbp
  4006ce: 48 89 e5               mov      %rsp,   %rbp
  4006d1: 48 83 ec 50            sub      $0x50,   %rsp
  4006d5: 48 89 7d b8            mov      %rdi,   -0x48(%rbp)
  4006d9: 64 48 8b 04 25 28 00    mov      %fs:0x28,  %rax
12

<!-- ===== page 13 ===== -->

  4006e0: 00 00
  4006e2: 48 89 45 f8            mov      %rax,   -0x8(%rbp)
  4006e6: 31 c0                  xor      %eax,   %eax
  4006e8: c6 45 d0 00            movb     $0x0,   -0x30(%rbp)
  4006ec: c6 45 e0 00            movb     $0x0,    (1)      (1) _-0x28(%rbp)_
  4006f0: 48 8b 45 b8            mov      _(2) ,   %rax     (2) _-0x48(%rbp) _
  4006f4: 48 89 c7               mov      %rax,   %rdi
  4006f7:                   callq    400510 <strlen@plt>
  4006fc:  89 45 cc               mov      _(3) ,   -0x34(%rbp)    (3) __%eax__ __
  4006ff:  83 7d cc 0e            cmpl     $0xe,   -0x34(%rbp)
  400703: 7f _(4) _                 jg       400752 <caller+0x85>   (4) __  4d____ _
  400705: 83 7d cc 09            cmpl     $0x9,   -0x34(%rbp)
  400709:                       jg       400720 <caller+0x53>
  40070b: 48 8b 55 b8            mov      -0x48(%rbp), %rdx
  40070f: 48 8d 45 d0            lea      _(5) ,   %rax     (5) _-0x30(%rbp)__
  400713: 48 89 d6               mov      %rdx,   %rsi
  400716: 48 89 c7               mov      %rax,   %rdi
  400719:                   callq    400500 <strcpy@plt>
  40071e:                      jmp      40073b <caller+0x6e>
  400720: 48 8b 45 b8            mov      -0x48(%rbp), %rax
  400724: 48 8d 50 0a            lea      0xa(%rax),  %rdx
  400728: 48 8d 45 d0            lea      -0x30(%rbp), %rax
  40072c: 48 83 c0 10            add       (6) ,   %rax     (6) __0x8_    __
  400730: 48 89 d6               mov      %rdx,   %rsi
  400733: 48 89 c7               mov      %rax,   %rdi
  400736:                   callq    400500 <strcpy@plt>
  40073b: ff 75 e8               pushq    -0x18(%rbp)
  40073e: ff 75 e0               pushq    -0x20(%rbp)
  400741: ff 75 d8               pushq    -0x28(%rbp)
  400744: ff 75 d0               pushq    -0x30(%rbp)
  400747: e8 _ (7) _           callq    400666 <callee>     (7) _1a ff ff ff__ _
  40074c: 48 83 c4 20            add      $0x20,   %rsp
  400750:                      jmp      400753 <caller+0x86>
  400752: 90                     nop
  400753: 48 8b 45 f8            mov       (8) ,   %rax      (8) _-0x8(%rbp)___
  400757: 64 48 33 04 25 28 00    xor      %fs:0x28,  %rax
  40075e: 00 00
13

<!-- ===== page 14 ===== -->

  400760:                       je       400767 <caller+0x9a>
  400762:                   callq    400520 <__stack_chk_fail@plt>
  400767: c9                     leaveq
  400768: c3                     retq
C代码：                                                 答案填写处：
#include <stdio.h>
#include "string.h"
#define N   _(9)_                                    (9)_____10_  __
#define M   _(10)_                                   (10)____5  ____
typedef union {char str_u[N]; long l;} union_e;
typedef struct {char str_s[M]; union_e u; long c;} struct_e;
void callee(struct_e s){
 char buf[M+N];
 strcpy(buf, s.str_s);
 strcat(buf, s.u.str_u);
 printf("%s \n",buf);
}
void caller(char *str){
 struct_e s;
 s.str_s[0]=‘\0’;
 s.u.str_u[0]=’\0’;
 int len = strlen(str);
 if(len>=  M+N)
  _(11)_;                         (11)___return____
 else if(len<N){
  strcpy(s.str_s, _(12)_);                    (12)__ __str_   __
 }
 else{
  strcpy(s.u.str_u,_(13)_);                  (13)___str+M__  _
 }
 callee(s);
14

<!-- ===== page 15 ===== -->

}
int main(int argc, char *argv[]){
 caller("0123456789abcd");
 return 0;
}
caller函数中，变量s 所占的内存空间为:           (14)    32 字节
该程序运行后，printf函数是否有输出？输出结果为:       (15)    abcd

---

### 2020期中-带答案 · 第三题参考答案与考察内容解析

> 出处：`原文/期中/2020期中-带答案.md` 第 303–348 行

参考答案：
1、（注：本题十六进制未带0x，不扣分）
（1）return;  (注：未带分号，不扣分)
（2）params->n
（3）%rdi
（4）-0xc
（5）%rbp
（6）sub  (注：写成subq，不扣分)
（7）jle
（8）%rax
（9）%edx
（10）-0x8(%rbp)
（11）0x00005555555551af < foo >  （只写数值或者<foo>，都算正确）
（12）0x555551f9
（13）0x555551de
10

<!-- ===== page 11 ===== -->

（14）0xffffe2f0
2、计算阶乘
考察内容：
1.  对51c8及51fb的理解，由51c8和51fb可以知道这是跳转指令，跳转到51fb，
阅读汇编代码可知这里就结束了。结合源代码这里是return退出
2.  对51ca和51ce的理解，由51ca可知此时rax保存的是param的地址，51ce
直接从地址取值，所以取出的是第一个数n，即params->n
3.  51d4和51d6通过两个寄存器传参，分别是%esi和%rdi，5195使用了%esi，推
出此处使用%rdi
4.  对源程序及5195的理解，由519c可知eax保存的是param->product，所以这
里是执行乘法操作，另一个操作数是参数x，5195处已经把x保存在-0xc(%rbp)
中，所以就从这里读取数据
5.  Callee保存的参数，518d保存，这里读取
6.  进入函数后首先分配栈帧，通过减%rsp实现
7.  源程序if (params->n <= 1)的判断
8.  源程序params->n--;，上一句已经把params->n读到%eax中，这里进行修改
9.  对源程序 params->n--;的理解，51e4 已经把计算结果保存在%edx 中，这里
把%edx的结果进行保存
10.  与51e7相同，与51d0的内容也相同，考察调用函数的传参方法
11.  函数递归调用，由foo函数的内容可得
12.  函数调用保存返回地址，首先进入foo函数，所以返回的是调用foo函数后的
下一条指令地址
13.  函数调用保存返回地址，在 foo 函数中进入bar函数，所以返回的是调用bar
后的下一条指令
14.  Push之后栈顶的内容，推测出此时的rbp是在上一次函数调用，进入callee时
设置的。上一次函数调用保存的返回地址在0x7fffffffe2f8，所以上一次rbp的
值是0x7fffffffe2f0

---

### 2021期中-带答案 · 第二题参考答案与解析（数据表示）

> 出处：`原文/期中/2021期中-带答案.md` 第 338–356 行

参考答案：
𝟏
(1)fbac  (2)负  (3)1108  (4)√  (5)×  (6)255  (7)860  (8)𝟔𝟒
(9)是  (10)0x00ffffff
解析：本大题共设基础题5分,中档题3分,难题2分.
I.本题考察数据换算和大小端,属基础题.首先通过x86-64判断该机器使用小端
法,由此得到该短整型的16进制表示为(1)0xfbac.由于其二进制最高位为1，
因此x是一个(2)负数.将其取反加一得到0x0453=1108,因此x的绝对值为
(3)1108.
II．本题考察整数的表示和运算,属基础题.因为x严格小于y,z,所以y和z都
不是TMin,所以答案为(4)√.由于sizeof()的返回值是无符号数,因此左边的
表达式被强制转化为无符号数UMax,因此填(5)×.
III.本题考察IEEE浮点数标准,浮点表示和舍入,属中档题.最大规格化数的二
进制表示为011101111111,值为(6)255.注意到该浮点系统下最小的负非规格
化数为−$(),所以−"!#$是非规格化数,其16进制表示为0x(7)860. "!#$的二进制
表示为0.00000011,根据向偶数舍入的规则得到(8)$().
IV.本题考察非规格化浮点数与规格化浮点数的表示方法,属难题.阶码为1时的
规格化浮点数和非规格化浮点数相邻两个数之间的差是相同的，过渡平滑.因此答
案为(9)是,(10)0x00ffffff.

---

### 2021期中-带答案 · 第三题参考答案（机器级编程）

> 出处：`原文/期中/2021期中-带答案.md` 第 406–425 行

答案：
（1）m == 1
（2）m & 1或 m % 2 == 1 或其余相同语义的表达式
（3）f(n - 1, m * 3 + 1)
（4）%rsp
（5）07
（6）516b <f+0x22>
（7）-0x20
（8）51ab <f+0x62>
（9）%rdx
（10）sar
（11）0x00007fffffffe580
（12）0x0000000000000005
（13）0x00005555555551a1
15

<!-- ===== page 16 ===== -->

（14）0x0000000000000003
（15）2

---

### 2021期中-带答案 · 第四题参考答案（Y86-64 间接跳转）

> 出处：`原文/期中/2021期中-带答案.md` 第 501–544 行

1.
Stage  jxx *rB
Fetch  icode : ifun ← M1[PC]
rA : rB <- M1[PC+1]
valP <- PC+2
Decode  valB <- R[rB]
Execute  valE <- valB + 0
Cnd = Cond(CC, ifun)
Memory  /
Write Back  /
Update PC  PC <- Cnd ? valE: valP
2. 不需要。间接跳转在decode阶段时SelectPC正好利用最新转发的valB
的值作为预测地址访问指令内存。
1 2 3 处都可以插入。插入的内容见下。④是无效的插入位置。注意，原来的
M_XXX条件和W_XXX条件互斥，所以其顺序任意，但它们都不会和新加入的条
件冲突。例如mispredict发生时，Decode阶段的指令已经被清空，所以最终
不会导致多个条件成立。
word f_pc = [
// D_icode == IJREGXX: d_valB;
(M_icode == IJXX || M_icode == IJREGXX) && !M_cnd : M_valA;
// D_icode == IJREGXX: d_valB;
W_icode == IRET : W_valM;
D_icode == IJREGXX: d_valB;
1 : F_predPC;
④
]
19

<!-- ===== page 20 ===== -->

3. E_icode == IJREGXX && !e_Cnd
F  D  E  M  W
normal/stall bubble  bubble  normal  normal
分析方法同IJXX。注意，触发条件是在E阶段，因为E阶段结束、M阶段开始
时就要控制流水线寄存器。
4. 15 13 20
n == -1: line 8分支预测错误，惩罚2个周期。一共9 + 2 + 4
(trailing cycles for ret) = 15。
n == 0: 一共9 + 4 (trailing cycles for ret) = 13。
n == 1: line 12和13发生load/use hazard （不考虑加载转发），惩
罚1个周期。一共12 + 1 + 4 (trailing cycles for ret) = 17。
n == 2: line 12 和 line 13，以及line 10 和 line 11 各发生一次
load/use hazard，共惩罚2个周期。一共14 + 2 + 4 (trailing
cycles for ret) = 20。

---

### 2021期中-带答案 · 第六题参考答案与考察点

> 出处：`原文/期中/2021期中-带答案.md` 第 707–722 行

答案：
1）4（考察union的大小是最长字段 + 末尾padding）
2）func函数计算一个s_element链表中所有元素u1.f的和。（考察源代码阅读）
3）movq  8(%rdx), %rdx （考察第三章汇编代码，同时考察结构体内部对齐的
padding。注意立即数前面没有$）
4）（考 察代码阅读 能 力  ）
① p->next
② p->next->u1.f
③ p->next->next
④ p
5）浮点数加法不满足结合律，可能会导致func1和func函数结果不同。（考察浮
点数的结合性，重新结合变量在循环展开优化时的限制）
6）寄存器溢出（，过多的循环变量会分配到栈上）（教材378页内容，答出寄存
器溢出的意思即可，考察对关键路径和循环展开的理解）
7）0x4098 -1（考察浮点数的表示，大小端，同类型指针之差是地址差除以数据
差，一半1分）

---

### 2022期中-带答案 · 第一题选择题答案表

> 出处：`原文/期中/2022期中-带答案.md` 第 48–51 行

题号  1  2  3  4  5  6  7  8  9  10
回答  D  D  D  B  C  D  B  B  C  B
题号  11  12  13  14  15  16  17  18  19  20
回答  B  D  B  C  C  D  A  B  A  D

---

### 2022期中-带答案 · 第二题参考答案与评分说明

> 出处：`原文/期中/2022期中-带答案.md` 第 333–346 行

答案：
1)  -1.8125 0x09    二进制浮点数到十进制浮点数的转化运算
2)  大于         浮点数的大小比较，先看符号位，再看阶码位
3)  01110000      整数到浮点数的转化运算，此处为上溢出的情况
4)  11112        考察浮点格式
5)  是 否        阶码位最大为 1102=610，6-3=3，能精确表达的
值为11112，故会发生溢出，但不会发生舍入
6)  更多        浮点数格式的考察
7)  5, 10, -1023/(2^24)  在符合IEEE标准的浮点系统下，实数1的
表示为阶码为 0111...1, 其余位为 0. 所以 m = 5, n = 10. 此浮
点系统能表示的最小负非规格化数的位级表示为 1000 0011 1111
1111, 即 -1023/(2^24).
第1-6题每题2分（两空的每空1分，一空的2分），第7题3分（每空1
分）

---

### 2022期中-带答案 · 第三题参考答案与补充说明

> 出处：`原文/期中/2022期中-带答案.md` 第 421–446 行

参考答案如下，此题源于习题3.31和3.41的合并，因而可以算作简单题。
void switcher(long a, long b, long c, struct prob *sp){
  long val;
  switch(a){
12

<!-- ===== page 13 ===== -->

    case     5    : c =      b^31       ;
    case     2    : val =    c+2022     ; break;
    case     0    : c =      c-54        ;
case     1    : val =    (c+b)*3     ;break;
    case     3    : val =    sp->s.x     ;break;
    case     7    :   sp->s.z = 1898     ;break;
    case     6    : val =    *(sp->p)    ;break;
    default:       sp->next = sp         ;break;
  }
  sp->s.y = val;
}
补充说明：
上面的每个单元格之间原则上是可以互换的，但应保持程序基本语义不变。
 (c+b)*3写成(b+c)*3或者3*(b+c)或者3*(c+b)也都算对。有同学写成了
3*b+3*c，周一阅卷的时候这样的写法没有给分，但后来我们注意到有的编译器
可能会将其优化为题目中的汇编代码。所以这样的书写也可以给分。
凡是不符合c语言语法的写法都不能给分。例如有同学写成3(b+c)的不能得分，
也有同学写成了b xor 31的同样不能给分。

---

### 2022期中-带答案 · 第四题参考答案（各阶段操作与周期数解析）

> 出处：`原文/期中/2022期中-带答案.md` 第 518–550 行

答1.案 ：
Stage  cpopqXX rA
icode:ifun  M1[PC]
Fetch  rvAa:lrPB    PCM+12[P C+1]
valB  R[%rsp]
Decode  v alA  R[%rsp]
valE  valB + 8
Execute  C nd ← Cond(CC, ifun)
Memory  valM  M8[valA]
if (Cnd) R[%rsp]  valE
Write back  i f (Cnd) R[rA]  valM
PC update  P C  valP
（每空1分，共7分）
23..  ①IPOPQ ②!e_Cnd （每空1分，共2分），第1空填ICPOPQXX也算对
触d_发sr条cB件} ：E_icode in {IMRMOVQ, IPOPQ} && e_dstM in {d_srcA,
控制逻辑：（选填stall, bubble和normal）
F  D  E  M  W
Stall  Stall  Bubble  normal  normal
（共3分，其中e_dstM in {d_srcA, d_srcB} 1分，全对才得分；控制逻
16

<!-- ===== page 17 ===== -->

辑2分，全对才得分）
4.
解析：循环过程为Line 4-9,共6条
n=3 : 4(填充流水线)+3(Line 1~3)+6*3(共三次循环)+1(Line
7-8:load-use hazard)+2(Line 9:branch misprediction)+1(ret指
令)=29
n=1 : 4(填充流水线)+3(Line 1~3)+6  (第一次循环)+1(Line
7-8:load-use hazard)+2(Line 9:branch misprediction)+1(ret指
令)=17
(对任意一空得2分, 两空全对得3分)

---

### 2022期中-带答案 · 第五题参考答案与解析

> 出处：`原文/期中/2022期中-带答案.md` 第 607–652 行

1.（1）.64（3分）
由S=4可得s=2, 故b=8-s-t=3，即每个cache block的大小为B=23=8 Bytes。
Cache总容量C=S*E*B=64 Bytes.
本题考察cache的基本概念，属于容易题。
（2）.否（2分）
  V  Tag  V  Tag
SET 0
SET 1
SET 2  1  110
SET 3
0xd2的二进制表示为110 10 010，可得其组号为set 2。在当前状态下set 2
虽然有tag为110的cache block，但此block的有效位V=0，所以不命中。
由于set 2有一个V=0的cache block，所以cache更新后，应当将这个block
的有效位设置为1，并将其tag位设置为110.
本题考察访问cache的基本操作，属于容易题。
注意：填写此表时只要表达的意思对即可给分。（比如只写了set 2的第一个block
的有效位，或者将其他没有改动的地方抄了下来都应算对）
（3）.50%（2分）；420（2分）
19

<!-- ===== page 20 ===== -->

0xc8的二进制为110 01 000，命中set 1。0x16的二进制为000 10 110，
查找set 2，由于没有标签为000的block，所以不命中。根据LRU策略，set
2中tag为101的block被替换出去。0x01的二进制为000 00 001，查找
set 0，其中tag为000的block有效位为1，命中。0xb5的二进制为101 10
101，查找set 2，由于tag为101的block已经被替换出去了，所以不命中。
综上，命中率为2/4*100%=50%.
总延迟为2*10+2*(10+190)=420周期。
此题考察cache的访存行为，较为综合，时间可能花费较长。
2.（1）.否（2分）；19（1分）
由于cache采用非写分配策略，所以代码运行到3、4行时并没有将f[0]和f[1]
读入cache，因此在第一次执行到第六行读取f[0]时是不命中的。
第一次循环体执行时，所有访存均不命中。当第i（i>1）次循环执行时，第6行
的读数据命中cache，第7行的读数据的地址由于在第(i-1) 次循环是写不命中，
而cache采取非写分配策略，因此该block还没有被加载到cache中，所以仍
是不命中。第9行的写是第一次访问该地址，因此也是不命中的。即在第二次即以
后每次执行循环体时，会有一次读命中、一次读不命中和一次写不命中。循环体共
执行20次，所以共命中cache 19次。
本题考查对cache写策略的理解。计算命中次数需要发现一定规律，难度中等。
（2）.40（1分）
由于本题中cache采用写分配策略，因此第一次写不命中时就会把相应的block
加载到cache中，从而在下一次读的时候就可以命中了。在每次循环体执行时，
第6行和第7行的读数据是命中的，第9行的写数据是不命中的。循环体共执行
20次，故命中cache总次数为4.
本题同上题，考察对cache写策略的理解。同样需要发现一定规律，难度中等。

---

### 2023期中-带答案 · 第一题选择题答案表

> 出处：`原文/期中/2023期中-带答案.md` 第 49–52 行

题号  1  2  3  4  5  6  7  8  9  10
回答  C  D  B  C  D  A  A  C  A  B
题号  11  12  13  14  15  16  17  18  19  20
回答  C  D  A  A  D  E  D  A  D  D

---

### 2023期中-带答案 · 第二题参考答案与评分标准修订

> 出处：`原文/期中/2023期中-带答案.md` 第 435–453 行

答案：
1. 011110112; 000000112 （2分2分）
2. 011111102, 448, 2 （2分 1分 1分）
3. 不会，会 （2分 2分）
4. 1/4, 3/8(向偶数舍入) （1分 1分）
5. E4M3 （1分 1分）
本题在深度学习模型量化压缩的场景下，主要考察对于IEEE-754标准的掌握和对
浮点型指数部分(E)和底数部分(M)对于范围和精度的影响，并拓展考察在实际应用
中浮点数计算顺序和选取适当浮点型的软件程序员需要注意和警惕的问题，引导同
学们深入思考并将ICS的知识真正的学以致用
评分标准修订：
(1) 写1110000000000000(13个0)可以给1分, 原来不得分
14

<!-- ===== page 15 ===== -->

(2) 写0.0000000000000011(算0.总共15个0)可以给1分, 原来不得分
(3) 写111000000(6个0)可以给1分, 原来不得分
以上三种答案必须1和0的个数正确方可得1分, 前面可以加0b的前缀, 其他

---

### 2023期中-带答案 · 第三题参考答案

> 出处：`原文/期中/2023期中-带答案.md` 第 508–527 行

答案：
1：0
2：1
3：n
4：1
5：%rbp
6：%rbx
7：-0x1或-1
17

<!-- ===== page 18 ===== -->

8：%esi
9：%edi
10：%eax
11：%edx
12：%ebx
13：ret
14：10
15：120

---

### 2023期中-带答案 · 第四题参考答案

> 出处：`原文/期中/2023期中-带答案.md` 第 587–600 行

答案：
(1) valE
(2) valA
(3) D_valP
(4) e_valE
(5) m_valM
(6) M_valE
(7) W_valM
(8) W_valE
(9) d_rvalA
(10) Bubble
(11) Normal
(12) Stall
(13) Stall

---

### 2024期中-带答案 · 第二题参考答案与解析

> 出处：`原文/期中/2024期中-带答案.md` 第 354–381 行

参考答案：
1. （1） 否；是。  （每空1分）
（2） 3.75。  （2分）
2. （1） 10000001；2-14。 （每空2分）
（2） 3。    （2分）
3. （1） 否；否。  （每空1分）
（2） -1105。  （3分）
解析：
本题题目背景较新颖，将第二、三章内容联系起来，考查学生对有关知识的综合理
解。考虑到本题为第一道大题，且覆盖的知识面较广，因此对题目整体难度的要求
较低，主要考察学生对基本概念的掌握和理解。
1. （1） a. 考查基本概念。该代码使用了 x86-64 指令集特有的vmovss指
令，只能在 x86-64 架构上运行，其他架构不支持这种特定的汇编指令。
     b. 考查对指针和指针引用的理解，属于简单题。
（2） 考查浮点数的表示以及x86-64的小端法表示，属于基础题。
2. 考查对浮点数表示方法的理解，属于基础题。
3. （1） a. 考查联合（union）的有关概念。converter.i和value有着相
同的位模式，而(int)value基于数值对value进行类型转换。因此在绝大
部分情况下代码的输出和printf语句的输出都不同。b. 考查基本概念，属
11

<!-- ===== page 12 ===== -->

于简单题。
（2）本题考查浮点数转换为整数的舍入规则（向零舍入）以及有符号整数的基
本运算，(int)(converter.f)的值为-1104（向零舍入）。converter.i
和 value 有着相同的位模式，而有符号整数和单精度浮点数的最高位均为符
号位，因此(converter.i >> 31)的值为-1。

---

### 2024期中-带答案 · 第三题参考答案与完整汇编

> 出处：`原文/期中/2024期中-带答案.md` 第 462–531 行

参考答案
void foo(char *p)
{
  int len = strlen(p);
  char tmp = *p;
  *p = *(p + len - 1);
  *(p + len - 1) = '\0';
  if (strlen(p + 1) > 1)
  {
    foo(p + 1);
  }
  *(p + len - 1) = tmp;
}
0000000000001189 <foo>:
    1189:  f3 0f 1e fa           endbr64
    118d:  55                     push   %rbp
    118e:  48 89 e5              mov    %rsp,%rbp
    1191:  48 83 ec 20           sub    $0x20,%rsp
    1195:  48 89 7d e8           mov    %rdi,-0x18(%rbp)
    1199:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    119d:  48 89 c7              mov    %rax,%rdi
    11a0:  e8 db fe ff ff        call   <strlen@plt>
    11a5:  89 45 fc              mov    %eax,-0x4(%rbp)
15

<!-- ===== page 16 ===== -->

    11a8:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11ac:  0f b6 00              movzbl (%rax),%eax
    11af:  88 45 fb              mov    %al,-0x5(%rbp)
    11b2:  8b 45 fc              mov    -0x4(%rbp),%eax
    11b5:  48 98                  cltq
    11b7:  48 8d 50 ff           lea    -0x1(%rax),%rdx
    11bb:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11bf:  48 01 d0              add    %rdx,%rax
    11c2:  0f b6 10              movzbl (%rax),%edx
    11c5:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11c9:  88 10                  mov    %dl,(%rax)
    11cb:  8b 45 fc              mov    -0x4(%rbp),%eax
    11ce:  48 98                  cltq
    11d0:  48 8d 50 ff           lea    -0x1(%rax),%rdx
    11d4:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11d8:  48 01 d0              add    %rdx,%rax
    11db:  c6 00 00              movb   $0x0,(%rax)
    11de:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11e2:  48 83 c0 01           add    $0x1,%rax
    11e6:  48 89 c7              mov    %rax,%rdi
    11e9:  e8 92 fe ff ff        call   <strlen@plt>
    11ee:  48 83 f8 01           cmp    $0x1,%rax
    11f2:  76 10                  jbe    1204 <foo+0x7b>
    11f4:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11f8:  48 83 c0 01           add    $0x1,%rax
    11fc:  48 89 c7              mov    %rax,%rdi
    11ff:  e8 85 ff ff ff        call   1189 <foo>
    1204:  8b 45 fc              mov    -0x4(%rbp),%eax
    1207:  48 98                  cltq
    1209:  48 8d 50 ff           lea    -0x1(%rax),%rdx
    120d:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    1211:  48 01 c2              add    %rax,%rdx
    1214:  0f b6 45 fb           movzbl -0x5(%rbp),%eax
    1218:  88 02                  mov    %al,(%rdx)
    121a:  90                     nop
    121b:  c9                     leave
121c:  c3                     ret
16

<!-- ===== page 17 ===== -->

12） “SCIEVOLI”
13）3

---

### 2024期中-带答案 · 第四题参考答案与评分标准

> 出处：`原文/期中/2024期中-带答案.md` 第 587–611 行

参考答案
1）
word d_valA = [
      D_icode in {ICALL,IJXX } : D_valP;
      d_srcA == e_dstE : e_valE;
      d_srcA == M_dstM : m_valM;
      d_srcA == M_dstE : M_valE;
      d_srcA == W_dstM : W_valM;
      d_srcA == W_dstE : W_valE;
      1 : d_rvalA;
]
2）
Memory(访存)，m_valM，1；
3）
Memory(访存)，Execute(执行)，M_valA；
4）
word e_valA = [
      E_icode in { IPUSHQ, IRMMOVQ } && E_srcA ==
M_dstM : m_valM;
1 : E_valA;
]
5）
Fetch  Decode  Execute  Memory  Write back
stall  stall  bubble  normal  normal
评分标准：每空1分

---

### 2019、2020期末-答案解析 · 全文即 2019、2020 期末答案解析（非完整题干）

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 1–276 行

# 2019、2020期末-答案解析

> 来源：`往年题/期末/2019、2020期末-答案解析.pdf`　共 8 页

<!-- ===== page 1 ===== -->

ICS2019、2020期末考题分析
王畅
2021年12月
注意：水平有限，不保证正确，祈请原谅。 最后更新于2021年12月26日18:34
2020年
选择题
1. C。A是正确的，不能把attacklab和bomblab混淆了。C的错误原因在于可以支持可变栈帧，
编译时不能确定大小，必须使用帧指针。
2. B。计算知该缓存有4组，每组2行4字节，所以容量为32字节。每行需要4字节存储块的
内容，1位有效位和2位tag。鉴于课本没有讲解cachephysicalsize的计算方法，而且实际上
cacheline可能还有一些额外的ﬂagbit，因此1项后半部分实属超纲。但额外的3位无论如何
也占不到2字节，因此可判断1错误。3说反了，B的格式导致相邻的缓存块进入相同的组
中，会影响空间局部性比较好的程序（顺序访问），这样一来4错误（参看书P432）。最后来
计算2，注意到访问1、7、8之后，三个缓存块会进入A中的不同组，而B则会发生一次替换
（8~11和0~3在同一组），后来再访问就会发生miss而A会命中，所以2正确。综上2正确。
3. A。取x=INT_MIN即可。B正确，因为~x+~y+1=~x+~y+2-1=-(x+y)-1=~(x+y)。讨论
x, y的大小关系立刻知道C是正确的。由于>>是向下舍入的，所以D正确。
4. B。送分题，float不能精确表示绝对值224+1及以上的整数。
5. D。送分题，RISC中寄存器一般更多。
6. D。指令长度为6字节，内存地址需要用基址加上偏移计算。
7. D。只有编译时打桩需要访问源代码，A错误。B，可执行目标文件中仍然会有ABS节（文件
名）。程序的入口是_start，后者跳到题干所说的位置，C错误。D是正确的（书P489原
话），但是-fPIC（大写）选项更好。
8. B。请注意编译器看不到两边x类型的不同，因此不会报错。链接器会将x初始化为0，在
f1.c中编译器生成的代码视其为浮点而在另一边视其为整数，所以自增结果是一个很小的
浮点数，转为整数是0。
第1页,共8页

<!-- ===== page 2 ===== -->

9. B。注意printf是行缓冲，缓冲区会被复制，最后都一次性输出。另外fork() && fork()
是父进程再fork()，子进程不fork()，而fork() || fork()则是子进程再fork()，
父进程不fork()。故实质上一次产生3个进程，所以答案为32×2=18。（如果不考虑缓冲
区则要去掉第二次产生的6个净拷贝，答案应为12。）
10. C。送分题，外部I/O会触发中断，CPU执行完当前指令之后可能会去处理该中断。
11. A。送分题，属于书上原话。
12. D。缺页是故障，这种故障需要重新执行引发故障的指令；系统调用是陷阱。二者都是同步的
异常，而且处理完毕是从内核态回到用户态，会处理信号。
13. B。A显然是正确的。B我们实验过，一般这种读取对于用户来说是允许的，参看书P511。C
一般同学不会实验过，需要推理一下，因为参数列表和环境变量实际上是程序自己处理的，
而且shelllab中重定向是shell帮忙完成的，故推测C正确。D是陆老师著名的“灵魂出窍”
例子，即printf在信号处理程序中可能导致死锁。
14. B。根据Corei7的用法，每张页表恰好有一页，每个页表项8字节，所以每个VPN都是
14−3=11位，于是四级VPN和VPO一共58位。
15. B。第二句话表明题目中的内存是按字节寻址的。首先计算VPO为10位，每个VPN都是8位，
恰好是34位虚拟地址。最好情况是1MB虚拟地址映射到连续的页，即占有1024页，所以需
要1024个三级页表条目（占有4页），1个二级页表条目（占1页）和1个一级页表条目（占
1页），即需要6KB。最坏情况是每字节都恰好映射到不同的页面，也就是占有1024×1024
个不同的页面（可以实现）。这些页面可以用尽全部256×256张三级页表（比如每16页用一
个三级页表），所以需要256×256+256+1=65793页，即65973KB。
16. B。和物理地址无关，VPO为13位，VPN均为10位，所以需要三级页表。
17. D。根据题目的描述就可以推断是A位和D位。
18. A。未解之谜。如果将共享区域理解为MAP_SHARED则D错误；否则共享库也是一种共享区
域，会发生COW。如果参照Wikipedia上的解说，COW是一种技术，用户可以自行实现，那
么对等线程之间也可能发生COW（例如string y=x之后修改y，C++中用COW实现）。
A可能是更好的选择。
19. A。其他段中都可能有指针，其引用的内存需要管理。代码段中则没有这种问题。
20. C。服务器端的进程通过accept来建立已连接套接字。D应阻塞在read，参看课程投影片。
21. D。送分题，根据这个命令的字面意思也能看出获得的是主机名，参数-i表示返回点分十进
制的IP地址。网络字节顺序和大端法是一回事。
22. C。a)是共享的（在数据段），b)也是共享的（栈是私有的），c)是共享的，属于书上原话，或
者从同一进程的概念中读解出，d)是特别的上下文，是私有的。所以有3个。
第2页,共8页

<!-- ===== page 3 ===== -->

23. C。此题意义不大。主要的困难在于最终的正确顺序并不是确定的一个全序，所以需要找
一个“最优”的全序。大概估计一下，𝐿2,𝑈2,𝑆2和𝐿4,𝑈4,𝑆4之间不能有重叠，𝐿1,𝑈1,𝑆1和
𝐿3,𝑈3,𝑆3之间亦然，所以可能是
𝐿2,𝐿1,𝑈1,𝑆1,𝐿3,𝑈2,𝑆2,𝐿4,𝑈4,𝑈3,𝑆4,𝑆3.
数出逆序数为12。实际上，合法的全序只有十几种，可以枚举验证答案正确性。
24. B。注意主线程如果调用诸如pthread_exit的函数退出，是不会引发其他线程退出的，所
以A为一错误描述。但是如果主线程调用了exit（或者return）,则整个进程都会结束，
自然其他线程也结束。
25. B。首先1和2分别获得a和c的锁，然后2再获得b的锁，1和3分别等d的锁和a的锁。
此时如果2释放c和b的锁，1和3无论如何都将出现互相等待（a、d）的情况，因此发生了
死锁。
解答题一
1. 10ns。送分题。
2. 60。题目中为一个8重循环，具体执行了什么不重要。每次循环出现数据冒险一次，故需要7
个周期。最后分支预测错误有2个周期的惩罚，但是已经算在4个trailingcycle中了，所以需
要60个周期。
3. 47；5；96。两个缓存都是5位偏移，10位tag（这里可能应该认为地址空间是16位）。因此
指令缓存只会不命中一次，剩下47次都是命中的。数据缓存每块可以放下4个长整数；但注
意起始位置不是32字节对齐的，所以会有3次不命中，剩下5次都是命中的。不命中一共额
外造成了9×4周期的惩罚，所以需要96周期。
解答题二
1. 答案如下：
符号 .symtab 有条目？ 符号类型 定义符号的模块 节
buf 有 外部 m.o .data
bufp0 有 全局 swap.o COMMON
count 有 局部 swap.o .bss
func 有 全局 swap.o .text
temp 无 / / /
送分题。注意外部符号要填定义的模块中的节。
第3页,共8页

<!-- ===== page 4 ===== -->

2. 0x00002020, 0x000000be, 0x0000a000, 0x0000900d, 0x00decade。
1处，ADDR=1000, offset=a, addend=-4，结果为302e-1000-a-4=0x00002020。3
处类似，结果为10e4-1000-22-4=0x000000be。4处结合汇编代码知道目标符号是buf
的地址移入，所以是0x0000a000（绝对重定位）。9处对应bufp1，下一条指令地址是知道
的，可以不用重定位算法，所以是a250-1243=0x0000900d。11处对应count，下一条指
令地址也是知道的，所以是dedd38-125a=0x00decade。具体填要注意小端法和立即数格
式。
解答题三 4行，内容为
a b c 0
a b a 1
a a b 1
a a a 2
此题直接画进程树，在结点旁边标注父进程和子进程，并写出状态变化就可以。考点为每次父进程
open时，指针都重新回到文件开头；dup则保持文件指针为同一个；count四个进程相互独立。
注意（相对的）父进程总是用wait(NULL)等待子进程，所以输出的顺序一定是子子、子父、父
子、父父。
解答题四 答案如下：
dTLB 失效次数
𝑛 缺页次数 1 2 3 4 5 6
8 1 1 1 1 1 1 1
16 2 2 2 2 2 2 2
64 24 24 24 24 24 24 24
512 1536 266436157 268661500 252182591 252182591 235241284 521528
题目看起来非常复杂，实际上分析一下就可以发现没有多少耦合，数据也凑得比较好，很容易
拿到大部分分数（但是此题意义不大，而且没有考察虚拟内存的精华）。
不难看出，缺页次数只和矩阵占的页数有关（无论怎么访问），而TLBmiss等价于为一个缓存
块4KB，64行的全相联高速缓存的miss次数。这样一来，数据占据页面的个数，也就是缺页次数
为⌈3𝑛2×8/212⌉，分别为1、2、24和1536。由于TLB是全相联的，只有满了之后才会发生替换，
所以前三行的答案已经全部得出（缺页次数=TLBmiss次数=页面个数）。
𝑛=512时的TLB行为模拟比较简单，但仍然有一定的工作量，这1536个页面每页恰好对应矩
阵的一行，所以TLBmiss的次数就转变为对行访问的分析，由于全相联缓存的行可以放在任何位
置，所以简单替换就可以，通过计算可以得出答案。
解答题五
第4页,共8页

<!-- ===== page 5 ===== -->

1. 死锁。可以看出，这实际上就是哲学家就餐问题，如果所有的同学同时拿起左边那个同学手
机P(UP(i))，就发生死锁。
2. 分别填0和0。观察代码知道Dave的方法每次只有一位同学去找洞主，也就是说26个同学
轮流去验证。由此知道只需要一个互斥锁即可。
3. 1 2 2 1。根据1问的例子可以知道依赖关系成环是最大的问题。因此我们可以让除一位同
学之外的同学正常工作，而那位同学则反过来工作，不难证明这个体系无死锁且无竞争（事
实上，还有一种方法，即要求单号同学先拿左边的手机，而双号先拿右边的手机）。
4. 分别填1、0、<、3、2、<=。根据代码容易看出mutex保护结构体，zero是一个“等待
信号量”，所以计数降到0以下时需要等待，由此发现其初值应该是0。请注意 3、2 不能
反，否则会造成死锁。
2019年
选择题
1. A。唯有这一项会先算d+a，可能发生不结合的问题。
2. B。数据冒险一般是指当前指令没有写回，而下几条指令在流水线就已经要用到的情况。
3. A。除法向零取整，移位向下取整；2相当于给负数添加一个修正，3相当于转成正数后模拟
除法行为。所以a=-2016, b=-2016, c=-2016。
4. C。CISC变长指令，有不少指令的长度是要比RISC短的。当代手机常常采用ARM架构，这
是RISC；实际上对能耗要求高或者结构简单的设备一般都用RISC。
5. B。DRAM常常组织成一个矩阵族，整行访问时效率比较高，B错误。SSD设备擦写的时间
会比读取要高一个数量级。一般来说，SRAM使用比较多的晶体管，而DRAM晶体管很少，
主要基于电容，SSD是闪存，晶体管也不会很多，因此后二者的存储密度相对高。
6. C。实际上对符号谈重定位是不正确的，应当对引用谈重定位，例如全局变量如果初始化为
值且不使用，则不需要重定位。需要留意，如果是同一C语言源文件中定义的函数则一般不
需要重定位。
7. C。除法错误是不可恢复故障，是同步的；I/O中断是异步的，一般会执行完当前指令，再去
处理，返回就不需要再处理了；缺页异常当然需要重新执行遇到问题的访存指令；时间片到
中断属于时钟中断，属于异步异常。
8. 未解之谜，CD。并行一定并发。
9. C。fork返回两次，setjmp可返回多次，longjmp和execve不返回。
10. A。高速缓存是物理寻址的，所以一定不用刷新。用户态和内核态的转换不会改变内存映射，
而上下文切换会改变虚拟内存到物理地址的对应关系，所以TLB在上下文切换时要刷新。
第5页,共8页

<!-- ===== page 6 ===== -->

11. C。VPO为11位，页表均占一页，则VPN都为8位，所以映射满48位地址空间至少需要5
级页表。
12. D。直接模拟就可以。
13. B。最好情况是高速缓存和TLB都命中，不需要访问内存；最坏情况是都不命中，需要访问
四级页表项以及主存中的数据，一共5次。
14. B。参看课程投影片，迭代服务器的第二个客户端会在read阻塞。
15. C。网络字节序规定为大端序，在不同的主机中可能需要转换。
16. A。文件名和参数应该用?分隔。
17. D。2和4都是很明显的，6仍然是陆老师著名的“灵魂出窍”例子，即printf在信号处理
程序中可能导致死锁（加锁后打断，在信号处理程序再调用即死锁，因为需要信号处理程序
返回后才能解锁）。
18. B。保持跨越多个调用的状态的函数不是线程安全的，而C项是隐式可重入函数，如果合理
使用就是线程安全的。
19. C。否则会在对等线程的赋值和主线程的accept之间引入竞争，如果赋值在accept之后
完成，描述符值就错了。
20. D。D是超纲选项，sem型指令会阻塞整个进程，而pthread_mutex型指令只会阻塞相应
线程，后者的效率更高。A、B、C都是容易看出正确的，所以可以用排除法做出。
解答题一
1. 8，送分题。
2. 48周期，即8×6。
3. 50周期。因为每个缓存块可存8个长整数，但起始地址不是64字节对齐，所以会发生2次
miss。
4. 42周期。因为只有前两个addq可以一次执行完，这样能节省8周期的时间。
5. 26周期。指令顺序可重新安排为
.L2:
movq (%rdi), %rbx
movq 8(%rdi), %rdx
addq %rbx, %rax
addq $16, %rdi
addq $2, %rcx
addq %rdx, %rax
第6页,共8页

<!-- ===== page 7 ===== -->

cmpq $8, %rcx
jl .L2
此时每次循环只需要6周期，一共4次循环，即24周期，补上两次miss的惩罚得到26周期。
解答题二
1. 答案如下：
符号 .symtab 有条目？ 符号类型 节 强弱符号
bufp1 有 全局 .data 强
buf 有 外部 UNDEF 弱
bufp0 有 全局 COMMON 弱
temp 无 / / /
count 有 局部 .bss 非强非弱
送分题。注意外部符号要填foo.o中的节，extern的变量严格说不能区分强弱，但是如果
要问则回答“弱”。
2. 未知；bufp1.foo。弱弱选弱，强弱选强。
3. 0x000000be, 0x0000a000, 0x0000900d, 0x0000babe。
1处，ADDR=f28, offset=16, addend=-4，结果为1000-f28-16-4=0x000000be。2处
结合汇编代码知道目标符号是buf的地址移入，所以是0x0000a000（绝对重定位）。6处对应
bufp1，下一条指令地址是知道的，可以不用重定位算法，所以是a050-1043=0x0000900d。
9处对应count，下一条指令地址也是知道的，所以是cb24-1066=0x0000babe。具体填
要注意小端法和立即数格式。
解答题三
1. 3, 4。注意0, 1, 2是标准I/O流占用的。
2. 4, 5。因为fd2已经被关闭，其描述符可复用；另外fd3, fd4虽然指针相同，但是描述
符的号码是不同的。
3. 0, 1, 2, 3。父进程等待子进程结束，所以子进程先输出，另外父子进程的count当然是
独立的。
4. 2019PKUCS。对f1.txt的写有三处，其中20、21行是独立的，得到2019PKU，最后只有
子进程再次写文件，此时fd1的指针在最后，即2019PKUCS。
5. PKUICS2019。鉴于dup产生fd4，而父子进程的文件描述符指向同样的打开文件表条目，
所以对f2.txt的写本质上只有一个指针，因为父进程等待子进程结束，所以先输出PKUICS
再输出2019。
第7页,共8页

<!-- ===== page 8 ===== -->

解答题四 此题我们课上讲过了，原题有几个数据错误，条件也不够。摘取正确题目的分析如下：
1. 4096；6；10。送分题。
2. 0xEAB450D, 0x67F000, 0xAA3000, 0xC3F000。
考虑父进程执行*b的写时的读写问题。在解析*b时，第一步当然是找出一级页表项，因此
从地址0x67F0E8读出0x80AA32C4就是从一级页表中，物理地址0x67F0E8的位置，读
出一级页表项的内容0x80AA32C4。根据题目对PTE结构的描述，我们知道0xAA3是二级
页表页的页号，即0xAA3000是二级页表的起始物理地址。由于一级页表是4KB对齐的，所
以一级页表项的物理地址就是0x67F000。
为什么会写两次？显然，我们知道COW机制在起作用，这段内存首先要被复制。0x80C3F110
这个数字当然是精心设计的，必然暗藏玄机。首先，一次写肯定是写*b，那么另一次写
呢？注意这次写也是父进程，因此和子进程无关。由于COW后内存映射需要修改，结合
后面也有类似于0xC3F...的物理地址，我们可以推定这个实际上就是COW后，b对应
的二级页表项。这样我们马上知道，其二级页表项的物理地址在 0xAA3AD0，而 b 指向
的真实物理地址是 0xC3F50D（页号 0xC3F）。这时我们就可以计算出 b 的值（即虚拟
地址）了。一级页表项的偏移是(0x67F0E8-0x67F000)/4=0x3A，二级页表项的偏移是
(0xAA3AD0-0xAA3000)/4=0x2B4，VPO=0x50D，所以虚拟地址是它们的拼接。注意不是
直接将16进制拼接，虚拟页号为11 1010 10 1011 0100=0xEAB4，所以b=0xEAB450D。
此题页表项中的最低12位是何含义，属于未解之谜。
解答题五
1. bind, connect, accept, writen, readlineb, readlineb, writen。容易读解，
但注意RIO包的API名称不能记错。
2. bind, listp, listenfd。
解答题六
1. 7, 14, 7, 2, 0。这时两个读者都在正常读，因为是读者优先，所以写者在14行阻塞等
待，写锁的值是0。
2. 14, 7, 3, 0。完全同理。
3. 会出现竞争的错误。例如两位读者同时进入，由于readcnt的写不是原子的，可能导致进入
后readcnt=1，当一位读者离开后，写者就错误进入了。
第8页,共8页

---

### chap 2-6 解析 · 选择题 1-10 的答案与题解

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 215–241 行

答案与题解：

1.答案：B。由代码可以知道，循环会在x与y的值首次不相等的时候终止，这当然会在y首次发生舍入附近。由于当y达到值16777216后就不会发生变化，因此之后就只考察x的变化。x在值为16777217时类型转换为float会向偶数舍入至16777216，因此最终x的值为16777218。

2.答案：D。大数吃小数。

3.答案：B。立即数不能作为mov指令的目标，A错误；mov指令无法操作两次内存，C错误；内存寻址比例因子必须是1、2、4、8，D错误。

4.答案：D。在foo()中读取0(%rbp)可以获得foo()开头保存的%rbp，也就是外层函数bar()的栈帧地址，向上偏移8即可获得函数bar()的返回地址。

5.答案：C

解析：A选项，RISC指令集有复杂化的趋势，早期RISC通常指令数量小于100条；B，CISC的指令是不定长的，有些长度比RISC短；C正确；D，CISC一定会将返回地址压入栈中，不可能避免内存引用。

本题考查对两种指令集的理解。

6.答案：D。要想不引起数据冒险，需要改变数据的指令在使用数据的指令进入译码阶段时已经完成写回阶段。因此至少需要插入3个nop指令。

书本P295

7.答案为D。送分。

8.答案：C。浮点数运算没有结合律，大多数编译器不会尝试优化。

9.答案：A。B中DRAM掉电后也会丢失，C中上层存储的内容可以独立于下层，例如加载到寄存器中的值不一定在内存中存在。D缓存利用了空间局部性，会把访问元素在同一块内的元素全部取到缓存里。

10．答案为D，见讲座PPT25页，凭直觉也可以获得答案：布局算法会影响互连线长和走线方式，因此A和B需要考虑，线长会影响延时，所以C 时序也需要考虑。D的逻辑深度在布局时不变。因此正确答案选D

---

### chap 2-6 解析 · 第二题标准答案、评分标准与详解

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 265–318 行

**标准答案(每空2分)：**

**(1) ＜**

**(2) 冷/强制性**

**(3) L3**

**(4) ＞**

**(5) 2·N<sub>0</sub>·S<sub>2</sub>**

**(6) N<sub>0</sub>**

**评分标准:**

1)  **写“小于”的酌情扣1分,回答其他答案（如≤）的不得分.**

2)  **写“冷”“强制性”也正确.写英文也正确.字写错或有拼写错误的,若不影响意思表示不额外扣分.**

3)  **写“L<sub>3</sub>”也正确,写“三级”的酌情扣一分.**

4)  **写“大于”的酌情扣1分.**

5)  **角标书写不规范,如写成“2·N0·S2”,若不影响意思表示不额外扣分.**

6)  **角标书写不规范,如写成“N0”,若不影响意思表示不额外扣分.**

**解析:本题设简单题8分,难题2分.预测平均分7.5分.**

1)  **考察高速缓存替换模拟,属简单题,预测正确率90%.应当注意FIFO和LRU替换机制的区别.**

2)  **考察缓存不命中的类型,属简单题,预测正确率90%.**

3)  **考察读图分析数据的能力,属简单题,预测正确率90%.因为L3高速缓存访存速度最慢,因此平均访问时间最长.**

4)  **考察读图分析数据的能力,属简单题,预测正确率80%.由于N=2N<sub>0</sub>时S<sub>1</sub>发生了L2到L3高速缓存的访存切换,S<sub>2</sub>发生了L1到L2高速缓存的访存切换,故有S<sub>1</sub>＞S<sub>2</sub>.**

5)  **考察对多路组相联高速缓存替换原理的理解,属难题,预测正确率25%.**

图2-2

> **(i) 虽然步长S是从1KiB开始测量的,但我们不妨先考虑步长更小,即S恰好与L1 d-cache缓存块大小相等的情形,如图2-2(a)所示.不失一般性,我们假设所开辟内存空间的起始地址对应到L1 d-cache的组0.当**$`\mathbf{S}\mathbf{\times N}`$**恰好为L1 d-cache的容量时,L1 d-cache恰好缓存了所有需要访问的值.此时,所有的访存都是在L1 d-cache中进行的.现在保持S不变,把N调整为N+1.如图2-2(b)所示.此时L1 d-cache不得不在组0中替换掉一行.根据先进先出的替换原则,被换出的行恰好是第一个被加载进L1 d-cache的行.所以,在第二遍访问所开辟内存空间的起始地址时,会遇到一次缓存不命中.而加载该地址的过程又会替换掉第一遍访问时第二个被加载进组0的行,使第二遍访问它时也是不命中的.以此类推,你发现访问所有对应到组0的地址都是不命中的.频繁的L2 cache访存导致平均访存时间的剧烈上升.  
> (ii) 再考虑**$`\mathbf{S}\mathbf{\times N}`$**保持不变,步长从S变成2S, 4S……时的情形.如图2-3所示,你发现当步长翻倍时,虽然访存次数减少到原来的一半,但是L1 d-cache缓存的有效的值的数量可能也会缩小到原来的一半.这使得平均访存时间可能是不变的.**

图2-3

> **假想S从B逐步增长到了S<sub>2</sub>,而N=2N<sub>0</sub>处平均访存时间发生剧烈的上升,这说明L1 d-cache的容量为2·N<sub>0</sub>·S<sub>2</sub>.**

6)  **考察多路组相联高速缓存相联度的性质,属难题,预测正确率25%.如果高速缓存是直接映射的,那么步长每增加一倍,则访存时间T的转折点横坐标应该变为原来的1/2,但如果高速缓存的相联度不为1,那么转折点横坐标在到达相联度的时候就不会再减小.从图中可以看出,步长S<sub>1</sub>至少是S<sub>2</sub>的4倍（因为S=S<sub>2</sub>,N=4N<sub>0</sub>时,平均访存时间T没有发生剧烈变化）.但S<sub>1</sub>的从T<sub>1</sub>到T<sub>2</sub>的转折点横坐标只是S<sub>2</sub>转折点横坐标的1/2.这说明L1 d-cache的相联度为N<sub>0</sub>.**

> **命题人：李浩雨,陈奕奇**

**2021年12月4日**

---

### chap 7 解析 · 第 1 题答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 15–25 行

**C 错误**

解析：

A 正确。objdump -dj .text \[file\]

B 正确。节头部表：readelf -S \[file\] 程序头部表：readelf -l \[file\]

C 错误。ls只是取得文件的元数据，这与文件内容无关，而linux文件元数据中也不包含对binary或者text编码属性的描述。其他诸如grep和file的工具使用heuristics确定文件的类型。

D 正确。gdb 可以支持单步调试。

---

### chap 7 解析 · 第 2 题答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 65–73 行

**D 正确**

A 错。它位于 .bss 节。

B 错。它位于 .bss 节。

C 错。注意 ld 时文件顺序的交换会改变 a.out 中两个符号的相对偏移。

于是 D 正确。

---

### chap 7 解析 · 第 3 题答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 113–131 行

**B 错误。**

解析：

省略 -ldl 标志报错，表明 ld 默认不会包含 libdl.so (与之对比，libc.so 默认包含)，并且 dlopen 的定义来自于该共享库。

A 正确。.dynsym 含有一个符号表条目。格式形如

0000000000001390 g DF .text 0000000000000085 GLIBC_2.2.5 dlopen

“动态链接符号表”的描述是准确的，也不影响理解。

B 错误，printf 只是一个未初始化的全局变量。它不是内置的 printf 函数。

C 正确。默认程序动态绑定 dlopen 到共享库，它需要自己的 PLT 表和 GOT 表。

D 正确。gcc 按照命令行顺序解析。不管是动态库还是静态库只解析当前已经被引用的符号（这一点容易推断，否则没有必要建立专门的库文件格式了。因此没有补充在题目中交代动态链接符号解析的规则。），所以 -ldl 放在第一个位置没有任何效果。最后会在链接阶段产生 dlopen、dlsym 或者 dlclose 未能解析的错误。

额外说明，libc.so 和 libdl.so 在实际系统上可能会带上版本号，路径名一般也更复杂。这里为了出题，做了合适的简化。

---

### chap 7 解析 · 第 4 题 Part A/B/C 解析与评分标准

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 254–293 行

解析：\[Part A 和 Part C 是基础题，Part B 难度适中。**答案均唯一**\]

**<u>Part A</u>**

| 符号名         | iter     | pnt      | Point  | total       | seed   |
|----------------|----------|----------|--------|-------------|--------|
| 是否在符号表中 | **是**   | **是**   | **否** | **是**      | **否** |
| 定义所在节     | **.bss** | **.bss** |        | **.rodata** |        |

Point和total的部分容易出错。Point作为类型定义，在C中其结构信息已经作为偏移量被汇编代码包含，不需要再显式地输出到.o文件中。total已经被初始化成一个非零值，由于const修饰 \[read-only\]，将放入.rodata中。\[改卷时 .data 和 .rodata 均给分\]

**评分标准：在符号表中的符号，必须正确写出其定义所在节才能得分。**

**<u>Part B</u>**

**pnt;  10;  d1 00 00 00**

由汇编可知 \<main+0x1c\> 处是准备if_inside函数的参数。于是符号是pnt。假设其相对.bss偏移为x，refaddr表示条目的地址，则根据重定位类型都是相对偏移，有

.bss + 0xc - refaddr = .bss + x - %rip

于是

x = 0xc + %rip – refaddr = 0xc + 0x4 = 0x10

因为if_inside – rand_point = 0x74不变，故第四问的结果是

0x69 – (0x11ad – 0x11a1) + 0x74 = 0xd1

**评分标准：第二空允许有若干前导0，其余每空必须完全一致才得分**

**<u>Part C</u>** **D; 用户**  \_start是OS执行这段程序的第一条语句，即入口点，它来自于crt0.o(或者crt1.o，代表 c run-time)模块\[因为这段程序没有自定义入口点函数\]。第二问的信息已经强烈暗示了该函数只能运行在用户态下\[否则直接破坏操作系统对机器的保护和用户间隔离的作用\]。实际上，\_start函数只需准备好 argc、argv和envp，然后准备好 \_\_libc_start_main 的参数。

具体的启动过程如下图所示\[图源：[<u>http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html</u>](http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html)\]

**评分标准：必须完全一致才得分**

<img src="media/media/image1.png" style="width:6.30196in;height:5.39233in" />

本题代码是一个简单的 Monte Carlo 法求积分的算法。

---

### 2022期末-答案 · 全文即 2022 期末参考答案与题解（非完整题干）

> 出处：`原文/期末/2022期末-答案.md` 第 1–87 行

# 2022期末-答案

> 来源：`往年题/期末/2022期末-答案.pdf`　共 3 页

<!-- ===== page 1 ===== -->

ICS22期末答案
By罗兆丰  曹思诺
第一题 填空题
1、RISC CISC
2、10
3、rdi rsi
4、符号解析 重定位
5、GOT PLT
6、① gcc p.o libx.a liby.a  ②gcc p.o libx.a liby.a libx.a
7、①发生异常，从用户态切换到内核态 ②进程A的信号处理程序
8、fork execve
9、MMU TLB
10、0x5d5
11、内存映射
12、36.152.44.95
13、bind
14、对等线程
15、互斥锁
第二题 处理器
(1)   E_icode     d_srcA      d_srcB
(2)   stall           bubble      normal
(3)   D_icode    E_icode     M_icode
(4)   bubble       normal      normal
(5)   3
(6)   前一条指令从内存中加载数据到寄存器 rsp 中，后面紧跟了一条 ret 指令

<!-- ===== page 2 ===== -->

第三题 链接
(1) 注意，最后一列填的是“此符号在定义该符号的模块中的节”。addvec在addvec.o中
是在.text，在main.o中是在UND中
符号  .symtab条目？  符号类型  定义符号的模块  节或伪节名
x  是  全局  main.o  .data
y  否  /  /  /
z  是  全局  main.o  COMMON
n  否  /  /  /
addvec  是  外部  addvec.o  .text
(2) 20 10 60 00
      25 00 00 00
(3) A
.interp节的内容其实就是一个字符串，为动态链接器的路径。把.interp节的所有字节一个
一个地翻译成字符，就得到/lib64/ld-linux-x86-64.so.2。（大家可以特别记一下，’0’的
ascii的16进制是0x30）
(4) 1 3
第四题
1. (1)  A: 0
          B:  1
          C: Sigprocmask
          D: &mask_all
          E: Sigsuspend
          F: 1
(2)  是
否则可能会 1) 父进程向子进程发送多个同类信号，而子进程只接受到1个，子进程死循环。2)
子进程处理SIGUSR1和SIGUSR2的顺序与父进程发信号的顺序不一致。两个情况都会导致出错
2. （这个小题应该是出错了，如果按照原题目的话：）不会输出。在sigusr_handler中，如果G为真，
执行return，那么就不会发送 SIGCONT给父进程，父进程阻塞在Sigsuspend，所以子进程也会阻塞，
导致没有输出。
第五题 虚拟内存管理
1、①代码 ②运行时堆 ③共享库的内存映射区域 ④用户栈
2、触发保护异常，终止进程  触发段错误，终止进程
3、
① 21行 所申请的内存大小不足，应该为malloc(size*sizeof(int));
② 27与31行 不能返回局部变量的地址
③59行 n所指向的地址在push后可能已经被施放
④ 61行 stack.data没有被释放，造成内存泄露

<!-- ===== page 3 ===== -->

 第六题 网络编程
((12))  SIPO地C址K_对S应TR的E主AM机 名
((34))  l每oc次al循ho环st 都50打00开0了  一个新的clientfd而没有关闭，导致文件数量过多，耗尽系统资源
((56))  2A2 小 C明los的e服(cl务ien器tfd在);迭  代处理两个客户端时，bal_cnt只会在某一次与其中一个客户端连
接时等于goal，之后便会设为0，而另一个客户端已经超过0，因此只会发送一次“You
win!”
第七题 并发
第一类:
1、 P(&mutex);           2、 P(&w);              3、 V(&mutex);           4、 P(&mutex);
5、 V(&w);                   6、 V(&mutex);      7、 P(&w);                  8、 V(&w);
第二类:
1、1               2、 P(&r);               3、 if(readcnt==1) P(&w);   4、 V(&r);
5、 if(readcnt==0) V(&w);  6、if(writecnt==1) P(&r);   7、if(writecnt==0) V(&r);

---

### 2024期末-带答案 · 第三题参考答案与解析

> 出处：`原文/期末/2024期末-带答案.md` 第 582–644 行

参考答案
Part A:
1）5 6
评分标准：每空1分
解析：本题考察对dup2()函数，dup()函数以及文件标识符分配的理解
第一空：在dup2前已经分配的文件标识符有fd[0]:3，fd[1]:4，在dup2后
文件fd[1]仍然为4，故新分配的fd[2]为5。
第二空：在dup前已经分配的文件标识符有fd[0]:3，fd[1]:4，在dup后文
件fd[1]变为5，文件标识符4对应的文件仍然没有被关闭，故新分配的fd[2]
为6。
2) HarryVoldemortHermioneRon
评分标准：本空3分，完全一致才得满分，可以看出的抄写错误可酌情给2分
解析：本体考察对文件写的理解，特别是和fork函数结合。
不论是dup，dup2还是fork，都不会创建新的文件，所以本题中所有的写都是
针对同一个文件的写，因此顺序写入字符串即为答案。
Part B:
1）问题：子进程信号注册函数位置存在问题。父进程在 kill后，子进程的信号
18

<!-- ===== page 19 ===== -->

处理函数可能未完全注册，导致信号丢失。解决方案：将 signal(SIGUSR1,
handler1); signal(SIGUSR2, handler2); 两行提至fork前。
评分标准：原因1分，解决方案1分。意思对即可。
2）① ⑦ ② ④ ② ⑥
评分标准：两个一句，每句1分，全对得1分，否则不得分。
Part C:
5）3，4，5，6，7，8，9      6，7，8，9
评分标准：每空1分，完全一致才得分
解析：本题考察对于父子进程局部变量关系，以及并发的理解。
观察循环体，可以发现对于最终形成的每一个进程，都经历了十次选择，也即：
for i in 0..10, 是否将i加到buffer的最后
并且每一个进程至少有一个选择是不同的，这导致最终形成的每一个进程的内容都
不一样，且共形成了2^10个进程。（如果不能理解这个过程，想想你在AI课上学
的决策树，你可以完全类似地画一棵进程树出来）
下面先考虑 content[9]可能出现的内容，已知必须写入一个长度至少为 10 的
buffer 才能让content[9]出现字符，而所有进程的buffer 中，只有总父亲
进程的buffer=”0123456789”满足长度要求，故content[9]只能为9。
接下来考虑content[j], j in 0..10，我们需要写入一个长度至少为j + 1
的buffer才能让content[j]的字符发生改变，而第buffer[j]之前的j个
数字又必须比buffer[j]的数字小，这就意味着buffer[j]至少为j。在10次
选择中，我们至多选择9 - j次不将数字i加入buffer最后，我们容易发现全
选靠前的数字不加入可以得到最大的content[j]，易得最大的content[j]为
9，同样的方法可以发现j..10均能取到。
这样本题的答案就被解出来了。
6）10!
评分标准：本空3分，答案为10的阶乘，写成3628800或其他等价表示也能得
分。
解析：根据上一问的结果，我们可以推出content[i]有10-i种取法，那么根据
乘法原理，content最多有10!种可能性。
下面证明确实可以取到10!种可能性，对于任意的一种可能性：
x_0 x_1 x_2 …… x_9
我们可以这样构造进程写的执行序列来得到它：
19

<!-- ===== page 20 ===== -->

1.遍历i，i从9取到0，每次递减1
2.对于每一个i，寻找一个进程，这个进程的buffer长度恰好为i + 1，且最
后一位数字为x_i。由上一问的论证，这样的进程恒存在。
3.遍历结束，我们得到了十个不同的进程，我们先以任意顺序完成这十个进程之外
的进程的写，然后再依次执行这十个进程的写，这样我们就构造出了我们想要的序
列。

---

### 2024期末-带答案 · 第四题答案与解析

> 出处：`原文/期末/2024期末-带答案.md` 第 731–785 行

答案：
Part I.
1）64, 1  2）0x6A1 或 0x06A1  3）8
4）B，C   5）0x00E77190, 0x0D000980
Part II.
1）C，0x11  2）C  3）A，1/16
4）A  5）12，0x10（或16或其它等价表述），12（如果代码两空正确，则可
以填写16）
合理答案或等价表述均可。
**Part I.**
1）64, 1
解析：由虚拟地址空间大小 8KB 可知虚拟地址实际使用位数为 13 位，页面大小
128B知VPO为7位，故VPN为6位，共2^6=64个页表项，每个页表项2字节，
共128字节，即1个物理页。
AI解释：虚拟地址空间大小是8KB，页大小为128B。
24

<!-- ===== page 25 ===== -->

8KB / 128B = 64个页表项。每个页表项占2B，因此存储完整的页表需要：64
个页表项 × 2B = 128B = 1页。
2）0x6A1 或 0x06A1
3）8
解析：第一次访存Set=3, Tag=4, TLB命中；第二次访存Set=0, Tag=5,
valid 位为 0，TLB 未命中并替换valid 位为 0 的条目；第三次访存Set=0,
Tag=7, TLB未命中，根据LRU，替换Tag=2的条目；第四次访存Set=0, Tag=2，
对应条目刚刚被替换出TLB，TLB未命中，根据LRU，替换Tag=5的条目；第五
次访问 Set=0, Tag=7, TLB 命中。因此共有 3 次 TLB 未命中，总访存次数
5+3=8次。
4）B，C
解析：对第一条指令进行翻译，发现其TLB未命中，同时对应页表项valid位为
0，触发缺页异常。第二条指令所表示的虚拟地址超出8了KB的范围限制，可以类
比为在64位系统中用户态访问超过2^48 的地址空间，会触发段错误。
AI解释：0x00D0 的 VPN=0，页表项有效与否决定是否会缺页异常0x。2226 属
于超出虚拟地址空间的范围，发生段错误。
5）0x00E77190, 0x0D000980
**Part II.**
1）C，0x11
解析：由于对齐实际分配块大小为16字节，故A处字节内容为0x10 | 0x1 =
0x11。
2）C
AI 解释：推迟合并意味着空闲块不会立即合并，只有在下一次分配或释放时，才
会检查是否可以合并相邻的空闲块。这种情况下，合并过程可能涉及遍历多个空闲
块，因此其时间复杂度至少是O(n)。
3）A，1/16
解析：当malloc(1)时空间利用率最低，实际分配16字节，利用率1/16。
AI 解释：立即合并意味着每次释放内存块时，分配器都会立即检查该块是否可以
与相邻的空闲块合并。由于每个内存块都有脚部，因此合并操作只需要O(1)时间，
不需要遍历整个堆。
4）A
解析：由于对其原因导致分配块至少为8字节，故一定有空间放置脚部。
5）12，0x10（或16或其它等价表述），12
解析：为了使合并出错，需要在合适位置设置与脚部相同的头部，由脚部设置可知
该块“大小”为16，故需要在偏移量12~15字节处设置头部，其余字节为零，只
需在12字节设置即可。

---

### 2024期末-带答案 · 第五题答案

> 出处：`原文/期末/2024期末-带答案.md` 第 1107–1114 行

答案：
4，5，3，2，3
A
①，①，⑦，⑧，③，⑨
2（flag, judger_pid）
不会；不是；是；不会
D
A;C

---

### 期末往年题勘误、详解 by Arthals · 全文即 2015/2016/2018-2022 期末勘误与详解（非完整题干）

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 1–249 行

# 期末往年题勘误、详解

<center>
  by <a href="https://arthals.ink/">Arthals</a>
</center>

整理自我的树洞 5833467 与 piazza。感谢树洞同学和 zzs 助教的帮助。

## 2015

### 第一题

第 17 问，废题，现代 Web 中 GET/POST/PUT 等都可以用于获得动态内容。

### 第二题

第（8）空，应该填写十进制 40，而不是 0x40。

### 第三题

第 4 问，应该在 AB 之间也插入一个寄存器。

### 第四题

如果你认为 a[0] 应当是 \*(0xdeadbeefcafebffe)，那么你的理解有误。

你可以使用 union 结构体来验证这个重复定义的全局变量。

### 第六题

第一问题出错了，TLBI 完全没考虑，你当 TLBI 不存在去寻址；第二问解答说的挺好的，第三问解答说的也还行，主要是你要知道一个 PTE 是 4B，然后 0x27\*4 得到 0x9C，最顶上那个 C 是因为这是虚存；最后一小问和 17 年虚存一样, 修改了页表项需要让上一级缓存 (也就是 TLB) 失效，否则下次访问命中 TLB 会从中取出已经过期的值

所谓大页，就是你可以理解为我不需要更低一级的页表了，我保证我的上一级页表每一项都可以映射到连续的大页上。或者你可以理解为低一级页表中的所有项目都是连续的，那么这个低一级页表当然就不再需要了。

### 第八题

答案有误，两个 mutex 信号量的初值应当都为 1，且 PB 应当如下：

```cpp
PB() {
    while(1) {
        P(&full1); // full1--
        P(&mutex1);
        // 从 Buff1 中取出一个记录
      	// V 操作可以挪到最后，因为此时持有 mutex1 保证不会有 PA 来竞争
        V(&mutex1);
      	V(&empty1) // empty1++
        // ---- ///
        P(&empty2); // empty2--
        P(&mutex2);
        // 将记录放入 Buff2
        // 这里顺序无所谓，V 操作不阻塞
        V(&mutex2);
        V(&full2); // full2++
    }
}
```

可以看做是两个队列问题，因为题目说明了只有 PA PB PC 三个线程，不存在 PB 和 PB 之间的竞争。

## 2016

### 第一题

第 2 问，隐藏位就是规格化数里大伙都有的 1，这里的意思是你要以这个 1 为基准，上下加减 M 表示数，再乘以 E 阶码位。考虑正常的话，尾数位的映射范围 1~2，现在就是 1/2~2，相当于很多数的阶码位、尾数位其实可以有了两种选择（即两种表示方式），不像 IEEE 那样充分利用了。比如，D 的指数位是 7，-bias 之后是 4，所以指数就是 16。然后补码那块，你看现在是 10101，那么有-x=~x+1，你假装他是一个整数，取非搞出来 01010，加一搞出来 01011，这个是 11，也就是 -x，那么 x 就是 -11，你再考虑这里的末位代表 2^-4（注意有一位符号位，即第一位 1 不算成 1/2，第二位 1 才是），所以尾数就是 1 - 11\*(2^-4)，你再拿这个乘以 16，应该就对了，我觉得这里挺扯淡的倒是（

第 10 问，A 是不会有信号的。在网络那一章中，只有链接异常断开会导致 SIGPIPE。A 中描述的“新连接到达监听端口”不会导致操作系统发送信号给进程，而是通过网络编程接口（如 POSIX 的 socket API）提醒应用程序有新的连接。这通常是通过 I/O 多路复用（如 select、poll、epoll 等系统调用）来实现的，其中应用程序会监控一个或多个网络端口的状态，当有新连接到来时，操作系统会唤醒正在等待的程序，而不是发送信号。

第 13 问，这里的所有符号都对应 bit 数。

第 20 问，关键点在于，printf 的时候因为这个 j 没有 volatile 定义，所以你考虑汇编的时候，这里肯定就是一个寄存器了，上面读完是啥就是啥，而寄存器是个线程上下文里的东西，所以你 V(&s) 之后到 printf 之间哪怕被切走，切回来的时候也是会恢复的，所以不会因为在别的线程里加了 j，我这里 printf 就会知道哦原来这个 j 变了，而是依旧恢复成切走的时候的 j（寄存器版本）。所以这题前三个都是可能的，只有 D，因为线程锁保证了这个 j 一定会加到 3，而对应的线程的打印一定能打出 3，所以 D 是错的。

### 第六题

第 2 问，权限解读如下：

-   r = read
-   w = write
-   x = execute
-   s = shared
-   p = private (copy on write)

第 3.1 问，D 选项，COW 写时复制和页表无关。

## 2018

### 第一题

第 3 问，对于 C 选项，直接考虑冷不命中次数就知道是对的；对于 B 选项，如果数组刚好比 cache 总大小大一点点，LRU 会不断产生 miss 从而不如其他算法。

第 6 问，执行过程中没有发生从未打开的描述符进行复制，所以错。实际测试：可以向一个未打开的描述符进行复制、从一个未打开的描述符复制（即未打开的描述符是 dup2 的第一个参数）都是合法的（但是后者一旦开始写就会报错）。

第 7 问，D 选项没说是 LIFO 还是按照地址排序，所以不确定。

第 11 问，D 选项。题目里的意思应该是，用 socket 创建的 fd 在连接后是可以用 unix 标准 io 读写的。

第 13 问，A 选项，可能使用了全局变量。

### 第二题

明显答案错了，少了 CD,FG 两个插入，这种题的普遍做法是，找到一条边最少的，逐次枚举，一个技巧是任何一条通路上的寄存器数量是相同的。

### 第四题

为什么 PartB 产生了 +-+--+..这样的结果？

父子进程是分叉后单独打开的文件，由于并发，所以父进程给子进程发信号的时候子进程可能还没把 fd1 改掉，所以打印第一个+，然后：

```text
-
++
 --
  +++
   ----
     ++++
...
=======
+-+--+---
```

### 第五题

第 2 问。

此问详细解答如下：

MMU 的 TLB 没有命中，找到一级页表项 0xC3F50D，由于一级页表 4KB 对齐，所以这个地址的低 12 位 0x50D 是一级页表项索引偏移，所以一级页表基址是 0x67F000；读出来 0x80AA32C4，8 代表最高位为 1，也就是有效，说明二级页表已经缓存在主存内，而读出来的 0x2C4 是一级页表项中存的对于二级页表的控制信息。所以二级页表基址为 0xAA3000，这里也可以由二级页表是 1024 个 PTE，说明二级页表项地址的最低至少 10 位为权限位，上取整到 4 的倍数 12，得到最低的 0x2C4 为控制信息。然后后两次写入，第一次为真正的写入物理内存，第二次为修改二级页表项目。所以根据物理内存地址 0xC3F50D，由于页大小是 4KB，所以低 12 位为 VPO/PPO，所以物理页基址为 0xC3F000；然后因为修改了物理页面，所以要修改对应的二级页表条目，标识 A 位引用与 D 位修改，所以写入地址 0xAA3AD0 的 0xAA3000 是二级页表基址，0xAD0 是二级页表项索引偏移，之所以写的还是 0x80C3F110，纯属巧合，说明运气很好，最高的 8 是有效位，0xC3F 是物理页表基址，0x110 是权限控制信息。然后根据如上过程，b 是指针，它的值其实就是这个过程中的虚拟地址，VPO 是 0x50D，VPN2 是二级页表偏移索引 0xAD0/4=0x2B4，注意只要低 10 位 1010110100，VPN1 是一级页表偏移索引 0x0E8/4 = 0x3A，注意这里每个 PTE 仍是 4B，这和页表项目数量无关，只和地址空间位数有关，也说明一级页表没有满其实，仍然注意只要低 6 位，111010，然后拼起来得到 1110101010110100，即 0xEAB4，这就是 VPN（总的），所以虚拟地址是 VPN+VPO = 0xEAB4AD0。

完成写之后该项 TLB 内容为？

```text
0x00ba4227 & (0xFFFFFFFF - ((1 << 12) - 1)) | 0x27 | (1 << 6) == 0x00ba4067
              ^--低12位取0                     ^       ^
                                              权限rw   |
                                                      Dirty bit
```

第 3 问，pid 和 cnt 在一个页里，你考虑第一次分叉，分叉时，子进程写时复制改 1 页；二次分叉，两个新的子进程写时复制都要改 1 页...所以是 1+2+4+8=15 次

### 第七题

第 4 问，信号量也可以等于 2，本质上是大于等于 2 的时候这个锁就失效了，相当于只有剩下的一个互斥锁（

### 第八题

1：显然这是是代码段之上的数据段，必然可读可写，但是因为 COW 机制，所以是 private 的，这样以后才会触发保护故障，所以 rw-p

2：动态链接器本身也是共享文件，所以是 ld.so

3：这里是打开的文件头，题目说 MAP_SHARED 就是暗示的这个，你看他的权限位是 rw-s

4：显然是栈

5：单进程的实际可用虚拟地址空间为 6500KB，所以多进程的时候就是 10\*6MB=60MB，上取整到 A

6：单进程实际使用虚拟地址空间 RSS 为 1600KB，不同进程因为 cow 写时复制机制的存在，所以代码段和共享库基本是共享的，只有自己的堆和栈是私有的页，而 heap 和 stack 的 size 都为 132KB，所以十个进程就是差不多 260KB\*10= 2MB，再加上单进程固有的 RSS 1600KB≈2MB，所以整体 RSS 差不多就是 4MB，考虑到铁铁不可能选择 2MB 版本的，肯定是上取整到 6MB，选 C

7：多进程共享空间基本上就是 6 中说的 6MB，除给每个进程之后就是 600KB，所以选 D

8：多线程的时候，虽然共用虚拟地址空间，但是对于每个线程来说，他自己的又映射了一层虚拟内存，所以 VSS 总可用等价于多进程的时候，也就是 5 中的情况（这个不太确定）

9：RSS 显然因为多线程共用虚拟地址空间，基本等价于单个进程的 RSS，也就是 1600KB。所以选择 D

## 2019

### 第一题

第 14 问，为什么阻塞在 `read` 而不是 `connect`？请注意，`connect` 并不是在 `accept` 之后才返回的。

连接成功意味着客户端发起的连接请求已经被服务端接受，此时 TCP 三次握手过程已经完成。在编程层面，客户端的 connect 函数会在连接成功时返回 0。所以只要服务端使用了 `listen`、当前连接数没超过 `listen` 的 backlog、网络畅通，那么客户端的 connect 就一定会返回 0。

服务端的 accept 函数用于**从监听队列中接受一个新的连接请求**。一旦客户端的 connect 请求到达服务器，服务器的操作系统会处理这个连接请求，完成三次握手过程，并将这个连接放入等待服务端 accept 的队列中。当服务器调用 accept 函数时，它会返回一个新的套接字描述符，这个描述符代表了与特定客户端的连接。

因此，从客户端的角度看，connect 返回 0 就表示连接成功。而服务端需要调用 accept 来正式接受这个连接，然后才能开始通过这个新的套接字与客户端进行通信。

### 第五题

第（1）问，题目有错，虚拟地址大小为 28 位。

### 第七题

为什么读写问题要一直 while？原因是要通过两个 while 每次循环之间的竞争来模拟读者一直读写者一直写。

## 2020

### 第一题

第 7 问，关于 D 选项，可能有些同学读书认为此时 ABS 节应当也不存在，但是书上说的是静态链接后的情况。你可以认为，在默认的编译选项下得到的可执行文件是会有这些伪节的。或者参考我的理解，我觉得书上说的是完全连接的可执行文件，你搞出来的是部分链接的可执行文件，其中还有一些共享库的条目？

第 18 问，感觉 AD 都有问题。

第 25 问，选项除 D 外均会死锁。因为线程 1 和线程 3 的 a，d 锁的获得顺序刚好相反。

### 第三题

④ 处怀疑是答案给错了，根据汇编看似乎应该是 count 才对，也就是 0x00dedd38（count 的地址，初始化置零）

### 第六题

第 1 问：首先你需要知道为什么会死锁？要是所有人都同时获得了 UP 的锁，那么 DOWN 的就一个都获取不到，就寄了。

然后如何保证不会发生这种情况？就需要规定获得锁的顺序，必须先获得大的，再获得小的（你可以自己思考一下正确性的原因）。所以答案是 1221 或者 2112.

第 2 问：实际上是用 value 存储你模拟的 sem 的值，用 mutex 保护 value，用 zero 实现等待。如果 value<0 了那么 P 操作就必须等待，所以 C 应该是<.

对于 F，如果 value 本来就<0，那么就需要唤醒一个 P 阻塞的线程。自增后<条件变为<=，故也填写<=.

具体的条件判断可以使用边界值判断法，就是考虑 value 为-1,0,1 三种特殊值就可以了。

## 2021

### 第三题

Part A，seed。老师想考的是非全局的局部静态变量（函数内的 static）会被重命名，加一个.x 的后缀，所以是否，后来讨论了之后还是认为有。

Part B，`<main+0x1f>` 处的偏移量计算：

一个简单的计算是，设 `pnt` 的地址是 `addr(pnt)`，那么我们要求的相当于是 `addr(pnt) - addr(.bss)`，你需要深入理解这个相对重定位的含义，为什么要有一个 addent？你考虑读完 1c 这条指令（即其进入 D 译码阶段时），PC 已经到下一条指令（23）处了，所以要加一个 addent = -4 字节来抵消这个偏移（也即 23 - 1f），使得读入“指针”的位置是正确的。

于是，有：addr(.bss) + 0xc = addr(pnt) - 4，所以偏移量是 0xc + 4 = 0x10。

Part C，既然这个函数是可以被换成自己指定的代码段的，那么肯定运行在用户态下。否则就构成越权了。

### 第六题

2.b，如果是 if，有：

```c
P(&mutex);
if (items == BUF_SIZE) {
    num_waiting_producer++;
    V(&mutex);
    P(&sem_waiting_producer);
    P(&mutex);
}
```

本质是第 30 行 P(&sem_waiting_producer); 和 31 行 P(&mutex); 之间可能被其他进程捷足先登。

而不是你出了 while 循环之后的问题，出了 while 循环时你已经持有锁 mutex 了。

## 2022

### 第三题

第 3 问，interp（最前面的一节）放路径，也就是 ascii 码，解读出来就是动态链接器的路径。

第 4 问，lt 其实给出了 plt0 了，就是 printf 前面那个，那个 push 和 jmp 明显是 plt0，所以是 1

---

### 2024期中-试题及答案勘误 · 2024期中试题及答案勘误

> 出处：`原文/期中/2024期中-试题及答案勘误.md` 第 7–43 行

2024 ICS期中试卷问题汇总
1. 选择题第2题：
void*类型的指针运算为未定义行为。
建议处理方式：所有选项均赋满分2分。
2. 选择题第5题B选项：
“栈帧”错打为“帧栈”
建议处理方式：不作处理。
3. 选择题第7题A选项：
准确来说，返回的结构体的地址在函数调用时存在%rdi中，在函数返回时存在%rax中，但
是A选项并没有说明时机，容易引起歧义。
建议处理方式：AC选项均赋满分2分。
4. 选择题第9题：
“转发次数”的定义并不明确，第九行两次用到了%rbx，可以理解为“两次转发”，这样总转发
次数为4次。
建议处理方式：BC选项均赋满分2分。
5. 大题第二题第2小题第（1）问第一空：
部分同学答案为-0.0000000000000001，也为该数的“二进制表示”。写出该答案证明同学
已理解IEEE表示方式，符合考察要素。

<!-- ===== page 2 ===== -->

建议处理方式：答案为-0.0000000000000001亦赋满分2分。
6. 大题第四题第（7）空：
图中并未示出d_rvalA名称，将其直接用于考察不妥。
建议处理方式：所有正确表明意图为“寄存器rA中的值”的答案均赋满分1分.
7. 大题第五题第4小问：
题目并没有说明题中的空缺哪里应该填入答案，哪里应该留空，也没有说明留空的具体含义。
可能会被误解为cache中没有被操作的地方就留空不写。
建议处理方式：如果同学答案除了valid=0的行留空之外全对，赋满分4分。否则正常按行
赋分，不予加分。
最终评分方式修改：
选择第2题 不做评分标准修改
选择题第7题AC均对
选择题第9题BC均算对
第二大题第2小题第（1）问第一空-0.0000000000000001赋满分2分
第四大题13问M算正确
第五大题判分标准不进行修改

---
