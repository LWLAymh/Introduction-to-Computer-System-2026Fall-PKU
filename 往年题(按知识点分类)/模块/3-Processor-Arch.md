# 处理器体系结构

> **英文模块名**：`Processor Arch`  

> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，
> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。

## 一、清单

共 132 道题，来自 32 份材料。

| 年份 | 试卷 | 类别 | 题号 | 考什么 |
|---|---|---|---|---|
| 2012 | 2012期中-带答案 | 期中 | Problem C 2 d) | IA32 与 x86-64 对比：32 位寄存器少、局部变量需落栈 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 9 | RISC 与 CISC 指令集对比 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 10 | 流水线吞吐率与数据冒险 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 11-13 | Y86 PIPE 数据冒险/转发信号判断 |
| 2013 | 2013期中-带答案 | 期中 | 第五题 1) | 流水线吞吐率计算 |
| 2013 | 2013期中-带答案 | 期中 | 第五题 2) | SEQ 单周期处理器吞吐率 |
| 2013 | 2013期中-带答案 | 期中 | 第五题 3) | Y86 程序段的数据相关与冒险 |
| 2013 | 2013期中-带答案 | 期中 | 第五题 4) | 转发通路解决方案（含答案与流水线结构图） |
| 2013 | 2013期中-带答案 | 期中 | 第六题 | Y86 SEQ 各阶段操作（cmovXX/call/decl） |
| 2014 | 2014期中-带答案 | 期中 | 第一题 9 | 组合电路逻辑门转 HCL 表达式 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 10 | 三级流水线执行 10 条指令所需时间 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 11 | CISC 与 RISC 指令集特点对比 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 12 | 流水线数据冒险、吞吐率与流水级划分 |
| 2014 | 2014期中-带答案 | 期中 | 第六题 | Y86 新增 caddXX 指令在 SEQ 各阶段的操作 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 11 | RISC/CISC 指令系统设计 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 12 | 组合逻辑+寄存器的最短延时与吞吐 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 13 | 流水线冒险与 data forwarding |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 14 | Y86 SEQ 的 PC 更新 HCL 数据来源 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第四题 1 | 新增 NewJE 指令在 SEQ 各阶段的操作 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第四题 2 | PIPE 中跳转条件不满足时错误执行条数 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第四题 3 | NewJE 预测错误的判断条件与控制信号 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第四题 4 | load-use 与误预测组合冒险的控制信号 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第四题 5 | data miss 时的各级流水线控制信号 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 8 | CISC 与 RISC 指令系统对比 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 9 | 流水线技术描述辨析 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 10 | 组合电路 HCL 表达式 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 11 | 转移预测错误的判断与恢复信号 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 12 | 三级流水线执行时间计算 |
| 2016 | 2016期中-带答案 | 期中 | 第四题 | Y86 新增条件返回指令 cretXX 的 SEQ/PIPE 设计 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 9 | RISC 与 CISC 特点辨析 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 10 | Y86 SEQ 的 mem_addr HCL 描述 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 11 | 流水线与数据冒险描述辨析 |
| 2017 | 2017期中-带答案 | 期中 | 第四题 | Y86 条件内存传送指令 crmmovqXX 的 SEQ/PIPE 实现 |
| 2018 | 2018期中-带答案 | 期中 | 第一题 9 | 编译技术/取指速度对 ISA 选择的影响 |
| 2018 | 2018期中-带答案 | 期中 | 第一题 10 | Y86 popl 的 SEQ 实现 |
| 2018 | 2018期中-带答案 | 期中 | 第四题 | Y86-32 流水线前递 HCL 与 load-use 冒险处理 |
| 2018 | 2018期中-带答案 | 期中 | 第六题 | PIPE 上循环代码的周期数（冒险/预测/缺失） |
| 2019 | 2019期中-带答案 | 期中 | 第一题 10 | RISC/CISC 指令集设计特征辨识 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 11 | 插入流水线寄存器后的最大吞吐率 |
| 2019 | 2019期中-带答案 | 期中 | 第四题 1 | irOpq 指令在 SEQ 各阶段的实现 |
| 2019 | 2019期中-带答案 | 期中 | 第四题 2(1) | 数据前递与 E_valA 的 HCL 描述 |
| 2019 | 2019期中-带答案 | 期中 | 第四题 2(2) | load/use 冒险检测的 HCL 表达 |
| 2019 | 2019期中-带答案 | 期中 | 第四题 2(3) | PIPE 上片段周期数与新指令优化收益 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 6 | PIPE 中 mem_addr 的 HCL 描述 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 7 | SEQ/PIPE 预测策略、CPI 与流水线划分 |
| 2020 | 2020期中-带答案 | 期中 | 第四题 1 | 新指令在 SEQ 各阶段的操作补全 |
| 2020 | 2020期中-带答案 | 期中 | 第四题 2 | PIPE 新增 enter 指令的硬件改造选项 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 8 | 组合逻辑延迟、流水线级数与吞吐率 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 9 | PIPE 上代码片段的数据转发次数 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 10 | SEQ 现有信号通路能否实现新指令 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 15 | Y86-64 PIPE 上片段总周期数与结果 |
| 2021 | 2021期中-带答案 | 期中 | 第四题 1 | 间接跳转指令 jxx *rB 的 SEQ 阶段补全 |
| 2021 | 2021期中-带答案 | 期中 | 第四题 2 | PIPE 预测下一条 PC 的旁路与 HCL 修改 |
| 2021 | 2021期中-带答案 | 期中 | 第四题 3 | 预测错误触发条件与流水线控制逻辑 |
| 2021 | 2021期中-带答案 | 期中 | 第四题 4 | 改造后 PIPE 上 foo 的周期数（分支/load-use） |
| 2022 | 2022期中-带答案 | 期中 | 第一题 11 | RISC/CISC的ISA特征描述 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 12 | 组合逻辑电路对应的HCL表达式 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 13 | 三级流水线吞吐量计算 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 14 | SEQ新增条件传送立即数指令（行218附图归属存疑） |
| 2022 | 2022期中-带答案 | 期中 | 第四题 | Y86-64新增cpopqXX条件POP指令（SEQ/PIPE与冒险） |
| 2023 | 2023期中-带答案 | 期中 | 第一题 11 | 用MUX4实现HCL表达式 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 16 | SEQ中newPC的HCL（ret阶段取valM） |
| 2023 | 2023期中-带答案 | 期中 | 第四题 | Y86-64新增Bxx/JxxR指令与PIPE前递、冒险控制 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 9 | PIPE中数据前递次数统计 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 10 | RISC与CISC的对比 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 11 | SEQ中mem_addr/mem_data的HCL补全 |
| 2024 | 2024期中-带答案 | 期中 | 第四题 | PIPE前递HCL补全、Load/Use冒险与新数据通路 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 4 | Y86 SEQ 中 PC 更新的 HCL 数据来源 |
| 2013 | 2013期末-带答案 | 期末 | 第三题 | 组合逻辑单元流水化与吞吐率计算 |
| 2014 | 2014期末-带答案 | 期末 | 第三题 | 组合逻辑流水化级数与吞吐率计算 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第三题 | 含 F 模块的组合逻辑流水化与吞吐率 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 4 | 四级流水线操作周期由最长段决定 |
| 2016 | 2016期末-带答案 | 期末 | 第三题 | 组合逻辑单元插入寄存器与吞吐率 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 4 | 由执行步骤识别 Y86 指令 |
| 2017 | 2017期末-无答案 | 期末 | 第三题 | 两级/三级流水线插入寄存器与最大吞吐率 |
| 2018 | 2018期末-带答案 | 期末 | 第二题 | 组合逻辑流水化插寄存器与吞吐率计算 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 5 | RISC 寄存器更多 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 解答题一 1 | 延迟 10ns |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 解答题一 2 | 数据冒险与分支预测惩罚周期数 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 2 | 数据冒险的定义 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 4 | CISC 变长指令与 ARM/RISC |
| 2019 | 2019期末-无答案 | 期末 | 第一题 2 | PIPE 流水线数据冒险的判定 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 4 | RISC 与 CISC 指令集特点 |
| 2019 | 2019期末-无答案 | 期末 | 第二题 (2) | SEQ 处理器理想情况下的周期数 |
| 2019 | 2019期末-无答案 | 期末 | 第二题 (4) | 增加加法器后双发射的周期数 |
| 2019 | 2019期末-无答案 | 期末 | 第二题 (5) | 循环展开并重排指令后的最短周期数（兼 Compilation） |
| 2020 | 2020期末-无答案 | 期末 | 第一题 5 | CISC 与 RISC 指令集特性 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 6 | Y86 rmovl 的 SEQ 数据通路 |
| 2020 | 2020期末-无答案 | 期末 | 第二题 1) | 五级流水线时钟周期与寄存器开销 |
| 2020 | 2020期末-无答案 | 期末 | 第二题 2) | Y86-64 代码在前递与分支预测下的周期数 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 3 | RISC 与 CISC 指令集特点 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 4 | PIPE 中无前递时的数据冒险判定 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 5 | 流水线延迟、吞吐率与插入寄存器 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 8 | 芯片布局算法的优化目标（存疑，属 VLSI/CAD，兼时序） |
| 2021 | chap 2-6 解析 | 期末 | 第一题 5 | RISC 与 CISC 指令集特征比较 |
| 2021 | chap 2-6 解析 | 期末 | 第一题 6 | Y86-64 PIPE 数据冒险与所需 nop 指令条数 |
| 2021 | chap 2-6 解析 | 期末 | 第一题 7 | 流水线延迟/吞吐率计算与插入流水线寄存器的影响 |
| 2021 | chap 2-6 解析 | 期末 | 第一题 10 | 芯片布局算法的优化目标（存疑：偏硬件/EDA 设计） |
| 2022 | 2022期末-无答案 | 期末 | 第二题 (1) | Y86 流水线 load-use 冒险的 HCL 检测表达式 |
| 2022 | 2022期末-无答案 | 期末 | 第二题 (2) | load-use 冒险时各流水级 stall/bubble 设置 |
| 2022 | 2022期末-无答案 | 期末 | 第二题 (3) | ret 处理时机 HCL 表达式（含流水线信号连接图） |
| 2022 | 2022期末-无答案 | 期末 | 第二题 (4) | ret 处理时各流水级 stall/bubble 设置 |
| 2022 | 2022期末-无答案 | 期末 | 第二题 (5) | ret 指令插入的 bubble 周期数 |
| 2022 | 2022期末-无答案 | 期末 | 第二题 (6) | load-use 与 ret 需同时处理的场景分析 |
| 2022 | 2022期末-答案 | 期末 | 第一题 1 | RISC/CISC 指令集设计 |
| 2022 | 2022期末-答案 | 期末 | 第一题 2 | 存疑：仅给出答案 10，考点不明 |
| 2022 | 2022期末-答案 | 期末 | 第二题 | 流水线 stall/bubble 与流水线寄存器 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 2 | RISC/CISC、流水线转发优先级与异常 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 3 | 组合逻辑延迟与流水线寄存器插位/吞吐率 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 14 | 摩尔定律/登纳德缩放与多核趋势（存疑） |
| 2024 | 2024期末-带答案 | 期末 | 第二题 | Y86-64 SEQ/PIPE 新增 cdeclXX 与周期数 |
| 2025 | 2025期末-带答案 | 期末 | 一 8 | Y86-64 指令编码 regids 与 valC 字段 |
| 2025 | 2025期末-带答案 | 期末 | 一 9 | ret 在 PIPE 中的控制冒险与 bubble |
| 2025 | 2025期末-无答案 | 期末 | 一 8 | Y86-64 指令编码 regids 与 valC 字段 |
| 2025 | 2025期末-无答案 | 期末 | 一 9 | ret 在 PIPE 中的控制冒险与 bubble |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2015 第三题 第4问 | AB 之间也需插入流水线寄存器 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2018 第二题 | 流水线寄存器插入 CD,FG |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第9讲 1 | 不定项：哪些描述属于 ISA 规定的内容 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第9讲 2 | Y86-64 mrmovq 为何不写成 D(rA),rB（指令编码设计） |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第9讲 3 | 由 HCL 布尔表达式补全组合逻辑电路图 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第9讲 4 | 根据电路图补全时序图中 Out 信号值 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第10讲 5 | Y86-64 popq 指令编码格式与操作步骤补全 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第10讲 6 | SEQ 中 aluA 信号生成逻辑的 HCL 补全 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第11讲 7 | 三级流水线的延迟与吞吐（细分流水级计算） |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第11讲 8 | PIPE 上 addq 的数据冒险检测与数据前递 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第11讲 9 | 写 Load-use 相关代码并说明前递能否解决 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第11讲 10 | 写 Load-use 与 ret 组合的 Y86-64 代码 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 26 | SEQ 中新增 iopq 指令需改动的 HCL 位置 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 27 | SEQ 到 pipe_std 五级流水线演进与冒险 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 28 | ncopy.ys 两段循环代码的流水线性能对比 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 29 | 评分 c=cpe+2*ac 下代码与架构的优化权衡 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 30 | pipe_std 关键路径/传播顺序与降低 ac 的优化 |

## 二、题目原文

### 2012期中-带答案 · Problem C 2 d)

> 出处：`原文/期中/2012期中-带答案.md` 第 409–414 行　·　模块判定：Processor Arch
> 考什么：IA32 与 x86-64 对比：32 位寄存器少、局部变量需落栈

   d) You learned about two different architectures in class, IA32 and x86 64. What architecture is
      this code written for and what major downside would occur from using the other
      architecture
      **x86_64**
      **32-bit has less registers than 64-bit mode, so local variables would need to be stored
      on the stack. Stack accessing takes extra instructions and extra time.**

---

### 2013期中-带答案 · 选择题 9

> 出处：`原文/期中/2013期中-带答案.md` 第 83–95 行　·　模块判定：Processor Arch
> 考什么：RISC 与 CISC 指令集对比

9、下面对RISC和CISC的描述中，错误的是：（      ）
A. CISC指令系统中的指令数目较多，有些指令的执行周期很长；而RISC指令系统中
通常指令数目较少，指令的执行周期都较短。
B. CISC 指令系统中的指令编码长度不固定；RISC 指令系统中的指令编码长度固定，
这样使得RISC机器可以获得了更短的代码长度。
C. CISC指令系统支持多种寻址方式，RISC指令系统支持的寻址方式较少。
D. CISC 机器中的寄存器数目较少，函数参数必须通过栈来进行传递；RISC 机器中的
2

<!-- ===== page 3 ===== -->

寄存器数目较多，可以通过寄存器来传递参数，避免了不必要的存储访问。
答案：BD

---

### 2013期中-带答案 · 选择题 10

> 出处：`原文/期中/2013期中-带答案.md` 第 96–101 行　·　模块判定：Processor Arch
> 考什么：流水线吞吐率与数据冒险

10、下面对流水线技术的描述，正确的是：（      ）
A. 流水线技术不仅能够提高执行指令的吞吐率，还能减少单条指令的执行时间。
B. 不断加深流水线级数，总能获得性能上的提升。
C. 流水级划分应尽量均衡，吞吐率会受到最慢的流水级影响。
D. 指令间的数据相关可能会引发数据冒险，可以通过数据转发或暂停流水线来解决。
答案：CD

---

### 2013期中-带答案 · 选择题 11-13

> 出处：`原文/期中/2013期中-带答案.md` 第 102–129 行　·　模块判定：Processor Arch
> 考什么：Y86 PIPE 数据冒险/转发信号判断

 (11-13)、在教材所描述的流水线处理器（the PIPE processor）上分别运行如下四段
Y86程序代码。请分析其中数据冒险的具体情况，并回答后续3个小题。
#Program 1:  #Program 2:
mrmovl   8(%ebx), %edx  mrmovl   8(%ebx), %edx
rmmovl   %edx, 16(%ecx)  nop
  rmmovl   %edx, 16(%ecx)
#Program 3:  #Program 4:
mrmovl   8(%ebx), %edx  mrmovl   8(%ebx), %edx
nop  nop
nop  nop
rmmovl   %edx, 16(%ecx)  nop
  rmmovl   %edx, 16(%ecx)
11、对于每段程序，请指出是否会因为数据冒险导致流水线停顿（Stall）。
Program 1：（   ），Program 2：（   ），Program 3：（   ），Program 4：
（   ）；
A. Stall     B. No-Stall
答案： A, B, B, B
12、对于每段程序，请指出流水线处理器内是否会产生数据转发（Forwarding）。
Program 1：（   ），Program 2：（   ），Program 3：（   ），Program 4：
（   ）；
A. Forwarding     B. No-Forwarding
答案: A,A,A,B
13、对于每段程序，请指出流水线处理器内使用哪个信号进行数据转发，如果不进行
数据转发，则用none表示。
Program 1：（   ），Program 2：（   ），Program 3：（   ），Program 4：
（   ）；
A. m_valM     B. W_valM     C. none
答案: A,A,B,C

---

### 2013期中-带答案 · 第五题 1)

> 出处：`原文/期中/2013期中-带答案.md` 第 323–327 行　·　模块判定：Processor Arch
> 考什么：流水线吞吐率计算

第五题（9分）
在“取指-译码-执行-写回”的四级流水线中，各流水级的工作内容和延迟如上图所示，寄存器的延迟
也已标出。数据和指令分别存放在不同的存储器中。Cycle N写入寄存器文件的数据Cycle N+1才可读出。
请问：
1）若不考虑流水线填充和清空时间，请计算该处理器的吞吐率。（1分）

---

### 2013期中-带答案 · 第五题 2)

> 出处：`原文/期中/2013期中-带答案.md` 第 328–328 行　·　模块判定：Processor Arch
> 考什么：SEQ 单周期处理器吞吐率

2）若将该处理器改造为单周期处理器（SEQ），请计算SEQ处理器的吞吐率。（1分）

---

### 2013期中-带答案 · 第五题 3)

> 出处：`原文/期中/2013期中-带答案.md` 第 329–337 行　·　模块判定：Processor Arch
> 考什么：Y86 程序段的数据相关与冒险

3）在上述流水线中，执行阶段包含了访问数据存储的时间。对于如下的Y86程序段，指令间存在哪些数据
相关（dependence），会引起哪些数据冒险（hazard）？（5分）
Prog:
irmovl$128, %edx    #instr1
irmovl$3, %ecx      #instr2
rmmovl  %ecx, 0(%edx)  #instr3
irmovl$10, %ebx   #instr4
mrmovl  0(%edx), %eax  #instr5
addl    %ebx, %eax    #instr6

---

### 2013期中-带答案 · 第五题 4)

> 出处：`原文/期中/2013期中-带答案.md` 第 338–363 行　·　模块判定：Processor Arch
> 考什么：转发通路解决方案（含答案与流水线结构图）

4）以上的数据冒险，可以通过转发（forward）的方法解决。请结合上述程序代码和流水线结构图逐个说明
解决方案。（2分）
答案：
1）1000/(280 + 20) = 1000/300 = 3.33GIPS
2）1000/(80 +60 +280 + 60 +20) = 1000/ 500 = 2 GIPS
3）
Prog：
irmovl$128, %edx     ; 1、dx= 128
irmovl$3, %ecx      ; 2、cx= 3
rmmovl  %ecx, 0(%edx)  ; 3、[dx] = cx
irmovl$10, %ebx   ; 4、bx= 10
mrmovl  0(%edx), %eax  ; 5、ax= [dx]
addl    %ebx, %eax    ; 6、bx = bx + ax
相关：1-3，2-3, 1-5，4-6，5-6
冒险：1-3，2-3，4-6，5-6
4）2-3，5-6：执行到译码的转发通路解决；1-3,4-6：写回到译码的转发通路解决。
10

![图](../../assets/期中/2013期中-带答案/p10-img9.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img10.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img11.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img12.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img13.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img14.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img15.jpg)
![图](../../assets/期中/2013期中-带答案/p10-img16.jpg)

---

### 2013期中-带答案 · 第六题

> 出处：`原文/期中/2013期中-带答案.md` 第 367–392 行　·　模块判定：Processor Arch
> 考什么：Y86 SEQ 各阶段操作（cmovXX/call/decl）

第六题（9分）
请分析Y86 ISA中定义的两条指令（cmovXX、call）和一条新加入Y86 ISA的IA32指
令（decl：将操作数减1）。若在教材所描述的SEQ处理器上执行这些指令，请按下表填
写每个阶段进行的操作。如果在某一阶段没有任何操作，请填写none指明。
注1、所用到的指令编码为：
cmovXX  rA, rB  2  fn  rA  rB
call  Dest  8  0  Dest
decl  rA  C  0  rA  F
注2、需说明的信号包括：icode, ifun, rA, rB, valA, valB, valC, valE, valP；the register file
R[], data memory M[], Program counter PC, condition codes CC。
（每格0.5分）
Stage  cmovXX  rA, rB  call  Dest  decl  rA
Fetch  icode:ifun ← M1[PC]  icode:ifun ← M1[PC]  icode:ifun ← M1[PC]
rA:rB ← M1[PC+1]    rA:rB ← M1[PC+1]
  valC ← M4[PC+1]
valP ← PC+2  valP ← PC+5  valP ← PC+2
Decode  valA ← R[rA]    valA ← R[rA]
valB ← R[%esp]
Execute  valE ← 0+valA  valE ← valB+(-4)  valE ← valA+(-1)
Cnd ← Cond(CC,ifun)  Cnd ← Cond(CC,ifun)
（也可以写Set CC）  （也可以写Set CC）
Memory  none  M4[valE] ← valP  none
Write  if(Cnd) R[rB] ← valE  R[%esp] ← valE  R[rA] ← valE
back
PC  PC ← valP  PC ← valC  PC ← valP
update

---

### 2014期中-带答案 · 第一题 9

> 出处：`原文/期中/2014期中-带答案.md` 第 173–186 行　·　模块判定：Processor Arch
> 考什么：组合电路逻辑门转 HCL 表达式

9、对应下述组合电路的正确 HCL 表达式为

![图](assets/期中/2014期中-带答案/page-05.png)

（图：组合电路图，输入 A、B 经一个与门输出 D，输入 A、C 经另一个与门输出 E，D 与 E 再经一个或门输出 X）

A. Bool X = (A || B) && (A || C)
B. Bool X = A || (B && C)
C. Bool X = A && (B || C)
D. Bool X = A || B || C

答：（　　　）

答案：C

---

### 2014期中-带答案 · 第一题 10

> 出处：`原文/期中/2014期中-带答案.md` 第 188–199 行　·　模块判定：Processor Arch
> 考什么：三级流水线执行 10 条指令所需时间

10、若处理器实现了三级流水线，每一级流水线实际需要的运行时间分别为 2ns、2ns 和 1ns，则此处理器不停顿地执行完毕 10 条指令需要的时间为：

A. 21ns
B. 22ns
C. 23ns
D. 24ns

答：（　　　）

答案：D

2+2+2*10 = 24

---

### 2014期中-带答案 · 第一题 11

> 出处：`原文/期中/2014期中-带答案.md` 第 201–215 行　·　模块判定：Processor Arch
> 考什么：CISC 与 RISC 指令集特点对比

11、关于 RISC 和 CISC 的描述，正确的是：

A. CISC 指令系统的指令编码可以很短，例如最短的指令可能只有一个字节，因此 CISC 的取指部件设计会比 RISC 更为简单。

<!-- ===== page 6 ===== -->

B. CISC 指令系统中的指令数目较多，因此程序代码通常会比较长；而 RISC 指令系统中通常指令数目较少，因此程序代码通常会比较短。
C. CISC 指令系统支持的寻址方式较多，RISC 指令系统支持的寻址方式较少，因此用 CISC 在程序中实现访存的功能更容易。
D. CISC 机器中的寄存器数目较少，函数参数必须通过栈来进行传递；RISC 机器中的寄存器数目较多，只需要通过寄存器来传递参数。

答：（　　　）

答案：C

考查对 CISC 和 RISC 基本特点的描述，A 和 B 都是描述反了，D 则是太绝对，RISC 也有可以用栈来传递参数。

---

### 2014期中-带答案 · 第一题 12

> 出处：`原文/期中/2014期中-带答案.md` 第 217–228 行　·　模块判定：Processor Arch
> 考什么：流水线数据冒险、吞吐率与流水级划分

12、关于流水线技术的描述，正确的是：

A. 指令间数据相关引发的数据冒险，一定可以通过暂停流水线来解决。
B. 流水线技术不仅能够提高执行指令的吞吐率，还能减少单条指令的执行时间。
C. 增加流水线的级数，一定能获得性能上的提升。
D. 流水级划分应尽量均衡，不均衡的流水线会增加控制冒险。

答：（　　　）

答案：A

说明：B 会增加单条指令的执行时间，C 可能会降低性能，D 和控制冒险没有关系

---

### 2014期中-带答案 · 第六题

> 出处：`原文/期中/2014期中-带答案.md` 第 554–583 行　·　模块判定：Processor Arch
> 考什么：Y86 新增 caddXX 指令在 SEQ 各阶段的操作

第六题（10 分）

请分析Y86 ISA中新加入的一条指令： caddXX，条件加法。其功能可以参考add和cmovXX两条指令。

![图](assets/期中/2014期中-带答案/page-15.png)

（图：Y86 新增指令 caddXX 的指令编码格式，字段依次为 C、fn、rA、rB）

```
caddXX | C | fn | rA | rB |
```

若在教材所描述的SEQ处理器上执行这条指令，请按下表填写每个阶段进行的操作。需说明的信号包括： icode, ifun, rA, rB, valA, valB, valC, valE, valP, Cnd； the register file R[], data memory M[], Program counter PC, condition codes CC。其中对存储器的引用必须标明字节数。如果在某一阶段没有任何操作，请填写none指明。

![图](assets/期中/2014期中-带答案/page-15.png)

（图：第六题 SEQ 各阶段操作填写表，行为 Fetch / Decode / Execute / Memory / Write back / PC update）

| Stage | caddXX rA, rB |
| --- | --- |
| Fetch | icode:ifun ← M<sub>1</sub>[PC]<br>rA:rB ← M<sub>1</sub>[PC+1]<br>valP ← PC+2 |
| Decode | valA ← R[rA]<br>valB ← R[rB] |
| Execute | valE ← valA+valB<br>Cnd ← Cond(CC,ifun) |
| Memory | none |
| Write back | if(Cnd) R[rB] ← valE |
| PC update | PC ← valP |

（每个操作 1 分）

注：Execute 阶段可以写上 if(Cnd) Set CC，不计分，但如果只写了 Set CC 是要扣分的。Write back 阶段的操作不可以写成 R[rB] ← Cnd? valE: valB

---

### 2015期中-带答案 · 选择题 11

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 154–160 行　·　模块判定：Processor Arch
> 考什么：RISC/CISC 指令系统设计

11. 下面有关指令系统设计的描述正确的是：
A. 采用CISC指令比RISC指令代码更长。
B. 采用CISC指令比RISC指令运行时间更短
C. 采用CISC指令比RISC指令译码电路更加复杂
D. 采用CISC指令比RISC指令的流水线吞吐更高
答案：C ，CISC 的比 RISC 代码复杂（如不定长），因此译码也更复杂，优点是
代码更短。运行时间和吞吐都谁更高要依据实际应用。

---

### 2015期中-带答案 · 选择题 12

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 161–170 行　·　模块判定：Processor Arch
> 考什么：组合逻辑+寄存器的最短延时与吞吐

12. 一个功能模块包含组合逻辑和寄存器，组合逻辑单元的总延迟是 100ps，单
个寄存器的延时是20ps，该功能模块执行一次并保存执行结果，理论上能达
到的最短延时和最大吞吐分别是多少？
A. 20ns, 50GIPS
B. 120ns，50GIPS
C. 120ns，10GIPS
D. 20ps,10GIPS
答案：B，主要考察延时和吞吐的区别，延时最小是 logic + 1 个 register，
吞吐最高时是把 logic 划分成无穷多份， 每一级需要 20ps, 1000/20ps =
50GIPS

---

### 2015期中-带答案 · 选择题 13

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 171–181 行　·　模块判定：Processor Arch
> 考什么：流水线冒险与 data forwarding

13. 关于流水线技术的描述，错误的是：
A. 流水线技术能够提高执行指令的吞吐率，但也同时增加单条指令的执行时
间。
B. 减少流水线的级数，能够减少数据冒险发生的几率。
C. 指令间数据相关引发的数据冒险，都可以通过data forwarding来解决。
5

<!-- ===== page 6 ===== -->

D. 现代处理器支持一个时钟内取指、执行多条指令，会增加控制冒险的开销。
答：C，load-use冒险 不能通过data forwarding来解决

---

### 2015期中-带答案 · 选择题 14

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 182–190 行　·　模块判定：Processor Arch
> 考什么：Y86 SEQ 的 PC 更新 HCL 数据来源

14. 在Y86的SEQ实现中，PC（Program Counter，程序计数器）更新的逻辑
结构如下图所示，请根据HCL描述为①②③④选择正确的数据来源。
其中：Icode为指令类型，Cnd为条件是否成立，valC表示指令中的常数值，
valM表示来自返回栈的数据，valP表示PC自增。
A. valC, valM, valP, valP
B. valC, valC, valP, valP
C. valC, valC, valM, valP
D. valM, valC, valC, valP
答：C

---

### 2015期中-带答案 · 第四题 1

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 400–421 行　·　模块判定：Processor Arch
> 考什么：新增 NewJE 指令在 SEQ 各阶段的操作

第四题（20分）
请分析Y86 ISA中新加入的一条指令：NewJE，其格式如下。
  NewJE  C  0  rA  rB  Dest
其功能为：如果R[rA]= R[rB]，则跳转到Dest继续执行，否则顺序执行。
1. 若在教材所描述的SEQ处理器上执行这条指令，请按下表补全每个阶段的操作。
需说明的信号可能会包括：icode, ifun, rA, rB, valA, valB, valC, valE,
valP, Cnd；the register file R[], data memory M[], Program
counter PC, condition codes CC。其中对存储器的引用必须标明字节数。
如果在某一阶段没有任何操作，请填写none指明。
Stage  NewJE rA, rB, Dest
icode:ifun  M1[PC]
Fetch  rA:rB  M1[PC+1]
valC  M4[PC+2]
valP  PC+6
valA  R[rA]
Decode  v alB  R[rB]
valE  valA – valB
Execute  （注：也可以是valB - valA）
Memory  n one
Write back  n one
PC update  P C  valE==0 ? valC : valP
  （红字处每行1分，共5分）

---

### 2015期中-带答案 · 第四题 2

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 422–432 行　·　模块判定：Processor Arch
> 考什么：PIPE 中跳转条件不满足时错误执行条数

2.若在教材所描述的PIPE处理器上执行NewJE指令，如果跳转条件不满足，一共
15

<!-- ===== page 16 ===== -->

会错误执行__2__条指令。
为了减小错误预测的代价，现将教材所描述的PIPE处理器做如下改进：在
Decode阶段增加一个比较器，用于判断（R[rA] = R[rB]）条件，比较器的输
出信号为d_equal。如果相等，则d_equal = 1，反之 d_equal = 0。
此时，如果执行NewJE指令时跳转条件不满足，一共会错误执行__1__条指令。
（每空1分，共2分）

---

### 2015期中-带答案 · 第四题 3

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 433–447 行　·　模块判定：Processor Arch
> 考什么：NewJE 预测错误的判断条件与控制信号

3.在教材所描述的PIPE处理器上执行JXX指令时，发生转移预测错误的判断条件
和各级流水线寄存器的控制信号如下所示：
Condition  Trigger
Mispredicted Branch  E_icode = IJXX & !e_Cnd
Condition  F  D  E  M  W
Mispredicted normal  bubble  bubble  normal  normal
Branch
在第（2）小题所述的改进后的处理器上执行NewJE指令，发生转移预测错误的判
断条件和各级流水线寄存器的控制信号应如何设置？
Condition  Trigger
Mispredicted Branch  D_icode = INewJE & !d_equal
Condition  F  D  E  M  W
Mispredicted normal  bubble  normal  normal  normal
Branch
（每空1分，共5分）

---

### 2015期中-带答案 · 第四题 4

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 448–467 行　·　模块判定：Processor Arch
> 考什么：load-use 与误预测组合冒险的控制信号

4.在第（2）小题所述的改进后的处理器上执行如下代码，
0x000:    mrmovl 0(%eax), %edx
16

<!-- ===== page 17 ===== -->

0x006:    NewJE %edx, %eax, t
0x00c:    irmovl $1, %eax    # Fall through
0x012:    nop
0x013:    nop
0x014:    nop
0x015:    halt
0x016: t:irmovl $3, %edx    # Target (Should not execute)
0x01c:    irmovl $4, %ecx    # Should not execute
0x022:    irmovl $5, %edx    # Should not execute
会发生load-use 和misprediction组合的hazard情况, 如下图所示
请问此时，各级流水线寄存器的控制信号应如何设置？
Condition  F  D  E  M  W
Combination C  stall  stall  bubble  normal  normal
（每空1分，共3分）

---

### 2015期中-带答案 · 第四题 5

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 468–482 行　·　模块判定：Processor Arch
> 考什么：data miss 时的各级流水线控制信号

5.在教材 PIPE 处理器设计中，data memory 实际是高速缓存(cache)。假设
在执行上述(4)中代码时，0x000 指令中的 0(%eax)地址中的数据不在 data
memory 中，则data memory会将输出信号 m_datamiss置为1，直到数据从
内存中取回到 data memory，再将 m_datamiss置为 0。（m_datamiss的默
认值为0）
这种情况的判断条件如下，请问各级流水线寄存器的控制信号应如何设置？
Condition  Trigger
Data Miss  M_icode in { IMRMOVL, IPOPL } && m_datamiss
17

<!-- ===== page 18 ===== -->

Condition  F  D  E  M  W
data miss  stall  stall  stall  stall  bubble
（每空1分，共5分）

---

### 2016期中-带答案 · 第一题 8

> 出处：`原文/期中/2016期中-带答案.md` 第 87–96 行　·　模块判定：Processor Arch
> 考什么：CISC 与 RISC 指令系统对比

8.  下面对指令系统的描述中，错误的是：（  ）
A. CISC 指令系统中的指令数目较多，有些指令的执行周期很长；而 RISC
指令系统中通常指令数目较少，指令的执行周期都较短。
B. CISC指令系统中的指令编码长度不固定；RISC指令系统中的指令编码长
度固定，这样使得CISC机器可以获得了更短的代码长度。
C. CISC指令系统支持多种寻址方式，RISC指令系统支持的寻址方式较少。
D. CISC机器中的寄存器数目较少，函数参数必须通过栈来进行传递；RISC
机器中的寄存器数目较多，只需要通过寄存器来传递参数，避免了不必要的存
储访问。
答案：D

---

### 2016期中-带答案 · 第一题 9

> 出处：`原文/期中/2016期中-带答案.md` 第 97–108 行　·　模块判定：Processor Arch
> 考什么：流水线技术描述辨析

9.  下面对流水线技术的描述，正确的是：（      ）
A. 流水线技术不仅能够提高执行指令的吞吐率，还能减少单条指令的执行时
间。
B. 不断加深流水线级数，总能获得性能上的提升。
C. 流水级划分应尽量均衡，吞吐率会受到最慢的流水级影响。
D. 指令间的数据相关可能会引发流水线停顿，但总是可以通过调度指令来解
决。
3

<!-- ===== page 4 ===== -->

答案：C

---

### 2016期中-带答案 · 第一题 10

> 出处：`原文/期中/2016期中-带答案.md` 第 109–114 行　·　模块判定：Processor Arch
> 考什么：组合电路 HCL 表达式

10. 对应下述组合电路的正确HCL表达式为：
A. Bool eq = ( a or b ) and ( !a or !b )
B. Bool eq = ( a and b) or ( !a and !b )
C. Bool eq = ( a or !b ) and ( !a or b )
D. Bool eq = ( a and !b ) or ( !a and b )
答案： B

---

### 2016期中-带答案 · 第一题 11

> 出处：`原文/期中/2016期中-带答案.md` 第 115–122 行　·　模块判定：Processor Arch
> 考什么：转移预测错误的判断与恢复信号

11. 流水线数据通路中的转移预测策略为总是预测跳转。如果转移预测错误，需要
恢复流水线，并从正确的目标地址开始取值。其中，用来判断转移预测是否正
确的信号是_①_和_②__，用来获得正确的目标地址的信号是_③_。
A．① M_icode  ② M_Bch ③ M_valA
B．① W_icode  ② M_Bch ③ M_valA
C．① W_icode  ② M_Bch ③ W_valM
D．① M_icode  ② M_Bch ③ W_valM
答案：A

---

### 2016期中-带答案 · 第一题 12

> 出处：`原文/期中/2016期中-带答案.md` 第 123–133 行　·　模块判定：Processor Arch
> 考什么：三级流水线执行时间计算

12. 若处理器实现了三级流水线，每一级流水线实际需要的运行时间分别为 1ns、
2ns 和 3ns，则此处理器不停顿地执行完毕 10 条指令需要的时间为：
A． 21 ns  B． 12 ns  C． 24 ns  D． 36 ns
4

![图](../../assets/期中/2016期中-带答案/p4-img1.jpg)
![图](../../assets/期中/2016期中-带答案/p4-img2.jpg)

<!-- ===== page 5 ===== -->

答案 D  3+3+10*3=36ns

---

### 2016期中-带答案 · 第四题

> 出处：`原文/期中/2016期中-带答案.md` 第 367–423 行　·　模块判定：Processor Arch
> 考什么：Y86 新增条件返回指令 cretXX 的 SEQ/PIPE 设计

（出题人：汪小林，易江芳）
请分析32位的Y86 ISA中新加入的一组条件返回指令：cretXX，其格式如下。
cretXX  9  fun
类似cmovXX，该组指令只有当条件码(Cnd)满足时，才执行函数返回；如果
条件不满足，则顺序执行。
1. 若在教材所描述的SEQ处理器上执行这条指令，请按下表补全每个阶段的操作。
需说明的信号可能会包括：icode, ifun, rA, rB, valA, valB, valC, valE,
valP, Cnd；the register file R[], data memory M[], Program
counter PC, condition codes CC。其中对存储器的引用必须标明字节数。
如果在某一阶段没有任何操作，请填写none指明。
Stage  cretXX Offset
Fetch  icode:ifun  M1[PC]
valP  PC+1
valB  R[%esp]
Decode  valA  R[%esp]
valE  valB + 4
Execute  Cnd ← Cond(CC, ifun)
valM  M4[valA]
Memory
if (Cnd) R[%esp]  valE
Write back
PC update  PC  Cnd ? valM : valP
（每个空1分，共9分）
2.为了执行cretXX指令，我们需要改进教材所描述的PIPE处理器，在W（Write
12

<!-- ===== page 13 ===== -->

Back）阶段引入流水线寄存器___W_Cnd(填W_Bch也算对)__________，并将
其连接到PC选择器（Select PC）以便有条件地更新PC。假设改进后的处理器总
是预测函数返回条件不满足，则如果返回条件满足时，一共会错误取指__3__条指
令。（每空1分，共2分）
3.在2中改进的PIPE处理器上执行cretXX指令时，发生预测错误时的判断条件和
各级流水线寄存器的控制信号应如何设置？
Condition  Trigger
Mispredicted cret  (E_icode = ICRETXX && e_Cnd) ||
(M_icode = ICRETXX && M_Cnd)
（算两个空，每空1分，共2分）
Condition  F  D  E  M  W
Mispredicted cret  Normal  bubble  bubble  normal  normal
（每空1分，共3分）
13

![图](../../assets/期中/2016期中-带答案/p13-img1.jpg)

<!-- ===== page 14 ===== -->

4. PIPE处理器上处理器上执行如下代码片段，
0x000:    xorl %eax, %eax
0x002:    popl %esp
0是x否00会4发: 生   lcoraedt-nues e 和misprediction cret组合的hazard情况？（1分）
答：不会
 如果此时“popl %esp”在流水线的Execute阶段，请问此时，各级流水线寄存
器的控制信号应如何设置？
Condition  F  D  E  M  W
Combination  stall  stall  bubble  normal  normal
（  每空1分，共3分）

---

### 2017期中-带答案 · 第一题 9

> 出处：`原文/期中/2017期中-带答案.md` 第 123–130 行　·　模块判定：Processor Arch
> 考什么：RISC 与 CISC 特点辨析

9.  下面关于RISC和CISC的描述中，正确的是:
A. CISC和早期RISC在寻址方式上相似，通常只有基址和偏移量寻址
B. CISC指令集可以对内存和寄存器操作数进行算术和逻辑运算，而RISC只能
寄存器操作数进行算术和逻辑运算
C. CISC和早期的RISC指令集都有条件码，用于条件分支检测
D. CISC机器中的寄存器数目较少，函数参数必须通过栈来进行传递；RISC机器
中的寄存器数目较多，只需要通过寄存器来传递参数，避免了不必要的存储访问
答案：B

---

### 2017期中-带答案 · 第一题 10

> 出处：`原文/期中/2017期中-带答案.md` 第 135–145 行　·　模块判定：Processor Arch
> 考什么：Y86 SEQ 的 mem_addr HCL 描述

10. 在Y86的SEQ实现中，对仅考虑IRMMOVQ，ICALL，IPOPQ，IRET指令，
对mem_addr的HCL描述正确的是：
word mem_addr = [
  icode in { (1), (2) } : valE;
  icode in { (3), (4) } : valA;
];
A. (1) IRMMOVQ  (2) IPOPQ   (3) IRET    (4) ICALL
B. (1) IRMMOVQ  (2) IRET    (3) IPOPQ   (4) ICALL
C. (1) ICALL   (2) IPOPQ   (3) IRMMOVQ  (4) IRET
D. (1) IRMMOVQ  (2) ICALL   (3) IPOPQ   (4) IRET
答案： D

---

### 2017期中-带答案 · 第一题 11

> 出处：`原文/期中/2017期中-带答案.md` 第 146–152 行　·　模块判定：Processor Arch
> 考什么：流水线与数据冒险描述辨析

11. 关于流水线技术的描述，错误的是:
A．流水线技术能够提高执行指令的吞吐率，但也同时增加单条指令的执行时间
B. 增加流水线级数，不一定能获得总体性能的提升
C. 指令间数据相关引发的数据冒险，不一定可以通过暂停流水线来解决。
D. 流水级划分应尽量均衡，吞吐率会受到最慢的流水级影响，均衡的流水线能提
高吞吐量。
答案：C

---

### 2017期中-带答案 · 第四题

> 出处：`原文/期中/2017期中-带答案.md` 第 292–376 行　·　模块判定：Processor Arch
> 考什么：Y86 条件内存传送指令 crmmovqXX 的 SEQ/PIPE 实现

第四题（20分）
分析64位的Y86 ISA中新加入的条件内存传送指令：crmmovqXX和cmrmovqXX。
crmmovqXX和cmrmovqXX指令在条件码满足所需要的约束时，分别执行和
rmmovq以及mrmovq同样的语义。其格式如下：
rmmovq  4  0  rA  rB  D（8字节）
crmmovqXX  4  fn  rA  rB  D（8字节）
mrmovq  5  0  rA  rB  D（8字节）
cmrmovqXX  5  fn  rA  rB  D（8字节）
1. 请按下表补全每个阶段的操作。需说明的信号可能会包括：icode, ifun, rA,
rB, valA, valB, valC, valE, valP, Cnd；寄存器堆R[],存储器M[], 程
序计数器PC, 条件码CC。其中对存储器的引用必须标明字节数。（10分）
阶段  rmmovq rA,D(rB)  cmrmovqXX D(rB),rA
取指  icode:ifun  M1[PC]
rA:rB  M1[PC+1]
valC  M8[PC+2]
valP  PC + 10
译码  valA  R[rA]
valB  R[rB]
执行  valE  valB + valC  valE  valB + valC
Cnd ← Cond(CC, ifun)
访存  M8[valE]  valA  valM  M8[valE]
或
if(Cnd) valM  M8[valE]
写回  none  if(Cnd) R[rA]  valM
更新PC  PC  valP
10

<!-- ===== page 11 ===== -->

2.为了执行上述新增指令，我们需要改进教材所描述的PIPE处理器，在回写（W：
Write Back）阶段引入寄存器以保持流水线信号___W_Cnd___（请参考教材对
信号的命名规则书写），以便有条件地更新寄存器内容。在如此改进的PIPE处理
器上，请写出如下信号的HCL代码。（6分）
信号  HCL代码
F_stall  (E_icode in {IMRMOVQ, IPOPQ} ||
(                      ①                )) &&
E_dstM in            ②              ||
IRET in              ③
E_bubble  (                      ④                ) ||
(E_icode in {IMRMOVQ, IPOPQ} ||
(                      ①                 )) &&
E_dstM in             ②
M_bubble  m_stat in             ⑤             ||
W_stat in             ⑤
附HCL描述中的常数值编码表如下：
IHALT    halt指令的代码     INOP    nop指令的代码
IRRMOVQ  rrmovq指令的代码    IIRMOVQ  irmovq指令的代码
IRMMOVQ  rmmovq指令的代码    IMRMOVQ  mrmovq指令的代码
ICRMMOVQ  crmmovqXX指令的代码  ICMRMOVQ  cmrmovqXX指令的代码
IOPL    整数运算指令的代码    IJXX    跳转指令的代码
ICALL    call指令的代码     IRET    ret指令的代码
IPUSHQ   pushq指令的代码    IPOPQ    popq指令的代码
FNONE    默认功能码        RNONE    表示没有寄存器文件访问
ALUADD   表示加法运算      RRSP    表示%rsp寄存器ID
SAOK    正常地址操作状态码    SADR    地址异常状态码
SINS    非法指令异常状态码    SHLT    halt状态码
①   E_icode == ICMRMOVQ && e_Cond
②  {d_srcA, d_srcB}
③  {D_icode, E_icode, M_icode}
④  E_icode == IJXX && !e_Cond
⑤  {SADR, SINS, SHLT}
11

<!-- ===== page 12 ===== -->

3.对于下面的Y86汇编代码，请使用上述条件内存传送指令将其修改为不带跳转的
汇编代码序列。假设下面的代码片段在教材所描述的PIPE处理器上运行，不考虑
该片段前后代码的影响以及高速缓存（cache）失效的情况，假设%rsi初值为0，
处理器设计使用总是选择（always taken）的预测策略。原始代码片段预计运
行___11__周期，改进代码片段预计执行___9(或8)___周期。（4分）
注：由于第2小题的HCL描述，要求带Cond，因为这是一个更优化的设计，而且和教材上对IJXX
的考虑一致。基于此，第3小题可以有两种指令序列，cmrmoveqne在前的序列执行需要8个周
期，cmrmoveqe在前的指令序列需要9个周期，因此最后一空填8或9都对。
原始代码  改进代码
andq %rsi %rsi  （9个周期的版本）
jne L1  andq %rsi %rsi
mrmovq 8(%rdx), %rax  cmrmovqe  8(%rdx), %rax
jmp L2  cmrmovqne 8(%rdx), %rbx
L1:    addq %rax, %rbx
mrmovq 8(%rdx), %rbx
L2:  （8个周期的版本）
  addq %rax, %rbx  andq %rsi %rsi
cmrmovqne 8(%rdx), %rbx
cmrmovqe  8(%rdx), %rax
addq %rax, %rbx

---

### 2018期中-带答案 · 第一题 9

> 出处：`原文/期中/2018期中-带答案.md` 第 153–163 行　·　模块判定：Processor Arch
> 考什么：编译技术/取指速度对 ISA 选择的影响

9.  请比较RISC和CISC的特点，回答下述问题：
假设编译技术处于发展初期，程序员更愿意使用汇编语言编程来解决实际问题，那
么程序员会更倾向于选用          ISA。
假设你设计的处理器速度非常快，但存储系统设计使得取指令的速度非常慢（也许
只是处理单元的十分之一）。这时你会更倾向于选用          ISA。
A) RISC、RISC   B) CISC、CISC   C) RISC、CISC  D) CISC、RISC
答案：B
//知识点1：CISC有更多的指令，有些更接近高级语言
//知识点2：CISC的指令功能更复杂，指令执行需要更多的周期，一定程度上可以
平衡处理速度与指令访存的速度差异。不过，通常处理器设计中，主要通过多层次
的存储体系结构来弥补两者之的速度差异。

---

### 2018期中-带答案 · 第一题 10

> 出处：`原文/期中/2018期中-带答案.md` 第 164–177 行　·　模块判定：Processor Arch
> 考什么：Y86 popl 的 SEQ 实现

10. Y86指令popl rA的SEQ实现如下图所示，其中❶和❷分别为：
A)  PC + 4  valA + 4
B)  PC + 4  valA + (- 4)
C)  PC + 2  valB + 4
D)  PC + 2  valB + (- 4)
答案：C
//知识点：popl 弹栈指令，栈结构
5

<!-- ===== page 6 ===== -->

1） popl是双字节指令，下一条指令位置PC+2
2） Y86是32位体系结构，popl弹出4字节，弹栈栈指针增加，valA +
4

---

### 2018期中-带答案 · 第四题

> 出处：`原文/期中/2018期中-带答案.md` 第 445–503 行　·　模块判定：Processor Arch
> 考什么：Y86-32 流水线前递 HCL 与 load-use 冒险处理

第四题（15分）
这是一款Y86-32流水线处理器的结构图（局部），请以此为基础，依次回答下列问
题。
1、该处理器设计采用了前递（forwarding）技术，一定程度上解决了数据相关的
问题，在上图中体现在Sel+FwdA和FwdB部件上。前者输出的信号会存到流水线寄
存器E的valA域（即E_valA信号），请补全该信号的HCL语言描述。
int E_valA = [
1
D_icode in { ICALL, IJXX } :             ; # ○ 答案：D_valP
d_srcA == e_dstE :              ;# ○2 答案：e_valE
d_srcA == M_dstM :              ;# ○3 答案：m_valM
15

<!-- ===== page 16 ===== -->

d_srcA == M_dstE : M_valE      ;
d_srcA == W_dstM : W_valM      ;
…
];
2、如果在该处理器上运行下面的程序，每条指令在不同时钟周期所处的流水线阶
段如下表所示。在这种情况下，哪条指令的执行结果会有错误？写出该指令的地址：
0x01e   。（1分）
demo1.ys  1  2  3  4  5  6  7  8  9  10  11  12
0x000: irmovl $128, %edx  F  D  E  M  W
0x006: irmovl $3, %ecx    F  D  E  M  W
0x00c: rmmovl %ecx, 0(%edx)      F  D  E  M  W
0x012: irmovl $10, %ebx
      F  D  E  M  W
0x018: mrmovl 0(%edx),%eax
        F  D  E  M  W
0x01e: addl %ebx, %eax
          F  D  E  M  W
0x020: halt
            F  D  E  M  W
3、如需检测出这个情况，需要增加逻辑电路，用HCL语言表达如下：
E_icode in {IMRMOVL,IPOPL} &&             in {                        }
答案：E_icode in {IMRMOVL,IPOPL} && E_dstM in { d_srcA, d_srcB }，2分，
全对才得分
4、当新增的电路检测出这个情况后，应对各流水线寄存器进行不同的设置，以便
在尽可能少影响性能的前提下解决该问题。请填写下表，可选的设置包括
normal/bubble/stall三种。
F  D  E  M  W
答案：stall,stall,bubble,normal,normal。3分，全对才得分
5、如果遇到下面程序代码所展示的情况，该处理器运行时仍然存在问题。因此，
还需要新增检测电路。当新增的电路检测出这个情况后，应对各流水线寄存器进
行不同的设置，以便在尽可能少影响性能的前提下解决该问题。请填写下表，可
选的设置包括normal/bubble/stall三种。
demo2.ys
…
16

<!-- ===== page 17 ===== -->

0x018: rmmovl %ecx, 0(%edx)
0x01e: irmovl $10, %ebx
0x024: popl %esp
0x026: ret
F  D  E  M  W
答案：stall,stall,bubble,normal,normal。3分，全对才得分

---

### 2018期中-带答案 · 第六题

> 出处：`原文/期中/2018期中-带答案.md` 第 577–617 行　·　模块判定：Processor Arch
> 考什么：PIPE 上循环代码的周期数（冒险/预测/缺失）

第六题（15分）
在PIPE处理器上运行如下Y86代码
  .L1 mrmov (%eax) %ebx
addl %ebx %ecx
    addl %ecx %eax
    xorl %ecx %edx
    jne .L1
    irmov $1 %eax
    irmov $1 %eax
1)  假设上述代码中的循环部分，一共执行了 N 遍后跳出循环，未采用数据前递
（data forwarding）,分支每次都预测正确，访存每次都命中缓存，命中缓存
时访存需要1个周期。请问共需执行多少个周期？在下面空格处，各填入一个
数字。
N * _11_ + _6_
答案：4+N * (5+3+3)+2，填充流水线 +4 ，一次load-use冒险 +3，一次RAW
冒险+3，循环后2指令 +2
    答案修订：N*12+5
4+(N-1)*(5+3+3+1)+(5+3+3)+2，填充流水线+4，一次load-use冒险+3（%ebx），
一次RAW冒险+3（%ecx），一次RAW冒险+1（%eax），循环后2指令+2，其中最
后一次循环%eax不会冒险。
2)  假设上述代码一共循环执行了 N 次后跳出循环，采用数据前递（data
forwarding）,分支每次都预测跳转（taken），访存每次都命中缓存，命中缓存
时访存需要1个周期。请问共需执行多少个周期？
在下面空格处，各填入一个数字。
N * _6_ + _8_
答案：4+N * (5+1)+4 ，填充流水线 +4 ，一次load-use冒险 +1，最后一次
预测错误+2，循环后2指令 +2
3)  假设上述代码一共循环执行了N次后跳出循环（N为偶数），采用数据前递（data
forwarding）,分支每次都预测不跳转（not taken），数据访存时缓存命中率为
50%，指令访存全部命中缓存，命中缓存时访存需要1个周期，未命中缓存时访
20

<!-- ===== page 21 ===== -->

存需要3个周期。请问共需执行多少个周期？
在下面空格处，各填入一个数字。
N * _9_ + _4_
答案：4+0.5*N * (5+1+2)+0.5*N*(5+3+2) +2-2，填充流水线 +4 ，hit一次
load-use冒险 +1，miss一次load-use冒险 +3，预测错误+2，循环后2指令 +2 ，
最后一次预测正确-2
（每小题5分。N相乘的那个数3分，常数2分）

---

### 2019期中-带答案 · 第一题 10

> 出处：`原文/期中/2019期中-带答案.md` 第 189–200 行　·　模块判定：Processor Arch
> 考什么：RISC/CISC 指令集设计特征辨识

10. 下面有三组对于指令集的描述，它们分别符合 ①____，②____，③____ 的
特点。
① 某指令集中，只有两条指令能够访问内存。
② 某指令集中，指令的长度都是4字节。
③ 某指令集中，可以只利用一条指令完成字符串的复制，也可以只利用一条指令
查找字符串中第一次出现字母K的位置。
A. CISC, CISC, CISC
B. RISC, RISC, CISC
C. RISC, CISC, RISC
D. CISC, RISC, RISC
【答】B。①的访存模式单一，更加符合RISC的特点；②的指令长度固定，更加
符合RISC的特点；③的指令功能丰富而复杂，更加符合CISC的特点。

---

### 2019期中-带答案 · 第一题 11

> 出处：`原文/期中/2019期中-带答案.md` 第 205–211 行　·　模块判定：Processor Arch
> 考什么：插入流水线寄存器后的最大吞吐率

11. 如下图所示，①~④为四个组合逻辑单元，对应的延迟已在图上标出，REG0为
一寄存器，延迟为20ps。通过插入额外的2个流水线寄存器REG1、REG2（延
迟均为 20ps），可以对其进行流水化改造。改造后的流水线的吞吐率最大为
________GIPS。
A. 7.69    B. 8.33    C. 10.00    D. 11.11
【答】C。额外的 2 个寄存器应当插入①②之间、②③之间，最慢的一级延迟为
30+50+20=100ps，吞吐率为1000/100=10GIPS

---

### 2019期中-带答案 · 第四题 1

> 出处：`原文/期中/2019期中-带答案.md` 第 492–515 行　·　模块判定：Processor Arch
> 考什么：irOpq 指令在 SEQ 各阶段的实现

第四题（15分）
请分析Y86-64 ISA中新加入的一族算术指令： irOpq V, rA, rB，其格式如
下：
C  Fn  rA  rB  V（8字节）
  与Opq类似，这族指令由四个指令组成，分别是iraddq, irsubq, irandq
和irxorq。其功能为：计算R[rA] OP V并将结果存入R[rB]中，这里OP根
据Fn的取值分别取+, -, &和^，且此过程会设置条件码寄存器。
1.若在教材所描述的SEQ处理器上执行这条指令，请按下表补全每个阶段的操作。
需说明的信号可能会包括：icode, ifun, rA, rB, valA, valB, valC,
valE, valP, Cnd; the register file R[], data memory M[],
Program counter PC, condition codes CC。其中对存储器的引用必须标
明字节数。如果在某一阶段没有任何操作，请填写none指明。（6分）
Stage  irOpq V, rA, rB
Fetch  icode : ifun ← M1[PC]
rA : rB ← M1[PC + 1]
valC ← M8[PC + 2]
valP ← PC + 10
Decode  valA ← R[rA]
valB ← R[rB]
Execute  valE ← valA OP valC
Set CC
Memory  none
Write Back  R[rB] ← valE
Update PC  PC ← valP

---

### 2019期中-带答案 · 第四题 2(1)

> 出处：`原文/期中/2019期中-带答案.md` 第 516–556 行　·　模块判定：Processor Arch
> 考什么：数据前递与 E_valA 的 HCL 描述

2.考虑如下一段Y86-64代码片段：
Loop:  mrmovq (%rdi), %r10   # line 1
    rmmovq %r10, (%rsi)   # line 2
    andq %r10, %r10      # line 3
    jle Npos          # line 4
    irmovq $1, %r10      # line 5
16

<!-- ===== page 17 ===== -->

    addq %r10, %rax      # line 6
Npos:  irmovq $1, %r10      # line 7
    subq %r10, %rdx      # line 8
    irmovq $8, %r10      # line 9
    addq %r10, %rdi      # line 10
    addq %r10, %rsi      # line 11
    andq %rdx, %rdx      # line 12
    jg Loop          # line 13
    ret           # line 14
（1）这段代码中存在一些指令间的数据相关，其中行5与行6的数据相关可以采
用数据前递（Forwarding）技术解决，在下图中体现在Sel+FwdA和FwdB部件
上。前者输出的信号会存到流水线寄存器E的valA域（即E_valA信号），请选
出该信号正确的HCL语言描述： B （2分）
17

<!-- ===== page 18 ===== -->

long d_valA = [
  D_icode in { ICALL, IJXX }: D_valP;
  ________;
  ________;
  ________;
  ________;
  ________;
  1: d_rvalA;
○1 d_srcA == e_dstE : e_valE
○2 d_srcA == M_dstE : M_valE
○3 d_srcA == M_dstM : m_valM
○4 d_srcA == W_dstE : W_valE
○5 d_srcA == W_dstM : W_valM
A ○1○2○3○4○5  B ○1○3○2○5○4  C ○4○5○2○3○1  D ○5○4○3○2○1

---

### 2019期中-带答案 · 第四题 2(2)

> 出处：`原文/期中/2019期中-带答案.md` 第 557–559 行　·　模块判定：Processor Arch
> 考什么：load/use 冒险检测的 HCL 表达

（2）同样是数据相关，上述代码中行1与行2的情况不能用以上方法解决。为了
检测这种情况，需要增加逻辑电路，用HCL语言表达如下：（3分）
E_icode in {IMRMOVQ, IPOPQ} && E_dstM in {d_srcA, d_srcB}

---

### 2019期中-带答案 · 第四题 2(3)

> 出处：`原文/期中/2019期中-带答案.md` 第 560–564 行　·　模块判定：Processor Arch
> 考什么：PIPE 上片段周期数与新指令优化收益

（3）假设该代码片段在教材所描述的PIPE处理器上运行，不考虑该片段代码前
后代码的影响以及高速缓存（cache）失效的情况，假设%rdx初值为10，%rdi
指向的内存中数组的元素均为正数，处理器设计使用总是选择（always taken）
的预测策略。该代码片段预计运行167周期，若使用新增加的irOpq指令来优化
这段代码，可以节省30周期的运行时间。（4分）

---

### 2020期中-带答案 · 第一题 6

> 出处：`原文/期中/2020期中-带答案.md` 第 103–116 行　·　模块判定：Processor Arch
> 考什么：PIPE 中 mem_addr 的 HCL 描述

6、在Y86-64的PIPE实现中，仅考虑ICALL、IPOPQ、IPUSHQ、IRET指令，
对mem_addr的HCL描述正确的是：A
 word mem_addr = [
      M_icode in { ①, ② } : M_valE;
      M_icode in { ③, ④ } : M_valA;
 ];
3

<!-- ===== page 4 ===== -->

A. ①IPUSHQ  ②ICALL  ③IPOPQ  ④IRET
B. ①IPUSHQ  ②IRET   ③ICALL  ④IRET
C. ①IPUSHQ  ②IPOPQ  ③IRET  ④ICALL
D. ①IPUSHQ  ②IRET  ③IPOPQ  ④ICALL

---

### 2020期中-带答案 · 第一题 7

> 出处：`原文/期中/2020期中-带答案.md` 第 117–124 行　·　模块判定：Processor Arch
> 考什么：SEQ/PIPE 预测策略、CPI 与流水线划分

7、下列说法正确的是：C
A. 在SEQ机器中，我们采用预测跳转总是选择（always taken）的策略比从不
选择（never taken）的策略要略好。
B. 流水级划分应尽量均衡，不均衡的流水线会增加控制冒险。
C.  如果一台机器的CPI小于1，则它必然不是普通流水线结构。
D.  由于rrmovq %rax, %rax不影响标记位，所以可使用其代替nop指令。
选项A，SEQ机器无所谓转移预测
选项D，rrmovq会带来潜在的数据相关

---

### 2020期中-带答案 · 第四题 1

> 出处：`原文/期中/2020期中-带答案.md` 第 354–372 行　·　模块判定：Processor Arch
> 考什么：新指令在 SEQ 各阶段的操作补全

 第四题（20分）
基于教材所描述的Y86-64 ISA和SEQ、PIPE处理器结构，完成下列问题。
（1）拟新加入指令lreramvoev。q其  语%r义b相p,当 %于r sp
请按下表补全SEQ处p理o器pq每  个阶%段rb的p 操作。需说明的信号可能会包括：icode,
ifun, rA, rB, valA, valB, valC, valE, valP, Cnd；寄存器堆R[],
存储器M[], 程序计数器PC, 条件码CC。其中对存储器的引用必须标明字节数。
（合计16分，详见下表内）
取  指  icovdael:Pi fun  PC  +M 1[1P C]
  （每行操作2分，一行全对才得分。共2行，合计4分）
译码  valA  R[%rbp]
  valB  R[%rbp]
  （4分，一行全对才得分）
执行  valE  v alB + 8
  （4分，一行全对才得分）
访存  valM  M8[valA]
  （每行操作2分，一行全对才得分。共2行，合计4分）
写回  RR[[%%rrsbpp]]    VVaallEM
更新 PC  PC  valP
 每个空内的语句顺序无所谓

---

### 2020期中-带答案 · 第四题 2

> 出处：`原文/期中/2020期中-带答案.md` 第 377–392 行　·　模块判定：Processor Arch
> 考什么：PIPE 新增 enter 指令的硬件改造选项

（2）类似的，如果尝试新加入指令enter。其语义相当于
pushq    %rbp
rrmovq    %rsp, %rbp
为执行拟新增的指令，你尝试改进PIPE处理器，最终完成的工作为（可多选）:
含有C但不含A不含B的组合，或单选G          。
补充说明：选G是常规思路；但是，含C的选项并试图维持可能的流水控制信号的
设计也可以算对。流水线处理器中里面的寄存器堆在常规情况下只安排2个
写口。含C选项相当于安排3个写口，虽然不是常规设计但仍可以实现。
A．增加了一个计算栈帧调整±8的ALU单元；
B. 为寄存器堆增加了一个读口；
C. 为寄存器堆增加了一个写口；
D. 在执行（E：Execution）阶段引入寄存器以保持新增的流水线信号；
E. 在访存（M：Memory Access）阶段引入寄存器以保持新增的流水线信号；
F. 在回写（W：Write Back）阶段引入寄存器以保持新增的流水线信号；
G. 认为现有框架无法有效支持这一改造。
（4分，完全正确才得分，多选、少选都不得分）

---

### 2021期中-带答案 · 第一题 8

> 出处：`原文/期中/2021期中-带答案.md` 第 141–162 行　·　模块判定：Processor Arch
> 考什么：组合逻辑延迟、流水线级数与吞吐率

8. A-G 为7个基本逻辑单元，下图中标出了每个单元的延迟，以及用箭头标出
了单元之间所有的依赖关系。寄存器的延迟均为20ps，在图中以REG符号表示。
假设流水线寄存器只能添加在有直接依赖关系的基本逻辑单元之间，而不能在C或
G与REG之间。以下说法正确的是：D
A. 原电路的吞吐量(throughput)舍入后大约是1000/150=6.667 GIPS。
B. 将该电路改造成2级流水线有8种方法
C. 如果将该电路改造成3级流水线，延迟最小可以到80 ps。
D. 不论实现该电路时遇到怎样的数据冒险和控制冒险，一定可以对流水线寄存器
使用暂停(stalling)解决。
5

<!-- ===== page 6 ===== -->

A. 错。1000/170 = 5.882 而非 1000/150 = 6.667。不要漏掉寄存器。
B. 错。考虑D-E-F-G这条路，要么插D-E，要么E-F，要么F-G。如果是D-E，那
么为了使每条极大路径上都恰有一个新插入的寄存器，考虑D-E-F-C，那么F-C之
间也不能插入了。但是A-E-F-G上又必须有一个，所以只能插A-E。这样之后不管
是插在A-B还是B-C所得方案都是合法的。对称地，如果是F-G，结果也是如此。
最后考虑E-F的情况，此时A-E，D-E，F-C，F-G之间均不能再插入，但A-B和
B-C任选一个插入得到的方案都合法。因此一共有2+2+2=6种。
C. 错。3阶段里的最优为90ps。
D. 对。最朴素的情况每条指令stall足够多次，电路回到SEQ的状态。

---

### 2021期中-带答案 · 第一题 9

> 出处：`原文/期中/2021期中-带答案.md` 第 163–180 行　·　模块判定：Processor Arch
> 考什么：PIPE 上代码片段的数据转发次数

9. 在课本Y86-64的PIPE上执行以下的代码片段，一共使用到了（    D    ）
次数据转发。假设在该段代码执行前和执行后PIPE都执行了足够多的nop指令。
mrmovq 0(%rdx), %rax
addq  %rbx, %rax
mrmovq 8(%rdx), %rcx
addq  %rcx, %rax
irmovq $10, %rcx
addq  %rcx, %rax
rmmovq %rax, 16(%rdx)
A. 3    B. 4    C. 5    D. 6
红色表示使用到数据转发的寄存器
mrmovq 0(%rdx), %rax
addq %rbx, %rax (1 stall)
mrmovq 8(%rdx), %rcx
addq %rcx, %rax (1 stall)（Decode时第二条指令结果还未写回）
irmovq $10, %rcx
addq %rcx, %rax
rmmovq %rax, 16(%rdx)

---

### 2021期中-带答案 · 第一题 10

> 出处：`原文/期中/2021期中-带答案.md` 第 181–193 行　·　模块判定：Processor Arch
> 考什么：SEQ 现有信号通路能否实现新指令

10. 在书中Y86的SEQ实现下，以下哪一条指令是现有信号通路能完成的：C
A. iaddq rA, V：将立即数V与R[rA]相加，其中rB域设为F，结果存入寄
存器rA
B. mmmovq rA, rB：将R[rA]存的地址开始的8字节数据，移动到R[rB]存的
地址
C. leave：相当于先执行rrmovq %rbp, %rsp，再执行popq %rbp
D. enter：相当于先执行pushq %rbp，再执行rrmovq %rsp, %rbp
6

<!-- ===== page 7 ===== -->

A和B还是比较显然的，D中涉及两次valE的写，这是做不到的，两写只能一个是valE，
一个是valM。

---

### 2021期中-带答案 · 第一题 15

> 出处：`原文/期中/2021期中-带答案.md` 第 265–296 行　·　模块判定：Processor Arch
> 考什么：Y86-64 PIPE 上片段总周期数与结果

15. 请阅读下面的Y86-64代码，并计算它在PIPE（书中图4.52）流水线处
理器上运行所需要的总周期数以及运行结束后%rax的值。假设分支预测默认为
跳转。只用统计从MAIN函数的第一条指令进入PIPE到ret执行完毕所需要的
周期数。(本题无效)
执行周期数和%rax的值（10进制）是：C
.align 8
Array:
    .quad 0x0
    .quad 0x2
    .quad 0x3
    .quad 0x5
  A) 56, 10
MAIN:  B) 55, 10
irmovq   Array,   %rdi  C) 57, 9
irmovq    $4,    %rsi  D) 55, 9
irmovq    $8,    %r10
irmovq    $0,    %rax
irmovq    $1,    %r8
LOOP:
mrmovq   (%rdi),  %rdx
rrmovq    %rdx,   %r9
subq      %rsi,    %r9
jg         AD
  addq      %rdx,   %rax
    jmp       CHECK
AD:
  addq      %rsi,    %rax
CHECK:
  addq      %r10,   %rdi
  subq      %r8,    %rsi
  jne         LOOP
ret

---

### 2021期中-带答案 · 第四题 1

> 出处：`原文/期中/2021期中-带答案.md` 第 427–443 行　·　模块判定：Processor Arch
> 考什么：间接跳转指令 jxx *rB 的 SEQ 阶段补全

第四题（15分）
请分析Y86-64 ISA中加入的一族间接跳转指令：jxx *rB，其格式如下：
C  Fn  F  rB
该指令的功能是跳转到寄存器 R[rB] 所存放的地址。类似于直接跳转指令，间
接跳转指令也包括无条件跳转和条件跳转，通过不同的功能码Fn来指示。为了
和直接跳转区别，icode为IJREGXX。时钟周期适当进行延长，在不修改原有
的硬件线路和信号设置的前提下，只增加和新指令有关的逻辑，回答以下问题。
1. 在教材中的SEQ处理器上实现该指令，请补全下表中每个阶段的操作。需要
说明的信号可能有：icode, ifun, rA, rB, valA, valB, valC, valE,
valP, Cnd, R[], M[], PC, CC
Stage  jxx *rB
Fetch  icode : ifun ← M1[PC]
Decode
Execute
Memory
Write Back
Update PC  PC <- Cnd ? valE: valP

---

### 2021期中-带答案 · 第四题 2

> 出处：`原文/期中/2021期中-带答案.md` 第 448–469 行　·　模块判定：Processor Arch
> 考什么：PIPE 预测下一条 PC 的旁路与 HCL 修改

2. 考虑在教材中的Pipeline处理器上实现该指令，采用总是选择分支（预测
下一条指令时使用跳转地址R[rB]）的预测策略。
  d
  _val
由于R[rB]需要到译码阶段才能得到，需要增加一条从Fwd B输出信号d_valB
到Select PC的旁路通路，增加线路如图所示。增加旁路后，为了预测jxx
*rB的下一条PC，________（需要/不需要）在该指令和下一条指令间插入气
泡。
Select PC的HCL代码如下图所示：
word f_pc = [
 ①
 (M_icode == IJXX || M_icode == IJREGXX) && !M_cnd :
M_valA;
 ②
 W_icode == IRET : W_valM;
 ③
 1 : F_predPC;
 ④
]
为了预测下一条PC，需要修改Select PC的HCL代码，增加一行 _______ :
________，增加的位置可以是 _________ （写出所有可能的位置，错填不得
分，漏填可得部分分）

---

### 2021期中-带答案 · 第四题 3

> 出处：`原文/期中/2021期中-带答案.md` 第 474–477 行　·　模块判定：Processor Arch
> 考什么：预测错误触发条件与流水线控制逻辑

 3. 请将该指令预测错误的触发条件，以及此时流水线的控制逻辑补充完整。
触发条件：（如果有多种可能请任写一种）
_控_制__逻__辑_： =（= 如I果JR有EG多X种X 可&&能 请__任__写_一_ 种）
F   D   E   M   W

---

### 2021期中-带答案 · 第四题 4

> 出处：`原文/期中/2021期中-带答案.md` 第 478–500 行　·　模块判定：Processor Arch
> 考什么：改造后 PIPE 上 foo 的周期数（分支/load-use）

 4. 基于改造后的Y86-64 PIPE考虑如下代码片段，回答问题。
#a rArrarya: y of 3 elements
..qquuaadd  rLe1 turn
.quad L2
 ##  vno iidn  f%orod(il,o nagr rn ,i nl o%nrgs i *arr)
frorom:o vq %rdi, %rdx           # line 1
aaddddqq  %%rrddxx,,  %%rrddxx                          ##  lliinnee  23
aidrdmqo v%qr daxr,r a%yr,d x% r c x                    ##  lliinnee  45
aadnddqq  %%rrddxi,,  %%rrcdxi                          ##  lliinnee  67
jge *%rcx                    # line 8
rreettu  r n :                                      #   l i n#e  9
Lm2r:m o#v q 16(%rsi), %rcx      # line 10
rLm1m:o  v q   %  r c x ,    8 ( % r s  i )               ##  line 11
mrmovq 8(%rsi), %rcx       # line 12
rjmmmpo vrqe t%urrcnx  ,   ( %  r s i )                 ##  lliinnee  1134
18

<!-- ===== page 19 ===== -->

在foo函数运行过程中，计算以下情况foo函数的执行周期数。（周期数计算从
执行foo第一条指令开始，直到其返回指令ret完全通过流水线为止。另外假设
foo函数开始的若干条指令不会和foo函数体外的指令形成冒险。）
n=-1：________；n=0：_________；n=2：_________

---

### 2022期中-带答案 · 第一题 11

> 出处：`原文/期中/2022期中-带答案.md` 第 177–194 行　·　模块判定：Processor Arch
> 考什么：RISC/CISC的ISA特征描述

11.下列 4 组对于 ISA 的描述, 它们分别符合(a)_____, (b)______,
(c)______, (d)______, 的特点.
(a) 某ISA中, 所有指令均不采用条件码
(b) 某ISA中, 只有基址和偏移量寻址
(c) 某ISA中, 执行一些指令需要经过复杂的译码电路
(d) 某ISA中, 指令长度最短1字节, 最长15字节以上
A. RISC, CISC, CISC, RISC
B. RISC, RISC, CISC, CISC
C. CISC, RISC, RISC, CISC
D. CISC, CISC, RISC, RISC
答案：B
5

<!-- ===== page 6 ===== -->

不采用条件码, 符合RISC指令的特征. 只有基址和偏移量寻址, 寻址模式单一, 也
符合RISC的描述. 具有复杂指令且需要经过复杂译码电路, 符合CISC的特征. 指
令长度可变并且变化范围达到最少1字节最长15字节, 只能是CISC

---

### 2022期中-带答案 · 第一题 12

> 出处：`原文/期中/2022期中-带答案.md` 第 195–201 行　·　模块判定：Processor Arch
> 考什么：组合逻辑电路对应的HCL表达式

12.对应下述组合电路的正确HCL表达式为：
A. Bool out = ( a && b) || (!a && c)
B. Bool out = (!a && b) || ( a && c)
C. Bool out = ( a || b) && ( a || c)
D. Bool out = ( a || b) && (!a || c)
答案：D；本体主要考察组合逻辑电路和HCL表达式。逻辑电路由2个或门、1个
与门、1个反向器构成，难度较易。

---

### 2022期中-带答案 · 第一题 13

> 出处：`原文/期中/2022期中-带答案.md` 第 202–208 行　·　模块判定：Processor Arch
> 考什么：三级流水线吞吐量计算

13.将一个延迟为 300ps 的组合逻辑划分为三级流水线，时钟寄存器的延迟为
20ps，则该流水线的吞吐量为：
A.10GIPS
B.8.33GIPS
C.3.33GIPS
D.2.77GIPS
答案：B；1 / (100ps + 20ps) = 8.33GIPS

---

### 2022期中-带答案 · 第一题 14

> 出处：`原文/期中/2022期中-带答案.md` 第 209–218 行　·　模块判定：Processor Arch
> 考什么：SEQ新增条件传送立即数指令（行218附图归属存疑）

14.如果在SEQ中添加一条新的指令ircmovq，其作用是根据当前处理器的条件
码来判断是否需要将一个立即数传送到寄存器内，则下列叙述错误的是：
A． 需要增加一个新的icode标识符
B． 该指令的长度为10字节
C． 只需要修改SEQ处理器的执行阶段的硬件逻辑
D． 在执行阶段valE信号的值会被赋值为valC的值
答案：C，可以和rrmovq指令共用一个icode
6

![图](../../assets/期中/2022期中-带答案/p6-img1.jpg)

---

### 2022期中-带答案 · 第四题

> 出处：`原文/期中/2022期中-带答案.md` 第 452–517 行　·　模块判定：Processor Arch
> 考什么：Y86-64新增cpopqXX条件POP指令（SEQ/PIPE与冒险）

第四题 请分析Y86-64 ISA中新加入的一组条件POP指令：cpopqXX，cpopqXX
和popq指令的机器码格式如下。
cpopqXX  B  fun  rA  F
popq  B  0  rA  F
类似cmovXX，该组cpopqXX指令在条件码(Cnd)满足时，会将栈顶的8字节数据
读入到寄存器rA中，并且使栈指针增加8；如果条件不满足，则不执行该指令，即
对rA、栈指针都无影响。
1.若在教材所描述的SEQ处理器上实现该指令，请按下表补全每个阶段的操作。需
说明的信号可能会包括：icode, ifun, rA, rB, valA, valB, valC, valE,
valP, Cnd；the register file R[], data memory M[], Program
counter PC, condition codes CC。其中对存储器的引用必须标明字节数。
如果在某一阶段没有任何操作，请填写none指明。
Stage  cpopqXX rA
icode:ifun  M1[PC]
Fetch  rA:rB  M1[PC+1]
valP  PC+2
Decode
Execute
Memory
Write back
PC update  PC  valP
14

<!-- ===== page 15 ===== -->

2.考虑在教材中的Pipeline处理器上实现该指令，需要改进教材所描述的PIPE
处理器在执行（E:Execute）阶段的处理逻辑，使其能够在条件不满足时不修改
rA和栈指针的值。请依据改进后的处理器，补全执行阶段的部分HCL代码：
word e_dstE = [
  (E_icode in {IRRMOVQ, ①        } && ②       ) : RNONE;
  1 : E_dstE;
];
word e_dstM = [
    (E_icode == ①        && ②       ) : RNONE;
    1 :  E_dstM;
]
3.和popq与mrmovq相同，在执行该指令的过程中有可能会引发加载-使用冒险
（load-use hazard）。请将在引入了cpopqXX 指令后的Y86-64 PIPE处理
器中，加载-使用冒险的触发条件以及处理冒险的控制逻辑补充完整。如有多种可
能，任写一种即可：
触发条件：E_icode in {IMRMOVQ, IPOPQ} && e_dstM in {     ,      }
控制逻辑：（选填stall, bubble和normal）
F  D  E  M  W
      normal  normal
4. 基于改造后的Y86-64 PIPE考虑如下代码片段，回答问题。
# long foo(long n)
# n in %rdi
foo:
    xor  %rax, %rax  # Line 1
    pushq  %rsp  # Line 2
    irmovq  $1, %rsi  # Line 3
L1:
    subq  %rsi, %rdi  # Line 4
    andq  %rdi, %rdi  # Line 5
    cpopqe  %rsi  # Line 6
    addq  %rsi, %rax  # Line 7
    andq  %rdi, %rdi  # Line 8
15

<!-- ===== page 16 ===== -->

    rjenet   L 1  ##  LLiinnee  91 0
假设条件分支总是预测跳转, 计算在输入的n值取1和3时，函数foo执行的周期数。
（周期数计算从执行foo第一条指令开始，直到其返回指令ret完全通过流水线为
止。另外在调用foo之前，处理器已经执行过足够多的nop指令。）
n为1时候需要执行          个周期；n为3时候需要执行          个周期。

---

### 2023期中-带答案 · 第一题 11

> 出处：`原文/期中/2023期中-带答案.md` 第 196–210 行　·　模块判定：Processor Arch
> 考什么：用MUX4实现HCL表达式

 11. 采用下列的四选一（MUX4）实现HCL表达式：out=（A || C）&& （B ||
C ），连接正确的是：
Word out =  [ !s1&& !s0: I0;   I0
!s1:       I1;  I1 M4U:1X out
!1 s0: :              II32 ;  II23
  ]；  S1 S0
A.S1=A, S0=C, I0= 0, I1= 1，I2=B，I3=0；
B.S1=B, S0=C, I0= 0, I1= 0，I2=A，I3=1；
6

<!-- ===== page 7 ===== -->

C.S1=A, S0=B, I0= C, I1= C，I2=C，I3=1；
D.S1=A, S0=B, I0= C, I1= C，I2=C，I3=0。
答案：C

---

### 2023期中-带答案 · 第一题 16

> 出处：`原文/期中/2023期中-带答案.md` 第 281–295 行　·　模块判定：Processor Arch
> 考什么：SEQ中newPC的HCL（ret阶段取valM）

16. 在教材中Y86-64的SEQ实现中，考虑对newPC的HCL描述，第三处填空
③应该填写的正确表述是：
word new_pc = [
    icode  == ICALL :   ①  ;
    icode  == IJxx && Cnd :   ②  ;
    icode  == IRET :   ③  ;
    1  :    ④  ;
];
A. ValA
B. ValB
C. ValC
D. ValE
E. ValM
F. ValP
答案：选E。中文教材P281-282，送分题

---

### 2023期中-带答案 · 第四题

> 出处：`原文/期中/2023期中-带答案.md` 第 533–586 行　·　模块判定：Processor Arch
> 考什么：Y86-64新增Bxx/JxxR指令与PIPE前递、冒险控制

 第四题（15分）
（a）                                 （ b ）
图  （a）和图（b）分别是教材中Y86-64处理器的SEQ和PIPE实现。
1） 为实现PC相对地址的条件控制转移指令，增加Bxx指令（其中xx为条件码），
跳转目标地址等于当前指令执行时的PC加上偏移offset，编码如下。
0xC  fn  Offset
请为该指令补全下面的HCL描述语句，以正确选择可能的PC来源（2分）。
w or d niecwo_dpec  ===  [I CALL :      略            ;
    icode == IJxx && Cnd :      略     ;
      iiccooddee  ====  IIBRxExT  &:&    C n d  略:   ( 1  )   _ _ _  _ _;_ ____     ;
 ];   1  :       略            ;
19

![图](../../assets/期中/2023期中-带答案/p19-img1.jpg)

<!-- ===== page 20 ===== -->

2） 为实现更长距离的灵活的间接跳转，增加JxxR指令（其中xx为条件码），
从寄存器中直接获得跳转目标地址，编码如下。
0xD  fn  rA  0xF
请为该指令补全下面的HCL描述语句，以正确选择可能的PC来源（2分）。
word new_pc = [
    icode == ICALL :      略            ;
    icode == IJxx && Cnd :      略     ;
    icode == IJxxR && Cnd: (2)  __________  ;
    icode == IRET :      略            ;
    1  :       略            ;
];
3）在Y86-64的PIPE实现中，采用前递（forwarding）技术解决程序执行过
程中存在的数据冒险（hazard），请为该流水线控制信号设计补全下面的HCL描
述语句，填写在括号中：(7分，每空1分)
word d_valA = [
 D_icode in { ICALL, IJXX } : (3)  __________
d_srcA == e_dstE : (4) _______________________
d_srcA == M_dstM : (5) _______________________
d_srcA == M_dstE : (6) _______________________
d_srcA == W_dstM : (7) _______________________
d_srcA == W_dstE : (8) _______________________
1  : (9) _______________
]；
4）如下图所示的流水线时空图中，假设第5个周期时，指令4发生了指令译码错
误遇到非法指令（INS），此时流水线寄存器 D 的控制信号应该是
(10)__________________。流水线寄存器 E 的控制信号应该是
(11)_________________。（请在暂停/Stall、气泡/Bubble、正常/Normal
中选择）。（2分）
20

<!-- ===== page 21 ===== -->

5）参考4）中的流水线时空图，这次其它指令正常执行，但在第5个周期时，指
令2在访存阶段遇到了一级高速缓存未命中（后续二级高速缓存访问命中），此时
流水线寄存器D的控制信号应该是(12)__________________，流水线寄存器
M 的控制信号应该是(13)____________________（请在暂停/Stall、气泡
/Bubble、正常/Normal中选择）。（2分）

---

### 2024期中-带答案 · 第一题 9

> 出处：`原文/期中/2024期中-带答案.md` 第 177–202 行　·　模块判定：Processor Arch
> 考什么：PIPE中数据前递次数统计

9.在课本中 Y86-64 的 PIPE 处理器设计上执行如下代码片段，只考虑d_valA 和
d_valB，假 设 在 该 段代码执行 前和P执IP行E处后理器都执行了足够多的nop指令。
请问一共使用到了（）次数据转发/前递（forwarding）。
Test:
xorq %rax, %rax
irmovq 16, %rbx
subq %rax, %rbx
jl .L2
addq %rax, %rax
jmp .L3
.L2:
addq %rbx, %rbx
addq %rbx, %rax
addq %rbx, %rcx
.L3:
ret
A．2
B．3
C．4
D．5
4行使用2, 3行
5行首先预测跳转，9行进入D阶段并使用4行，10行只进入F阶段不使用
答案为3次（选择B）。
如果未考虑到预测相关，结果是2次。
如果错误理解预测为not taken，结果为2次。
如果不能区分jl和jg，结果为5次（10行和11行各使用一次）

---

### 2024期中-带答案 · 第一题 10

> 出处：`原文/期中/2024期中-带答案.md` 第 203–212 行　·　模块判定：Processor Arch
> 考什么：RISC与CISC的对比

10.下列关于RISC和CISC的表述中，错误的是：
A. RISC一般没有延迟较长的指令；CISC有些指令延迟很长
6

<!-- ===== page 7 ===== -->

B. RISC指令编码长度可变；CISC指令编码长度固定
C. RISC寻址方式简单；CISC寻址方式多样
D. 现代指令系统及处理器的设计实现结合了二者思想
答案：B。

---

### 2024期中-带答案 · 第一题 11

> 出处：`原文/期中/2024期中-带答案.md` 第 213–227 行　·　模块判定：Processor Arch
> 考什么：SEQ中mem_addr/mem_data的HCL补全

11.在Y86-64的SEQ实现中，对mem_addr和mem_data的HCL补全正确的
是：
word mem_addr = [
icode in {IRMMOVQ, IPUSHQ, ICALL, IMRMOVQ} :    ①   ；
icode in {IPOPQ, IRET} :    ②   ；
];
word mem_data = [
icode in {IRMMOVQ, IPUSHQ} :    ③   ；
icode == ICALL :    ④   ；
];
A. ①valA    ②valE    ③valE    ④valC
B. ①valE    ②valA    ③valE    ④valC
C. ①valA    ②valE    ③valA    ④valP
D. ①valE    ②valA    ③valA    ④valP
答案：D。

---

### 2024期中-带答案 · 第四题

> 出处：`原文/期中/2024期中-带答案.md` 第 537–582 行　·　模块判定：Processor Arch
> 考什么：PIPE前递HCL补全、Load/Use冒险与新数据通路

 第四题（20分）
(a)
18

<!-- ===== page 19 ===== -->

图(a)是在教材中 Y86-64 的简单流水线处理器（PIPE）实现图。其中部分展示
了通过数据前递（forwarding）解决数据冒险(hazard)的流程。
1.  （7分）若当前指令从内存中加载了数据至一个寄存器中，且该寄存器是下一
条指令的源寄存器，那么通过数据前递的方式可以减少流水线的暂停（stall）。
请根据前递的工作原理，补全下列HCL描述语句，以实现正确的d_valA的
选择。
word d_valA = [
      D_icode in {ICALL,IJXX } : ___(1)___;
      d_srcA == e_dstE : ___(2)___;
      d_srcA == M_dstM : ___(3)___;
      d_srcA == M_dstE : ___(4)___;
      d_srcA == W_dstM : ___(5)___;
      d_srcA == W_dstE : ___(6)___;
      1 : ___(7)___;
]
2.  （3分）考虑如下两条Y86-64指令系统的指令顺序完成执行：
1    mrmovq 0(%rcx),%rdx
2    pushq %rdx
这两条指令的执行会导致流水线中出现Load/Use数据冒险。当指令1执行到(8)
阶段时，会获得对应内存地址中的数据，该数据将会以信号(9)            进
行数据前递。此时按照图(a)的方式，仍然需要停顿来正确执行指令2，流水线需
要停顿(10)             个周期来保证程序执行正确。
3.  （3分）针对第2小题中的问题，可以通过设计一条额外的数据通路(path)
进行前递的方式来解决这种冲突，从而使得指令1、2之间无需插入气泡。这
条数据通路应当从(11)              阶段将数据前递至(12)
阶段，用于选择流水线寄存器(13)                 的值。
4.  （3分）补充通路后的流水线处理器局部如图(b)所示
19

<!-- ===== page 20 ===== -->

(b)
请根据图示和设计逻辑，补全下列HCL描述语句，以实现正确的e_valA的选择。
w _ o_ r_ d( 1  E4e_)_i_vc_ao l dA e   = i  n [   _{   I:P U  S H(Q1,5 )I R M M  O V Q   }    & &  ;E _srcA ==
]  1 :   (16)                ;
5.  （4分）在补充了第4小题中的功能后，流水线依然存在需要暂停才可以处理
的3数  据  冒po险pq情 况%r。dx例 如，下两条指令顺序执行：
这两条4指  令  会rm导mo致v流q 水%r线a中x,出0(现%rLdoxa)d /Use 数据冒险，请用 stall、bubble、
normal 填写下面的控制信号条件表，说明当前流水线对于这种冒险的处理方式。
 F(e1t7c) h  D(e1c8o) de  E(x1e9c) ute  M(e2m0o) ry  Wnroirtmea l back

---

### 2013期末-带答案 · 第一题 4

> 出处：`原文/期末/2013期末-带答案.md` 第 71–82 行　·　模块判定：Processor Arch
> 考什么：Y86 SEQ 中 PC 更新的 HCL 数据来源

4、 在Y86的SEQ实现中，PC（Program Counter，程序计数器）更新的逻辑
结构如下图所示，请根据HCL描述为①②③④选择正确的数据来源。
2

<!-- ===== page 3 ===== -->

其中：Icode为指令类型，Cnd为条件是否成立，valC表示指令中的常数值，valM
表示来自返回栈的数据，valP表示PC自增。
①    A ：A）valC  B）valM   C）valP
②    A ：A）valC  B）valM   C）valP
③    B ：A）valC  B）valM   C）valP
④    C ：A）valC  B）valM   C）valP

---

### 2013期末-带答案 · 第三题

> 出处：`原文/期末/2013期末-带答案.md` 第 344–366 行　·　模块判定：Processor Arch
> 考什么：组合逻辑单元流水化与吞吐率计算

第三题 （12分）
如图所示，每个模块表示一个单独的组合逻辑单元，每个单元的延迟已在图中标出。
通过在两个单元间添加寄存器的方式，可以对该数据通路进行流水化改造。假设每
个寄存器的延迟为20ps。
1）如果改造为一个二级流水线（只插入一个寄存器），为获得最大的吞吐率，该寄
存器应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。
插入在CD间（1分）
1000/(80+40+60+20) = 1000/200= 5GIPS（过程1分，结果1分）
2）如果改造为一个三级流水线（插入两个寄存器），为获得最大的吞吐率，寄存器
应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。
插入在BC间和DE间（1分）
1000/(80+40+20) = 1000/140 = 7.143 GIPS（过程1分，结果1分）
3）如果改造为一个四级流水线（插入三个寄存器），为获得最大的吞吐率，寄存器
应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。
插入AB间、CD间、DE间（1分）
1000/(100+20) = 1000/120 = 8.33 GIPS（过程1分，结果1分）
4）不改变单元划分，为获得最大性能，该设计至少需要划分成几级？请计算对应
的吞吐率，并说明计算过程。
至少划分成5级（1分）
1000/(80+20) = 10 GIPS（过程1分，结果1分）
11

![图](../../assets/期末/2013期末-带答案/p11-img1.jpg)

---

### 2014期末-带答案 · 第三题

> 出处：`原文/期末/2014期末-带答案.md` 第 422–449 行　·　模块判定：Processor Arch
> 考什么：组合逻辑流水化级数与吞吐率计算

第三题（10分） 处理器
如图所示，每个模块表示一个单独的组合逻辑单元，每个单元的延迟已在图中标出。
通过在两个单元间添加寄存器的方式，可以对该数据通路进行流水化改造。假设每
个寄存器的延迟为20ps。注意，由于电路互联特点A与B之间如果插入寄存器，
B本身的延迟将增加到50ps。
R
A B C D E F E
60ps 40ps 50ps 30ps 50ps G
70ps 20ps
1）如果改造为一个二级流水线（只插入一个寄存器），为获得最大的吞吐率，该寄
存器应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。结果可以是分数
形式也可以是小数形式。
插入在CD间（1分）
1000/(60+40+50+20) = 1000/170= 5.88 GIPS（过程和结果1分）
2）如果改造为一个三级流水线（插入两个寄存器），为获得最大的吞吐率，寄存器
应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。结果可以是分数形式
也可以是小数形式。
插入在BC间和DE间（1分）
1000/(50+70+20) = 1000/140 = 7.143 GIPS（过程和结果1分）
3）如果改造为一个四级流水线（插入三个寄存器），为获得最大的吞吐率，寄存器
应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。结果可以是分数形式
也可以是小数形式。
插入AB间、CD间、EF间（1分）
1000/(50+50+20) = 1000/120 = 8.33 GIPS（过程1分，结果1分）
4）不改变单元划分，为获得最大性能，该设计至少需要划分成几级？请计算对应
的吞吐率，并说明计算过程。结果可以是分数形式也可以是小数形式。
至少划分成6级（1分）
1000/(70+20) = 1000/90 = 11.11 GIPS（过程1分，结果1分）

---

### 2015期末-20160104-带答案 · 第三题

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 429–454 行　·　模块判定：Processor Arch
> 考什么：含 F 模块的组合逻辑流水化与吞吐率

第三题（13分）处理器
如图所示，每个模块表示一个单独的组合逻辑单元，每个单元的延迟已在图中标出。
通过在两个单元间添加寄存器的方式，可以对该数据通路进行流水化改造。假设每
个寄存器的延迟为20ps。设计人员考虑在额外增加一个模块F支持新的指令功能，
形成图形状的流水线。提示：每个模块必须在一个时钟周期内。
  F
70ps
  A   B   C   D   E REG
50ps 20ps 30ps 40ps 60ps 20ps
1）如果没有F模块，请计算该流水线改造前的吞吐率，并说明计算过程。结果保
留小数点后两位。
1000/(50+20+30+40+60+20) = 1000/220 = 4.55GIPS（过程和结果2分）
2）如果有F模块，请计算该流水线改造前的吞吐率，并说明计算过程。结果保留
小数点后两位。
1000/(50+70+40+60+20) = 1000/240 =  4.17GIPS（过程和结果2分）
3）如果有 F 模块，改造为一个二级流水线（可以插入多个寄存器），为获得最大
的吞吐率，寄存器应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。结
果保留小数点后两位。
插入在FD间和CD间（2分）
1000/(50+70+20) = 1000/140 = 7.14 GIPS（过程和结果2分）
4）如果有 F 模块，改造为一个三级流水线（插入多个寄存器），为获得最大的吞
吐率，寄存器应在哪里插入？请计算该流水线的吞吐率，并说明计算过程。结果保
留小数点后两位。
插入在AF间、FD间、CD间（3分，可以酌情部分给分）
1000/(40+60+20) = 1000/120 =  8.33 GIPS（过程和结果2分）
15

---

### 2016期末-带答案 · 第一题 4

> 出处：`原文/期末/2016期末-带答案.md` 第 85–89 行　·　模块判定：Processor Arch
> 考什么：四级流水线操作周期由最长段决定

4.  现有四级指令流水线，分别完成取指、取数、运算、传送结果4步操作。若完
成上述操作的时间依次为9ns、10ns、6ns、8ns，则流水线的操作周期应设
计为 _______ ns。
A．6    B．8    C．9    D．10
答案：D（考察对流水线运行原理的理解）

---

### 2016期末-带答案 · 第三题

> 出处：`原文/期末/2016期末-带答案.md` 第 377–399 行　·　模块判定：Processor Arch
> 考什么：组合逻辑单元插入寄存器与吞吐率

第三题（12分）
如图所示，每个模块表示一个单独的组合逻辑单元，每个单元的延迟以及数据依赖
关系已在图中标出。通过在两个单元间添加寄存器的方式，可以对该数据通路进行
流水化改造。假设每个寄存器的延迟为10ps。
R
A B C D E
G
30ps 30ps 80ps 20ps 10
ps
R
D E F G E
G
60ps 40ps 20ps 80ps 10
ps
1）如果改造为一个二级流水线，为获得最大的吞吐率，该寄存器应在哪里插入？
请计算该流水线的吞吐率，并说明计算过程。结果可以是分数形式也可以是小数形
式。
插入在BC间以及EF（4分，不完整酌情扣1~2分）
1000/(80+20+10) = 1000/110= 9.09 GIPS（正确结果1分，单位1分）。
2）如果改造为一个三级流水线，为获得最大的吞吐率，寄存器应在哪里插入？请
计算该流水线的吞吐率，并说明计算过程。结果可以是分数形式也可以是小数形式。
插入在AE、FD、BC、CD、DE和FG间（4分，不完整酌情扣1~2分）
1000/(80+10) = 1000/90 = 11.11 GIPS（正确结果1分，单位1分）。

---

### 2017期末-无答案 · 第一题 4

> 出处：`原文/期末/2017期末-无答案.md` 第 68–72 行　·　模块判定：Processor Arch
> 考什么：由执行步骤识别 Y86 指令

4.  分析下图的指令执行步骤，请问这是Y86指令系统的哪条指令？
A. call
B. ret
C. pushl
D. popl

---

### 2017期末-无答案 · 第三题

> 出处：`原文/期末/2017期末-无答案.md` 第 293–315 行　·　模块判定：Processor Arch
> 考什么：两级/三级流水线插入寄存器与最大吞吐率

第三题（12分）
如图所示，每个模块表示一个单独的组合逻辑单元，每个单元的延迟以及数据依赖
关系已在图中标出。通过在两个单元间添加寄存器的方式，可以对该数据通路进行
流水化改造。假设每个寄存器的延迟为10ps。
R
A  B  C  D  E
G
60ps  30ps  30ps  40ps  10ps
R
E  F  G  H  E
G
20ps  60ps  40ps  30ps  10ps
1. 如果改造为一个二级流水线，为获得最大的吞吐率：
a) 需要在_______模块之间和_______模块之间插入寄存器；
b) 插入寄存器改造后二级流水线的最长延时路径为_____，最长延时为____
c) 流水线最大吞吐率为：____________________________________
（用分数表示，约分到最简形式，并写明单位）
2. 如果改造为一个三级流水线，为获得最大的吞吐率：
a) 需要在________________________________________________
模块之间插入寄存器；
b) 插入寄存器改造后三级流水线的最长路径延时为:__________；
c) 流水线最大吞吐率为：____________________________________
（用分数表示，约分到最简形式，并写明单位）

---

### 2018期末-带答案 · 第二题

> 出处：`原文/期末/2018期末-带答案.md` 第 262–289 行　·　模块判定：Processor Arch
> 考什么：组合逻辑流水化插寄存器与吞吐率计算

第二题（12分）
如图所示，每个模块表示一个单独的组合逻辑单元，每个单元的延迟以及数据依赖
关系已在图中标出。通过在两个单元间添加寄存器的方式，可以对该数据通路进行
流水化改造。假设每个寄存器的延迟为10ps。
R
A  B  C  D  E
G
40ps  20ps  20ps  80ps  10ps
R
E  F  G  H  E
G
20ps  30ps  30ps  40ps  10ps
1）如果改造为一个二级流水线，为获得最大的吞吐率，该寄存器应在哪里插入？
请计算该流水线的吞吐率，并说明计算过程。结果可以是分数形式也可以是小数形
式。
（6分）插入在CD、CF、AF、EF（2分）
1000/(30+30+40+10) = 1000/110= 9.09 GIPS（过程1分和结果正确包括单位1
分）。
2）如果改造为一个三级流水线，为获得最大的吞吐率，寄存器应在哪里插入？请
计算该流水线的吞吐率，并说明计算过程。结果可以是分数形式也可以是小数形式。
（请给出至少两种实现最大吞吐率的设计方案）
8

<!-- ===== page 9 ===== -->

（6分）插入在AB、AF、EF间（2分）
1000/(80+10) = 1000/90 = 11.11 GIP（S 过程1分和结果正确包括单位1分）。
其他解法如果正确也可以得分

---

### 2019、2020期末-答案解析 · 2020 选择题 5

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 25–25 行　·　模块判定：Processor Arch
> 考什么：RISC 寄存器更多

5. D。送分题，RISC中寄存器一般更多。

---

### 2019、2020期末-答案解析 · 2020 解答题一 1

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 85–85 行　·　模块判定：Processor Arch
> 考什么：延迟 10ns

1. 10ns。送分题。

---

### 2019、2020期末-答案解析 · 2020 解答题一 2

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 86–88 行　·　模块判定：Processor Arch
> 考什么：数据冒险与分支预测惩罚周期数

2. 60。题目中为一个8重循环，具体执行了什么不重要。每次循环出现数据冒险一次，故需要7
个周期。最后分支预测错误有2个周期的惩罚，但是已经算在4个trailingcycle中了，所以需
要60个周期。

---

### 2019、2020期末-答案解析 · 2019 选择题 2

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 156–156 行　·　模块判定：Processor Arch
> 考什么：数据冒险的定义

2. B。数据冒险一般是指当前指令没有写回，而下几条指令在流水线就已经要用到的情况。

---

### 2019、2020期末-答案解析 · 2019 选择题 4

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 159–160 行　·　模块判定：Processor Arch
> 考什么：CISC 变长指令与 ARM/RISC

4. C。CISC变长指令，有不少指令的长度是要比RISC短的。当代手机常常采用ARM架构，这
是RISC；实际上对能耗要求高或者结构简单的设备一般都用RISC。

---

### 2019期末-无答案 · 第一题 2

> 出处：`原文/期末/2019期末-无答案.md` 第 59–63 行　·　模块判定：Processor Arch
> 考什么：PIPE 流水线数据冒险的判定

2.  在本课程的PIPE流水线中，下列情况会出现数据冒险的是：
A. 当前指令会改变下一条指令的目的操作数
B. 当前指令会改变下一条指令的源操作数
C. 下一条指令会改变当前指令的目的操作数
D. 下一条指令会改变当前指令的源操作数

---

### 2019期末-无答案 · 第一题 4

> 出处：`原文/期末/2019期末-无答案.md` 第 73–77 行　·　模块判定：Processor Arch
> 考什么：RISC 与 CISC 指令集特点

4.  下述关于RISC和CISC的讨论，哪个是错误的
A. RISC指令集包含的指令数量通常比CISC的少
B. RISC的寻址方式通常比CISC的寻址方式少
C. RISC的指令长度通常短于CISC的指令长度
D. 手机处理器通常采用RISC，而PC采用CISC

---

### 2019期末-无答案 · 第二题 (2)

> 出处：`原文/期末/2019期末-无答案.md` 第 256–258 行　·　模块判定：Processor Arch
> 考什么：SEQ 处理器理想情况下的周期数

（2）  现有一个类似课上SEQ的处理器来运行上述汇编代码，在理想情况下，其
每个周期可以处理完一条汇编代码，请计算：理想情况下，执行完上述代码段
（即结束循环）一共需要多少周期？

---

### 2019期末-无答案 · 第二题 (4)

> 出处：`原文/期末/2019期末-无答案.md` 第 265–268 行　·　模块判定：Processor Arch
> 考什么：增加加法器后双发射的周期数

（4）  为了提升处理器的性能，增加了一个加法器。因此，在没有数据依赖、并
且不改变指令顺序的情况下，新的处理器可以同时处理两个addq指令、或者
一个addq加一个compq指令。注意：movq和跳转指令仍旧需要单独执行，
其他设置同上一问。请再次计算：完成上述汇编代码段一共需要多少周期？

---

### 2019期末-无答案 · 第二题 (5)

> 出处：`原文/期末/2019期末-无答案.md` 第 269–284 行　·　模块判定：Processor Arch
> 考什么：循环展开并重排指令后的最短周期数（兼 Compilation）

（5）  为了进一步减少处理时间，程序员将代码进行循环展开，新的代码如下：
.L2:
movq    (%rdi), %rbx
movq    8 (%rdi), %rdx
addq    %rbx, %rax
7

<!-- ===== page 8 ===== -->

addq    %rdx, %rax
addq    $16, %rdi
addq    $2, %rcx
cmpq    $8, %rcx
jl     .L2
假设在不影响程序正确性的情况下，可以调整上述指令的顺序，请问最
短需要多少个周期可以完成该代码段（注：其他设置和上一问相同）。

---

### 2020期末-无答案 · 第一题 5

> 出处：`原文/期末/2020期末-无答案.md` 第 92–97 行　·　模块判定：Processor Arch
> 考什么：CISC 与 RISC 指令集特性

5.  下面对指令系统的描述中，错误的是：（  ）
A. 通常CISC指令集中的指令数目较多，有些指令的执行周期很长；而RISC指令集中
指令数目较少，指令的执行周期较短。
B. 通常CISC指令集中的指令长度不固定；RISC指令集中的指令长度固定。
C. 通常CISC指令集支持多种寻址方式，RISC指令集支持的寻址方式较少。
D. 通常CISC指令集处理器的寄存器数目较多，RISC指令集处理器的寄存器数目较少。

---

### 2020期末-无答案 · 第一题 6

> 出处：`原文/期末/2020期末-无答案.md` 第 98–100 行　·　模块判定：Processor Arch
> 考什么：Y86 rmovl 的 SEQ 数据通路

6.  Y86指令rmmovl的SEQ实现如下图所示，其中①和②分别为：
A． PC + 4，  valB + 4      B．  PC + 4， valB + valC
C． PC + 6， valB + 4          D．  PC + 6， valB + valC

---

### 2020期末-无答案 · 第二题 1)

> 出处：`原文/期末/2020期末-无答案.md` 第 262–268 行　·　模块判定：Processor Arch
> 考什么：五级流水线时钟周期与寄存器开销

有一个五级流水线处理器，和课程中的PIPE处理器类似，包含：取指（F）、译码（D）、执
行（E）、访存（M）、写回（W）五级，
1） 在理想设计情况下，流水线每一级的电路处理时间如下表所示，每两级流水线阶段之间
插入的寄存器耗时为1ns
  F  D  E  M  W
处理时间（ns）  8  5  9  8  4
  请问流水线运行的时钟周期，最快为 _______ ns

---

### 2020期末-无答案 · 第二题 2)

> 出处：`原文/期末/2020期末-无答案.md` 第 269–277 行　·　模块判定：Processor Arch
> 考什么：Y86-64 代码在前递与分支预测下的周期数

2） 需要执行如下Y86-64汇编代码，寄存器的初始状态如右下表格所示：
0x000  t:  mrmovq   (%rdi), %rbx
0x002    addq    %rbx, %rax  %rdi  0x8008
0x004    addq    $8, %rdi  %rax  0
0x006    addq    $1, %rcx  %rbx  0
0x008    xorq     $8, %rcx  %rcx  0
0x00a    jne      t
流水线支持课上讲的数据前递（data forwarding），分支预测设计为“始终跳转（” predicted
as taken），请问执行上述代码，需要        个时钟周期？

---

### 2021期末-无答案 · 第一题 3

> 出处：`原文/期末/2021期末-无答案.md` 第 68–74 行　·　模块判定：Processor Arch
> 考什么：RISC 与 CISC 指令集特点

3. 下列关于RISC和CISC的描述中，正确的是：
A.在RISC指令集的发展过程中，其指令数量始终少于100条。
B.CISC 指令集中的指令比 RISC 指令集更复杂，因此其指令长度总是比
RISC指令集中的指令要长。
C.早期的RISC指令集没有条件码，对条件检测来说，要用明确的测试指令，
这些指令会将测试结果放在一个普通的寄存器中。
D.RISC指令集中的所有过程都需要进行内存引用。

---

### 2021期末-无答案 · 第一题 4

> 出处：`原文/期末/2021期末-无答案.md` 第 75–93 行　·　模块判定：Processor Arch
> 考什么：PIPE 中无前递时的数据冒险判定

4. 在Y86-64 PIPE处理器中（不考虑数据前递），以下哪个指令序列会造成
数据冒险？
A.
irmovq $10, %rdx
addq %rdx, %rax
B.
irmovq $10, %rdx
nop
addq %rdx, %rax
  3

<!-- ===== page 4 ===== -->

C.
irmovq $10, %rdx
nop
nop
addq %rdx, %rax
D. 以上三个选项都会引发数据冒险

---

### 2021期末-无答案 · 第一题 5

> 出处：`原文/期末/2021期末-无答案.md` 第 94–100 行　·　模块判定：Processor Arch
> 考什么：流水线延迟、吞吐率与插入寄存器

5. 根据下图所示的流水线结构，判断错误的选项是：
A.当前流水线的延迟为(20ps+40ps+80ps+50ps+10ps)=200ps，吞吐
率为5GIPS。
B.可以通过插入寄存器的方式来使这个流水线变为二级流水线。
C.倘若只能插入两个寄存器(延迟均为10ps)，那么该流水线处理每条指令
的平均时间最多减少20ps (假设每条指令平均使用一个周期的时间)。
D.流水线的级数越深，处理器就一定能获得越好的性能。

---

### 2021期末-无答案 · 第一题 8

> 出处：`原文/期末/2021期末-无答案.md` 第 120–125 行　·　模块判定：Processor Arch
> 考什么：芯片布局算法的优化目标（存疑，属 VLSI/CAD，兼时序）

8. 布局是数字芯片设计自动化流程的必要步骤，下面哪一项不是布局算法需
要优化的目标？
A. 互连线长（Wirelength）
B. 可布线性（Routability）
C. 时序（Timing）
D. 逻辑深度（Logic depth）

---

### chap 2-6 解析 · 第一题 5

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 137–145 行　·　模块判定：Processor Arch
> 考什么：RISC 与 CISC 指令集特征比较

5.下列关于RISC和CISC的描述中，正确的是：

A.在RISC指令集的发展过程中，其指令数量始终少于100条。

B.CISC指令集中的指令比RISC指令集更复杂，因此其指令长度总是比RISC指令集中的指令要长。

C.早期的RISC指令集没有条件码，对条件检测来说，要用明确的测试指令，这些指令会将测试结果放在一个普通的寄存器中。

D.RISC指令集中的所有过程都需要进行内存引用。

---

### chap 2-6 解析 · 第一题 6

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 147–173 行　·　模块判定：Processor Arch
> 考什么：Y86-64 PIPE 数据冒险与所需 nop 指令条数

6.在Y86-64 PIPE处理器中（不考虑数据前递），以下哪个指令序列会造成数据冒险？

A.

irmovq \$10, %rdx

addq %rdx, %rax

B.

irmovq \$10, %rdx

nop

addq %rdx, %rax

C.

irmovq \$10, %rdx

nop

nop

addq %rdx, %rax

D. 以上三个选项都会引发数据冒险

---

### chap 2-6 解析 · 第一题 7

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 175–183 行　·　模块判定：Processor Arch
> 考什么：流水线延迟/吞吐率计算与插入流水线寄存器的影响

7.根据下图所示的流水线结构，判断错误的选项是？

<img src="media/media/image1.png" style="width:5.34653in;height:2.2368in" alt="pic_00" />A.当前流水线的延迟为(20ps + 40ps + 80ps + 50ps + 10ps)=200ps，吞吐率为5GIPS。

B.无法通过只插入一个寄存器的方式来使这个流水线变为二级流水线。

C.倘若只能插入两个寄存器(延迟均为10ps)，那么该流水线处理每条指令的平均时间最多减少20ps (假设每条指令平均使用一个周期的时间)。

D.流水线的级数越深，处理器就一定能获得越好的性能。

---

### chap 2-6 解析 · 第一题 10

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 205–213 行　·　模块判定：Processor Arch
> 考什么：芯片布局算法的优化目标（存疑：偏硬件/EDA 设计）

10\. 布局是数字芯片设计自动化流程的必要步骤，下面哪一项不是布局算法需要优化的目标？

A. 互连线长（Wirelength）

B. 可布线性（Routability）

C. 时序（Timing）

D. 逻辑深度（Logic depth）

---

### 2022期末-无答案 · 第二题 (1)

> 出处：`原文/期末/2022期末-无答案.md` 第 133–135 行　·　模块判定：Processor Arch
> 考什么：Y86 流水线 load-use 冒险的 HCL 检测表达式

(1) 要解决"load-use"冒险，首先要能检测出来。根据下面的处理器信号连接图，补全检测"load-use"冒险的 HCL 表达式。（每空 1 分）

　　____________ in { IMRMOVQ, IPOPQ } && E_dstM in { __________, __________ }

---

### 2022期末-无答案 · 第二题 (2)

> 出处：`原文/期末/2022期末-无答案.md` 第 137–141 行　·　模块判定：Processor Arch
> 考什么：load-use 冒险时各流水级 stall/bubble 设置

(2) 检测到"load-use"冒险后，各流水级应该如何设置？在下表中填入 normal/stall/bubble。（每空 1 分）

| F | D | E | M | W |
| --- | --- | --- | --- | --- |
| stall |  |  |  | normal |

---

### 2022期末-无答案 · 第二题 (3)

> 出处：`原文/期末/2022期末-无答案.md` 第 143–149 行　·　模块判定：Processor Arch
> 考什么：ret 处理时机 HCL 表达式（含流水线信号连接图）

![图](assets/期末/2022期末-无答案/page-04.png)

图为 Y86 流水线处理器的信号连接图（教材 HCL 图）：左侧标注 Execute、Decode 等阶段，包含 ALU A/ALU B、CC、Set_cc、e_dstE、dstE/dstM/srcA/srcB、Register file（Write back / Read ports）、d_srcA/d_srcB/d_rvalA/d_rvalB、Instr valid/need_regids/need_valC 等信号块，右侧一列为各阶段的状态码。

(3) ret 指令因为在流水线很晚阶段才能获得转移目标地址，所以也要特殊处理。参考上面的处理器信号连接图（注意：图中信号可能不完整，但足够推测出所需的信号），补全检测 ret 指令处理时机的 HCL 表达式。（每空 1 分）

　　IRET in { __________, __________, __________ }

---

### 2022期末-无答案 · 第二题 (4)

> 出处：`原文/期末/2022期末-无答案.md` 第 151–155 行　·　模块判定：Processor Arch
> 考什么：ret 处理时各流水级 stall/bubble 设置

(4) 检测到需要处理的 ret 指令后，各流水级应该如何设置？在下表中填入 normal/stall/bubble。（每空 1 分）

| F | D | E | M | W |
| --- | --- | --- | --- | --- |
| stall |  |  |  | normal |

---

### 2022期末-无答案 · 第二题 (5)

> 出处：`原文/期末/2022期末-无答案.md` 第 157–157 行　·　模块判定：Processor Arch
> 考什么：ret 指令插入的 bubble 周期数

(5) 执行 ret 指令时，其会插入______个周期的 bubble。（1 分）

---

### 2022期末-无答案 · 第二题 (6)

> 出处：`原文/期末/2022期末-无答案.md` 第 159–161 行　·　模块判定：Processor Arch
> 考什么：load-use 与 ret 需同时处理的场景分析

(6) 什么场景下，上面提到的 load-use 和 ret 需要处理的情况会同时出现？（2 分）

________________________________________________________________________________

---

### 2022期末-答案 · 第一题 1

> 出处：`原文/期末/2022期末-答案.md` 第 10–10 行　·　模块判定：Processor Arch
> 考什么：RISC/CISC 指令集设计

1、RISC CISC

---

### 2022期末-答案 · 第一题 2

> 出处：`原文/期末/2022期末-答案.md` 第 11–11 行　·　模块判定：Processor Arch
> 考什么：存疑：仅给出答案 10，考点不明

2、10

---

### 2022期末-答案 · 第二题

> 出处：`原文/期末/2022期末-答案.md` 第 25–31 行　·　模块判定：Processor Arch
> 考什么：流水线 stall/bubble 与流水线寄存器

第二题 处理器
(1)   E_icode     d_srcA      d_srcB
(2)   stall           bubble      normal
(3)   D_icode    E_icode     M_icode
(4)   bubble       normal      normal
(5)   3
(6)   前一条指令从内存中加载数据到寄存器 rsp 中，后面紧跟了一条 ret 指令

---

### 2024期末-带答案 · 第一题 2

> 出处：`原文/期末/2024期末-带答案.md` 第 101–120 行　·　模块判定：Processor Arch
> 考什么：RISC/CISC、流水线转发优先级与异常

2. 下列关于处理器体系结构的说法，正确的是：
A. RISC的设计理念是精简指令，为了减少指令的数量，它使用的指令长度可变。
B. 在设计处理器时，硬件上复制逻辑块的成本要比软件中复制代码的成本低得多，
而且在硬件系统中处理各种特殊情况也比用软件处理简单。
C. 在处理器的流水线中，异常指令在到达写回阶段之前，不用让异常事件影响流
水线中的指令流，只需要禁止后面的指令更新条件码和修改内存等产生永久影响的
操作即可。
D. 在处理器的流水线中，在译码阶段需要处理转发（Forwarding）。如果 有相 同
目标的多个转发源，赋予不同优先级是十分重要的，来自越靠后流水线阶段的转发
源的优先级越高。
答案：C。
A. CISC使用可变长度指令，RISC使用的是固定长度的指令。
B. 我们希望复用各类算术/逻辑单元恰恰是因为硬件上复制逻辑块的成本更大。
3

<!-- ===== page 4 ===== -->

可参见中文版课本P265。
C. 正确，参见中文版课本P308。
D. 应该是越靠前流水线阶段的转发源的优先级越高。

---

### 2024期末-带答案 · 第一题 3

> 出处：`原文/期末/2024期末-带答案.md` 第 121–129 行　·　模块判定：Processor Arch
> 考什么：组合逻辑延迟与流水线寄存器插位/吞吐率

3. 如下图所示，现有4个组合逻辑单元①~④和一个寄存器REG0，对应的延迟
已在图中标出。现在需要插入2个额外的流水线寄存器REG1和REG2（延迟均
为20ps），则 改造 后 流水线 的 最 量大为吞_吐____GIPS。
  30ps  40ps  20ps  45ps  20ps
①   ②  ③  ④  REG0
A. 16.7             B. 12.5              C. 10             D. 8.33
答案：B。
2个流水线寄存器应分别插在①②之间和③④之间，最终最长的一级延迟为
40ps+20ps+20ps=80ps，故最大吞吐率为1000/80=12.5(GIPS)

---

### 2024期末-带答案 · 第一题 14

> 出处：`原文/期末/2024期末-带答案.md` 第 345–361 行　·　模块判定：Processor Arch
> 考什么：摩尔定律/登纳德缩放与多核趋势（存疑）

14. 下列关于摩尔定律的描述，不正确的是：
A. 摩尔定律预测了芯片上晶体管数量的增长趋势，这种增长在一定程度上推动芯
片厂商尝试采用3D堆叠技术实现单位面积晶体管数量的增加。
B. 摩尔定律所描述的晶体管数量增长与芯片成本降低的关系，促使半导体产业不
断追求技术进步以获取更高利润。
C. 登纳德缩放（Dennard Scaling）定律的失效对摩尔定律产生了负面影响，
使得芯片性能无法提升。
D. 尽管面临诸多挑战，摩尔定律在过去几十年间仍然是半导体产业发展的重要指
导原则，并推动了消费电子产品的创新和普及。
10

<!-- ===== page 11 ===== -->

参考答案
C． Dennard缩放定律的失效以及由此导致的无法显著提高时钟频率，导致大多
数 CPU 制造商将重点放在处理器核心数量增长上，并将其作为提高芯片整体性能
的重要方法。

---

### 2024期末-带答案 · 第二题

> 出处：`原文/期末/2024期末-带答案.md` 第 375–438 行　·　模块判定：Processor Arch
> 考什么：Y86-64 SEQ/PIPE 新增 cdeclXX 与周期数

第二题（15分）
请结合教材第四章“处理器体系结构”的有关知识回答问题。
1） 现在Y86-64 ISA中加入一条新指令：cdeclXX，条件减一。其功能和用法
为，如果条件码满足条件（同cmovXX系列指令），则将寄存器数据减1。cdeclXX
编码如下：
C  Fn  0xF  rB
4位  4位  4位  4位
考虑教材中的SEQ处理器，进行必要的改动使得cdeclXX指令能够根据之前指令
产生的条件码执行操作，并根据计算结果正常设置条件码。请填写下表中缺失的4
条操作，每空只包含一条操作（或其一部分）。（每空2分，共8分）
Stage  cdecl rB
Fetch  icode:ifun ← M1[PC]
rA:rB ← ①_______
②____________
Decode  valB ← R[rB]
Execute  ③____________
Cnd ← Cond(CC, ifun)
Memory  none
Write back  ④____________
PC Update  PC ← valP
2） 考虑教材中的PIPE处理器，部分如下图所示。在取指阶段，PC选择逻辑从
三个程序计数器源中进行选择。请根据PIPE 处理器的实现，补全下面的HCL 代
码。（每空1分，共3分）
12

<!-- ===== page 13 ===== -->

word f_pc = [
M_icode ==IJXX && ①         : ②        ;
W_icode == IRET : ③        ;
1 : F_predPC
]
3） 在教材中的PIPE处理器增加cdeclXX指令，分支预测的策略为“总是跳转”。
考虑如下代码片段，回答以下问题。
# long bar(long x)
# x in %rdi
bar:
    xorq    %rax, %rax
    irmovq  $1, %rsi
    rrmovq  %rsi, %r9
Lo:
13

<!-- ===== page 14 ===== -->

    xorq    %r9, %rsi
    cdecle  %rdi
    addq    %rdi, %rax
    andq    %rdi, %rdi
jne     Lo
    ret
周期数计算从执行bar第一条指令开始，直到其返回指令ret完全通过流水线为
止。在调用bar之前，处理器已经执行过足够多的nop指令。
当函数bar的参数 x=0 时，需要执行______个周期；x=3 时需要执行______
个周期。（每空2分，共4分）
参考答案
1）① M1[PC + 1]
② valP ← PC + 2
③ valE ← (-1) + valB（写valB + (-1)亦可，但valB – 1扣1分）
④ if(Cnd) R[rB] ← valE
2）① ！M_Cnd
② M_valA
③ W_valM
3) 15; 35

---

### 2025期末-带答案 · 一 8

> 出处：`原文/期末/2025期末-带答案.md` 第 53–57 行　·　模块判定：Processor Arch
> 考什么：Y86-64 指令编码 regids 与 valC 字段

8. 在 Y86-64 指令集中，下列哪些指令在指令字节序列中同时包含 regids 字节与
valC 常量字段？
答案：AB
解析：irmovq/rmmovq/mrmovq 需要寄存器说明（regids）且需要常量/位移（valC）。
call/jXX 只有 valC；OPq 只有 regids；ret 两者都不需要。

---

### 2025期末-带答案 · 一 9

> 出处：`原文/期末/2025期末-带答案.md` 第 58–62 行　·　模块判定：Processor Arch
> 考什么：ret 在 PIPE 中的控制冒险与 bubble

9. 关于 ret 在 PIPE 中引发的控制冒险，下列说法哪些正确？
答案：ABDE
解析：ret 的返回地址要等到读内存后才知道；因此常见做法是暂停取指并用 bubble 填
充前端，直到返回地址可用，再用 W_valM 改道 PC。它不是普通的寄存器 RAW 冒险，
不能靠 forwarding“提前变出”目标 PC。

---

### 2025期末-无答案 · 一 8

> 出处：`原文/期末/2025期末-无答案.md` 第 144–150 行　·　模块判定：Processor Arch
> 考什么：Y86-64 指令编码 regids 与 valC 字段

8. 在 Y86-64 指令集中，下列哪些指令在指令字节序列中同时包含 regids 字节与
valC 常量字段？
A. irmovq V, rB
B. rmmovq rA, D(rB)
C. call Dest
D. OPq rA, rB
E. ret

---

### 2025期末-无答案 · 一 9

> 出处：`原文/期末/2025期末-无答案.md` 第 151–157 行　·　模块判定：Processor Arch
> 考什么：ret 在 PIPE 中的控制冒险与 bubble

9. 关于 ret 在 PIPE 中引发的控制冒险，下列说法哪些正确？
A. ret的目标PC来自从栈中读出的返回地址，取指阶段无法提前知道
B. 只要流水线中存在 ret（如在 D/E/M 任一阶段），常见策略是设置F_stall=1 避免
取错指令
C. ret带来的控制冒险，可完全靠 forwarding 解决，不需要 stall
D. 为了让流水线“继续流动”但不引入错误指令，常见做法是在D 阶段注入 bubble
E. 当 ret 终于在 W 阶段得到 W_valM 后，PC 选择逻辑可用它作为下一条取指地址

---

### 期末往年题勘误、详解 by Arthals · 2015 第三题 第4问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 19–21 行　·　模块判定：Processor Arch
> 考什么：AB 之间也需插入流水线寄存器

### 第三题

第 4 问，应该在 AB 之间也插入一个寄存器。

---

### 期末往年题勘误、详解 by Arthals · 2018 第二题

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 99–101 行　·　模块判定：Processor Arch
> 考什么：流水线寄存器插入 CD,FG

### 第二题

明显答案错了，少了 CD,FG 两个插入，这种题的普遍做法是，找到一条边最少的，逐次枚举，一个技巧是任何一条通路上的寄存器数量是相同的。

---

### 2025第2次阶段测验-带答案 · 第9讲 1

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 54–61 行　·　模块判定：Processor Arch
> 考什么：不定项：哪些描述属于 ISA 规定的内容

1. （不定项选择，2分）以下描述，哪些属于ISA规定的内容：ABCFG
A. 有15个通用寄存器，每个寄存器64位
B. 有3个条件码，分别是ZF、SF、OF
C. 过程调用指令（call）会将下一条指令地址压入栈中
D. 过程调用的前2个参数放在寄存器rdi、rsi
E. 过程调用返回值放在寄存器rax
F. 内存是字节寻址的，字节序采用小端法
G. 访存指令支持寄存器加偏移的寻址模式

---

### 2025第2次阶段测验-带答案 · 第9讲 2

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 62–67 行　·　模块判定：Processor Arch
> 考什么：Y86-64 mrmovq 为何不写成 D(rA),rB（指令编码设计）

2. （2分）Y86-64中的这两条指令：
rmmovq rA,D(rB)
mrmovq D(rB),rA
第2条指令为什么不设计成mrmovq D(rA),rB？这样都是rA在前rB在后，看起来
更加规整。
答：硬件电路上都通过rB的通路计算出地址，电路更为简单

---

### 2025第2次阶段测验-带答案 · 第9讲 3

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 68–76 行　·　模块判定：Processor Arch
> 考什么：由 HCL 布尔表达式补全组合逻辑电路图

3. （各3分，共6分）根据HCL表达式补全电路图
(1)bool eq = (a&&b)||(!a&&!b)
2

<!-- ===== page 3 ===== -->

答案：
(2)bool out = (s&&a)||(!s&&b)
答案：

---

### 2025第2次阶段测验-带答案 · 第9讲 4

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 77–79 行　·　模块判定：Processor Arch
> 考什么：根据电路图补全时序图中 Out 信号值

4. （2分）根据下面左边电路图，补全右边时序图里Out信号的值（In/Out均用10进
制表示）
答案：1 4 9 7 16 27

---

### 2025第2次阶段测验-带答案 · 第10讲 5

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 81–95 行　·　模块判定：Processor Arch
> 考什么：Y86-64 popq 指令编码格式与操作步骤补全

5. （8分）Y86-64的popq指令编码格式如下：
3

![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img1.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img2.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img3.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img4.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img5.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img6.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p3-img7.jpg)

<!-- ===== page 4 ===== -->

根据popq指令的操作，补全下表（共需填8行9空）
答案：

---

### 2025第2次阶段测验-带答案 · 第10讲 6

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 96–113 行　·　模块判定：Processor Arch
> 考什么：SEQ 中 aluA 信号生成逻辑的 HCL 补全

6. （8分）以下是SEQ处理器中ALU的A口输入端信号（aluA）生成逻辑的分析，只列
出了部分指令。根据各指令功能，并参考下面已经给出的信息，补全空缺（表格中2
空，HCL代码中6空）。
4

![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p4-img1.jpg)
![图](../../assets/阶段测验/2025第2次阶段测验-带答案/p4-img2.jpg)

<!-- ===== page 5 ===== -->

int aluA = [
icode in { IRRMOVQ, IOPQ } : valA;
icode in { IIRMOVQ, IRMMOVQ, IMRMOVQ } : valC;
icode in { ICALL, IPUSHQ } : -8;
icode in { IRET, IPOPQ } : 8;
# Other instructions don't need ALU
];
答案：

---

### 2025第2次阶段测验-带答案 · 第11讲 7

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 122–125 行　·　模块判定：Processor Arch
> 考什么：三级流水线的延迟与吞吐（细分流水级计算）

7. （4分）如下图所示的三级流水线结构，单条指令的延迟（delay）是 340 ps，
流水线满负荷运转时，每 180 ps完成一条指令。如果能理想化地进一步细分流水
级（不跨现有流水级重排电路、也不过度细分），恰好划分成均衡流水线，那单条指令
的延迟（delay）是 420 ps，流水线满负荷运转时，每 60 ps完成一条指令。

---

### 2025第2次阶段测验-带答案 · 第11讲 8

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 126–133 行　·　模块判定：Processor Arch
> 考什么：PIPE 上 addq 的数据冒险检测与数据前递

8. （6分）阅读下面这段Y86-64汇编代码
1 irmovq $1,%rax
2 irmovq $2,%rax
3 irmovq $3,%rdx
4 addq %rax,%rdx
当这段代码在PIPE处理器上运行时，当addq指令在流水级D/Decode/译码（任一
都对）阶段时，会检测到数据冒险。此时运用了数据前递技术，其中在流水级 M 阶
段的指令前递数据 2 作为操作数%rax的值。

---

### 2025第2次阶段测验-带答案 · 第11讲 9

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 134–143 行　·　模块判定：Processor Arch
> 考什么：写 Load-use 相关代码并说明前递能否解决

9. （4分）写出一段存在Load-use相关的Y86-64汇编代码（要求代码简洁明了），
并说明能否用数据前递技术解决，为什么？
答：代码示例如下（2分）：
mrmovq 0(%rdx),%rax
addq %rbx,%rax
注意：代码不用一模一样，关键点是前一条指令读内存到某个寄存器（这里是rax)，后一条指令要
读取这个寄存器
“Load-use”不能用数据前递技术解决，因为上面的add指令在译码阶段就要“use”，
这时前一条指令还在执行阶段，还有一个周期才能到访存阶段进行“load”。（2分）
注意：如果回答用数据前递技术可以部分解决，也算对。

---

### 2025第2次阶段测验-带答案 · 第11讲 10

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 144–149 行　·　模块判定：Processor Arch
> 考什么：写 Load-use 与 ret 组合的 Y86-64 代码

10.（2分）写出一段存在Load-use相关和ret组合的Y86-64汇编代码（要求代码简
洁明了）。
答：代码示例如下（2分）：
mrmovq 0(%rdx),%rsp
ret
注意：代码不用一模一样，关键点是前一条指令读内存到rsp寄存器，后一条指令是ret

---

### 2025Lab测验-无答案 · Lab 任务 26

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 569–596 行　·　模块判定：Processor Arch
> 考什么：SEQ 中新增 iopq 指令需改动的 HCL 位置

26. （2分）在ArchLab Part B中，我们需要在SEQ架构的基础上实现iopq指令。该
指令的定义如下：iopq V, rB：计算rB op V，并将结果存入寄存器rB。下面是
SEQ架构中的部分HCL-rs定义，其中哪些位置需要添加IOPQ？
A. (1)(2)(3)
B. (1)(3)(5)
C. (2)(3)(5)
D. (2)(4)(5)
u8 srcA = [
    icode in { CMOVX, RMMOVQ, OPQ, PUSHQ  } : ialign.rA;  // (1)
    icode in { POPQ, RET } : RSP;
    true : RNONE;
];
u8 dstE = [
    icode in { CMOVX } && cnd : ialign.rB;
    icode in { IRMOVQ, OPQ } : ialign.rB;                   // (2)
    icode in { PUSHQ, POPQ, CALL, RET } : RSP;
    true : RNONE;
];
u64 aluA = [
    icode in { CMOVX, OPQ } : reg_read.valA;               // (3)
    icode in { IRMOVQ, RMMOVQ, MRMOVQ } : ialign.valC;   // (4)
    icode in { CALL, PUSHQ } : NEG_8;
    icode in { RET, POPQ } : 8;
];
u8 alufun = [
    icode == OPQ : ifun;                                        // (5)
    true : ADD;
];

---

### 2025Lab测验-无答案 · Lab 任务 27

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 601–606 行　·　模块判定：Processor Arch
> 考什么：SEQ 到 pipe_std 五级流水线演进与冒险

27. （2分）在ArchLab Part B中，我们将架构从SEQ一步步改进到pipe_std这个
标准的五级流水线架构。下列说法中错误的一项是？
A. 随着架构的一步步改进，关键路径的长度逐渐变短，时钟频率可以逐渐提高
B. 从pipe_s2演化到pipe_s3a的过程中引入了数据冒险，可通过增加寄存器解决
C. pipe_s4a将架构中的执行阶段分离出来，使内存访问和ALU计算可以并行执行
D. 标准的五级流水线pipe_std具有分支预测，可能发生分支预测错误

---

### 2025Lab测验-无答案 · Lab 任务 28

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 607–625 行　·　模块判定：Processor Arch
> 考什么：ncopy.ys 两段循环代码的流水线性能对比

28. （2分）ArchLab Part C 中，我们需要优化ncopy.ys代码。下面两个代码片段
截取自某两个同学的ncopy.ys，它们均使用标准的五级流水线架构。下列关于这两段
代码性能的说法，正确的一项是？
A. 代码S性能更优，因为将访问内存的指令集中在了一起，可以有效增加缓存命中率
B. 代码S性能更优，因为将功能相似的指令如iaddq集中在一起，便于流水线优化
C. 代码T性能更优，因为将部分公共指令提前执行，使每个循环中平均指令数量变少
D. 代码T性能更优，因为将iaddq指令插入到了前面，避免了加载/使用冒险的发生
代码S  代码T
Loop:  Loop:
    mrmovq (%rdi), %r10      mrmovq (%rdi), %r10
    rmmovq %r10, (%rsi)      iaddq $8, %rdi
    andq %r10, %r10      rmmovq %r10, (%rsi)
    jle Skip      iaddq $8, %rsi
    iaddq $1, %rax      andq %r10, %r10
Skip:      jle Skip
    iaddq $8, %rdi      iaddq $1, %rax
    iaddq $8, %rsi  Skip:
    iaddq $-1, %rdx      iaddq $-1, %rdx
    jg Loop      jg Loop

---

### 2025Lab测验-无答案 · Lab 任务 29

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 626–631 行　·　模块判定：Processor Arch
> 考什么：评分 c=cpe+2*ac 下代码与架构的优化权衡

29. （2分）在ArchLab Part C中，我们需要同时优化代码ncopy.ys和架构ncopy.rs，
评分标准基于c=cpe+2*ac。关于这一部分的优化策略，下列说法中正确的一项是？
A. 应该优先优化cpe，因为ac的权重不大，且cpe不依赖于架构的设计
B. 应该优先优化ac，因为这样可以提高时钟频率，降低执行与调试的时间
C. cpe和ac相互独立，优化cpe不会影响ac，优化ac也不会影响cpe
D. 在ncopy.rs中添加更多的流水线阶段可以降低ac，但可能使cpe增加

---

### 2025Lab测验-无答案 · Lab 任务 30

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 636–656 行　·　模块判定：Processor Arch
> 考什么：pipe_std 关键路径/传播顺序与降低 ac 的优化

30. （2分）在 ArchLab Part C中，某同学准备在标准的五级流水线架构pipe_std
的基础上进一步优化。该同学输入命令./target/debug/ysim --arch pipe_std
-I，得到了下面的结果。该同学进行下列哪一项优化，可以在降低ac的同时，不使cpe
显著增加？
A. 在架构中增加iopq指令，提高部分指令的执行效率
B. 在架构中缩短e_cnd, d_bubble等信号的路径长度
C. 在架构中执行和访存阶段中间增加“设置条件码”阶段
D. 在架构中将设置条件码从执行阶段改到访存阶段进行
propagate order:
lv.1: w_stall m_icode d_dstM m_dstM prog_stat mem_write d_srcB e_dstM
m_stall m_valE d_dstE w_dstM e_ifun e_stat e_icode d_stat f_pc aluB
mem_read e_valA m_dstE alufun w_bubble d_icode w_valE e_stall aluA
mem_data f_bubble d_srcA mem_addr d_valC d_ifun w_dstE w_valM prog_term
d_stall f_stall
lv.2: imem alu dmem reg_file f_align f_icode f_ifun e_valE m_valM
m_stat  d_rvalA  d_rvalB  instr_valid  need_regids  need_valC  m_bubble
set_cc f_stat
lv.3: ialign pc_inc reg_cc f_rA f_rB f_valC f_valP cc f_pred_pc
lv.4: cond e_cnd d_bubble e_bubble e_dstE d_valA d_valB
dependency  graph  visualization  is  generated  at:
pipe_std_dependency_graph.html

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
