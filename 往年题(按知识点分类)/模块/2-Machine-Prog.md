# 程序的机器级表示

> **英文模块名**：`Machine Prog`  

> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，
> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。

## 一、清单

共 156 道题，来自 31 份材料。

| 年份 | 试卷 | 类别 | 题号 | 考什么 |
|---|---|---|---|---|
| 2012 | 2012期中-带答案 | 期中 | Problem A 5 | 函数返回值放在 %eax 的调用约定 |
| 2012 | 2012期中-带答案 | 期中 | Problem A 6 | x86-64 中 double/寄存器/指针宽度判断题 |
| 2012 | 2012期中-带答案 | 期中 | Problem A 9 | mov 与 lea 的语义区别（访存 vs 算地址） |
| 2012 | 2012期中-带答案 | 期中 | Problem A 11 | pushq 后 %rsp 的取值（栈向低地址增长） |
| 2012 | 2012期中-带答案 | 期中 | Problem A 12 | C 语句 a[n] 对应的比例变址寻址汇编 |
| 2012 | 2012期中-带答案 | 期中 | Problem A 13 | mov 0x10(%rax,%rcx,4),%rdx 的 C 等价形式 |
| 2012 | 2012期中-带答案 | 期中 | Problem C 1 | 由汇编反推 C 代码：选择排序（含汇编清单与填空模板） |
| 2012 | 2012期中-带答案 | 期中 | Problem C 2 a) | lea (%rax,%r8,1),%ecx 对应的 C 表达式 |
| 2012 | 2012期中-带答案 | 期中 | Problem C 2 b) | mov (%rdi,%rax,4),%eax 对应的 C 表达式 |
| 2012 | 2012期中-带答案 | 期中 | Problem C 2 c) | 本题代码中为何没有 leave 指令 |
| 2012 | 2012期中-带答案 | 期中 | Problem D A | IA32 栈帧、递归调用参数与 leave 前栈内容推算 |
| 2012 | 2012期中-带答案 | 期中 | Problem D B | ret 前 %esp 与 %ebp 的取值 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 4 | gdb 断点与运行命令（Bomb Lab） |
| 2013 | 2013期中-带答案 | 期中 | 选择题 5 | lea 乘法指令识别（n*10） |
| 2013 | 2013期中-带答案 | 期中 | 选择题 7 | x86 寻址方式与指令合法性 |
| 2013 | 2013期中-带答案 | 期中 | 选择题 8 | leal 用途、传参、寄存器保存与条件码 |
| 2013 | 2013期中-带答案 | 期中 | 第三题 1) | 64 位机器 long 的位数（int_sqrt 题干代码） |
| 2013 | 2013期中-带答案 | 期中 | 第三题 2) | 反汇编填空：int_sqrt 整数平方根（含答案） |
| 2013 | 2013期中-带答案 | 期中 | 第四题 | 结构体 sizeof 与递归函数汇编/运行结果 |
| 2013 | 2013期中-带答案 | 期中 | 第七题 1) | 由汇编还原 transform 的 C 代码 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 4 | 只改条件码不改寄存器的指令 CMP/TEST |
| 2014 | 2014期中-带答案 | 期中 | 第一题 5 | x86 各寻址方式写法的正确性 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 7 | 缓冲区溢出的防护做法正误 |
| 2014 | 2014期中-带答案 | 期中 | 第一题 8 | switch 跳转表的 jmp 汇编写法与比例因子 |
| 2014 | 2014期中-带答案 | 期中 | 第四题 1） | x86-64 递归函数汇编，据 gdb 反汇编补全 C 代码 |
| 2014 | 2014期中-带答案 | 期中 | 第四题 2） | 补全缺失的两条汇编指令并判断栈寄存器 |
| 2014 | 2014期中-带答案 | 期中 | 第四题 3） | 递归调用 retq 处栈帧内容填写 |
| 2014 | 2014期中-带答案 | 期中 | 第五题 | 由 IA32 汇编补全 C 代码缺失部分并说明功能 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 6 | x86 寻址模式正确性 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 8 | 跳转表汇编与标号取值范围 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 9 | leal/传参/条件码等汇编细节 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 选择题 10 | CMP/TEST 与条件码 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第三题 2 | 由汇编补全结构体成员赋值语句 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第三题 3 | X86/Y86 汇编代码错误定位与更正 |
| 2015 | 2015期中-带答案（同 2015期末-20151109-带答案） | 期中 | 第三题 4 | 二维数组寻址与 lea 偏移（求 A、B，含本大题答案） |
| 2016 | 2016期中-带答案 | 期中 | 第一题 1 | 会改变条件码 CF 的指令辨析 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 2 | CMP 指令不区分有无符号 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 3 | je 相对跳转目标地址计算 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 4 | C 条件表达式对应的条件转移条数 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 5 | 寄存器清零指令辨析 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 6 | switch 跳转表与未出现的标号 |
| 2016 | 2016期中-带答案 | 期中 | 第一题 7 | lea 求数组元素地址 |
| 2016 | 2016期中-带答案 | 期中 | 第三题 (1) | switch 跳转表与 gdb 内存检查输出 |
| 2016 | 2016期中-带答案 | 期中 | 第三题 (1) 答案 | gdb x/6g 输出参考答案 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 4 | x86-64 指令书写错误辨析 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 5 | 条件传送指令的语义与限制 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 6 | 函数指针的过程调用指令 |
| 2017 | 2017期中-带答案 | 期中 | 第一题 7 | 二维数组指针运算与地址计算 |
| 2017 | 2017期中-带答案 | 期中 | 第三题 | 缓冲区溢出程序的汇编缺失代码补全 |
| 2018 | 2018期中-带答案 | 期中 | 第一题 4 | movl/cltq/movabsq/movswq 语义 |
| 2018 | 2018期中-带答案 | 期中 | 第一题 7 | 控制结构的机器码实现（jmp/cmov/跳转表） |
| 2018 | 2018期中-带答案 | 期中 | 第一题 8 | 条件码的读写与改变 |
| 2018 | 2018期中-带答案 | 期中 | 第三题 2、3 | 结构体访问汇编填空与汇编反推 C 代码 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 4 | x86-64 指令 idivq/jmp/shr/leaq 辨析 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 5 | call 后栈上第 k 个参数的地址 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 6 | cmpq 后 jg 跳转的条件码表达式 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 7 | 函数指针数组的 sizeof |
| 2019 | 2019期中-带答案 | 期中 | 第一题 8 | 栈帧定长、编译时确定大小 |
| 2019 | 2019期中-带答案 | 期中 | 第一题 9 | pushq %rbp 的等价指令序列 |
| 2019 | 2019期中-带答案 | 期中 | 第三题 | C 与 x86-64 汇编填空：栈帧、strcpy、结构体 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 1 | 二维数组元素访问的寻址方式 addl |
| 2020 | 2020期中-带答案 | 期中 | 第一题 2 | 条件码与 set/cmp/test/leaq 指令 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 3 | 静态数组与指针数组的地址计算 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 4 | x86-64 过程调用与栈帧释放 |
| 2020 | 2020期中-带答案 | 期中 | 第一题 5 | 结构体成员偏移与 movl/leaq 选择 |
| 2020 | 2020期中-带答案 | 期中 | 第三题 1 | C 与 x86-64 汇编填空：递归、参数传递 |
| 2020 | 2020期中-带答案 | 期中 | 第三题 2 | 断点处栈帧地址与存储值的推断 |
| 2020 | 2020期中-带答案 | 期中 | 第三题 3 | 递归函数 foo 的功能 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 5 | 栈的增长方向、参数对齐与金丝雀 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 6 | movabsq/INC/popq/call 指令语义辨析 |
| 2021 | 2021期中-带答案 | 期中 | 第一题 7 | 由 leaq/addq 汇编反推二维数组维数 |
| 2021 | 2021期中-带答案 | 期中 | 第三题 1 | C 与 x86-64 汇编填空：递归、除法与移位 |
| 2021 | 2021期中-带答案 | 期中 | 第三题 2 | 断点处栈内容与栈帧布局 |
| 2021 | 2021期中-带答案 | 期中 | 第三题 3 | 递归函数 f(7,6) 的返回值 |
| 2021 | 2021期中-带答案 | 期中 | 第六题 1 | struct/union 的大小与末尾 padding |
| 2021 | 2021期中-带答案 | 期中 | 第六题 2 | 链表求和函数的功能 |
| 2021 | 2021期中-带答案 | 期中 | 第六题 3 | 补全链表遍历汇编，含结构体对齐 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 6 | mov指令操作数大小与合法寻址方式 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 7 | 由lea指令序列反推C表达式 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 8 | cmp/set指令后缀与data_t类型匹配 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 9 | 结构体对齐填充与总大小计算 |
| 2022 | 2022期中-带答案 | 期中 | 第一题 10 | 缓冲区溢出攻击的防护手段 |
| 2022 | 2022期中-带答案 | 期中 | 第三题 | switch跳转表汇编还原C代码与结构体 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 4 | x86-64 mov指令操作数与寄存器的合法组合 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 5 | 数组寻址lea指令与下标反推 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 6 | cmp/test/set与条件传送指令语义 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 7 | call指令将返回地址压栈 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 8 | struct/union对齐与成员偏移 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 9 | 指针数组声明的sizeof计算 |
| 2023 | 2023期中-带答案 | 期中 | 第一题 12 | 栈帧布局与缓冲区溢出对局部变量的影响 |
| 2023 | 2023期中-带答案 | 期中 | 第三题 | 递归函数ncr的C与汇编代码补全 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 4 | 结构体对齐与指针数组声明的sizeof/指针差 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 5 | x86-64栈结构与参数构造区 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 6 | 缓冲区溢出防护与金丝雀值检测 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 7 | 结构体参数与返回值经栈/寄存器传递 |
| 2024 | 2024期中-带答案 | 期中 | 第一题 8 | 条件传送cmove与分支实现对比 |
| 2024 | 2024期中-带答案 | 期中 | 第三题 | 递归函数foo的C与汇编代码补全 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 2 | x86-64 callq 后第一个参数的位置 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 3 | 用 leal 计算 5x+7 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 3 | 由汇编 lea/cmov 反推 C 表达式 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 4 | 结构体数据对齐与 sizeof 比较 |
| 2014 | 2014期末-带答案 | 期末 | 第二题 2 | 反汇编填空（movzbl/shl/push/pop 等） |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 1 | 哪条指令不改变 esp |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 3 | x86 寻址方式合法性 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第二题 | 由汇编/输出结果补全 C 代码与汇编填空 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 3 | 缓冲区溢出的常见防御手段辨析 |
| 2016 | 2016期末-带答案 | 期末 | 第二题 | 32 位汇编反推 C 函数并计算返回值 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 1 | gdb 单步进入被调函数（si/ni） |
| 2017 | 2017期末-无答案 | 期末 | 第一题 3 | 指令长度、test 与 cmp 等价、跳转表 |
| 2017 | 2017期末-无答案 | 期末 | 第二题 1 | 结构体偏移与浮点汇编代码填空 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 2 | 结构体对齐填充与汇编寻址偏移 |
| 2018 | 2018期末-带答案 | 期末 | 第七题 1 | i++ 对应的 x86-64 汇编代码 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 1 | 栈帧与帧指针（可变栈帧） |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 6 | 指令长度与基址加偏移寻址 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 11 | 存疑：仅注“书上原话”，考点不明 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 12 | 存疑：仅注“直接模拟”，考点不明 |
| 2019 | 2019期末-无答案 | 期末 | 第二题 (1) | 由汇编循环推断 C 代码循环次数（含共用汇编段） |
| 2020 | 2020期末-无答案 | 期末 | 第一题 1 | x86-64/Y86 汇编、栈帧与跳转表 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 2 | 合法的 x86-64 汇编指令与寻址方式 |
| 2021 | chap 2-6 解析 | 期末 | 第一题 3 | 判断合法 x86-64 指令：立即数目标、双内存操作、比例因子 |
| 2021 | chap 2-6 解析 | 期末 | 第一题 4 | 由栈帧中保存的 %rbp 读取调用者的返回地址 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 1 | ISA 两大类 RISC/CISC 的指令数与寻址方式对比 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 3 | x86-64/Linux 传参前两个寄存器 |
| 2022 | 2022期末-答案 | 期末 | 第一题 3 | rdi/rsi 参数传递寄存器 |
| 2025 | 2025期末-带答案 | 期末 | 一 5 | addl 结果、写 %eax 清零高位与标志位 |
| 2025 | 2025期末-带答案 | 期末 | 一 6 | 栈帧布局、%rsp 对齐与 leave 语义 |
| 2025 | 2025期末-带答案 | 期末 | 一 7 | 8 个 long 参数的寄存器/栈传递与 ABI |
| 2025 | 2025期末-无答案 | 期末 | 一 5 | addl 执行结果与 CF/ZF/OF 标志 |
| 2025 | 2025期末-无答案 | 期末 | 一 6 | 栈帧布局、%rsp 对齐与 leave 语义 |
| 2025 | 2025期末-无答案 | 期末 | 一 7 | 8 个 long 参数的寄存器/栈传递与 ABI |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2016 第一题 第13问 | 存疑：仅注“所有符号都对应 bit 数” |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第4讲 7 | 通用寄存器低 32 位/最低字节的名称 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第4讲 8 | swap 汇编中寄存器与内存访问次数统计 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第4讲 9 | 比例变址寻址方式地址计算 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第5讲 10 | cmp/test 与 sub/and 的等价关系 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第5讲 11 | cmp+set 指令补全汇编，movzbl 功能与高位清零 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第5讲 12 | absdiff 分支实现与条件传送 cmov 实现对比 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第5讲 13 | loopy 循环汇编补全对应 C 代码 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第5讲 14 | 跳转表 jmp *.L1(,%rdi,8) 的目标计算 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第6讲 15 | popq 指令各步骤与 %rsp 变化 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第6讲 16 | 过程调用栈帧、callq/ret、参数寄存器与被调用者保存 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第6讲 17 | 取地址与解引用，变量存放于寄存器还是内存 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第7讲 18 | 二维数组 arr_data[x][y] 寻址补全汇编 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第7讲 19 | 变长二维数组 var_ele 的参数传递与寻址 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第7讲 20 | 汇编代码输出结果（原文 OCR 列错行，内容难辨） |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第7讲 21 | 数组循环 C 代码与汇编，求常量 A、B（OCR 错行） |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第7讲 22 | 浮点参数经 xmm 寄存器传递的汇编分析 |
| 2025 | 2025第1次阶段测验-带答案 | 阶段测验 | 第8讲 24 | 缓冲区溢出攻击防御方法对比（兼 VM 保护机制） |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 17 | GDB 常用命令（break/info registers/ni/si/p）辨误 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 18 | BombLab phase_1 反汇编分析 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 19 | BombLab phase_2 反汇编（数列递推）分析 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 20 | BombLab phase_3 跳转表与断点处寄存器分析 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 22 | 缓冲区溢出漏洞、ASLR、金丝雀与 ROP 说法判断 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 23 | gdb 调试 ctarget 的命令用法 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 24 | getbuf 函数栈帧大小计算 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 25 | AttackLab phase3 栈布局与 ROP 题解判断 |

## 二、题目原文

### 2012期中-带答案 · Problem A 5

> 出处：`原文/期中/2012期中-带答案.md` 第 54–58 行　·　模块判定：Machine Prog
> 考什么：函数返回值放在 %eax 的调用约定

5. How does x86 assembly store the return value when a function is finished? **(f-f10 1-4)**　**答案：B**
   a) The ret instruction stores it in a special retval register.
   b) By convention, it is always in %eax.
   c) It is stored on the stack just above the (%ebp) of the callee.
   d) It is stored on the stack just above all the arguments to the function

---

### 2012期中-带答案 · Problem A 6

> 出处：`原文/期中/2012期中-带答案.md` 第 60–67 行　·　模块判定：Machine Prog
> 考什么：x86-64 中 double/寄存器/指针宽度判断题

6. Which of the following is FALSE concerning x86-64 architecture? **(f-f10 1-9)**　**答案：D**
   a) A double is 64 bits long.
   b) Registers are 64 bits long.

<!-- ===== page 02 ===== -->

   c) Pointers are 64 bits long.
   d) Pointers point to locations in memory that are multiples of 64 bits apart.

---

### 2012期中-带答案 · Problem A 9

> 出处：`原文/期中/2012期中-带答案.md` 第 81–85 行　·　模块判定：Machine Prog
> 考什么：mov 与 lea 的语义区别（访存 vs 算地址）

9. What is the difference between the mov and lea instructions? **(m-f11 1-2)**　**答案：B**
   a) lea dereferences an address, while mov doesn’t.
   b) mov dereferences an address, while lea doesn’t.
   c) lea can be used to copy a register into another register, while mov cannot.
   d) mov can be used to copy a register into another register, while lea cannnot.

---

### 2012期中-带答案 · Problem A 11

> 出处：`原文/期中/2012期中-带答案.md` 第 94–99 行　·　模块判定：Machine Prog
> 考什么：pushq 后 %rsp 的取值（栈向低地址增长）

11. %rsp is 0xdeadbeefdead0d0. What is the value in %rsp after the following instruction executes?
    pushq %rbx **(m-s11 1-3)**　**答案：D**
   a) 0xdeadbeefdead0d4
   b) 0xdeadbeefdead0d8
   c) 0xdeadbeefdead0cc
   d) 0xdeadbeefdead0c8

---

### 2012期中-带答案 · Problem A 12

> 出处：`原文/期中/2012期中-带答案.md` 第 101–109 行　·　模块判定：Machine Prog
> 考什么：C 语句 a[n] 对应的比例变址寻址汇编

12. Consider an int *a and an int n. If the value of %ecx is a and the value of %edx is n, which of the
    following assembly snippets best corresponds to the C statement return a[n]? **(m-s11 1-1)**　**答案：C**
   a) ret (%ecx,%edx,4)
   b) leal (%ecx,%edx,4),%eax
      ret
   c) mov (%ecx,%edx,4),%eax
      ret
   d) mov (%ecx,%edx,1),%eax
      ret

---

### 2012期中-带答案 · Problem A 13

> 出处：`原文/期中/2012期中-带答案.md` 第 111–115 行　·　模块判定：Machine Prog
> 考什么：mov 0x10(%rax,%rcx,4),%rdx 的 C 等价形式

13. What is the C equivalent of mov 0x10 (%rax,%rcx,4), %rdx　**(2pts) (m-s11 1-8)**　**答案：C**
   a) rdx = rax + rcx + 4 + 10
   b) *(rax + rcx + 4 + 10) = rdx
   c) rdx = *(rax + rcx*4 + 0x10)
   d) rdx = *(rax + rcx + 4 + 0x10)

---

### 2012期中-带答案 · Problem C 1

> 出处：`原文/期中/2012期中-带答案.md` 第 255–359 行　·　模块判定：Machine Prog
> 考什么：由汇编反推 C 代码：选择排序（含汇编清单与填空模板）

1. The function below is hand-written assembly code for a sorting algorithm. Fill in the blanks
   on the next page by converting this assembly to C code　**(m-s09-4) (13pts)**

<!-- ===== page 06 ===== -->

![图](assets/期中/2012期中-带答案/page-06.png)

> 上图为本页内容（汇编代码清单 + 红色印刷的 C 语言参考代码）。

```asm
	.globl mystery_sort	# exports the symbol so other .c files
				# can call the function

mystery_sort:
	jmp	loop1_check

loop1:
	xor	%rdx, %rdx
	mov	%rsi, %rcx
	jmp	loop2_check

loop2:
	mov	(%rdi, %rcx, 8), %rax
	cmp	%rax, (%rdi, %rdx, 8)
	jg	loop2_check
	mov	%rcx, %rdx

loop2_check:
	dec	%rcx
	test	%rcx, %rcx
	jnz	loop2

	dec	%rsi
	mov	(%rdi, %rsi, 8), %rax
	mov	(%rdi, %rdx, 8), %rcx
	mov	%rcx, (%rdi, %rsi, 8)
	mov	%rax, (%rdi, %rdx, 8)

loop1_check:
	test	%rsi, %rsi
	jnz	loop1

	ret
```

**答案（原卷红色印刷）：**

```c
void mystery_sort (long* array, long len)
{
    long a, b, tmp;
    while(len>0)
    {
        a = 0;
        for(b=len-1; b>0; b--)
        {
            if(array[b]>array[a])
            {
                a=b;
            }
        }
        len--;
        tmp = array[len];
        array[len] = array[a];
        array[a] = tmp;
    }
}
```

<!-- ===== page 07 ===== -->

![图](assets/期中/2012期中-带答案/page-07.png)

> 上图为待填空的 C 代码模板（原卷空白卷面，横线处需要填写）。

```c
void mystery_sort (long* array, long len)
{
    long a, b, tmp;

    while (_____ > _____)
    {

        a = _____;

        for (b = _____; b > _____; b--)
        {

            if (array[_____] > array[_____])
            {

                _____ = _____;
            }
        }

        len--;

        tmp = array[_____];

        array[_____] = array[_____];

        array[_____] = tmp;
    }
}
```

---

### 2012期中-带答案 · Problem C 2 a)

> 出处：`原文/期中/2012期中-带答案.md` 第 363–399 行　·　模块判定：Machine Prog
> 考什么：lea (%rax,%r8,1),%ecx 对应的 C 表达式

![图](assets/期中/2012期中-带答案/page-08.png)

> 上图为本页内容（objdump 反汇编清单 + 红色印刷的参考答案）。

2. Below is some assembly code to a famous algorithm. Please briefly read the code then
   answer the questions on the following page. **(m-s09-6) 12pts**

```asm
0000000000400498 <mystery>:
 400498:  41 b8 00 00 00 00   mov    $0x0,%r8d
 40049e:  eb 22               jmp    4004c2 <mystery+0x2a>
 4004a0:  89 c8               mov    %ecx,%eax
 4004a2:  c1 e8 1f            shr    $0x1f,%eax
 4004a5:  01 c8               add    %ecx,%eax
 4004a7:  d1 f8               sar    %eax            ; arith shift right 1 bit
 4004a9:  42 8d 0c 80         lea    (%rax,%r8,1),%ecx
 4004ad:  48 63 c1            movslq %ecx,%rax
 4004b0:  8b 04 87            mov    (%rdi,%rax,4),%eax
 4004b3:  39 d0               cmp    %edx,%eax
 4004b5:  7d 05               jge    4004bc <mystery+0x24>
 4004b7:  41 89 c8            mov    %ecx,%r8d
 4004ba:  eb 06               jmp    4004c2 <mystery+0x2a>
 4004bc:  39 d0               cmp    %edx,%eax
 4004be:  7e 10               jle    4004d0 <mystery+0x38>
 4004c0:  89 ce               mov    %ecx,%esi
 4004c2:  89 f1               mov    %esi,%ecx
 4004c4:  44 29 c1            sub    %r8d,%ecx
 4004c7:  85 c9               test   %ecx,%ecx
 4004c9:  7f d5               jg     4004a0 <mystery+0x8>
 4004cb:  b9 ff ff ff ff      mov    $0xffffffff,%ecx
 4004d0:  89 c8               mov    %ecx,%eax
 4004d2:  c3                  retq
```

   a) Please write a single line of C code to represent the instruction lea (%rax,%r8,1),%ecx (Use C
      variables named rax,r8, and ecx, you can ignore types).
      **ecx = rax + r8**

---

### 2012期中-带答案 · Problem C 2 b)

> 出处：`原文/期中/2012期中-带答案.md` 第 401–404 行　·　模块判定：Machine Prog
> 考什么：mov (%rdi,%rax,4),%eax 对应的 C 表达式

   b) Please write a single line of C code to represent the instruction mov (%rdi,%rax,4),%eax (Use
      C variables named rdi and rax, you can ignore types).
      **eax = \*(rdi + rax)　　// rdi is int \***
      **eax = \*(rdi + 4 \* rax) // rdi is char \***

---

### 2012期中-带答案 · Problem C 2 c)

> 出处：`原文/期中/2012期中-带答案.md` 第 406–407 行　·　模块判定：Machine Prog
> 考什么：本题代码中为何没有 leave 指令

   c) Commonly found in assembly is the leave instruction; why is that instruction not in this code?
      **no stack to return from, no push %ebp**

---

### 2012期中-带答案 · Problem D A

> 出处：`原文/期中/2012期中-带答案.md` 第 416–539 行　·　模块判定：Machine Prog
> 考什么：IA32 栈帧、递归调用参数与 leave 前栈内容推算

**Problem D Stack (10 pts)**

Stack discipline. Consider the following C code and assembly code for a recursive function . **(m-
f11-5) 10pts**

<!-- ===== page 09 ===== -->

```c
int gcd(int a, int b)
{
    if (!b)
    {
        return a;
    }

    return gcd(b, a % b);
}
```

```asm
0x08048394 <+0>:     push   %ebp
0x08048395 <+1>:     mov    %esp,%ebp
0x08048397 <+3>:     sub    $0x10,%esp
0x0804839a <+6>:     mov    0x8(%ebp),%eax
0x0804839d <+9>:     mov    0xc(%ebp),%ecx
0x080483a0 <+12>:    test   %ecx,%ecx
0x080483a2 <+14>:    je     0x80483b7 <gcd+35>
0x080483a4 <+16>:    mov    %eax,%edx
0x080483a6 <+18>:    sar    $0x1f,%edx
0x080483a9 <+21>:    idiv   %ecx
0x080483ab <+23>:    mov    %eax,0x4(%esp)
0x080483af <+27>:    mov    %ecx,(%esp)
0x080483b2 <+30>:    call   0x8048394 <gcd>
0x080483b7 <+35>:    leave
0x080483b8 <+36>:    ret
```

Imagine that a program makes the procedure call gcd(213, 18). Also imagine that prior to the
invocation, the value of %esp is 0xffff1000—that is, 0xffff1000 is the value of %esp immediately
before the execution of the call instruction.

**A.** Note that the call gcd(213, 18) will result in the following function invocations: gcd(213, 18),
gcd(18, 15), gcd(15, 3), and gcd(3, 0). Using the provided code and your knowledge of IA32 stack
discipline, fill in the stack diagram with the values that would be present immediately before the
execution of the leave instruction for gcd(15, 3). Supply numerical values wherever possible, and
cross out each blank for which there is insufficient information to complete with a numerical
value.

**Hints:** The following set of C style statements describes an approximation of the operation of
the instruction idiv %ecx, where ’/’ is the division operator and ’%’ is the modulo operator:

```
%eax = %eax / %ecx

%edx = %eax % %ecx
```

Also, recall that leave is equivalent to movl %ebp, %esp; popl %ebp

***Part A:***

![图](assets/期中/2012期中-带答案/page-09.png)

> 上图为本页底部的栈内容图（Part A 的上半部分，地址由高到低），红色为参考答案；该图在下一页继续。

```
+-------------------------------------+---------------
|              unknown                |  0xffff1008
+-------------------------------------+---------------
|                18                   |  0xffff1004
+-------------------------------------+---------------
|                213                  |  0xffff1000
+-------------------------------------+---------------
|              unknown                |  0xffff0ffc
+-------------------------------------+---------------
|              unknown                |  0xffff0ff8
+-------------------------------------+---------------
|              unknown                |  0xffff0ff4
+-------------------------------------+---------------
```

<!-- ===== page 10 ===== -->

![图](assets/期中/2012期中-带答案/page-10.png)

> 上图为本页的栈内容图（Part A 的下半部分，接上一页，地址由高到低），红色为参考答案。

```
+-------------------------------------+---------------
|              unknown                |  0xffff0ff0
+-------------------------------------+---------------
|                15                   |  0xffff0fec
+-------------------------------------+---------------
|                18                   |  0xffff0fe8
+-------------------------------------+---------------
|            0x080483b7               |  0xffff0fe4
+-------------------------------------+---------------
|            0xffff0ff8               |  0xffff0fe0
+-------------------------------------+---------------
|              unknown                |  0xffff0fdc
+-------------------------------------+---------------
|              unknown                |  0xffff0fd8
+-------------------------------------+---------------
|                3                    |  0xffff0fd4
+-------------------------------------+---------------
|                15                   |  0xffff0fd0
+-------------------------------------+---------------
|            0x080483b7               |  0xffff0fcc
+-------------------------------------+---------------
|            0xffff0fe0               |  0xffff0fc8
+-------------------------------------+---------------
|              unknown                |  0xffff0fc4
+-------------------------------------+---------------
|              unknown                |  0xffff0fc0
+-------------------------------------+---------------
|                0                    |  0xffff0fbc
+-------------------------------------+---------------
|                3                    |  0xffff0fb8
+-------------------------------------+---------------
|              unknown                |  0xffff0fb4
+-------------------------------------+---------------
|              unknown                |  0xffff0fb0
+-------------------------------------+---------------
```

---

### 2012期中-带答案 · Problem D B

> 出处：`原文/期中/2012期中-带答案.md` 第 541–545 行　·　模块判定：Machine Prog
> 考什么：ret 前 %esp 与 %ebp 的取值

**B.** What are the values of %esp and %ebp immediately before the execution of the ret
instruction for gcd(15, 3)?

**esp: 0xffff0fcc**
**ebp: 0xffff0fe0**

---

### 2013期中-带答案 · 选择题 4

> 出处：`原文/期中/2013期中-带答案.md` 第 44–53 行　·　模块判定：Machine Prog
> 考什么：gdb 断点与运行命令（Bomb Lab）

4、 在完成Bomb Lab的时候，通常先执行gdb bomb启动调试，然后执行 ___  explode_bomb
命令以防引爆炸弹，之后在进行其他必要的设置后，最后执行___命令以便开始执行程序。
上述两个空格对应的命令是（       ）
1

<!-- ===== page 2 ===== -->

A. st, ru   B. br, go   C. br, ru    D. st, go
答案：c
说明：根据之前的讨论，出一道题目检查同学们是否自己做过lab

---

### 2013期中-带答案 · 选择题 5

> 出处：`原文/期中/2013期中-带答案.md` 第 54–62 行　·　模块判定：Machine Prog
> 考什么：lea 乘法指令识别（n*10）

5、已知函数int x( int n ) {  return  n*____; } 对应的汇编代码如下：
lea (%rdi, %rdi, 4), %rdi
lea (%rdi, %rdi, 1), %eax
retq
请问横线上的数字应该是（        ）
A. 4   B. 5   C. 2   D. 10
答案：D
说明：此题目考察对于乘法的转换，难度较低，适合出选择题。还可以把乘法换成除法，就
可以出大题或者简答题。

---

### 2013期中-带答案 · 选择题 7

> 出处：`原文/期中/2013期中-带答案.md` 第 71–76 行　·　模块判定：Machine Prog
> 考什么：x86 寻址方式与指令合法性

7、x86体系结构的内存寻址方式有多种格式，请问下列哪些指令是正确的：（      ）
A. movl  $34,  (%eax)
B. movl  (%eax),  %eax
C. movl  $23,  10(%edx, %eax)
D. movl  (%eax),  8(%ebx)
答案：ABC，寻址不支持内存到内存的访问

---

### 2013期中-带答案 · 选择题 8

> 出处：`原文/期中/2013期中-带答案.md` 第 77–82 行　·　模块判定：Machine Prog
> 考什么：leal 用途、传参、寄存器保存与条件码

8、 x86体系结构中，下面哪些选项是错误的？答：（      ）
A. leal指令只能够用来计算内存地址
B. x86_64机器可以使用栈来给函数传递参数
C. 在一个函数内，改变任一寄存器的值之前必须先将其原始数据保存在栈内
D. 判断两个寄存器中值大小关系，只需要SF（符号）和ZF（零）两个conditional code
答案：ACD

---

### 2013期中-带答案 · 第三题 1)

> 出处：`原文/期中/2013期中-带答案.md` 第 204–222 行　·　模块判定：Machine Prog
> 考什么：64 位机器 long 的位数（int_sqrt 题干代码）

第三题 （11分）
阅读下面的C代码：
/ **  Copyright (C) 2013 Davidlohr Bueso <davidlohr.bueso@hp.com>
   ***     Bsqausaerde  orno otth efr oshmif tG-aunyd L-s.u Sbtterealcet.  algorithm for computing integer
 */
/ *** i nt_sqrt - rough approximation to sqrt
   ***   A@ vxe: riyn treoguegrh o af pwphroicxhi mtoa tciaolnc utola tthe et hseq rstq()r tf unction.
 */
u{  nsignuedn sliognnge din lto_nsgq rbt(, umns, iyg n=e 0d;  long x)
   if (x <= 1)
     return x;
   mwh =il e1 U(mL  !<=< 0 ()B {I TS_PER_LONG - 2);
    b = y + m;
     y >>= 1;
      i f (x >=x  b-=)  {b ;
       }  y += m;
    }  m >>= 2;
  }  return y;
1 ）在64位的机器上BITS_PER_LONG的定义为long类型的二进制位数，它是多少位？

---

### 2013期中-带答案 · 第三题 2)

> 出处：`原文/期中/2013期中-带答案.md` 第 223–285 行　·　模块判定：Machine Prog
> 考什么：反汇编填空：int_sqrt 整数平方根（含答案）

 2）填写下面反汇编中的缺失的内容：
<    in44t00_00s44qccrt45>:::       pmuosvh       %%rbrspp ,%rbp
   4004c8:    mov    %rdi,-0x28(%rbp)
    44000044cdc4::       mcmopvqq      $ 0 x(11), -0 x 2 8 ( %  rb p )   ,-0x8(%rbp)
   4004d9:    ja       (2)               <int_sqrt+??>
   4004db:    mov    -0x28(%rbp),%rax
    44000044de1f::       jmmopv l       $0 x(30), -0 x 1 0 ( %  rb p )      <int_sqrt+??>
   4004e8:    movl     (4)              ,-0xc(%rbp)
   4004ef:     jmp      (5)               <int_sqrt+??>
    44000044ff15::       mmoovv        --00xx180(%(%rbrpbp),)%,%rdrxax
6

<!-- ===== page 7 ===== -->

  4004f9:    lea      (6)              ,%rax
  4004fd:    mov    %rax,-0x18(%rbp)
  400501:    shrq   -0x8(%rbp)
  400505:    mov    -0x28(%rbp),%rax
  400509:    cmp    -0x18(%rbp),%rax
  40050d:    jb       (7)            <int_sqrt+??>
  40050f:    mov    -0x18(%rbp),%rax
  400513:    sub    %rax,-0x28(%rbp)
  400517:    mov    -0x10(%rbp),%rax
  40051b:    add    %rax,-0x8(%rbp)
  40051f:    shrq     (8)            ,-0x10(%rbp)
  400524:    cmpq   $0x0,-0x10(%rbp)
  400529:    jne      (9)            <int_sqrt+??>
  40052b:    mov    -0x8(%rbp),   (10)
  40052f:    leaveq
  400530:    retq
答案：
1、 答：64
2、
<int_sqrt>:
  4004c4:   push   %rbp
  4004c5:    mov    %rsp,%rbp
  4004c8:    mov    %rdi,-0x28(%rbp)
  4004cc:    movq   $0x0,-0x8(%rbp)
  4004d4:    cmpq   $0x1,-0x28(%rbp)
  4004d9:    ja     4004e1 <int_sqrt+0x1d>
  4004db:    mov    -0x28(%rbp),%rax
  4004df:    jmp    40052f <int_sqrt+0x6b>
  4004e1:    movl   $0x0,-0x10(%rbp)
  4004e8:    movl   $0x40000000,-0xc(%rbp)
  4004ef:     jmp    400524 <int_sqrt+0x60>
  4004f1:    mov    -0x10(%rbp),%rax
  4004f5:    mov    -0x8(%rbp),%rdx
  4004f9:    lea    (%rdx,%rax,1),%rax
  4004fd:    mov    %rax,-0x18(%rbp)
  400501:    shrq   -0x8(%rbp)
  400505:    mov    -0x28(%rbp),%rax
  400509:    cmp    -0x18(%rbp),%rax
  40050d:    jb     40051f <int_sqrt+0x5b>
  40050f:    mov    -0x18(%rbp),%rax
  400513:    sub    %rax,-0x28(%rbp)
  400517:    mov    -0x10(%rbp),%rax
  40051b:    add    %rax,-0x8(%rbp)
  40051f:    shrq   $0x2,-0x10(%rbp)
  400524:    cmpq   $0x0,-0x10(%rbp)
  400529:    jne    4004f1 <int_sqrt+0x2d>
  40052b:    mov    -0x8(%rbp),%rax
  40052f:    leaveq
  400530:    retq

---

### 2013期中-带答案 · 第四题

> 出处：`原文/期中/2013期中-带答案.md` 第 290–318 行　·　模块判定：Machine Prog
> 考什么：结构体 sizeof 与递归函数汇编/运行结果

第四题（10分）
阅<  f>4读:0 0下4c面4: 的 汇  编代pus码h ：   %rbp
            444444000000000000444444ddcccc58cf35::::::                     ms jmau oob vv         cm    m4  $o0%$p0v00l xr 4x1 s d1p0  c,,, %%$% %<0errfxebas+1dppx0, i  x-,0-10x8x4>4( %(%rrbbpp) )
          44444000000000044444dddee24acf:::::                  jmtjmensoept v          a  % n4 4d0e-0 0a00 xx45 4,f%52 (%d $e<0 ar<fxxb+f1 p+0,)0x%,%x3e16ea9>ax> x
              4444444000000000000004444444eeeffff58bd6cf:::::::                            m  ov  matjma eend s ooddt0 vv   x      2      0   %  04  $$40a%-0004l0x,xxe0%511a4(0,,%xa(%%e%l, 0 r<eeixrpaafb2+xx)p0,0  %)0x,%4e43aae7x>a ( x%   r ip )      #   6 0 0 9#2 c6 0<0x9.126c0 <4x>. 1604>
            44444400000000000045555500011ff58e14: :::::                    mamsmudooobdvvv            m        $o$%%-0v00 xxxee1 1aa4, ,xx(%% %,,0%0eexrxaaeb2x2xdp0 0 i)0 0,%4422e2ba(x(%% rriipp)) ,%  e a x      #   6 0 0 9#3 06 0<0y9.13600 <5y>. 1605>
            4444440000000000005555551122226b14ad::::::                    cmlmlleeeaaaaool  vlvvq  e   q          4 ((  0%%000xxrr4da22cxx004,,00% %<44rfr00d>af2xx ((%,,%11)r)r,i,i%%pp))ee,,%da%xxee  daxx                ##  66000099320c  <<yx..11660054>>
  1 ）40程05序2em{   :    a  in    (ufo)n rs i(gnren=teq1d ;   ni n< t  4n;;  n++) {
的 #d运efi行ne结    }N    果      为 }(  1： )  f p( 1ri )n= tf1 (， "f (f %( 2d )=)  4 =e  %，  xf \(n 3" ),= n9,f ，f(n请));填  写f函数所需要的内容（每空1分）：
# ss ttdrruuefccittn  PPe 12M  {{ cin ht a i(r[2 Mc)[ N] ; ] c;  hc ah ra  jr[  M* d ][; N s ]h ;o  cr ht  ak r[  Me []N; ]};  P} 2P;1 ;
u{    n  s  i  g  n((e34d))   in  t     f(  u  n  s  ig  n  e  d     in  t   n  )   uunnssiiggnneedd  iinntt  xy  ==  ssiizzeeooff((PP21))8;;

<!-- ===== page 9 ===== -->

        i f  (    r(e5t)u r n  1 ;                 )
         i f  (    x(+6)+ ;                    )
         i f  (    y(+7)+ ;                    )
  }    return  (8)                  ;
 2、程序m{  ain()
   }的  运  行pri结ntf果("%为x：, %（x2\n分", ）f(2 ), f(2));
  1#、def答in案e N：    3
# stdruefcitn Pe 1M { c h a5r  c[N]; char *d[N]; char e[N]; } P1;
s utnrusicgtn Pe2d  {inint tf (iu[Mns]i;g cnheadr  ijn[tM n]);  short k[M]; } P2;
{         ssttaattiicc  uunnssiiggnneedd  iinntt  xy  ==  ssiizzeeooff((PP21));;
         i f  ( n <r=et1u)r n 1;
         i f  ( ( nx &+ +1;)  == 0)
         i f  ( ( ny &++ 1;)  == 1)
  }    return f(n-1) + (y) +  (x);
 2 、答案：4f, 4e   （回答4e, 4f给一半的分）

---

### 2013期中-带答案 · 第七题 1)

> 出处：`原文/期中/2013期中-带答案.md` 第 397–413 行　·　模块判定：Machine Prog
> 考什么：由汇编还原 transform 的 C 代码

第七题（10分）
已知如下的汇编程序实现了函数transform(char* src, char* tgt, char delta)
transform:
  jmp L2
L1:
  add %edx, %eax
  add $1, $rdi
  mov %al, (%rsi)
  add $1, $rsi
L2:
  movzbl (%rdi), %eax
  test %al, %al
  jne L1
movb $0, (%rsi)
retq
参考信息：64位指令集中传递前三个参数分别使用寄存器%rdi, %rsi和%rdx
1）写出transform函数对应的C语言版本（2分）

---

### 2014期中-带答案 · 第一题 4

> 出处：`原文/期中/2014期中-带答案.md` 第 89–100 行　·　模块判定：Machine Prog
> 考什么：只改条件码不改寄存器的指令 CMP/TEST

4、下列的指令组中，那一组指令只改变条件码，而不改变寄存器的值？

A. CMP, SUB
B. TEST, AND
C. CMP, TEST
D. LEAL, CMP

答：（　　　）

答案：C

SUB 和 AND 都同时会改变条件码和寄存器的值，LEAL 不改变改变条码。

---

### 2014期中-带答案 · 第一题 5

> 出处：`原文/期中/2014期中-带答案.md` 第 102–113 行　·　模块判定：Machine Prog
> 考什么：x86 各寻址方式写法的正确性

5、下列指令中，寻址方式不正确的是

A. MOVB %ah, 0x20(, %ecx, 8)
B. LEAL (0xA, %eax), %ebx
C. SUBB 0x1B, %bl
D. INCL (%ebx, %eax)

答：（　　　）

答案：B

存储器数的基地址应该存放在一个基址寄存器中。

---

### 2014期中-带答案 · 第一题 7

> 出处：`原文/期中/2014期中-带答案.md` 第 145–156 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出的防护做法正误

7、关于如何避免缓冲区溢出带来的程序风险，下述错误的做法为？

A. 编程时定义大的缓冲区数组
B. 编程时避免使用 gets，而采用 fgets
C. 程序运行时随机化栈的偏移地址
D. 在硬件级别引入不可执行代码段的机制

答：（　　　）

答案：A

B、C、D 均为讲义中所提及的解决缓冲区溢出风险的方法。A 策略则无法从根本上解决缓冲区溢出问题，只要输入足够长数据就仍然可以实现缓冲区溢出攻击。

---

### 2014期中-带答案 · 第一题 8

> 出处：`原文/期中/2014期中-带答案.md` 第 158–171 行　·　模块判定：Machine Prog
> 考什么：switch 跳转表的 jmp 汇编写法与比例因子

8、对简单的 switch 语句常采用跳转表的方式实现，在 x86-64 系统中，下述最有可能正确的 switch 分支跳转汇编指令为哪个？

A. jmp .L3(, %eax, 4)
B. jmp .L3(, %eax, 8)
C. jmp *.L3(, %eax, 4)
D. jmp *.L3(, %eax, 8)

<!-- ===== page 5 ===== -->

答：（　　　）

答案：D

A 与 B 都是错误的基于跳转表跳转的指令正确格式。C、D 的指令格式正确，但在 x86-64 系统中，每个地址占 8 个字节，因此更有可能的答案是 D。

---

### 2014期中-带答案 · 第四题 1）

> 出处：`原文/期中/2014期中-带答案.md` 第 387–406 行　·　模块判定：Machine Prog
> 考什么：x86-64 递归函数汇编，据 gdb 反汇编补全 C 代码

第四题（10 分）

一个函数如下，其中部分代码被隐去，请通过gdb调试信息补全代码（4分）。

```c
int f(int n, int m) {
    if (m > 0) {
        if (n > 1) {
            int r = f(n - 1, m);
            return (r - 1 + m) % n + 1;
        }
        else if (n == 1) {
            return 1;
        }
    }
    return 0;
}
```

{考察点：x86-64函数调用、参数传递及栈的使用。函数调用通过rdi和rsi传递第一和第二个参数，栈中只记录函数的返回地址。由于是递归调用，需要用栈保存递归过程中参数变量的值。同时考察xor、test、lea、idiv、sete等指令的使用。难点1：两个判断"n > 1"和"n == 1"在汇编代码中只有一次比较，第二次判断相等是通过sete使得n==1时返回值为1，否则返回值为0实现的。难点2：表达式"(r - 1 + m) % n + 1"比较复杂，需要综合多条语句的信息才能分析出来，并且变量r对应于f(n-1,m)的返回值即寄存器%eax，因而不存在相应的赋值指令。}

---

### 2014期中-带答案 · 第四题 2）

> 出处：`原文/期中/2014期中-带答案.md` 第 408–442 行　·　模块判定：Machine Prog
> 考什么：补全缺失的两条汇编指令并判断栈寄存器

如下是通过"gcc -g -O2"命令编译后，在gdb中通过"disas f"命令得到的反汇编代码，其中有两个汇编指令不全，请补全这两条汇编指令（2分）。

```
0x00000000004004e0 <f+0>:            mov    %rbx,-0x10(%rsp)
0x00000000004004e5 <f+5>:            mov    %rbp,-0x8(%rsp)
0x00000000004004ea <f+10>:           xor    %eax,%eax
0x00000000004004ec <f+12>:           sub    $0x10,%rsp
0x00000000004004f0 <f+16>:           test   %esi,%esi
0x00000000004004f2 <f+18>:           mov    %edi,%ebp
0x00000000004004f4 <f+20>:           mov    %esi,%ebx
0x00000000004004f6 <f+22>:           jle    0x400513 <f+51>
0x00000000004004f8 <f+24>:           cmp    $0x1,%edi
```

<!-- ===== page 12 ===== -->

```
0x00000000004004fb <f+27>:           jle    0x400521 <f+65>
0x00000000004004fd <f+29>:           lea    -0x1(%rbp),%edi
0x0000000000400500 <f+32>:           callq  0x4004e0 <f>
0x0000000000400505 <f+37>:           lea    -0x1(%rax,%rbx,1),%edx
0x0000000000400509 <f+41>:           mov    %edx,%eax
0x000000000040050b <f+43>:           sar    $0x1f,%edx
0x000000000040050e <f+46>:           idiv   %ebp
0x0000000000400510 <f+48>:           lea    0x1(%rdx),%eax
0x0000000000400513 <f+51>:           mov    (%rsp),%rbx
0x0000000000400517 <f+55>:           mov    0x8(%rsp),%rbp
0x000000000040051c <f+60>:           add    $0x10,%rsp
0x0000000000400520 <f+64>:           retq
0x0000000000400521 <f+65>:           sete   %al
0x0000000000400524 <f+68>:           movzbl %al,%eax
0x0000000000400527 <f+71>:           jmp    0x400513 <f+51>
```

{考察点：函数中使用到了%rbp和%rbx寄存器，两者都是callee保存的寄存器，使用前需要压栈，函数返回时需要弹栈恢复寄存器的值。通过前后汇编代码的对比，应该可以猜出两个空分别填写什么；但要注意，压栈和弹栈时，%rsp寄存器的值不同，因而对应的地址表示也不同。}

---

### 2014期中-带答案 · 第四题 3）

> 出处：`原文/期中/2014期中-带答案.md` 第 446–495 行　·　模块判定：Machine Prog
> 考什么：递归调用 retq 处栈帧内容填写

已知在调用函数f(4, 3)时，我们在函数f中指令retq处设置了断点，下面列出的是程序在第一次运行到断点处暂停时，相关通用寄存器的值。请根据你对函数及其汇编代码的理解，填写当前栈中的内容。如果某些内存位置处内容不确定，请填写X。（4分）

```
rax            0x1
rbx            0x3
rcx            0x3
rdx            0x309c552970
rsi            0x3
rdi            0x1
rbp            0x2
rsp            0x7fffffffe340
rip            0x400520
```

![图](assets/期中/2014期中-带答案/page-13.png)

（图：栈内容填写表，左列为栈地址（0x7ffffffe38c 到 0x7ffffffe320，每 4 字节一行），右列为对应内容（红色为答案））

| 栈地址 | 内容 |
| --- | --- |
| 0x7ffffffe38c | X |
| 0x7ffffffe388 | X |
| 0x7ffffffe384 | X |
| 0x7ffffffe380 | X |
| 0x7ffffffe37c | X |
| 0x7ffffffe378 | X |
| 0x7ffffffe374 | 0x0 |
| 0x7ffffffe370 | 0x00400505 |
| 0x7ffffffe36c | 0x0 |
| 0x7ffffffe368 | 0x4 |
| 0x7ffffffe364 | 0x0 |
| 0x7ffffffe360 | 0x3 |
| 0x7ffffffe35c | 0x0 |
| 0x7ffffffe358 | 0x00400505 |
| 0x7ffffffe354 | 0x0 |
| 0x7ffffffe350 | 0x3 |
| 0x7ffffffe34c | 0x0 |
| 0x7ffffffe348 | 0x3 |
| 0x7ffffffe344 | 0x0 |
| 0x7ffffffe340 | 0x00400505 |
| 0x7ffffffe33c | 0x0 |
| 0x7ffffffe338 | 0x2 |
| 0x7ffffffe334 | 0x0 |
| 0x7ffffffe330 | 0x3 |
| 0x7ffffffe32c | X |
| 0x7ffffffe328 | X |
| 0x7ffffffe324 | X |
| 0x7ffffffe320 | X |

{考察点：递归调用的返回地址共三处是明确的，并且相同，值可以从反汇编代码中确定（1 分）；三次递归调用程序栈中，压入的%rbx（m）的值不变，压入的%rbp（n）的值为每次减小 1（1 分）；注意 x86-64，栈中的数据都是 64 位的，但因为数值均比较小，所以这 9 个位置处的高 4 字节均为 0（1 分）；其余位置的内容均是不确定的（1 分）。}

---

### 2014期中-带答案 · 第五题

> 出处：`原文/期中/2014期中-带答案.md` 第 499–550 行　·　模块判定：Machine Prog
> 考什么：由 IA32 汇编补全 C 代码缺失部分并说明功能

第五题（8 分）

阅读下面的汇编代码，根据汇编代码填写 C 代码中缺失的部分，然后描述该程序的功能。

（原文左右分栏：左列为汇编代码，右列为 C 代码）

```asm
        pushl  %ebp
        movl   %esp,%ebp
        movl   $0x0, %ecx
        cmpl       $0x0, 8(%ebp)
        jle .L1
.L2
        movl   $0x0, %edx
        movl   8(%ebp), %eax
        divl   $0xa
        addl   %edx, %ecx
        movl   %eax, 8(%ebp)
        cmpl   $0x0, 8(%ebp)
        jg .L2
.L1
        movl   0x0, %edx
        movl   %ecx, %eax
        divl   0x3
        cmpl      0x0, %edx
        jne .L3
        movl   0x1, %eax
        jmp .L4
.L3
        movl   0x0, %eax
.L4
```

```c
int fun(unsigned x) {
        int bit_sum = 0;

        while ( (int) x > 0  ) {
                bit_sum += x % 10 ;
                x = x / 10             ;
        }

        if ( bit_sum % 3 == 0     )
                return 1;
        else
                return 0;
}
```

红色下划线部分为答案，每空 1 分。

该程序用来判断一个不大于 2<sup>n</sup>-1 的非负整数是否为 3 的倍数，如果大于 2<sup>n</sup>-1，则直接返回 1（3 分）。

---

### 2015期中-带答案 · 选择题 6

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 117–120 行　·　模块判定：Machine Prog
> 考什么：x86 寻址模式正确性

6. A.下 (列%寻ea址x,模 式, 中4)， 正确的是：
BC..  (1%2e3 ax, %esp, 3)
D. $1(%ebx, %ebp, 1)
  选择C. A中不能省略Ei，B中比例因子错误，D中偏移地址表示错误。

---

### 2015期中-带答案 · 选择题 8

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 126–135 行　·　模块判定：Machine Prog
> 考什么：跳转表汇编与标号取值范围

8.  假设mo某v条l C8(语%言ebspw)i,t c%hea语x 句编译后产生了如下.的L7汇: 编代码及跳转表：
scumbpll  $$488,,  %%eeaaxx   ..lloonngg  ..LL32
jjam p. L*2. L7(, %eax, 4)  ..lloonngg  ..LL25
  .long .L4
...lllooonnnggg   ...LLL562
.long .L3
在A.源 ‘程2’序,中 ‘，7下’ 面的哪些（个）标号出现过：
BC..  1‘ 3’
D. 5
选  择C. 标号的取值范围为’0’ – ，’1’、’2’、’7’、’9’、…等没有出现。

---

### 2015期中-带答案 · 选择题 9

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 136–146 行　·　模块判定：Machine Prog
> 考什么：leal/传参/条件码等汇编细节

9.  x86体系结构中，下面哪个说法是正确的？
A. leal指令只能够用来计算内存地址
B. x86_64机器可以使用栈来给函数传递参数
4

<!-- ===== page 5 ===== -->

C. 在一个函数内，改变任一寄存器的值之前必须先将其原始数据保存在栈内
D. 判断两个寄存器中值大小关系，只需要SF和ZF两个条件码
答案：B
A.leal指令做普通算术运算；C.caller saved寄存器才需要；D.还需要OF

---

### 2015期中-带答案 · 选择题 10

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 147–153 行　·　模块判定：Machine Prog
> 考什么：CMP/TEST 与条件码

10. 下列的指令组中，哪一组指令只改变条件码，而不改变寄存器的值？
A. CMP, SUB
B. TEST, AND
C. CMP, TEST
D. LEAL, CMP
答案：C
SUB和AND都同时会改变条件码和寄存器的值，LEAL不改变改变条码。

---

### 2015期中-带答案 · 第三题 2

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 323–331 行　·　模块判定：Machine Prog
> 考什么：由汇编补全结构体成员赋值语句

2.假设编译器为process的主体产生了如下了代码，请补充完整下面的过程:(6
分)
（  只有一个不需要任何强制类型转换且不违反任何类型限制的答案）
mmoovvll  8((%%eeabxp)),,%%eecax x
mmoovvll  4((%%eedcxx)),,%%eeddx x
subl 4(%eax),%edx
 voidm opvrlo c%eesdsx(,u(n%ieocnx )E L E * up)
{
 }  up->________________=________________ - ________________;

---

### 2015期中-带答案 · 第三题 3

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 336–358 行　·　模块判定：Machine Prog
> 考什么：X86/Y86 汇编代码错误定位与更正

3.请查看下文完成如下功能的汇编代码，定位错误语句并进行更正: (6分)
给出 n(在%ebp+8 位置,n>=1),up(在%ebp+12 位置,ELE* 类型),假设
以*up为头元素(设*up为第0个),由声明中的next连接形成了一个链表,请将
第n个元素(假设链表足够长)的x的值放入%eax中
 X86代码
xorl %ecx,%ecx
movl 8(%edx),%ebp
movl 12(%ebp),%eax
LOOP:
movl (%eax),%eax
add $1,%ecx
test %ecx,%edx
jne LOOP
movl (%eax),%eax
Y86代码
mrmovl 8(%edx),%ebp
mrmovl 12(%ebp),%eax
irmovl $1,%ecx
LOOP:
mrmovl (%eax),%eax
test %ecx,%edx
jne LOOP
mrmovl (%eax),%eax

---

### 2015期中-带答案 · 第三题 4

> ⚠️ 同一份卷子也存在于：`原文/期末/2015期末-20151109-带答案.md`（正文等同，已去重）
> 出处：`原文/期中/2015期中-带答案.md` 第 359–394 行　·　模块判定：Machine Prog
> 考什么：二维数组寻址与 lea 偏移（求 A、B，含本大题答案）

4.阅读下列代码，回答后面的问题
typedef struct {
  short x[A][B];
  int y;
12

<!-- ===== page 13 ===== -->

} str1;
t ypecdheafr  satrrruacyt[ B{] ;
  int t;
  }strsi2hn;ot r tu ; s[B];
void setVal(str1 *p,str2 *q) {
   iinntt  vv12==qq-->>tu;;
 }   p->y=v1+v2;
( short以2字节计算)
G CCm为ovsle t1V2a(l%的eb主p体),产%e生a下x 面的代码:
movl 28(%eax),%edx
ammdoodvvlll   88%((e%%deexab,xp4))4,,(%%%eeedaaxxx)
请  直接写出A和B的值各是多少?(6分)
答  案
12..  8u p->next->x=*(up->next->p)-(up->y)
3 .  (3个错, 每个错2分)
Xxo8r6l代 码%e cx,%ecx
mmoovvll  81(2%(e%dexb)p,)%,e%bepa x     ||应为： movl 8(%ebp),%edx
13

<!-- ===== page 14 ===== -->

LmaOodOvdPl : $(1 %,e%aexc)x, %eax
tj menosevt l L %O(eO%cPe xa,x%)e,d%xe ax
 Y86代码
mmi rrrmmmooovvvlll   81$(21%(,e%%deexbc)px ,)%,e%bepa x   ||应为： mrmovl 8(%ebp),%edx
Lmtj OrenOmsePot :v Ll%O  eO(cP %xe,a%xe)d,x%  e a x       ||应为：subl %ecx,%edx
m 4r. movl (%eax),%eax
A  =3 B=7

---

### 2016期中-带答案 · 第一题 1

> 出处：`原文/期中/2016期中-带答案.md` 第 48–50 行　·　模块判定：Machine Prog
> 考什么：会改变条件码 CF 的指令辨析

1.  在下列指令中，其执行会影响条件码中的CF位的是：
A. jmp NEXT    B. jc NEXT  C. inc %bx  D. shl $1,%ax
答案：D

---

### 2016期中-带答案 · 第一题 2

> 出处：`原文/期中/2016期中-带答案.md` 第 51–54 行　·　模块判定：Machine Prog
> 考什么：CMP 指令不区分有无符号

2.  下列关于比较指令CMP说法中，正确的是：
A. 专用于有符号数比较    B. 专用于无符号数比较
C. 专用于串比较       D. 不区分比较的对象是有符号数还是无符号数
答案：D

---

### 2016期中-带答案 · 第一题 3

> 出处：`原文/期中/2016期中-带答案.md` 第 55–59 行　·　模块判定：Machine Prog
> 考什么：je 相对跳转目标地址计算

3.  在如下代码段的跳转指令中，目的地址是：
400020: 74 F0   je ________
400022: 5d   pop %rbp
A. 400010   B. 400012   C. 400110   D. 400112
答案：B（有符号跳转，向后跳转-0x10）

---

### 2016期中-带答案 · 第一题 4

> 出处：`原文/期中/2016期中-带答案.md` 第 60–63 行　·　模块判定：Machine Prog
> 考什么：C 条件表达式对应的条件转移条数

4.  对于如下的C语言中的条件转移指令，它所对应的汇编代码中至少包含几条条
件转移指令：if (a > 0 && a != 1 || a < 0 && a != -1) b=a;
A. 2条     B. 3条     C. 4条   D. 5条
答案：B（这个条件相当于!(a==0 || a==1 || a==-1)）

---

### 2016期中-带答案 · 第一题 5

> 出处：`原文/期中/2016期中-带答案.md` 第 64–67 行　·　模块判定：Machine Prog
> 考什么：寄存器清零指令辨析

5.  将AX清零，下列指令错误的是（ ）
A. sub %ax, %ax      B. xor %ax, %ax
C. test %ax, %ax     D. and $0, %ax
答案：C（test相当于and）

---

### 2016期中-带答案 · 第一题 6

> 出处：`原文/期中/2016期中-带答案.md` 第 72–81 行　·　模块判定：Machine Prog
> 考什么：switch 跳转表与未出现的标号

6.  在如下switch语句对应的跳转表中，哪些标号没有出现在分支中（ ）
addq $1, %rdi
cmpq $8, %rdi
ja .L2
jmp *.L4(, %rdi, 8)
.L4:  .quad .L9   .quad .L5   .quad .L6   .quad .L7
   .quad .L2
   .quad.L7    .quad .L8   .quad .L2   .quad .L5
A. 3, 6      B. -1, 4      C. 0, 7    D. 2, 4
答案：A

---

### 2016期中-带答案 · 第一题 7

> 出处：`原文/期中/2016期中-带答案.md` 第 82–86 行　·　模块判定：Machine Prog
> 考什么：lea 求数组元素地址

7.  已知短整型数组S的起始地址和下标i分别存放在寄存器%rdx和%rcx，将
&S[i]存放在寄存器%rax中所对应的汇编代码是（ ）
A. leaq (%rdx, %rcx, 1), %rax   B.movw (%rdx, %rcx, 2), %rax
C. leaq (%rdx, %rcx, 2), %rax   D.movw (%rdx, %rcx, 1), %rax
答案：C

---

### 2016期中-带答案 · 第三题 (1)

> 出处：`原文/期中/2016期中-带答案.md` 第 264–317 行　·　模块判定：Machine Prog
> 考什么：switch 跳转表与 gdb 内存检查输出

第三题（20分）
（出题人：熊英飞，审核人：陈钟、焦文品）
(1) 观察下面C语言函数和它相应的X86-64汇编代码
int foo(int x, int i)
{
switch(i)
{
case 1:
x -= 10;
case 2:
x *= 8;
break;
case 3:
x += 5;
case 5:
x /= 2;
break;
case 0:
x &= 1;
default:
x += i;
}
return x;
}
00000000004004a8 <foo>:
4004a8: mov %edi,%edx
4004aa: cmp $0x5,%esi
4004ad: ja 4004d4 <foo+0x2c>
4004af: mov %esi,%eax
4004b1: jmpq *0x400690(,%rax,8)
4004b8: sub $0xa,%edx
4004bb: shl $0x3,%edx
4004be: jmp 4004d6 <foo+0x2e>
4004c0: add $0x5,%edx
9

<!-- ===== page 10 ===== -->

4004c3: mov %edx,%eax
4004c5: shr $0x1f,%eax
4004c8: lea (%rdx,%rax,1),%eax
4004cb: mov %eax,%edx
4004cd: sar %edx
4004cf: jmp 4004d6 <foo+0x2e>
4004d1: and $0x1,%edx
4004d4: add %esi,%edx
4004d6: mov %edx,%eax
4004d8: retq
调用gdb命令x/kg $rsp 将会检查从rsp中的地址开始的k个8字节字，请填写下
面gdb命令的输出（每空一分）。
>(gdb) x/6g 0x400690
0x400690: 0x__________________ 0x__________________
0x4006a0: 0x__________________ 0x__________________
0x4006b0: 0x__________________ 0x__________________

---

### 2016期中-带答案 · 第三题 (1) 答案

> 出处：`原文/期中/2016期中-带答案.md` 第 346–350 行　·　模块判定：Machine Prog
> 考什么：gdb x/6g 输出参考答案

答案：
(1)每空1分
0x400690:   0x00000000004004d1      0x00000000004004b8
0x4006a0:   0x00000000004004bb      0x00000000004004c0
0x4006b0:   0x00000000004004d4      0x00000000004004c3

---

### 2017期中-带答案 · 第一题 4

> 出处：`原文/期中/2017期中-带答案.md` 第 80–84 行　·　模块判定：Machine Prog
> 考什么：x86-64 指令书写错误辨析

4.  在下列的x86-64汇编代码中，错误的是：
A. movq %rax, (%rsp)      B. movl $0xFF, (%ebx)
C. movsbl (%rdi), %eax     D. leaq (%rdx, 1), %rdx
答案：B/D都对
解析：B:地址寄存器必须是64位寄存器;D:括号里少了一个逗号

---

### 2017期中-带答案 · 第一题 5

> 出处：`原文/期中/2017期中-带答案.md` 第 85–94 行　·　模块判定：Machine Prog
> 考什么：条件传送指令的语义与限制

5.  在下列关于条件传送的说法中，正确的是：
A. 条件传送可以用来传送字节、字、双字、和4字的数据
B. C语言中的“?:”条件表达式都可以编译成条件传送
C. 使用条件传送总可以提高代码的执行效率
D. 条件传送指令不需要用后缀（例如b, w, l, q）来表明操作数的长度
答案：D
解析：A.条件传送不支持单字节传送；B.如果“?:”涉及到的两个表达式中有一
个出错或者有副作用，用条件传送会导致非法行为；C.如果被旁路的分支的计算
量很大，计算就白做了；D.从目标寄存器的名字可以推断出条件传送指令的操作
数长度

---

### 2017期中-带答案 · 第一题 6

> 出处：`原文/期中/2017期中-带答案.md` 第 95–104 行　·　模块判定：Machine Prog
> 考什么：函数指针的过程调用指令

6.  有如下代码段：
int func(int x, int y);
int (*p) (int a, int b);
p = func;
p(0,0);
对应的下列x86-64过程调用正确的是：
A. call *%rax     B. call (%rax)
C. call *(%rax)    D. call func
答案：A/D都对
解析：用O0编译可以得到A，用Og编译可以得到D。

---

### 2017期中-带答案 · 第一题 7

> 出处：`原文/期中/2017期中-带答案.md` 第 105–117 行　·　模块判定：Machine Prog
> 考什么：二维数组指针运算与地址计算

7.  有A的定义：int  A[3][2] = {{1,2}，{3,3}，{2,1}}；
那么A[2]的值为：
3

<!-- ===== page 4 ===== -->

A. &A+16      B. A+16    C. *A+4    D. *A+2
答案：C
解析：参见书P177页表格，机器在计算指针与常数的运算时，会将常数乘以指针
指向的元素大小。&A常数扩大的倍数为sizeof(A[3][2]) = 3*2*4; A常数
扩大的倍数为sizeof(A[0])=2*4; *A 常数扩大的倍数为sizeof(int) = 4。
正确的答案应为A+2或*A+4，故应选择C。
程序验证如下：

---

### 2017期中-带答案 · 第三题

> 出处：`原文/期中/2017期中-带答案.md` 第 222–286 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出程序的汇编缺失代码补全

第三题（15分）
分析下面C语言程序和相应的x86-64汇编程序。其中缺失部分代码（被遮挡），请
在对应的横线上填写缺失的内容。（注:每格1分）
## iinncclluuddee  <"ssttdriion.gh.>h"
v{o id myprint(char *str)
cshtarrc pbyu(fbfuefrf[e1r6,]st;r );       ○1strcpy
}   printf("%s \n",buffer);
v{o id alert(void)
printf("Where am I?\n");    ○2Where am I?
} i nt main(int argc,char *argv[])
{  myprint("1234567123456712345671234567\xaa\x84\x04\x08");
}  return 0;
* .*LC**0.:*s *e*c*t*i*o*n* ****.*r*o*d*a*t*a* ***************************************
  .string "%s \n"         ○3%s \n
   ..tgelxotb l  myprint
 mypr.itnytp:e   myprint, @function
.  LFB.p0cu:fs ih_qs ta%rrtbppr oc
   ..ccffii__doefff_scefta _6o,f f-s1e6t  16
   m.ocvfqi_ def%_rcsfpa,_ r%ergbips ter 6
   smuobvqq   $%4r8d,i , %r-s4p0 (%r bp)     ○4%rsp
   mmoovvqq   %%frsa:x4,0 ,- 8%(r%raxb p)             ○5%rax
    xmlooervalqq    %--e43a02x((,%% rr%bbeppa))x,,   %%rradxx      ○6-40(%rbp)
  movq  %rdx, %rsi                ○7%rsi
   mcoavlql   %srtarxc,p y% rdi        ○8movq  %rax, %rdi
  leaq  -32(%rbp), %rax             ○9leaq
    mmmooovvvqll    %$$r.0aL,xC ,0% ,e% ar%xse idi
  call  printf
8

<!-- ===== page 9 ===== -->

  nop
  movq  -8(%rbp), %rax     ○10movq  -8(%rbp)
  xorq  %fs:40, %rax              ○11%fs:40, %rax
   jceal l. L2  __st ack_ chk_ fail      ○ 12.L2
.L2:                注：下面这种回答也对：
  Leave              ○10movq  %fs:40
  .cfi_def_cfa 7, 8        ○11-8(%rbp), %rax
  .LFEr.0ec:tf  i_endproc
   ..ssiezcet ionm ypr.irnotd,a t.a- myprint
. LC1.:s tring "Where am I?"
  .text
   ..gtlyopbel   aalleerrtt,  @function
a.lLeFrBt1::
   .pcufsih_qs ta%rrtbppr oc
   ..ccffii__doefff_scefta _6o,f f-s1e6t  16
   m.ocvfqi_ def%_rcsfpa,_ r%ergbips ter 6
   mcoavlll   $p.uLtCs1 , %edi
    np.oocppf qi_ def%_rcbfpa  7, 8
  ret               ○13ret
 . LFE..1cs:fi iz_ee ndaplreorct , .-alert
   ..saelcitgino n8   .rodata
.LC2:
  .string "1234567123456712345671234567\252\204\004\b"  ○14204
    ...tgtelyxoptbe l   mmaaiinn , @function
m.aLiFnB:2 :
   .pcufsih_qs ta%rrtbppr oc
   ..ccffii__doefff_scefta _6o,f f-s1e6t  16
   m.ocvfqi_ def%_rcsfpa,_ r%ergbips ter 6
   smuobvql   $%1e6d,i ,% r-s4p( %rbp)
   mmoovvql   %$r.sLiC,2 , -%1e6d(i%r bp)
  call  myprint         ○15call  myprint
   mloevalve   $0, %eax
   .rcefti _def_cfa 7, 8
 . LFE..2cs:fi iz_ee ndmparionc,  .-main

---

### 2018期中-带答案 · 第一题 4

> 出处：`原文/期中/2018期中-带答案.md` 第 86–92 行　·　模块判定：Machine Prog
> 考什么：movl/cltq/movabsq/movswq 语义

4.  在x86-64下，以下哪个选项的说法是错误的？
A) movl指令以寄存器作为目的时，会将该寄存器的高位4字节设置为0
B) cltq指令的作用是将%eax符号扩展到%rax
C) movabsq指令只能以寄存器作为目的
D) movswq指令的作用是将零扩展的字传送到四字节目的
答案：D
movswq应该是符号扩展

---

### 2018期中-带答案 · 第一题 7

> 出处：`原文/期中/2018期中-带答案.md` 第 127–138 行　·　模块判定：Machine Prog
> 考什么：控制结构的机器码实现（jmp/cmov/跳转表）

7.  下列关于程序控制结构的机器代码实现的说法中，正确的是：
A)  使用条件跳转（conditional jump）语句实现的程序片段比使用条件赋值
（conditional move）语句实现的同一程序片段的运行效率高
B)  使用条件跳转语句实现的程序片段与使用条件赋值语句实现的同一程序片段
虽然效率可能不同，但在C语言的层面上看总是有着相同的行为
C)  一些switch语句不会被gcc用跳转表的方式实现
D)  以上说法都不正确
答案：C。条件跳转本身开销大于条件赋值，但条件赋值会将两个分支中的运算都
完成，故分支中的运算较为复杂时，使用条件赋值语句实现的程序效率较低，故a
错误。分支中的运算带有副作用时，条件跳转语句和条件赋值语句实现的程序行为
不同，故b错误。switch语句中的case若比较稀疏，则不会被用跳转表的方式实
现，故c正确。

---

### 2018期中-带答案 · 第一题 8

> 出处：`原文/期中/2018期中-带答案.md` 第 139–152 行　·　模块判定：Machine Prog
> 考什么：条件码的读写与改变

8.  下列关于条件码的描述中，不正确的是（）
A)  所有算术指令都会改变条件码
B)  所有比较指令都会改变条件码
C)  所有与数据传送有关的指令都会改变条件码
4

<!-- ===== page 5 ===== -->

D)  条件码一般不会直接读取，但可以直接修改
答案：C，leaq是movq指令的变形，它只传送地址，不改变条件码。
答案修订：ABCD均给分。
  AB没有指明是x86指令系统；x86指令系统中有SIMD类指令不改变条件码；
  C 数据传送一般不改变条件码；
  D 正确，SAHF、STC、CLC、CMC等指令均可以直接写条件码。

---

### 2018期中-带答案 · 第三题 2、3

> 出处：`原文/期中/2018期中-带答案.md` 第 380–439 行　·　模块判定：Machine Prog
> 考什么：结构体访问汇编填空与汇编反推 C 代码

2、当N=4时，该数据结构初始化代码如下：
void init(int n)
{
        int i;
        for (i=0; i<n; i++) {
                t1[i].ip = &(t1[i].ii[i]);
        }
}
根据上述代码，填写下面汇编中缺失的内容：
init:
        movl    $0, %ecx
12

<!-- ===== page 13 ===== -->

        jmp     .L2
.L3:
        movslq  %ecx, %rax
        leaq    (  (1)   ,%rax,8), %rsi
        leaq    0(,%rsi,4), %rdx
        addq    $t1+4, %rdx
        salq      (2)   , %rax
        movq      (3)   , (  (4)   )
        addl    $1, %ecx
.L2:
        cmpl      (5)   , %ecx
        jl      .L3
        rep ret
答案：
（1）%rax（2）$5 （3）%rdx （4）t1+24(%rax) （5）%edi
答案修订：(4) 全给分，卷面多了一对括号。
3、当N=3时，函数fun的汇编代码如下：
fun:
        movslq  %esi, %rax
        movslq  %edi, %rdi
        leaq    (%rdi,%rdi), %rdx
        leaq    (%rdx,%rdi), %r8
        leaq    (%r8,%r8), %rcx
        addq    %rcx, %rax
        movl    %esi, t1+4(,%rax,4)
        addq    %rdx, %rdi
        leaq    0(,%rdi,8), %rax
        movq    t1+16(%rax), %rax
        movl    %esi, (%rax)
        ret
根据上述代码，填写函数fun的C语言代码：
void fun(int x, int y)
{
  (1)   =   (2)   ;
          (3)   =   (4)   ;
13

<!-- ===== page 14 ===== -->

}
答案：
（1）t1[x].ii[y]
（2）y
（3）*(t1[x].ip)
（4）y

---

### 2019期中-带答案 · 第一题 4

> 出处：`原文/期中/2019期中-带答案.md` 第 111–131 行　·　模块判定：Machine Prog
> 考什么：x86-64 指令 idivq/jmp/shr/leaq 辨析

4.  以下关于x86-64指令的描述，说法正确的有几项？
a)  有符号除法指令idivq S将%rdx（高64位）和%rax（低64位）中的
128位数作为被除数，将操作数S的值作为除数，做有符号除法运算；指
令将商存在%rdx寄存器中，将余数存在%rax寄存器中。
b)  我们可以使用指令 jmp %rax 进行间接跳转，跳转的目标地址由寄存
器%rax的值给出。
c)  算术右移指令 shr 的移位量既可以是一个立即数，也可以存放在单字节
寄存器%cl中。
d)  leaq指令不会改变任何条件码。
3

<!-- ===== page 4 ===== -->

A. 1
B. 2
C. 3
D. 4
答案：A
本题考察x86-64中的一些基本指令，答案为A。a项错误，原因是idivq将余
数存在%rdx中，将商存在%rax里。b项错误，间接跳转的正确书写格式应为jmp
*%rax。C项错误，算术右移指令应为sar。

---

### 2019期中-带答案 · 第一题 5

> 出处：`原文/期中/2019期中-带答案.md` 第 132–141 行　·　模块判定：Machine Prog
> 考什么：call 后栈上第 k 个参数的地址

5.  已知函数func的参数超过6个。当x86-64机器执行完指令call func之
后，%rsp的值为S。那么func的第k(k > 6)个参数的存储地址是？
A. S + 8 * (k - 6)
B. S + 8 * (k - 7)
C. S – 8 * (k - 6)
D. S – 8 * (k - 7)
答案：A
本题考察x86-64运行时栈帧结构，答案为A。当执行完call指令后，S处存储
的是函数的返回地址；再往上依次是第7、第8个函数参数…故第k个函数参数存
储在S + 8 * (k - 6)的地址处。

---

### 2019期中-带答案 · 第一题 6

> 出处：`原文/期中/2019期中-带答案.md` 第 142–154 行　·　模块判定：Machine Prog
> 考什么：cmpq 后 jg 跳转的条件码表达式

6.  X86-64指令提供了一组条件码寄存器；其中ZF为零标志，ZF=1表示最近的
操作得出的结构为0；SF为符号标志，SF=1表示最近的操作得出的结果为负
数；OF为溢出标志，OF=1表示最近的操作导致一个补码溢出（正溢出或负溢
出）。当我们在一条cmpq指令后使用条件跳转指令jg时，那么发生跳转等价
于以下哪一个表达式的结果为1？
A. ~(SF ^ OF) & ~ZF
B. ~(SF ^ OF)
C. SF ^ OF
D. (SF ^ OF) | ZF
答案：A。本题考察x86-64条件码，答案为A。cmpq a, b相当于通过b – a
的值来设置条件码。SF ^ OF为1表示b < a（减法结果要么负溢出要么为负
数），于是~(SF ^ OF)表示b >= a，再与上b != a的条件（~ZF），就可以得
到最终结果(b > a)。

---

### 2019期中-带答案 · 第一题 7

> 出处：`原文/期中/2019期中-带答案.md` 第 155–169 行　·　模块判定：Machine Prog
> 考什么：函数指针数组的 sizeof

7.  考虑以下C语言变量声明：
int *(*f[3])();
那么在一台x86-64机器上，sizeof(f)和sizeof(*f)的值是多少？
A. 8 24
B. 24 8
C. 8 8
D. 8 不确定
4

<!-- ===== page 5 ===== -->

答案：B 本题考察指针和数组的存储方式，答案为B。f是一个数组，每个元素都
是一个函数指针，指向返回值为int *的函数。对于f而言，sizeof(f)返回整
个指针数组的大小，为3 * 8 = 24；对于*f而言，它是f[0]元素，是一个指
针变量，大小为8。

---

### 2019期中-带答案 · 第一题 8

> 出处：`原文/期中/2019期中-带答案.md` 第 170–180 行　·　模块判定：Machine Prog
> 考什么：栈帧定长、编译时确定大小

8.  大多数过程的栈帧是____的，其长度在____时确定。（注：此处的编译指从高
级语言转化为汇编语言的过程）
A.  定长，编译
B.  定长，汇编
C.  可变长，汇编
D.  可变长，运行
答案：A。
说明：大多数过程的栈帧是定长的，在过程开始时通过减小栈指针的方式分配，
减小的大小由编译器在编译时计算。大家常常在汇编代码中过程的开头看到
“subq $24, %rsp”，就是编译器计算出了栈帧大小并写在了汇编代码里。（书
P165）

---

### 2019期中-带答案 · 第一题 9

> 出处：`原文/期中/2019期中-带答案.md` 第 181–188 行　·　模块判定：Machine Prog
> 考什么：pushq %rbp 的等价指令序列

9.  pushq %rbp的行为等价于以下（）中的两条指令。
A.  subq  $8, %rsp   movq  %rbp,  (%rdx)
B.  subq  $8, %rsp   movq  %rbp,  (%rsp)
C.  subq  $8, %rsp   movq  %rax,  (%rsp)
D.  subq  $8, %rax   movq  %rbp,  (%rdx)
答案：B。
说明：x86-64系统中，pushq %rbp 指令将栈指针减8，并向其中存入%rbp寄
存器的值（书P127）

---

### 2019期中-带答案 · 第三题

> 出处：`原文/期中/2019期中-带答案.md` 第 294–387 行　·　模块判定：Machine Prog
> 考什么：C 与 x86-64 汇编填空：栈帧、strcpy、结构体

第三题 机器级编程（15分，每空1分）
下面的C程序包含main(), caller(), callee()三个函数。本题给出了该程序的部
分C代码和X86-64汇编与机器代码。请分析给出的代码，补全空白处的内容，并回答问题。
注：汇编与机器码中的数字用16进制数填写
X86-64汇编与机器代码：                答案填写处：
00000000004006cd <caller>:
  4006cd: 55                   push     %rbp
  4006ce: 48 89 e5               mov      %rsp,   %rbp
  4006d1: 48 83 ec 50            sub      $0x50,   %rsp
  4006d5: 48 89 7d b8            mov      %rdi,   -0x48(%rbp)
  4006d9: 64 48 8b 04 25 28 00    mov      %fs:0x28,  %rax
  4006e0: 00 00
  4006e2: 48 89 45 f8            mov      %rax,   -0x8(%rbp)
  4006e6: 31 c0                  xor      %eax,   %eax
  4006e8: c6 45 d0 00            movb     $0x0,   -0x30(%rbp)
  4006ec: c6 45 e0 00            movb     $0x0,    (1)      (1)
  4006f0: 48 8b 45 b8            mov      _(2) ,   %rax     (2)
  4006f4: 48 89 c7               mov      %rax,   %rdi
  4006f7:                   callq    400510 <strlen@plt>
  4006fc:  89 45 cc               mov      _(3) ,   -0x34(%rbp)    (3)
  4006ff:  83 7d cc 0e            cmpl     $0xe,   -0x34(%rbp)
  400703: 7f _(4) _                 jg       400752 <caller+0x85>   (4)
  400705: 83 7d cc 09            cmpl     $0x9,   -0x34(%rbp)
  400709:                       jg       400720 <caller+0x53>
  40070b: 48 8b 55 b8            mov      -0x48(%rbp), %rdx
  40070f: 48 8d 45 d0            lea      _(5) ,   %rax        (5)
  400713: 48 89 d6               mov      %rdx,   %rsi
  400716: 48 89 c7               mov      %rax,   %rdi
  400719:                   callq    400500 <strcpy@plt>
  40071e:                      jmp      40073b <caller+0x6e>
  400720: 48 8b 45 b8            mov      -0x48(%rbp), %rax
  400724: 48 8d 50 0a            lea      0xa(%rax),  %rdx
  400728: 48 8d 45 d0            lea      -0x30(%rbp), %rax
  40072c: 48 83 c0 10            add       (6) ,   %rax     (6)
10

<!-- ===== page 11 ===== -->

  400730: 48 89 d6               mov      %rdx,   %rsi
  400733: 48 89 c7               mov      %rax,   %rdi
  400736:                   callq    400500 <strcpy@plt>
  40073b: ff 75 e8               pushq    -0x18(%rbp)
  40073e: ff 75 e0               pushq    -0x20(%rbp)
  400741: ff 75 d8               pushq    -0x28(%rbp)
  400744: ff 75 d0               pushq    -0x30(%rbp)
  400747: e8 _ (7) _           callq    400666 <callee>     (7)
  40074c: 48 83 c4 20            add      $0x20,   %rsp
  400750:                      jmp      400753 <caller+0x86>
  400752: 90                     nop
  400753: 48 8b 45 f8            mov       (8) ,   %rax      (8)
  400757: 64 48 33 04 25 28 00    xor      %fs:0x28,  %rax
  40075e: 00 00
  400760:                       je       400767 <caller+0x9a>
  400762:                   callq    400520 <__stack_chk_fail@plt>
  400767: c9                     leaveq
  400768: c3                     retq
C代码：                                                 答案填写处：
#include <stdio.h>
#include "string.h"
#define N   _(9)_                                  (9)         __
#define M   _(10)_                                 (10)       __
typedef union {char str_u[N]; long l;} union_e;
typedef struct {char str_s[M]; union_e u; long c;} struct_e;
void callee(struct_e s){
 char buf[M+N];
 strcpy(buf, s.str_s);
 strcat(buf, s.u.str_u);
 printf("%s \n",buf);
}
11

<!-- ===== page 12 ===== -->

void caller(char *str){
 struct_e s;
 s.str_s[0]=‘\0’;
 s.u.str_u[0]=’\0’;
 int len = strlen(str);
 if(len>=  M+N)
  _(11)_;                       (11)
 else if(len<N){
  strcpy(s.str_s, _(12)_);                  (12)
 }
 else{
  strcpy(s.u.str_u,_(13)_);                (13)
 }
 callee(s);
}
int main(int argc, char *argv[]){
 caller("0123456789abcd");
 return 0;
}
caller函数中，变量s 所占的内存空间为:         (14)
该程序运行后，printf函数是否有输出？输出结果为:     (15)

---

### 2020期中-带答案 · 第一题 1

> 出处：`原文/期中/2020期中-带答案.md` 第 52–62 行　·　模块判定：Machine Prog
> 考什么：二维数组元素访问的寻址方式 addl

1、某C语言程序中对数组变量a的声明为“int a[10][10];”，有如下一段代
码：
for (i=0; i<10; i++)
for (j=0; j<10; j++)
     sum+= a[i][j];
假设执行到“sum+= a[i][j];”时，sum的值在%rax中，a[i][0]所在的地址
在%rdx中，j在%rsi中，则“sum+= a[i][j];”所对应的指令是（  A   ）。
A. addl 0 (%rdx, %rsi, 4), %eax
B. addl 0 (%rsi, %rdx, 4) , %eax
C. addl 0 (%rdx, %rsi, 2) , %eax
D. addl 0 (%rsi, %rdx, 2) , %eax

---

### 2020期中-带答案 · 第一题 2

> 出处：`原文/期中/2020期中-带答案.md` 第 63–69 行　·　模块判定：Machine Prog
> 考什么：条件码与 set/cmp/test/leaq 指令

2、条件码描述了最近一次算术或逻辑操作的属性。下列关于条件码的叙述中，哪
一个是不正确的？（   C   ）
A. set指令可以根据条件码的组合将一个字节设置为0或1
B. cmp指令和test指令可以设置条件码但不更改目的寄存器
C. leaq指令可以设置条件码CF和OF
D. 除无条件跳转指令jmp外，其他跳转指令都是根据条件码的某种组合跳转到标
号指示的位置

---

### 2020期中-带答案 · 第一题 3

> 出处：`原文/期中/2020期中-带答案.md` 第 70–82 行　·　模块判定：Machine Prog
> 考什么：静态数组与指针数组的地址计算

3、假定静态int型二维数组a和指针数组pa的声明如下：
static int a[4][4]={ {3, 8, -2, 6}, {2, 1, -5, 3 }, {1, 18, 4,
10},{4, -2, 0, 8}};
2

<!-- ===== page 3 ===== -->

static int *pa[4]={a[0], a[1], a[2], a[3]};
若a的首地址为0x601080，则&pa[0]和pa[1]分别是:A
A. 0x6010c0、0x601090
B. 0x6010e0、0x601090
C. 0x6010c0、0x6010a0
D. 0x6010e0、0x6010a0

---

### 2020期中-带答案 · 第一题 4

> 出处：`原文/期中/2020期中-带答案.md` 第 83–88 行　·　模块判定：Machine Prog
> 考什么：x86-64 过程调用与栈帧释放

4、下列关于x86-64过程调用的叙述中，哪一个是不正确的？C
A. 每次递归调用都会生成一个新的栈帧，空间开销大
B. 当传递给被调用函数的参数少于6个时，可以通过通用寄存器传递
C. 被调用函数要为局部变量分配空间，返回时无需释放这些空间
D. 过程调用返回时，向程序计数器中推送的地址是调用函数中调用指令的下一条
指令的地址

---

### 2020期中-带答案 · 第一题 5

> 出处：`原文/期中/2020期中-带答案.md` 第 89–102 行　·　模块判定：Machine Prog
> 考什么：结构体成员偏移与 movl/leaq 选择

5、假设结构体类型student_info的声明如下：
struct student_info {
        char id[8];
        char name[16];
        unsigned zip;
        char address[50];
        char phone[20];
}x;
若x的首地址在%rdx中，则“unsigned xzip=x.zip;”所对应的汇编指令
为:B
A. movl 0x24(%rdx), %eax
B. movl 0x18(%rdx), %eax
C. leaq 0x24(%rdx), %rax
D. leaq 0x18(%rdx), %rax

---

### 2020期中-带答案 · 第三题 1

> 出处：`原文/期中/2020期中-带答案.md` 第 233–283 行　·　模块判定：Machine Prog
> 考什么：C 与 x86-64 汇编填空：递归、参数传递

请分析下面的C语言程序和对应的x86-64汇编代码。
1.其中，有一部分缺失的代码（用标号标出），请在标号对应的横线上填写缺失的
内容。注:汇编与机器码中的数字用 16 进制数填写。
（1-11每空1分，共11分）
C语言代码如下：
typedef struct _parameters {
    int n;
    int product;
} parameters;
int bar(parameters *params, int x) {
    params->product *= x;
}
void foo (parameters *params) {
    if (params->n <= 1)
        ___（1）___                        （1）____________
    bar(params,    （2）   );             （2）____________
    params->n--;
    foo(params);
}
x86-64汇编代码如下（为简单起见，函数内指令地址只给出后四位，需要时可补
全）：（
0x0000555555555189 <bar>：
    5189: f3 0f 1e fa    endbr64
    518d: 55            push   %rbp
    518e: 48 89 e5       mov    %rsp,%rbp
    5191: 48 89 7d f8   mov    _（3）_,-0x8(%rbp)  （3）_________
    5195: 89 75 f4       mov    %esi,-0xc(%rbp)
    5198: 48 8b 45 f8   mov    -0x8(%rbp),%rax
    519c: 8b 40 04        mov    0x4(%rax),%eax
    519f: 0f af 45 f4   imul   _（4）_(%rbp),%eax  （4）_________
    51a3: 89 c2           mov    %eax,%edx
    51a5: 48 8b 45 f8    mov    -0x8(%rbp),%rax
8

<!-- ===== page 9 ===== -->

                55551111aaaa9cde::::    895c90d3       5   0       0      4                            mnprooeovptp  q        %_e（d5x）,0_x 4 (  % r a x )     （5）_________
 0    0  0  0555115ab5f35::5  5f55355  5 01 f a  f1  e <  f f oa o  > :   epnudsbhr  6 4% rbp
        55551111bbbb7b4f::::    44448888    8888399b    e7e4cd55     1ff 088                m_mm（ooovv6v  ）    _        %%-$rr00sdxxpi81,,(0%-%,r0r%bxbrp8ps ()p%, r% br p a) x     （6）_________
                55551111cccc358a::::    8874b3e8    0f38081b      04  15       f   8                   c_mm（moopvv7   ）     _     5$(-10%0fxrxb1a8 ,x(<%)%fe,roa%boxep+ a)0x,x %4rca>x    （7）_________
            555111cdde04:::   848b89   18d0b6     4  5     f  8              mmmooovvv            (%-%e0rdxax8x,()%%,er%sbeipd )x, %rax
            555111ddd69e:::   4e4888   8a89bb   cf47f5    ff f8     f  f   m moovv c   a  l  l%-qr0 ax x80,(x%%0rr0db0ip0 )5,5%5r5a5x5 555189 <bar>
            555111eee247:::   884bd8   05800b    f4 f5     f  8              lmmoeovav       -   0-(x0%1xr(8a_（(x%)8r,）b%_pe))a,,x%% erdaxx     （8）_________
    51eb: 89 10          mov   _（9）_,(%rax)       （9）__________
        5511efd1::  4488  88b9  4c57   f 8      mmoovv    _ （ %1r0a）x_, %,r%dria x       （10）_________
        5511ff94::  eeb8  0b16   f f   f f    f f j  m p  c a l l5q1 f c  _（<f1o1o）+_0 x 4 d >    （11）_________
            555111fffbcd:::   9cc093                                             nlreeoatpvq  eq
9

<!-- ===== page 10 ===== -->

---

### 2020期中-带答案 · 第三题 2

> 出处：`原文/期中/2020期中-带答案.md` 第 284–301 行　·　模块判定：Machine Prog
> 考什么：断点处栈帧地址与存储值的推断

2.在程序执行到0x000055555555518e时（该指令还未执行），此时的栈帧如下，
请填写空格中对应的值。（每空2分，共6分）
地址  值
0x7fffffffe308  0xffffe340
0x7fffffffe304  0x00000000
0x7fffffffe300  0x00000000
0x7fffffffe2fc  0x00005555
0x7fffffffe2f8  （12）_________
0x7fffffffe2f4  0x00007fff
0x7fffffffe2f0  0xffffe310
0x7fffffffe2ec  0x00007fff
0x7fffffffe2e8  0xffffe340
0x7fffffffe2e4  0x00000004
0x7fffffffe2e0  0xffffe350
0x7fffffffe2dc  0x00005555
0x7fffffffe2d8  （13）_________
0x7fffffffe2d4  0x00007fff
0x7fffffffe2d0  （14）_________

---

### 2020期中-带答案 · 第三题 3

> 出处：`原文/期中/2020期中-带答案.md` 第 302–302 行　·　模块判定：Machine Prog
> 考什么：递归函数 foo 的功能

3.当params={n,1}时，foo(&params)函数的功能是什么？（3分）

---

### 2021期中-带答案 · 第一题 5

> 出处：`原文/期中/2021期中-带答案.md` 第 106–111 行　·　模块判定：Machine Prog
> 考什么：栈的增长方向、参数对齐与金丝雀

5.在x86-64机器上，有关栈的描述中，说法不正确的是：C
A. 通过栈传递参数时，所有的数据大小都向8的倍数对齐。
B. 对一个局部变量使用地址运算符‘&’，它的 地址 可以 被 放在  栈 上。
C. 栈是向上增长（由低地址向高地址增长）的。
D. 为了保护返回地址不被破坏，通常会在栈中设置金丝雀值（stack canary）。
栈是向下增长的。

---

### 2021期中-带答案 · 第一题 6

> 出处：`原文/期中/2021期中-带答案.md` 第 112–119 行　·　模块判定：Machine Prog
> 考什么：movabsq/INC/popq/call 指令语义辨析

6.以下关于x86-64指令的描述，说法正确的是：B
A. 数据传送指令 movabsq $Imm, (%rax) 将以64位二进制补码表示的立即
数Imm放到目的地址(%rax)中。
B. INC和DEC指令会设置溢出标志OF和零标志ZF，但不会改变进位标志CF。
C. call *%rax指令以%rax中的值作为读地址，从内存中读出调用目标。
D. popq %rax指令的行为等效于movq %rsp, %rax; addq $8, %rsp。
A中movabsq的目的操作数只能是寄存器，C中%rax的值即为跳转目标，D中等
效于movq (%rsp), %rax; addq $8, %rsp。

---

### 2021期中-带答案 · 第一题 7

> 出处：`原文/期中/2021期中-带答案.md` 第 124–140 行　·　模块判定：Machine Prog
> 考什么：由 leaq/addq 汇编反推二维数组维数

7.阅读下列C代码和在x86-64机器上得到的汇编代码：
int a[__A__][__B__];
for (int i = 0; i < __C__; i++)
a[i][__C__ - i] = 1;
leaq 40(%rdi), %rax
addq $440, %rdi
.L2:
movl $1, (%rax)
addq $40, %rax
cmpq %rdi, %rax
jne  .L2
假设a的地址初始时放在%rdi中，假设程序正常运行且没有发生越界问题，则C
代码中的A、B、C处应分别填：A
A. 10、11、10
B. 9、11、9
C. 11、10、10
D. 11、11、11

---

### 2021期中-带答案 · 第三题 1

> 出处：`原文/期中/2021期中-带答案.md` 第 362–384 行　·　模块判定：Machine Prog
> 考什么：C 与 x86-64 汇编填空：递归、除法与移位

第 三题（15分）请阅读并分析下面的C语言程序和对应的x86-64汇编代码。
1. 其中，有一部分缺失的代码（用标号标出），请在标号对应的横线上填写缺失的
内C代容码。如注下:汇：编 与机器码中的数字用16进制数填写。
l{ oirnfeg t (ufnr( nl= o=mn ;g 0  n|,|  l_o_n_g（ m1)） ___)
i{ fl o(n_g_ _r(e2t) _=_ __)_ _（3）___;
}e lrseet urn ret;
{ lroentgu rrne tr e=t ; f(n - 1, m >> 1);
x}8 6}- 64汇编代码如下（为简单起见，函数内指令地址只给出后四位，需要时可补
全0）x：00 00555555555149 <f>:
            5551114449de:::    f54358    08 f9    1e  e5     f  a                                epmnuodsvbh  r   6  4_% _r （bp4 ）__,%rbp
            555111555159:::    444888   888399   e77cd5   2ee080                                 smmuoobvv            $%%0rrxds2ii0,,,--%00rxxs12p80 ((%%rrbbpp))
            555111566d24:::    474848   8_83_3（  775dd）  ee_80_   00  01                        ccjmmepp qq          $$_00_xx（016,,）--00_xx_12 80 ((%%rrbbpp))
5551116669bf:::    74e58b   0856bf     4  5     e    0                               jmjnomevp            5_51_17d（107  ）<<ff_++_00(xx%28r87b>>p  ),%rax
13

<!-- ===== page 14 ===== -->

555551111177777158bd:::::      4847483848     8e8?8b05?b      40c5 5105        ee    00                                                      matjmoneeovds v   t                _$--%_000r（xxxa122x8,00,）%((%e%%r_arra_xbbx  pp )),,%%rradxx
555511118888147a::::     44448888    8008911d    dcd50000       0   1                                            maaloddevdda                %%0%rrxrdd1axx(x,,%,%%r%rraraaxaxx)x,   %rdx
55555511111189999a9e26c1::::::       4444e4888888      8888a8b39989      4edcf45867f5        e0ff  81f8           f       f                                              msmmcmouooaovbvvlv    l      q            $_%%-50_rr01xaa（x41xx199,,,8 ）%%-(<rr0%f_adxr>_xi8b,   (p%%)rr,sb%ipr )a x
5555511111aaaab59bf2:::::      4e4448b888     828d8b5b19      44fc 5582        fe    80                                                      mjm_momo_o（vpvv    1        0    ）5%--1r00_daxx_0x82   ,(0 <%%( frr%%+dbrr0xpbax )px8,) 7%,>r% arxa x
55551111bbbc59d0::::     44448888    8888b399    4edc5867      e0  81                                            msmmouoovbvv                $_%-0_r0xa（x1x19,,8）%%(rr%_adr_xib,  p%)r,s%ir ax
5555511111dcccd138c0:::::      e44cc88893       888  19b       f44    f55       fff  f00           f    f                                    cmmlraooeelvvatl  vq  qe     q     %-5 r01ax4x19,0 -(<0%fxr>1b 0p()%,r%brpa)x

---

### 2021期中-带答案 · 第三题 2

> 出处：`原文/期中/2021期中-带答案.md` 第 389–404 行　·　模块判定：Machine Prog
> 考什么：断点处栈内容与栈帧布局

2. 已知在调用函数f(7,6)时，我们在gdb中使用b f指令在函数f处加上了
断点，下面是程序某一次运行到断点时从栈顶开始的栈的内容，请在空格中填入相
应的值。（U表示不要求填写）
0x7fffffffe558  0x00005555555551c8
0x7fffffffe550  （11）______
0x7fffffffe548  U
0x7fffffffe540  U
0x7fffffffe538  U
0x7fffffffe530  （12）______
0x7fffffffe528  （13）______
0x7fffffffe520  0x00007fffffffe550
0x7fffffffe518  U
0x7fffffffe510  U
0x7fffffffe508  （14）______
0x7fffffffe500  0x0000000000000010
0x7fffffffe4f8  0x00005555555551c8

---

### 2021期中-带答案 · 第三题 3

> 出处：`原文/期中/2021期中-带答案.md` 第 405–405 行　·　模块判定：Machine Prog
> 考什么：递归函数 f(7,6) 的返回值

3. 运行函数f(7,6)后得到的值是多少？ （15）_________

---

### 2021期中-带答案 · 第六题 1

> 出处：`原文/期中/2021期中-带答案.md` 第 639–656 行　·　模块判定：Machine Prog
> 考什么：struct/union 的大小与末尾 padding

第六题（15分）
struct s_element{
union u_inner{
    float f;
    short s[2];
} u1;
    s_element* next;
};
float func(s_element* p){
    float ans = 0;
    while( p ){
        ans += p->u1.f;
        p = p->next;
    }
    return ans;
}
1.  若 tmp 是一个 s_element 类型的变量 ,  则 sizeof  (tmp.u1)  =
_________。（1分）

---

### 2021期中-带答案 · 第六题 2

> 出处：`原文/期中/2021期中-带答案.md` 第 657–657 行　·　模块判定：Machine Prog
> 考什么：链表求和函数的功能

2. 简述函数func的功能。（2分）

---

### 2021期中-带答案 · 第六题 3

> 出处：`原文/期中/2021期中-带答案.md` 第 658–665 行　·　模块判定：Machine Prog
> 考什么：补全链表遍历汇编，含结构体对齐

3. 函数func循环部分的汇编代码如下，补全汇编代码：（2分）
提示：vaddss S1, S2, D实现单精度浮点数加法D ← S1+S2
L1:
  vaddss   (%rdx), %xmm0, %xmm0
______________________________
L2:
  testq    %rdx, %rdx
  jne L1

---

### 2022期中-带答案 · 第一题 6

> 出处：`原文/期中/2022期中-带答案.md` 第 120–125 行　·　模块判定：Machine Prog
> 考什么：mov指令操作数大小与合法寻址方式

6.如下汇编语句不会产生错误信息的是（    ）
A．movq %rax, $0x123
B．movl %rax, (%rsp)
C．movb %al, %sl
D．movw %si, 8(%rbp)
答案：D

---

### 2022期中-带答案 · 第一题 7

> 出处：`原文/期中/2022期中-带答案.md` 第 126–142 行　·　模块判定：Machine Prog
> 考什么：由lea指令序列反推C表达式

7.考虑下面的C语言代码，我们省略了被计算的表达式：
long scale2(long x, long y, long z){
long t = __________________________;
return t;
}
用GCC编译实际的函数得到如下的汇编代码：
scale2:
    leaq  (%rdi, %rdi, 2), %rax
    leaq  (%rax, %rsi, 4), %rax
    leaq  (%rax, %rdx, 8), %rax
    ret
则C代码中缺失的表达式是（     ）
A. ((x + 2) + y + 4) + z + 8
B. 3*x + 4*y + 8*z
C. ((z + 2) + y + 4) + x + 8
D. 3*z + 4*y + 8*x
答案：B

---

### 2022期中-带答案 · 第一题 8

> 出处：`原文/期中/2022期中-带答案.md` 第 143–161 行　·　模块判定：Machine Prog
> 考什么：cmp/set指令后缀与data_t类型匹配

8.考虑下面的C语言代码：
int comp(data_t a, data_t b){
return a COMP b;
}
代码给出了数据a和b之间比较的一般形式，这里参数的数据类型data_t为某
种有符号或无符号的整数类型。COMP操作通过#define进行定义。假设a在%rdi
中某个部分，b在%rsi某个部分。对于下面每个指令序列，组合和描述正确的是
（    ）
4

<!-- ===== page 5 ===== -->

  指令序列  data_t  COMP      指令序列  data_t  COMP
cmpl %esi,%edi  cmpw %si,%di
A  setl %al  long  ＜  B  setge %al  short  ≥
  指令序列  data_t  COMP      指令序列  data_t  COMP
cmpb %sil,%dil  cmpq %rsi,%rdi
C  setbe %al  char  ≤  D  setne %al  int  !＝
答案：B，ACD分别应该是int、unsigned char和long

---

### 2022期中-带答案 · 第一题 9

> 出处：`原文/期中/2022期中-带答案.md` 第 162–170 行　·　模块判定：Machine Prog
> 考什么：结构体对齐填充与总大小计算

9.下列结构体的总大小字节数为 A，重新排列优化后的最小字节数是 B，则 A-B=
（    ）
struct {
    char *a;  short b;  double c;  short d;
    float e;  char  f;  long    g; int    h;
}rec;
A. 12             B. 15
C. 16             D. 19
答案：C（56-40）。有同学可能忽略padding，从而算成52-37=15

---

### 2022期中-带答案 · 第一题 10

> 出处：`原文/期中/2022期中-带答案.md` 第 171–176 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出攻击的防护手段

10.下面列举了若干技术改进方案，其中不能防止缓冲区溢出攻击的是（     ）
A. 使用金丝雀值（canary）支持对栈破坏检测。
B. 支持变长栈帧。
C. 限制可执行代码区域。
D. 地址空间布局随机化（ASLR）。
答案：B

---

### 2022期中-带答案 · 第三题

> 出处：`原文/期中/2022期中-带答案.md` 第 352–420 行　·　模块判定：Machine Prog
> 考什么：switch跳转表汇编还原C代码与结构体

第三题 下列的C代码描述了一个switcher：
struct prob{
  long *p;
  struct { long x; long y; long z;}s;
  struct prob *next;
};
void switcher(long a, long b, long c, struct prob *sp){
  long val;
  switch(a){
    case ①            : c = ⑧                ;
    case ②            : val = ⑨              ; break;
    case ③            : c = ⑩               ;
    case ④            : val = ⑪              ; break;
    case ⑤            : val = ⑫               ; break;
    case ⑥            : ⑬                  ;break;
    case ⑦            : val = ⑭                ;break;
    default: ⑮                ; break;
  }
  sp->s.y = val;
}
采用GCC编译器产生的汇编代码如下所示，请根据此进行分析，补全上述代码。
switcher:
        cmpq    $7, %rdi
        ja      .L2
        jmp     *.L4(,%rdi,8)
.L4:
        .quad   .L3
        .quad   .L5
        .quad   .L6
        .quad   .L7
        .quad   .L2
        .quad   .L8
        .quad   .L9
        .quad   .L10
11

<!-- ===== page 12 ===== -->

.L8:
        movq    %rsi, %rdx
        xorq    $31, %rdx
.L6:
        leaq    2022(%rdx), %rax
        movq    %rax, 16(%rcx)
        ret
.L3:
        subq    $54, %rdx
.L5:
        addq    %rdx, %rsi
        leaq    (%rsi,%rsi,2), %rax
        movq    %rax, 16(%rcx)
        ret
.L7:
        movq    8(%rcx), %rax
        movq    %rax, 16(%rcx)
        ret
.L10:
        movq    $1898, 24(%rcx)
        movq    %rax, 16(%rcx)
        ret
.L9:
        movq    (%rcx), %rax
        movq    (%rax), %rax
        movq    %rax, 16(%rcx)
        ret
.L2:
        movq    %rcx, 32(%rcx)
        movq    %rax, 16(%rcx)
        ret

---

### 2023期中-带答案 · 第一题 4

> 出处：`原文/期中/2023期中-带答案.md` 第 102–117 行　·　模块判定：Machine Prog
> 考什么：x86-64 mov指令操作数与寄存器的合法组合

4. 以下 x86-64 汇编指令中，正确的是
①  movw  $0x40  (%eax)
②  movb  %dl  %sl
③  movb  %spl  %al
④  movq  %rax  %rsi
⑤  movw  (%rcx)  %dx
⑥  movl  %rsp  (%r8)
A.①③⑤
B.②④⑥
C.③④⑤
D.①⑤⑥
3

<!-- ===== page 4 ===== -->

答案：C

---

### 2023期中-带答案 · 第一题 5

> 出处：`原文/期中/2023期中-带答案.md` 第 118–138 行　·　模块判定：Machine Prog
> 考什么：数组寻址lea指令与下标反推

5.有如下函数（包含一处空缺，用__表示）:
long func1(long a[][3], long x, long y) {
    return a[x*2+y][__];
}
该函数经gcc –Og编译后得到如下x86-64汇编代码
// x86_64 Linux calling convension
// return: RAX
// parameters: RDI, RSI, RDX, RCX
// sizeof(int) = 4
// sizeof(long) = 8
func1(long (*) [3], long, long):
        leaq    (%rdx,%rsi,2), %rax
        leaq    (%rax,%rax,2), %rax
        movq    48(%rdi,%rax,8), %rax
        ret
则空缺处应为：
A.0
B.2
C.4
D.6
答案：D

---

### 2023期中-带答案 · 第一题 6

> 出处：`原文/期中/2023期中-带答案.md` 第 139–153 行　·　模块判定：Machine Prog
> 考什么：cmp/test/set与条件传送指令语义

6.以下说法中错误的是：
A.cmpq %rsi, %rdi setl %al连续执行这两条指令的效果是如果%rsi的值
小于%rdi，则将%al设置为1。
B.testq %rax, %rax sete %al连续执行这两条指令的效果是如果%rax中
的值等于0，则将%al设置为1。
C.条件传送指令的源和目的操作数可以为16/32/64位寄存器，但是不支持单字
节传送。
D.set*（如sete, setne, seta） 指令中的目的操作数只能是一个低位单字
4

<!-- ===== page 5 ===== -->

节寄存器，该指令会根据条件是否成立将一个字节设置为0或1。
答案：A，应该是%rdi的值小于%rsi，B、C、D正确，具体见CSAPP中对应指令
的定义。

---

### 2023期中-带答案 · 第一题 7

> 出处：`原文/期中/2023期中-带答案.md` 第 154–160 行　·　模块判定：Machine Prog
> 考什么：call指令将返回地址压栈

7.考虑在x86-64 + Linux情景，在使用call指令进行过程/函数调用时，计
算机会做如下哪一条描述的事情：
A. 将此call指令的下一条指令的地址放入栈中
B. 将此call指令的下一条指令的地址放入%rsp寄存器中
C. 将此call指令的地址放入栈中
D. 将此call指令的地址放入%rsp寄存器中
答案：A

---

### 2023期中-带答案 · 第一题 8

> 出处：`原文/期中/2023期中-带答案.md` 第 161–176 行　·　模块判定：Machine Prog
> 考什么：struct/union对齐与成员偏移

8.在x86-64架构、Linux操作系统下，有如下C定义。
  struct {
  union {
      short s1;
      char c[3];
  } u;
  double d;
  short s2;
  } s;
考虑使用GCC默认选项进行编译，下列逻辑表达式为真的是：
A. sizeof s.u == 3
B. sizeof s.u == 8
C. (&s.s2 - &s.u.s1) == 8
D. (&s.s2 - &s.u.s1) == 16
答案：C
sizeof s.u应为4。

---

### 2023期中-带答案 · 第一题 9

> 出处：`原文/期中/2023期中-带答案.md` 第 181–189 行　·　模块判定：Machine Prog
> 考什么：指针数组声明的sizeof计算

 9.在 x86-64 架构、LINUX 操作系统下，有如下 C 定义。那么 sizeof A +
sizeof *A + sizeof **A + sizeof ***A的值为？
   int (*A[2])[3];
A. 40
B. 44
C. 48
D. 84
 答案：A
16 + 8 + 12 + 4 = 40。

---

### 2023期中-带答案 · 第一题 12

> 出处：`原文/期中/2023期中-带答案.md` 第 211–239 行　·　模块判定：Machine Prog
> 考什么：栈帧布局与缓冲区溢出对局部变量的影响

12.缓冲区溢出不仅会破坏返回地址，也有可能破坏局部变量。在 x86-64 架构、
LINUX操作系统下，对于给出的C代码和汇编代码，下列说法错误的是？
 int foo(char *s) {  int foo(char *s)
     int a = 0x1;  s in %rdi
     char c[4];  foo:
     strcpy(c, s);  55                   push    %rbp
     return a;  48 89 e5              mov     %rsp,%rbp
 }  48 83 ec 20           sub     $0x20,%rsp
   48 89 7d e8           mov     %rdi,-
 int main() {  0x18(%rbp)
     char s[8] = "01234567";  c7 45 fc 01 00 00 00  movl    $0x1,-
     printf("%x\n", foo(s));  0x4(%rbp)
     return 0;  48 8b 55 e8           mov     -
 }  0x18(%rbp),%rdx
  48 8d 45 f8           lea     -
  0x8(%rbp),%rax
  48 89 d6              mov     %rdx,%rsi
  48 89 c7              mov     %rax,%rdi
  e8 cd fe ff ff        call    strcpy
  8b 45 fc              mov     -
  0x4(%rbp),%eax
  c9                    leave
  c3                    ret
A. %rbp被用作帧指针，便于局部变量寻址
B. leave指令具有释放整个栈帧的效果
C. 函数foo的返回值为0x37363534
D. 函数foo的返回地址未被破坏
答案：D
注意字符串结尾有‘\0’。

---

### 2023期中-带答案 · 第三题

> 出处：`原文/期中/2023期中-带答案.md` 第 460–507 行　·　模块判定：Machine Prog
> 考什么：递归函数ncr的C与汇编代码补全

第 三题（15分）一个函数的C语言代码和汇编代码分别如下，请分别补全对应的
代码内容：
i{n t ncr(int n, int r)
  if (n<r)  return   （1）   ;
  if (r==0) return   （2）   ;
  if (r==1) return   （3）   ;
   if (n==1) return   （4）   ;
 }  return ncr(n-1, r-1) + ncr(n-1, r);
 0000000000001149 <ncr>:
    1149:  f3 0f 1e fa           endbr64
        111144de::   5458   8 9   e 5                            pmuosvh       % r （sp5,）%r  b p
        11115512::   5438   8 3   e c    1 8                     psuusbh       $ 0 （x168）,%  r s p
        11115569::   8899  77d5  eec8                            mmoovv        %%eedsii,,--00xx1148((%%rrbbpp))
    115c:  8b 45 ec              mov    -0x14(%rbp),%eax
            111111566f24:::    37bbd8   400570    e0 80     0  0      0  0                       cjmmgopev            1$-1006xxb01 ,8<%(ne%carrxb +p0)x,2%2e>a x
        1111669b::   e8b3  570d   e 8   0 0                      jcmmpp l      1$10bxb0 ,<-n0cxr1+80(x%7r2b>p )
        111167f1::   7b58  0071   0 0   0 0    0 0               jmnoev        1$107x81 ,<%necarx +0x2f>
    1176:  eb 43                  jmp    11bb <ncr+0x72>
        1111778c::   8735  70d5   e 8   0 1                      cjmnpel       1$108x31 ,<-n0cxr1+80(x%3rab>p )
        111178e1::   8ebb  4358   e c                            mjomvp        1-10bxb1 4<(n%crrb+p0)x,7%2e>a x
16

<!-- ===== page 17 ===== -->

    1183:  83 7d ec 01           cmpl   $0x1,-0x14(%rbp)
    1187:  75 07                  jne    1190 <ncr+0x47>
    1189:  b8 01 00 00 00        mov    $0x1,%eax
    118e:  eb 2b                  jmp    11bb <ncr+0x72>
    1190:  8b 45 e8              mov    -0x18(%rbp),%eax
    1193:  8d 50 ff              lea     （7）  (%rax),%edx
    1196:  8b 45 ec              mov    -0x14(%rbp),%eax
    1199:  83 e8 01              sub    $0x1,%eax
    119c:  89 d6                  mov    %edx, （8）
    119e:  89 c7                  mov    %eax, （9）
    11a0:  e8 a4 ff ff ff        call   1149 <ncr>
    11a5:  89 c3                  mov    %eax,%ebx
    11a7:  8b 45 ec              mov    -0x14(%rbp),%eax
    11aa:  8d 50 ff              lea    -0x1(%rax),%edx
    11ad:  8b 45 e8              mov    -0x18(%rbp),%eax
    11b0:  89 c6                  mov      （10）  ,%esi
    11b2:  89 d7                  mov      （11）  ,%edi
    11b4:  e8 90 ff ff ff        call   1149 <ncr>
    11b9:  01 d8                  add      （12）  ,%eax
    11bb:  48 8b 5d f8           mov    -0x8(%rbp),%rbx
    11bf:  c9                     leave
    11c0:  c3                       （13）
调用ncr( 5, 2)的返回结果为：  （14）
调用ncr(10, 3)的返回结果为：  （15）

---

### 2024期中-带答案 · 第一题 4

> 出处：`原文/期中/2024期中-带答案.md` 第 81–124 行　·　模块判定：Machine Prog
> 考什么：结构体对齐与指针数组声明的sizeof/指针差

4.在 x86-64 架构、Linux 操作系统下，有如下代码：
#include <stdio.h>
struct student {
    int id;
    char name[6];
    short age;
    char gender;
    float score;
};
int main() {
    struct student s;
    struct student* (*p[8])[4];
    printf("%lu\n", sizeof(s));
    printf("%lu\n", sizeof(**p));
    printf("%lu\n", (char*)&p[2] - (char*)p);
    printf("%lu\n", &p[4] - p);
    return 0;
}
那么四个输出之和为？
A. 72
B. 48
C. 56
D. 84
答案：A。
由于 student 结构体内，最大的数据类型为 int/float，这就要求 student
3

<!-- ===== page 4 ===== -->

整体字节数为 4 的倍数。进行内部/外部对齐后，得到 student 的长度为：
4(0)+6(0)+2(0)+1(3)+4(0)=20 字节（括号内为对应的内部对齐）。
所以 sizeof(s)=20。
继续看 p 的声明，采用左右法则阅读表达式，可以知道 p 是一个有着 8 个元素
的数组，元素类型为指针，指向一个有着 4 个元素的数组，元素类型为指针，指
向 student 类型。
所以，我们得到 **p 实际上是一个有着 4 个元素的数组，元素类型为 student
类型的指针，所以 sizeof(**p)=4*8=32。
接着，看 (char*)&p[2] - (char*)p，注意到这里都先强转为了 char* 类
型，所以其计算得到的就是 &p[2] 和 p 的实际差值，由于 p 是一个数组，其
元素为指针，所以这里的差就是 2 个指针的字节长度，从而 (char*)&p[2] -
(char*)p=16。
最后，看 &p[4] – p，与上一行不同，这里没有发生强转，所以实际上计算得到
的实际差值会除以步长，从而 &p[4] – p = 4。
综上，此题答案为 20+32+16+4=72。

---

### 2024期中-带答案 · 第一题 5

> 出处：`原文/期中/2024期中-带答案.md` 第 125–137 行　·　模块判定：Machine Prog
> 考什么：x86-64栈结构与参数构造区

5.下述关于 x86-64 的栈结构说法错误的是？
A. 被调用者保存寄存器包括：%rbp %rbx %r12 %r13 %r14 %r15
B. 过程的返回地址属于调用者的帧栈
C. 过程传参时，参数 1~6 通过寄存器传递，在参数构造区中存放其他参数，其
中，参数 7 最先压栈
D. call 指令的执行过程是：先将下一条指令的地址压栈，随后将PC设为目标
地址
答案：C。
4

<!-- ===== page 5 ===== -->

在参数构造区中存放 7 及以上的参数，参数 7 是最后压栈的。

---

### 2024期中-带答案 · 第一题 6

> 出处：`原文/期中/2024期中-带答案.md` 第 138–150 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出防护与金丝雀值检测

6.下述说法错误的是？
A. 我们可以使用安全的函数编写程序如 fgets strncpy 指定每次读取的字节
数来避免缓冲区溢出，对抗攻击
B. 可以使用地址随机化来随机化程序的内存布局，从而使得攻击代码的位置不再
确定，但此处存在权衡：随机的范围必须足够大才足以对抗攻击，但又要足够小避
免浪费太多程序空间
C. 可以在过程开始时，从一个特殊的只读段中获取一个金丝雀值放入栈中，在函
数返回时，先使用 cmpq 指令来进行比较，随后使用 jle 指令来根据条件码跳
转
D. 可以限制哪些内存页内的数据可以当做代码来执行，检查一个页是否可以执行
是由硬件来完成的，效率上没有损失
答案：C。
返回时，先使用 xorq 指令进行比较，随后使用 je 指令来根据条件码跳转。

---

### 2024期中-带答案 · 第一题 7

> 出处：`原文/期中/2024期中-带答案.md` 第 151–158 行　·　模块判定：Machine Prog
> 考什么：结构体参数与返回值经栈/寄存器传递

7.在作业题中，我们考察过GCC为一个参数和返回值都是结构体的函数产生的汇
编代码，此时参数和返回值都是通过栈传递的，以下有关说法错误的是：
A．返回的结构体的地址被存放在%rax寄存器中
B．虽然参数是通过栈传递的，但这里依旧使用到了%rdi
C．返回的结构体实际上是存放在被调用者的栈帧当中
D．如果结构体很小的话，GCC可能会直接用寄存器来传输参数和返回值
答案：C。
C. 返回的结构体实际上存放在调用者的栈帧当中，而非被调用者

---

### 2024期中-带答案 · 第一题 8

> 出处：`原文/期中/2024期中-带答案.md` 第 159–176 行　·　模块判定：Machine Prog
> 考什么：条件传送cmove与分支实现对比

8.在x86-64中，关于GCC对read1和read2编译的结果，下列说法正确的是：
long read1(long *xp) {  long read2(long *xp) {
return (xp ? *xp:0);  if (xp) return *xp;
}  else return 0;
}
A．read1和read2的功能一致，并且编译的汇编代码结果也一致
B．read1在运行时具有安全隐患，当xp的值为NULL时会导致错误
C．read2由于可能出现分支预测错误，所以比read1的效率更低
D．对于cmove(%rdi), %rax这条指令来说，如果ZF为0，那么就不会报错
5

<!-- ===== page 6 ===== -->

答案：A。
B．二者的汇编代码均采用了跳转指令，因此不会出现错误
C. 二者汇编代码结果一致，所以效率也是相同的
D．无论条件转移指令的条件是否成立，cmove都会读取%rdi指向的内存空间，
当%rdi指向了非法地址时，就会报错

---

### 2024期中-带答案 · 第三题

> 出处：`原文/期中/2024期中-带答案.md` 第 387–461 行　·　模块判定：Machine Prog
> 考什么：递归函数foo的C与汇编代码补全

第三题（15分）
下列C代码实现了一个名为foo的函数，请阅读并分析该C代码及其对应的x86
汇编代码，补全代码中缺失的部分，并回答相应问题。（注：第（14）题不要求作
答。）
v{ oid foo(char *p)
    ic*nhpta  r=l   et nm( p1= 4 =)s   t  r;（l e1n）( p );;
    i f( 1(4s)t r l e=n ('p\ 0+' ;1 )  （2）  1)
   {      （3）   ;
  }  }   (14)   = tmp;
 0000000000001189 <foo>:
    1189:  f3 0f 1e fa           endbr64
        111188de::   5458   8 9   e  5                           pmuosvh       %%rrsbpp,   （4）
        11119915::   4488  8839  e7cd  2e08                      smuobv        $%0rxd2i0,,-%0rxs1p8 (%rbp)
            11111199a9d0:::    44e888   88db9b   4cf57e    ef 8f     f   f                       mmcooavvl  l         %-<r0saxtx1r,8l%(er%ndr@ibp pl)t,>% rax
        1111aa58::   8498  485b  f4c5   e 8                      mmoovv        %-e0axx1,8-(0%xr4b(p%)r,b%pr)a x
        1111aacf::   08f8  b465  0f0b                            mmoovvz  b l  %(a%lr,a-x0)x,5%(e%arxb p)
    11b2:  8b 45 fc              mov    -0x4(%rbp),%eax
        1111bb57::   4488  988d   5 0   f  f                     clletaq       - 0x1(%rax),%rdx
13

<!-- ===== page 14 ===== -->

    11bb:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11bf:  48 01 d0              add    %rdx,%rax
    11c2:  0f b6 10              movzbl (%rax),%edx
    11c5:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11c9:  88 10                  mov    %dl,(%rax)
    11cb:  8b 45 fc              mov    -0x4(%rbp),%eax
    11ce:  48 98                    （5）
    11d0:  48 8d 50 ff           lea    -0x1(%rax),%rdx
    11d4:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11d8:  48 01 d0              add    %rdx,%rax
    11db:  c6 00 00              movb   $0x0,(%rax)
    11de:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11e2:  48 83 c0 01           add    $0x1,%rax
    11e6:  48 89 c7              mov      （6）  ,%rdi
    11e9:  e8 92 fe ff ff        call   <strlen@plt>
    11ee:  48 83 f8 01           cmp    $0x1,%rax
    11f2:  76 （7）               jbe    1204 <foo+0x7b>
    11f4:  48 8b 45 e8           mov    -0x18(%rbp),%rax
    11f8:  48 83 c0 01           add    $0x1,%rax
    11fc:  48 89 c7              mov    %rax,  （8）
    11ff:  e8 85 ff ff ff        call   1189 <foo>
    1204:  8b 45 fc              mov    -0x4(%rbp),%eax
    1207:  48 98                  cltq
    1209:  48 8d 50 ff           lea    （9）(%rax),%rdx
    120d:  48 8b 45 e8           mov      （10）  ,%rax
    1211:  48 01 c2              add    %rax,%rdx
    1214:  0f b6 45 fb           movzbl -0x5(%rbp),%eax
    1218:  88 02                  mov    %al,(%rdx)
    121a:  90                     nop
    121b:  c9                     leave
    121c:  c3                       （11）
若在程序中， main 函数调用了 foo 函数，且传递的参数指向字符
串”ILOVEICS\0”，则调用该函数后的字符串内容变为  （12）  。
若main函数向foo函数传递的参数指向字符串”ICS2024\0”，则main函数在
调用foo函数时，栈中最多会同时存在 （13） 个foo函数的帧。（注意：程序
中其他地方不会调用foo函数）
（1）
14

<!-- ===== page 15 ===== -->

（2）
（3）
（4）
（5）
（6）
（7）
（8）
（9）
（10）
（11）
（12）
（13）

---

### 2013期末-带答案 · 第一题 2

> 出处：`原文/期末/2013期末-带答案.md` 第 59–63 行　·　模块判定：Machine Prog
> 考什么：x86-64 callq 后第一个参数的位置

2、按照教材描述的原则，对于 x86_64 程序，在 callq 指令执行后，函数的第
一个参数一般存放在哪里？答：（     ）
A. 8(%rsp)    B. 4(%rsp)    C. %rax    D. %rdi
答案：D
考察学生对x86_64与IA-32在函数参数传递上的不同。

---

### 2013期末-带答案 · 第一题 3

> 出处：`原文/期末/2013期末-带答案.md` 第 64–70 行　·　模块判定：Machine Prog
> 考什么：用 leal 计算 5x+7

3、已知变量x的值已经存放在寄存器eax中，现在想把5x+7的值计算出来并存
放到寄存器ebx中，如果不允许用乘法和除法指令，则至少需要多少条IA-32指
令完成该任务？答：（     ）
A. 1条     B. 3条     C. 2条     D. 4条
答案：A
考察学生对leal指令的用法是否熟悉。
使用一条指令“leal 7(%eax, %eax, 4), %ebx”即可。

---

### 2014期末-带答案 · 第一题 3

> 出处：`原文/期末/2014期末-带答案.md` 第 67–83 行　·　模块判定：Machine Prog
> 考什么：由汇编 lea/cmov 反推 C 表达式

3.  左边的C函数中，在x86_64服务器上采用GCC编译产生的汇编语言如右边
所示。那么（1）和（2）的内容分别是：（    ）
<arith>:
int arith(int x, int y) {  lea    (%rsi,%rdi,1),%eax
   return (x < y) ? ( 1 ) : ( 2 );  mov    %esi,%edx
}  sub    %edi,%edx
cmp    %esi,%edi
2

<!-- ===== page 3 ===== -->

cmovge %edx,%eax
retq
（提示：第一个参数放在rdi寄存器中，第二个参数放在rsi寄存器中）
A. x-y，x+y   B. x+y，x-y  C. x+y，y-x   D. y-x，x+y
答案：C
说明：考查lea和cmov的指令理解

---

### 2014期末-带答案 · 第一题 4

> 出处：`原文/期末/2014期末-带答案.md` 第 84–92 行　·　模块判定：Machine Prog
> 考什么：结构体数据对齐与 sizeof 比较

4.  假定struct P {int i; char c; int j; char d;}; 在x86_64服
务器的 Linux 操作系统上，下面哪个结构体的大小与其它三个不同：答：
（      ）
A.  struct P1 {struct P a[3]};
B.  struct P2 {int i[3]; char c[3]; int j[3]; char d[3]};
C.  struct P3 {struct P *a[3]; char *c[3];};
D.  struct P4 {struct P *a[3]; int *f[3];};
答案：B
说明：考查数据对齐，P的sizeof为16，A/C/D都为48，B为32

---

### 2014期末-带答案 · 第二题 2

> 出处：`原文/期末/2014期末-带答案.md` 第 370–416 行　·　模块判定：Machine Prog
> 考什么：反汇编填空（movzbl/shl/push/pop 等）

2、填写下面反汇编中的缺失的内容：（数组d的地址为0x6009a0）
（提示：注意反汇编格式与汇编格式有所区别）
00000000004004d0 <b>:
  4004d0:       mov    %edi,%eax
  4004d2:       movzbl %dil,%edx
  4004d6:       movzbl 0x6009a0(%rdx),%edx
  4004dd:       movzbl %ah,    (1)
  4004e0:       movzbl 0x6009a0(%rax),%eax
  4004e7:       shl        (2)     ,%edx
  4004ea:       or     %edx,%eax
  4004ec:       retq
11

<!-- ===== page 12 ===== -->

00000000004004f0 <c>:
  4004f0:       mov    %edi,%eax
  4004f2:       push       (3)
  4004f3:       mov    %edi,%ebx
  4004f5:       shr        (4)     ,%eax
  4004f8:       movzbl %bh,%ebx
  4004fb:       movzbl %al,    (5)
  4004fe:       movzbl %ah,    (6)
  400501:       movzbl 0x6009a0(%rdx),%edx
  400508:       movzbl 0x6009a0(%rax),%eax
  40050f:       shl        (7)     ,%edx
  400512:       or     %edx,%eax
  400514:       movzbl %dil,%edx
  400518:       movzbl 0x6009a0(%rdx),%ecx
  40051f:       movzbl 0x6009a0(%rbx),%edx
  400526:       movzwl %ax,%eax
  400529:       pop        (3)
  40052a:       shl    $0x8,%ecx
  40052d:       or     %ecx,%edx
  40052f:       shl    $0x10,%edx
  400532:       or     %edx,    (8)
  400534:       retq
答案（每项1分）：
（1）%eax
（2）$0x8
（3）%rbx
（4）$0x10
（5）%edx
（6）%eax
（7）$0x8
（8）%eax
说明：考察汇编程序理解

---

### 2015期末-20160104-带答案 · 第一题 1

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 52–54 行　·　模块判定：Machine Prog
> 考什么：哪条指令不改变 esp

1.  下面  哪条指令不会引起esp的变化？
ABC...   mpcouavsllhl l       %p%eresibpnp,t  f% ebp
答  案：D.A ，s考ub察l 汇  编$2指0令, 和%e栈s的p 理解。

---

### 2015期末-20160104-带答案 · 第一题 3

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 59–61 行　·　模块判定：Machine Prog
> 考什么：x86 寻址方式合法性

 3 .  下面  哪条指令不是X86正确的寻址方式
ABC...  mmmooovvvlll      $($3%24e3,a, x   )(1,%0 e( a%%xee)ad xx , %eax)
答案：D.D 。mo考vl察 寻 (址%e方ax式)的, 理 8解(%。e bx)

---

### 2015期末-20160104-带答案 · 第二题

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 323–423 行　·　模块判定：Machine Prog
> 考什么：由汇编/输出结果补全 C 代码与汇编填空

 第二题（12分）汇编
 下 面分别是一个程序的C语言代码、汇编语言代码，以及其执行结果，请根据其逻
辑分别填写空出来的内容：
1. C语言代码
# include <stdio.h>
long f1(long x, long y)
{   return     (1)        ;
} lo ng f2(long x, long y)
{   return     (2)        ;
}
long a[6] = {1, 0, 0, 0, 0, 0};
 void foo(void)
{   long (*f)(long, long);
     l o n g i(;3 )        long count = 0;
  for (i=0; i<     (4)        ; i++) {
        i efl s(ef(  c=o ufn1t;  % 2) == 0)
       f = f2;
      ac[oiu+n1t]  +=+ ;f (a[i],      (5)        );
  }
11

<!-- ===== page 12 ===== -->

  for (i=0; i<6; i++) {
    printf("%ld\n", a[i]);
  }
}
int main()
{
  foo();
  foo();
}
2. 汇编语言代码
.LC0:
  .string       (6)
f1:
  leaq  (%rdi,%rsi), %rax
  ret
f2:
  movq  %rdi, %rax
  imulq %rsi, %rax
  ret
foo:
  pushq %r12
  pushq %rbp
       (7)
  movl  $a, %ebx
  movl  $a +      (8)        , %r12d
  movl  $f1, %ebp
.L5:
  movq  count, %rsi
  movq  %rsi, %rax
  andl  $1, %eax
  movl  $f2, %eax
  cmove %rbp, %rax
12

<!-- ===== page 13 ===== -->

  movq  (%rbx), %rdi
  call  *%rax
  movq  %     (9)         , 8(%rbx)
  addq  $1, count
  addq  $8, %rbx
  cmpq  %r12, %rbx
  jne .L5
  movl  $0, %ebx
.L6:
  movq  a(,%rbx,8), %rdx
  movl  $.LC0, %esi
  movl  $1, %edi
  movl  $0, %eax
  call  printf
  addq  $1, %rbx
  cmpq  $6, %rbx
  jne .L6
  popq  %rbx
  popq  %rbp
       (10)
  ret
3. 输出结果
1
1
1
3
     (11)
13
1
5
11
77
85
     (12)
13

<!-- ===== page 14 ===== -->

答12))案  ((：（xx  每+*空  yy一))分  ）
3456))))s   c"5t %oalutdni\tcn  "（必需有引号）
789)))p  0ruxas4xh 0q 或者%r6b4x（ 40也可给分，因为汇编默认是16进制）
111012)))p  97o 6p5q   %r12

---

### 2016期末-带答案 · 第一题 3

> 出处：`原文/期末/2016期末-带答案.md` 第 78–84 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出的常见防御手段辨析

3.  缓冲区溢出会带来程序风险，下列避免方法中错误的是：
A. 在栈中存放特殊字段用于检测是否发生缓冲区溢出
B. 避免使用有风险的库函数，如gets等
C. 随机设置栈的偏移地址
D. 分配尽可能大的缓冲区数组
答案：D
分配大缓冲区无法从根本上解决溢出问题，输入足够长数据就仍然可以实现攻击。

---

### 2016期末-带答案 · 第二题

> 出处：`原文/期末/2016期末-带答案.md` 第 291–371 行　·　模块判定：Machine Prog
> 考什么：32 位汇编反推 C 函数并计算返回值

第二题（12分）
下面程序是一个完整C函数myfunction经编译器优化后生成的32位汇编语言
代码：
myfunction:
  pushl  %ecx
  movl 0x10(%esp), %ecx
  movl 8(%esp), %edx
  pushl %ebx
  movl 0x18(%esp), %ebx
  pushl %esi
  movl 0x14(%esp), %esi
  pushl %ebp
  xorl %eax, %eax
  pushl %edi
  jmp .L2
  leal (%esp), %esp
.L2:
  movl 8(%esi), %edi
  imull 4(%edx,%eax,8), %edi
  movl (%esi), %ebp
  imull (%edx,%eax,8), %ebp
  addl %ebp, %edi
  movl %edi, (%ecx)
  movl 0xc(%esi), %edi
  imull 4(%edx,%eax,8), %edi
  movl 4(%esi), %ebp
  imull (%edx,%eax,8), %ebp
  addl %ebp, %edi
  movl (%ecx), %ebp
  addl %edi, %ebp
  addl %ebp, %ebx
  movl %edi, 4(%ecx)
  incl %eax
  addl $8, %ecx
  cmpl $2, %eax
  jl .L2
  popl %edi
  popl %ebp
  popl %esi
  movl %ebx, %eax
  popl %ebx
  popl %ecx
9

<!-- ===== page 10 ===== -->

  ret
提示：32位汇编使用栈来传递所有参数，参数压栈顺序为从右至左。
1. 请根据上述汇编代码，根据提示，补全 myfunction 的代码。注意，每行一
条语句；不能定义新的变量。
int myfunction(int a[], int b[], int c[], int d) {
  int i;
  for (i = 0; i <       ; i++) {
              =                                        ;
              =                                        ;
              =                                        ;
  }
  return       ;
}
2. 请给出以下程序的输出结果。
int main( )
{
int a[5] = {1, 2, 3, 4, 5};
int b[5] = {9, 8, 5, 6, 4};
int c[5] = {7, 9, 8, 10, 11};
int d = 5;
int ret = myfunction(a, b, c, d);
printf("%d\n", ret);
return 0;
}
答案：
1. for (i = 0; i <  2 ; i++) { //（1分）
//下面第一二个等式左边都对得1分，第三个等式左边写对得1分
    c[2*i] = b[0] * a[2*i] + b[2] * a[2*i+1]; //（等式右边
乘加乘序列得1分，等式右边写对2*i和2*i+1得1分）
    c[2*i+1] = b[1] * a[2*i] + b[3] * a[2*i+1]; //（等式右
边乘加乘序列得1分，等式右边写对2*i和2*i+1得1分）
    d = d + c[2*i] + c[2*i+1];  //（等式右边两个加号得1分，等
式右边写对2*i和2*i+1得1分）
  return    d   ;  //（1分）
2. 139  （2分）

---

### 2017期末-无答案 · 第一题 1

> 出处：`原文/期末/2017期末-无答案.md` 第 57–59 行　·　模块判定：Machine Prog
> 考什么：gdb 单步进入被调函数（si/ni）

1.  在gdb调试中，下一条指令是call func1。下面哪条gdb指令能执行该指令并
且停留在func1的第一条指令？
A. br func1    B. si      C. ni      D. disas func1

---

### 2017期末-无答案 · 第一题 3

> 出处：`原文/期末/2017期末-无答案.md` 第 63–67 行　·　模块判定：Machine Prog
> 考什么：指令长度、test 与 cmp 等价、跳转表

3.  下面说法正确的是：
A. 不同指令的机器码长度是相同的
B. test %rax, %rax恒等于cmp $0, %rax
C. switch编译后总是会产生跳转表
D. 以上都不对

---

### 2017期末-无答案 · 第二题 1

> 出处：`原文/期末/2017期末-无答案.md` 第 227–278 行　·　模块判定：Machine Prog
> 考什么：结构体偏移与浮点汇编代码填空

第二题（12分）
假设程序运行在x86-64的小端法机器上，编译器按照标准规则对齐，并且有nan
参  与的算术比较运算都返回0。请回答下列问题：
1. 请根据左边C程序和右边对应的汇编代码，填写空白处的代码。
struct a {  ……
    cinhta ir;  c[2][3];  p roc1…: …
}st;r uct b {    mmoovvssss   (.L%Crc0x(%), r%ipx)m, %mx1m m0
  float f;    addss  %xmm1, %xmm0
    scthraurc tc ;a  a;     cmvotsvss2ds d  %%xxmmmm02,,  %-8x(%mrmbp2)
};    movss  (%rcx), %xmm0
u n isotrnu cct { a  a;     cmvotsvss2ds d  %.LxCm1(m%0r,i p%),x %mxmm0m  1
  struct b b;    addsd  %xmm1, %xmm0
 };  struct b* pb;    m…o…vq   %xmm0, -16(%rbp)
v o dido upbrolec 1a( u=n uio->nb c.*f  u ) {        ;  proc2…: …
    dporiunbtfl(e" %b =d \un-">, ba=.f=  b );          ;  proc3…: …
}
    movb  %al, -1(%rbp)
void proc2(union c* u){    movzbl  2(%rcx), %eax
    cchhaarr**  ab  ==  u(u->->aa.c.c[1 +]  +1) 1[1; ];    m…o…vb   %al, -2(%rbp)
 }  printf("%d\n", b - a);   p r o c 4…: …
 void proc3(union c* u){     mmoovvll   8%(%earxc,x -)4, (%%erabxp )
  char x = u->a.c[1][0];    movzbl  16(%rcx), %eax
8

<!-- ===== page 9 ===== -->

  char y =                 ;    movsbl  %al, %eax
  if (x == 0x7F && (y & 0x80) == 0x80)     movl  %eax, -8(%rbp)
    printf("%d\n", (u->b.f < u->a.i));      ……
  else  main:
    printf("0\n");      ……
}    leaq 32(%rsp), %rbx
    movq  %rbx, %rcx
void proc4(union c* u){    call proc1
  int x = u->a.i;    movq  %rbx, %rcx
  int y =              ;    call proc2
  printf("%d\n", (x > y) != (-x<-y));     movq  %rbx, %rcx
}    call proc3
    movq  %rbx, %rcx
void main(){    call proc4
  unsigned int i;      ……
  printf("%d\n", sizeof(struct a));    .align 4
  printf("%d\n", sizeof(struct b));  .LC0:
  printf("%d\n", sizeof(union c));    .long  1048576000
  //十六进制3E800000
  union c u;    .align 8
  …… //随机初始化u  .LC1:
  proc1(&u);    .long  0
  proc2(&u);    .long  1070596096
  proc3(&u);  //十六进制 3FD00000
  proc4(&u);
}

---

### 2018期末-带答案 · 第一题 2

> 出处：`原文/期末/2018期末-带答案.md` 第 65–95 行　·　模块判定：Machine Prog
> 考什么：结构体对齐填充与汇编寻址偏移

2.  有如下结构定义和程序片段
struct A
{
    char c;
    int i;
    double d;
    int array[10];
};
struct B
{
    int array[10];
2

<!-- ===== page 3 ===== -->

    double d;
    char c;
    int i;
};
void foo(struct A *pa, struct B *pb, int index)
{
    pb->i = pa->array[index];
}
 在Linux下使用GCC编译器，仅采用-O2选项，上述代码对应的汇编语言是：（将
选项依次填入空格内）
 movslq %edx, %rdx
 movl __(%rdi,%rdx,__), %eax
 movl %eax, __(%rsi)
A.  (16, 4, 52)   B. (24, 4, 52)   C. (16, 4, 49)   D. (24, 4, 49)
答案：A
 (注意char和int共用一个8字节)

---

### 2018期末-带答案 · 第七题 1

> 出处：`原文/期末/2018期末-带答案.md` 第 693–722 行　·　模块判定：Machine Prog
> 考什么：i++ 对应的 x86-64 汇编代码

第七题（10分）
给定如下程序：
#include <stdio.h>
#include <pthread.h>
int i = 0;
int j = 0;
void *do_stuff1(void * arg __attribute__((unused))) {
int a;
for (a = 0; a < 1000; a++)
{i++; j++;}
return NULL;
}
void *do_stuff2(void * arg __attribute__((unused))) {
int a;
for (a = 0; a < 1000; a++)
{j++; i++;}
return NULL;
}
int main() {
pthread_t tid1, tid2;
pthread_create(&tid1, NULL, do_stuff1, NULL);
pthread_create(&tid2, NULL, do_stuff2, NULL);
pthread_join(tid1, NULL);
pthread_join(tid2, NULL);
printf("%d, %d\n", i, j);
return 0;
}
1.  （2分）用以下元素的编号写出i++编译后的汇编代码。
(a) mov   (b) add   (c) 0x601040   (d) %eax (e) $0x1
比如，回答(a) (e) (d)表示mov $0x1, %eax

---

### 2019、2020期末-答案解析 · 2020 选择题 1

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 13–14 行　·　模块判定：Machine Prog
> 考什么：栈帧与帧指针（可变栈帧）

1. C。A是正确的，不能把attacklab和bomblab混淆了。C的错误原因在于可以支持可变栈帧，
编译时不能确定大小，必须使用帧指针。

---

### 2019、2020期末-答案解析 · 2020 选择题 6

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 26–26 行　·　模块判定：Machine Prog
> 考什么：指令长度与基址加偏移寻址

6. D。指令长度为6字节，内存地址需要用基址加上偏移计算。

---

### 2019、2020期末-答案解析 · 2020 选择题 11

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 42–42 行　·　模块判定：Machine Prog
> 考什么：存疑：仅注“书上原话”，考点不明

11. A。送分题，属于书上原话。

---

### 2019、2020期末-答案解析 · 2019 选择题 12

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 180–180 行　·　模块判定：Machine Prog
> 考什么：存疑：仅注“直接模拟”，考点不明

12. D。直接模拟就可以。

---

### 2019期末-无答案 · 第二题 (1)

> 出处：`原文/期末/2019期末-无答案.md` 第 242–255 行　·　模块判定：Machine Prog
> 考什么：由汇编循环推断 C 代码循环次数（含共用汇编段）

第二题（10分）
现有如下汇编代码段，相关寄存器的初始值也在右侧表格中给出:
.L2:
    movq    (%rdi), %rbx
    addq    %rbx, %rax  %rdi  0x8008
    addq    $8, %rdi  %rax  0
    addq    $1, %rcx  %rbx  0
    cmpq    $8, %rcx  %rcx  0
    jl     .L2
（1）  请在下面C代码中，补充缺失的部分。
  for(i=0; i<_____ ; i++)
  {
    sum=sum+a[i];
  }

---

### 2020期末-无答案 · 第一题 1

> 出处：`原文/期末/2020期末-无答案.md` 第 51–60 行　·　模块判定：Machine Prog
> 考什么：x86-64/Y86 汇编、栈帧与跳转表

1.  下列关于x86-64汇编，说法错误的是：
．．
A. Bomblab中bomb程序的代码段基址每次运行可能不同，因此其switch语句跳转表存
储的不是目标代码的绝对地址，而是相对于某基址的偏移量。
B. 本门课程主要讲述的是 ATT 格式的汇编，其 mov 等双操作数指令一般以第一个操作
数作为源而第二个操作数作为目标，这种操作数顺序通常与Intel格式的汇编相反。
C. 函数栈帧的长度在编译时被确定，因此 x86-64 中通用寄存器%rbp 不会再作为桢指针
使用，但%rbp依然是被调用者保存的寄存器。
D. 多数同学Archlab书写Y86-64汇编时，在过程调用中修改了%rbx等部分寄存器而未
事先保存，且未在过程调用结束时恢复，这种行为在x86-64汇编下是不可取的。

---

### 2021期末-无答案 · 第一题 2

> 出处：`原文/期末/2021期末-无答案.md` 第 63–67 行　·　模块判定：Machine Prog
> 考什么：合法的 x86-64 汇编指令与寻址方式

2. 下列选项中是合法x86-64汇编指令的是：
A. movq %rax, $1
B. xorq %rsp, %rsp
C. movq (%rax), (%rbx)
D. movq (%rax, %rbx, 3), %rcx

---

### chap 2-6 解析 · 第一题 3

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 53–61 行　·　模块判定：Machine Prog
> 考什么：判断合法 x86-64 指令：立即数目标、双内存操作、比例因子

3.下列选项中是合法x86-64汇编指令的是（）

A.movq %rax, \$1

B. xorq %rsp, %rsp

C. movq (%rax), (%rbx)

D. movq (%rax, %rbx, 3), %rcx

---

### chap 2-6 解析 · 第一题 4

> 出处：`原文/期末/2021期末-带答案/chap 2-6 解析.md` 第 63–135 行　·　模块判定：Machine Prog
> 考什么：由栈帧中保存的 %rbp 读取调用者的返回地址

4.现假定所有函数均使用%rbp寄存器描述栈帧，并且函数体进入时一定以pushq %rbp; movq %rsp, %rbp开始，函数体退出前一定以leaveq; retq结束。有编译器内置函数 \_\_builtin_return_address(1)表示获取调用当前函数的函数的返回地址，举例来说，若有如下代 码：

long foo(void)

{

return (long) \_\_builtin_return_address(1);

}

同时函数bar()调用了函数foo()，则函数foo()的返回值是函数bar()的返回地址(即bar()调用 完成后控制流转向的地址)，保证bar()和foo()都不是内联函数，则将函数foo()编译，生成的 汇编指令可能是（）

A.

foo:

pushq %rbp

movq %rsp, %rbp

movq 8(%rbp), %rax

leaveq

retq

B.

foo:

pushq %rbp

movq %rsp, %rbp

movq 0(%rbp), %rax

movq 0(%rax), %rax

leaveq

retq

C.

foo:

pushq %rbp

movq %rsp, %rbp

movq 0(%rbp), %rax

movq -8(%rax), %rax

leaveq

retq

D.

foo:

pushq %rbp

movq %rsp, %rbp

movq 0(%rbp), %rax

movq 8(%rax), %rax

leaveq

retq

---

### 2022期末-无答案 · 第一题 1

> 出处：`原文/期末/2022期末-无答案.md` 第 40–40 行　·　模块判定：Machine Prog
> 考什么：ISA 两大类 RISC/CISC 的指令数与寻址方式对比

1. 对比指令系统体系结构（ISA）的两大类别，____________通常比____________的指令数量和寻址方式都少。

---

### 2022期末-无答案 · 第一题 3

> 出处：`原文/期末/2022期末-无答案.md` 第 44–44 行　·　模块判定：Machine Prog
> 考什么：x86-64/Linux 传参前两个寄存器

3. 在 x86-64/Linux 的约定中，函数传递参数的前两个分别放在______和______寄存器。

---

### 2022期末-答案 · 第一题 3

> 出处：`原文/期末/2022期末-答案.md` 第 12–12 行　·　模块判定：Machine Prog
> 考什么：rdi/rsi 参数传递寄存器

3、rdi rsi

---

### 2025期末-带答案 · 一 5

> 出处：`原文/期末/2025期末-带答案.md` 第 32–36 行　·　模块判定：Machine Prog
> 考什么：addl 结果、写 %eax 清零高位与标志位

5. 观察下面的汇编代码：
答案：ACD
解析： addl 是 32 位加法：%eax=0xFFFFFFFF + 1 -> 0x00000000（低 32 位回
绕）。写 %eax 会把 %rax 的高 32 位清零，所以 %rax 变为全 0。回绕产生进位所以
CF=1；结果为 0 所以 ZF=1；有符号角度是 -1 + 1 = 0 不溢出，OF=0。

---

### 2025期末-带答案 · 一 6

> 出处：`原文/期末/2025期末-带答案.md` 第 37–46 行　·　模块判定：Machine Prog
> 考什么：栈帧布局、%rsp 对齐与 leave 语义

6. 观察下面的汇编代码片段：
答案：ABDE
解析： push %rbp; mov %rsp,%rbp 后，%rbp 指向保存的旧%rbp，其上方 8 字节
是返回地址。入口通常 8(mod16)，push 后变 0(mod16)，再 sub48 仍为 0(mod16)，
1

<!-- ===== page 2 ===== -->

所以 C 错。leave语义是mov %rbp,%rsp; pop %rbp，在该帧结构下等价于先把%rsp
加回 48 再弹出%rbp。

---

### 2025期末-带答案 · 一 7

> 出处：`原文/期末/2025期末-带答案.md` 第 47–51 行　·　模块判定：Machine Prog
> 考什么：8 个 long 参数的寄存器/栈传递与 ABI

7. 调用一个有 8 个 long 参数的函数 f(a1,...,a8)，调用点使用如下汇编代码序列
答案：ABC
解析： 超过 6 个整数参数后，其余从栈上传递；在被调函数入口，0(%rsp)是返回地址，
因此第 7 个参数在 8(%rsp)，第 8 个在 16(%rsp)。caller 负责把自己 push 的参
数空间收回。%r10/%r11不是传参寄存器；是否用%rbp是编译器选择，不是 ABI 强制。

---

### 2025期末-无答案 · 一 5

> 出处：`原文/期末/2025期末-无答案.md` 第 96–105 行　·　模块判定：Machine Prog
> 考什么：addl 执行结果与 CF/ZF/OF 标志

5. 观察下面的汇编代码：
movq $0x12345678FFFFFFFF, %rax
movq $0x0000000000000001, %rcx
addl %ecx, %eax
下列哪些说法正确？
A. 执行后 %rax == 0x0000000000000000
B. 执行后 %rax == 0x1234567800000000
C. 执行后 CF=1
D. 执行后 ZF=1
E. 执行后 OF=1

---

### 2025期末-无答案 · 一 6

> 出处：`原文/期末/2025期末-无答案.md` 第 106–121 行　·　模块判定：Machine Prog
> 考什么：栈帧布局、%rsp 对齐与 leave 语义

6. 观察下面的汇编代码片段：
baz:
pushq %rbp
movq %rsp, %rbp
subq $48, %rsp
...
callq qux
...
leave
retq
下列说法哪些正确？
A. 0(%rbp) 处保存的是调用者的旧 %rbp
B. 8(%rbp) 处保存的是返回地址
C. 紧挨着执行 callq qux 之前，%rsp ≡ 8 (mod16)
D. subq $48,%rsp 为局部数据预留了 48 字节（不含保存的%rbp和返回地址）
E. 这里的 leave 等价于 addq $48,%rsp; popq %rbp（假设 %rbp 未被改写）

---

### 2025期末-无答案 · 一 7

> 出处：`原文/期末/2025期末-无答案.md` 第 122–143 行　·　模块判定：Machine Prog
> 考什么：8 个 long 参数的寄存器/栈传递与 ABI

7. 调用一个有 8 个 long 参数的函数 f(a1,...,a8)，调用点使用如下汇编代码序列
（省略取值细节）：
movq a1, %rdi
3

<!-- ===== page 4 ===== -->

movq a2, %rsi
movq a3, %rdx
movq a4, %rcx
movq a5, %r8
movq a6, %r9
pushq a8
pushq a7
callq f
addq $16, %rsp
下列说法哪些正确？
A. 在 f 的入口处（尚未动 %rsp），a7 位于 8(%rsp)
B. 若把两条 push 顺序改为先 push a7 再 push a8，则 f 看到的 a7/a8 会互换
C. 应当由caller回收栈上的传参空间（用 addq $16,%rsp）
D. a7,a8也可以放在%r10,%r11中传递
E. 因为用了栈传参，所以f中必须设置和管理%rbp帧指针

---

### 期末往年题勘误、详解 by Arthals · 2016 第一题 第13问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 69–69 行　·　模块判定：Machine Prog
> 考什么：存疑：仅注“所有符号都对应 bit 数”

第 13 问，这里的所有符号都对应 bit 数。

---

### 2025第1次阶段测验-带答案 · 第4讲 7

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 89–90 行　·　模块判定：Machine Prog
> 考什么：通用寄存器低 32 位/最低字节的名称

7. x86-64的通用寄存器中，对应rbx低32位的寄存器名称为： ebx ；对应rcx
最低字节的寄存器名称为： cl 。

---

### 2025第1次阶段测验-带答案 · 第4讲 8

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 91–96 行　·　模块判定：Machine Prog
> 考什么：swap 汇编中寄存器与内存访问次数统计

8. 以下代码中，有 8 次通用寄存器访问，有 4 次内存访问（均不含取指令相关操作）。
swap:
movq (%rdi), %rax
movq (%rsi), %rdx
movq %rdx, (%rdi)
movq %rax, (%rsi)

---

### 2025第1次阶段测验-带答案 · 第4讲 9

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 97–99 行　·　模块判定：Machine Prog
> 考什么：比例变址寻址方式地址计算

9. 若寄存器内容为rdx:0xc000,rcx:0x0200,则计算下列地址的值（十六进制表示）：
0x10(%rdx,%rcx,4):0xC810
0x30(,%rdx,8):0x60030

---

### 2025第1次阶段测验-带答案 · 第5讲 10

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 101–103 行　·　模块判定：Machine Prog
> 考什么：cmp/test 与 sub/and 的等价关系

10.对于以下汇编指令，给出与之内在操作流程相同、只是会修改目的寄存器的指令：
cmpq %rbx,%rax → subq %rbx,%ra
testq %rbx,%rax → andq %rbx,%rax

---

### 2025第1次阶段测验-带答案 · 第5讲 11

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 104–117 行　·　模块判定：Machine Prog
> 考什么：cmp+set 指令补全汇编，movzbl 功能与高位清零

11.下面的C语言代码与汇编语言代码对应
3

<!-- ===== page 4 ===== -->

intcmpxy(longx,longy) cmpq %rsi, %rdi
{ return x > y; smeotvgzbl%%aall, %eax
（1）}修改C语言代码如下，相应补全汇编语r言et代码
intcmpxy(longx,longy) cmpq %rsi, %rdi
{ return x <= y; smeotvlzebl %%aall, %eax
（2）}movzbl指令本身的功能是：：从源操r作et数取出1个字节，零扩展为32位后存
入 目的操作数
（3）在x86-64中，这条movzbl隐含操作还有：将目的操作数寄存器（这个程序里
是rax） 的高32位清零

---

### 2025第1次阶段测验-带答案 · 第5讲 12

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 118–135 行　·　模块判定：Machine Prog
> 考什么：absdiff 分支实现与条件传送 cmov 实现对比

12.下面的C语言代码与汇编语言代码对应，补全汇编代码
long absdiff(long x, long y) absdiff:
{ long result; cjmgpq.L4 %rsi, %rdi
ifre(sxul<t= =y)x-y; msouvbqq %%rrdsii,, %%rraaxx
elrseesult = y-x; .L4r:et
} return result; msouvbqq %%rrsdii,, %%rraaxx
（2）如果用条件传送指令实现上述功能，对应汇编语言r代et码如下，补全缺失的代码，
（注意要符合编译器生成代码的常规情况）：
absdiff:
movq %rdi, %rax
smsuoubvbqqq %%%rrrssdiii,,, %%%rrraddxxx
ccmmpoqvg %%rrsdix,, %%rrdaix
（4r）e有t些情况不适合使用条件传送指令，因为条件传送指令需要：把条件成立和不成
4

<!-- ===== page 5 ===== -->

立的两种情况都提前计算出来，会增加计算量，还有可能有副作用

---

### 2025第1次阶段测验-带答案 · 第5讲 13

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 136–138 行　·　模块判定：Machine Prog
> 考什么：loopy 循环汇编补全对应 C 代码

13.12考虑l下oo面pm:的ov汇l编代%码e：si, %ecx
3456789 .L3:mmjmaooomonrvvpvdqllqq .%$$%%Lr10rr28,,dd,ix,,%%%eerda%%axxrrx88
11111补l{01234o全ng.下llLoo面2lnn:ostjrgg对oaeneplsep应rm(qt;eal的qssoruknCel;gtt.%语%Lcrx言3=ld,,x代,i码%0nr%t：drxdn;x)

---

### 2025第1次阶段测验-带答案 · 第5讲 14

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 139–145 行　·　模块判定：Machine Prog
> 考什么：跳转表 jmp *.L1(,%rdi,8) 的目标计算

14.}.考s虑ecf}r.下toeai面rtlouir汇nrg(ennm编sau.代sr8lrekt码osdu=片|al=t段ta;：1x&ma;skmask != ; 0 ; mask = mask<<n ) {
.L1:....qqqquuuuaaaadddd ....LLLL11111234
.j.m.p *.L1(,%rdi,8) 5

<!-- ===== page 6 ===== -->

若执行到jmp指令时，rdi的值为2，则该指令会跳转到 .L13 指向的位置。

---

### 2025第1次阶段测验-带答案 · 第6讲 15

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 147–150 行　·　模块判定：Machine Prog
> 考什么：popq 指令各步骤与 %rsp 变化

15.x86-64中，执行popq %rbx的操作依次为如下步骤：
（1）从寄存器 %rsp 中读出数据x，以x为地址，读出对应内存中的数据y；
（2）将（1）中提到的寄存器（加减多少）： 加8 ；
（3）将y存到寄存器 %rbx 中。

---

### 2025第1次阶段测验-带答案 · 第6讲 16

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 151–175 行　·　模块判定：Machine Prog
> 考什么：过程调用栈帧、callq/ret、参数寄存器与被调用者保存

16.以下两组对应的C语言代码和汇编语言代码：
void multstore (long x, long y, 0000000000400640 <multstore>:
long *dest) 400640: push %rbx
{ 400641: mov %rdx,%rbx
400644: callq 400650 <mult2>
long t = mult2(x, y);
*dest = t; 400649: mov %rax,(%rbx)
} 40064c: pop %rbx
40064d: retq
long mult2 (long a, long b)
0000000000400650 <mult2>:
{ 400650: mov %rdi,%rax
long s = a * b; 400653: imul %rsi,%rax
return s;
} 400657: retq
（1）假设准备执行callq指令时，%rsp内容为0x110，那执行完callq指令后，
%rsp内容为 0x108 ，%rsp指向的内存中的数值为 0x400649 。随后执行完地址
400657处的retq指令后，%rsp内容为 0x110 。（均为十六进制）
（2）C代码中的下列变量分别保存在哪个寄存器中：
x:%rdi y:%rsi a:%rdi b:%rsi s:%rax
（3）汇编代码中，地址400641的指令修改了%rbx，地址400649的指令使用了%rbx，
而二者中间有过程调用call，是什么机制保证了%rbx不会被修改：ABI 中规定的寄存器
保存规则，要求%rbx 是被调用者保存
（4）如果把C代码中的mult2(x,y)改为mult2(y,x)，汇编代码会有什么变化：
需要在call指令之前交换%rdi和%rsi的内容

---

### 2025第1次阶段测验-带答案 · 第6讲 17

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 176–191 行　·　模块判定：Machine Prog
> 考什么：取地址与解引用，变量存放于寄存器还是内存

17.考虑以下C语言代码：
long bit_not1(long a) {
long x = ~a; //考卷有笔误，写成了~p
return x;
6

<!-- ===== page 7 ===== -->

}
longlloobnniggt_xyno==t2*~(pxl;ong *p) {
} return y;
longlocnagllv_0bi=tn1o0t1(0); {
lloonngg vv12 == 1b0i1t0_;not1(v0);
lroentgurnv3v2=+vb3i;t_not2(&v1);
}下列变量分别存放在寄存器还是内存中？
v0：寄存器 v1：内存 v2：寄存器 v3：寄存器

---

### 2025第1次阶段测验-带答案 · 第7讲 18

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 193–199 行　·　模块判定：Machine Prog
> 考什么：二维数组 arr_data[x][y] 寻址补全汇编

18.考虑下面的C语言代码:
#idn{et{f9ia0nr0er,_dC9aN0tT1a,4[C9N0T2],[C9N0T3]},=
{{991200,, 991211,, 991222,, 992133}},,
int{9g3e0t,_d9i3g1i,t(9i3n2t,x9,33i}n}t;y)
{ return arr_data[x][y];
}补全对应的汇编代码：
get_smdhoilvgqlit: $a4r,r_d%artdai(%rdi, %rsi, 4 ), %eax

---

### 2025第1次阶段测验-带答案 · 第7讲 19

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 200–201 行　·　模块判定：Machine Prog
> 考什么：变长二维数组 var_ele 的参数传递与寻址

19.C语言re中t传参n×n二维数组时，如果n是变量，应该如何传递？补全下面的汇编代码。
# int var_ele(size_t n, int a[7n][n], size_t i, size_t j)

---

### 2025第1次阶段测验-带答案 · 第7讲 20

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 205–205 行　·　模块判定：Machine Prog
> 考什么：汇编代码输出结果（原文 OCR 列错行，内容难辨）

20.##v##ti考addyn虑reept{h_ffeimiamrz下eiidnrmomdoeilnnetea面vudvtpeeef:tiqlql_{的:unqd{{{r(%ZPii代111n)rLCng,,,%%(dEOt%码rr%iNUra{p555，dcr[,Ndzg,,,xxs%Tiii5h输,i,]rp,[222,s[_4出P,,,%%%jid%C结rrr,]irO110aaa;%gaU果,,,xxxr[xN,dZ}是T3764xL]}}}：),E,,,,%N=r]%c;e1xa6x

---

### 2025第1次阶段测验-带答案 · 第7讲 21

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 206–214 行　·　模块判定：Machine Prog
> 考什么：数组循环 C 代码与汇编，求常量 A、B（OCR 错行）

21.}t}t考yy虑ppseetiiipilc下ddrnnnrnohee1面tttitnaff;ngrpl*z的t**rx{gi(issflze[ya代1hnlptt;r(iisA,[ei1rr码"npu]r2an[uuare1l[5]re4，cceatBy,[_a]tt[sr]=A3zr;u_;B=2]i_{{和]lz(,pzti;i[i+:pn21pB/t,4*=%是]+d*1U用)\(}+1nni}6k"np;)#n,tgdoh+ew[*rfn)e1i]snc8u;peolgnth定s);t义;an的t常s数A：and B */

<!-- ===== page 9 ===== -->

islnhotonrgtt;u;s[A];
}voisdtllroo2snne;ggtVvva12l(==stqqr--1>>tu*;;p, str2 *q) {
}G#sCeCtpVpm为ai-oln>v:yss%elrqt=dViav,8l1(%q产+r生sivin2如);,%下r汇s%ir编ax代码（x86-64 System V 调用约定）：
求Aamr和doedvtqqB 的值3%是2r(a多%xr,少s？i1)8,4(%%rrdaix)
A： 9 B： 5

---

### 2025第1次阶段测验-带答案 · 第7讲 22

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 215–218 行　·　模块判定：Machine Prog
> 考什么：浮点参数经 xmm 寄存器传递的汇编分析

22.d考o虑ub下le面的miCx_语c言om代pu码t和e(对lo应n的g汇*a编,语d言ou代b码le：*b, float c) {
}mix_drcoeoutmbuplruenterr:eessuulltt;= *a + *b + c;
mmcacoovdvvvtdtsqsssdids22ssdd((%%%x%%rrmrxdsmamii1xm)),,0,,,%%%x%x%rmxmxammmmx2m2m10
Cb:代%r码arsde中idts的d下列%变xcm:量m%，2x,m分m0%别x在mm哪0个r寄e存su器lt中:：%xmm0

---

### 2025第1次阶段测验-带答案 · 第8讲 24

> 出处：`原文/阶段测验/2025第1次阶段测验-带答案.md` 第 235–248 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出攻击防御方法对比（兼 VM 保护机制）

24.课上讲授了防御或者避免缓冲区攻击的几种主要方法，分析它们的特点。以普遍性情况
为准，不用考虑少见的软硬件需求。（每行算作一空）
是否需要修改用户程 是否需要重新编译 是否需要更换新的
序源代码？ 用户程序？ CPU硬件？
使用fgets()等安
是 是 否
全的库函数
栈初始位置随机化 否 否 否
在内存访问权限上设
否 否 是
置“可执行”位
“金丝雀”（哨兵）
否 是 否
机制

---

### 2025Lab测验-无答案 · Lab 任务 17

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 268–276 行　·　模块判定：Machine Prog
> 考什么：GDB 常用命令（break/info registers/ni/si/p）辨误

17. （2分）GDB是一款功能强大的调试工具，下列关于 GDB 的用法错误的是？
A. BombLab 中为了避免炸弹爆炸，可使用命令 break explode_bomb 下断点，
使程序自动跳过 explode_bomb 函数的执行
B. 命令info registers可显示程序中所有寄存器的值，包括 16 个通用寄存器和
程序计数器、条件码寄存器等其他寄存器
C. 命令 ni, si 都会执行下一条指令，但如果该指令是函数调用，命令 ni 不会进
入函数内部，命令 si 会进入函数内部
D. 命令 p $rsp 表示将 $rsp 寄存器中的值打印出来，如果 p 后面加上 /x 或
/d，表示打印成以十六进制或整数的形式

---

### 2025Lab测验-无答案 · Lab 任务 18

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 277–299 行　·　模块判定：Machine Prog
> 考什么：BombLab phase_1 反汇编分析

18. （2分）下面是phase_1函数的反汇编代码，下面描述正确的是：
A. phase_1中需要比较两个字符串是否相等，即使输入的字符串更长，但只要内置字
符串是输入字符串的前缀子串，就会判定为两个字符串相等
B. strings_not_equal是库函数，可以通过替换libc库使该函数返回0，从而直
接完成phase_1
C. 利用binutils的strings命令可以快速找到phase_1需要比对的内置字符串
D. 只查看phase_1的反汇编和寄存器信息无法获得需要比对的内置字符串的地址
 9 / 28

<!-- ===== page 10 ===== -->

0000000000002798 <phase_1>:
    2798:  f3 0f 1e fa            endbr64
    279c:  48 83 ec 08            sub    $0x8,%rsp
27a0:  48 8d 35 a1 1b 00 00  lea    0x1ba1(%rip),%rsi
      # 4348 <_IO_stdin_used+0x348>
    27a7:  e8 a6 05 00 00        call   2d52 <strings_not_equal>
    27ac:  85 c0                  test   %eax,%eax
    27ae:  75 05                  jne    27b5 <phase_1+0x1d>
    27b0:  48 83 c4 08            add    $0x8,%rsp
    27b4:  c3                     ret
    27b5:  e8 c7 06 00 00        call   2e81 <explode_bomb>
    27ba:  eb f4                  jmp    27b0 <phase_1+0x18>

---

### 2025Lab测验-无答案 · Lab 任务 19

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 300–344 行　·　模块判定：Machine Prog
> 考什么：BombLab phase_2 反汇编（数列递推）分析

19. （2分）下面是phase_2函数的反汇编代码。下列哪个输入使 bomb 爆炸？
A. 0 1 1 2 3 5
B. 0 1 1 3 5 11
C. 2 3 5 8 12 17
D. 2 3 5 9 17 33
00000000000027bc <phase_2>:
    27bc:  f3 0f 1e fa            endbr64
    27c0:  53                     push   %rbx
    27c1:  48 83 ec 20            sub    $0x20,%rsp
    27c5:  64 48 8b 04 25 28 00  mov    %fs:0x28,%rax
    27cc:  00 00
    27ce:  48 89 44 24 18        mov    %rax,0x18(%rsp)
    27d3:  31 c0                  xor    %eax,%eax
    27d5:  48 89 e6               mov    %rsp,%rsi
    27d8:  e8 d0 06 00 00        call   2ead <read_six_numbers>
    27dd:  83 3c 24 00            cmpl   $0x0,(%rsp)
    27e1:  78 07                  js     27ea <phase_2+0x2e>
    27e3:  bb 01 00 00 00        mov    $0x1,%ebx
    27e8:  eb 0a                  jmp    27f4 <phase_2+0x38>
    27ea:  e8 92 06 00 00        call   2e81 <explode_bomb>
 10 / 28

<!-- ===== page 11 ===== -->

    27ef:  eb f2                  jmp    27e3 <phase_2+0x27>
    27f1:  83 c3 01               add    $0x1,%ebx
    27f4:  83 fb 05               cmp    $0x5,%ebx
    27f7:  7f 1c                  jg     2815 <phase_2+0x59>
    27f9:  48 63 c3               movslq %ebx,%rax
    27fc:  8d 53 ff               lea    -0x1(%rbx),%edx
    27ff:  48 63 d2               movslq %edx,%rdx
    2802:  8b 14 94               mov    (%rsp,%rdx,4),%edx
    2805:  8d 54 12 ff            lea    -0x1(%rdx,%rdx,1),%edx
    2809:  39 14 84               cmp    %edx,(%rsp,%rax,4)
    280c:  74 e3                  je     27f1 <phase_2+0x35>
    280e:  e8 6e 06 00 00        call   2e81 <explode_bomb>
    2813:  eb dc                  jmp    27f1 <phase_2+0x35>
    2815:  48 8b 44 24 18        mov    0x18(%rsp),%rax
    281a:  64 48 2b 04 25 28 00  sub    %fs:0x28,%rax
    2821:  00 00
    2823:  75 06                  jne    282b <phase_2+0x6f>
    2825:  48 83 c4 20            add    $0x20,%rsp
    2829:  5b                     pop    %rbx
    282a:  c3                     ret
282b:  e8 60 fa ff ff        call   2290 <__stack_chk_fail@plt>

---

### 2025Lab测验-无答案 · Lab 任务 20

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 349–456 行　·　模块判定：Machine Prog
> 考什么：BombLab phase_3 跳转表与断点处寄存器分析

20. （2分）某同学在使用 GDB 调试BombLab phase_3 时，在 *phase_3 + 0x84
处设置了断点。然后该同学在 phase_3 中输入了0 0，触发了断点，并在断点处输
入了 info registers，获得寄存器信息。下面是phase_3的反汇编信息和断点处
的寄存器信息。下列哪个 phase_3 的输入不会使 bomb 爆炸？
A. 0 -197
B. 1 -901
C. 6 0
D. 7 -772
# objdump -d bomb
0000000000001829 <phase_3>:
    1829:  f3 0f 1e fa            endbr64
    182d:  48 83 ec 18            sub    $0x18,%rsp
    1831:  64 48 8b 04 25 28 00  mov    %fs:0x28,%rax
    1838:  00 00
    183a:  48 89 44 24 08        mov    %rax,0x8(%rsp)
    183f:  31 c0                  xor    %eax,%eax
    1841:  48 8d 4c 24 04        lea    0x4(%rsp),%rcx
    1846:  48 89 e2               mov    %rsp,%rdx
1849:  48 8d 35 50 2e 00 00  lea    0x2e50(%rip),%rsi
        # 46a0 <transition_table+0x340>
    1850:  e8 eb fa ff ff        call   1340 <__isoc99_sscanf@plt>
    1855:  83 f8 01               cmp    $0x1,%eax
    1858:  7e 1e                  jle    1878 <phase_3+0x4f>
    185a:  83 3c 24 07            cmpl   $0x7,(%rsp)
    185e:  0f 87 9a 00 00 00     ja     18fe <phase_3+0xd5>
    1864:  8b 04 24               mov    (%rsp),%eax
1867:  48 8d 15 b2 2a 00 00  lea    0x2ab2(%rip),%rdx
        # 4320 <_IO_stdin_used+0x320>
    186e:  48 63 04 82            movslq (%rdx,%rax,4),%rax
    1872:  48 01 d0               add    %rdx,%rax
    1875:  3e ff e0               notrack jmp *%rax
    1878:  e8 07 08 00 00        call   2084 <explode_bomb>
    187d:  eb db                  jmp    185a <phase_3+0x31>
    187f:  b8 00 00 00 00        mov    $0x0,%eax
 12 / 28

<!-- ===== page 13 ===== -->

    1884:  2d 1a 03 00 00        sub    $0x31a,%eax
    1889:  05 99 02 00 00        add    $0x299,%eax
    188e:  2d 04 03 00 00        sub    $0x304,%eax
    1893:  05 04 03 00 00        add    $0x304,%eax
    1898:  2d 04 03 00 00        sub    $0x304,%eax
    189d:  05 04 03 00 00        add    $0x304,%eax
    18a2:  2d 04 03 00 00        sub    $0x304,%eax
    18a7:  83 3c 24 05            cmpl   $0x5,(%rsp)
    18ab:  7f 06                  jg     18b3 <phase_3+0x8a>
    18ad:  39 44 24 04            cmp    %eax,0x4(%rsp)
    18b1:  74 05                  je     18b8 <phase_3+0x8f>
    18b3:  e8 cc 07 00 00        call   2084 <explode_bomb>
    18b8:  48 8b 44 24 08        mov    0x8(%rsp),%rax
    18bd:  64 48 2b 04 25 28 00  sub    %fs:0x28,%rax
    18c4:  00 00
    18c6:  75 42                  jne    190a <phase_3+0xe1>
    18c8:  48 83 c4 18            add    $0x18,%rsp
    18cc:  c3                     ret
    18cd:  b8 bf 02 00 00        mov    $0x2bf,%eax
    18d2:  eb b0                  jmp    1884 <phase_3+0x5b>
    18d4:  b8 00 00 00 00        mov    $0x0,%eax
    18d9:  eb ae                  jmp    1889 <phase_3+0x60>
    18db:  b8 00 00 00 00        mov    $0x0,%eax
    18e0:  eb ac                  jmp    188e <phase_3+0x65>
    18e2:  b8 00 00 00 00        mov    $0x0,%eax
    18e7:  eb aa                  jmp    1893 <phase_3+0x6a>
    18e9:  b8 00 00 00 00        mov    $0x0,%eax
    18ee:  eb a8                  jmp    1898 <phase_3+0x6f>
    18f0:  b8 00 00 00 00        mov    $0x0,%eax
    18f5:  eb a6                  jmp    189d <phase_3+0x74>
    18f7:  b8 00 00 00 00        mov    $0x0,%eax
    18fc:  eb a4                  jmp    18a2 <phase_3+0x79>
    18fe:  e8 81 07 00 00        call   2084 <explode_bomb>
    1903:  b8 00 00 00 00        mov    $0x0,%eax
    1908:  eb 9d                  jmp    18a7 <phase_3+0x7e>
    190a:  e8 91 f9 ff ff        call   12a0 <__stack_chk_fail@plt>
 13 / 28

<!-- ===== page 14 ===== -->

# objdump -s -j .rodata bomb
4320 add5ffff 5fd5ffff b4d5ffff bbd5ffff  ...._...........
4330 c2d5ffff c9d5ffff d0d5ffff d7d5ffff  ................
(gdb) info registers
rax            0xffffff3a         4294967098
rbx            0x55555555e6a0    93824992274080
rcx            0x0                 0
rdx            0x555555558320    93824992248608
rsi            0x0                 0
rdi            0x7fffffffd3c0    140737488344000
rbp            0x7fffffffdae0    0x7fffffffdae0
rsp            0x7fffffffda20    0x7fffffffda20
r8             0xffffffff         4294967295
r9             0x0                 0
r10            0x7ffff7db1fc0    140737351720896
r11            0x7fffffffd840    140737488345152
r12            0x1                 1
r13            0x0                 0
r14            0x55555555acc8    93824992259272
r15            0x7ffff7ffd000    140737354125312
rip            0x5555555558ad    0x5555555558ad <phase_3+132>
eflags         0x293              [ CF AF SF IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
fs_base        0x7ffff7fa1740   140737353750336
gs_base        0x0                0

---

### 2025Lab测验-无答案 · Lab 任务 22

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 475–482 行　·　模块判定：Machine Prog
> 考什么：缓冲区溢出漏洞、ASLR、金丝雀与 ROP 说法判断

22. （2分）下列关于AttackLab的描述中，哪个选项是正确的？
A. AttackLab的目标程序（target）往往包含缓冲区溢出漏洞，这个漏洞只存在于
getbuf函数的栈帧中
B. 在AttackLab中，我们尝试进行了空操作雪橇（nop sled）攻击
C. ctarget, starget, rtarget都没有使用地址空间布局随机化（ASLR）技术，
因此可以直接注入可执行的攻击代码
D. 因为存在金丝雀值保护机制，所以我们不能在栈上直接注入可执行的攻击代码，而
必须使用ROP技术

---

### 2025Lab测验-无答案 · Lab 任务 23

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 483–489 行　·　模块判定：Machine Prog
> 考什么：gdb 调试 ctarget 的命令用法

23. （2分）在AttackLab中，gdb调试器用于调试目标程序，分析程序的运行状态和内
存布局。假设现在需要调试一个名为ctarget的目标程序，下列哪个选项是正确的的？
A. 使用命令gdb ctarget启动gdb调试器后，想要调试的程序自动开始运行
B. 如果我们想要以十六进制格式打印出寄存器$rdi的值，可以使用命令x/x $rdi
C. 可以使用命令break getbuf或b getbuf在getbuf函数入口处设置断点
D. 在gdb中，可以使用命令run > input.txt将文件input.txt的内容作为输
入传递给目标程序

---

### 2025Lab测验-无答案 · Lab 任务 24

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 494–507 行　·　模块判定：Machine Prog
> 考什么：getbuf 函数栈帧大小计算

24. （2分）下面给出了AttackLab中ctarget目标程序的getbuf函数的汇编代码；
在call指令执行完成后，getbuf的栈帧大小为；
A. 0x38字节
B. 0x3C字节
C. 0x40字节
D. 0x44字节
0000000000401cb2 <getbuf>:
  401cb2:  f3 0f 1e fa            endbr64
  401cb6:  48 83 ec 38            sub    $0x38,%rsp
  401cba:  48 89 e7               mov    %rsp,%rdi
  401cbd:  e8 57 03 00 00        call   402019 <Gets>
  401cc2:  b8 01 00 00 00        mov    $0x1,%eax
  401cc7:  48 83 c4 38            add    $0x38,%rsp
  401ccb:  c3                     ret

---

### 2025Lab测验-无答案 · Lab 任务 25

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 508–561 行　·　模块判定：Machine Prog
> 考什么：AttackLab phase3 栈布局与 ROP 题解判断

25. （2 分）在 AttackLab 的 phase3 中，我们需要通过缓冲区溢出来执行特定的函数
touch3。下面给出了touch3以及其调用的hexmatch的函数原型，以及phase3的
一种题解。判断下面说法错误的是：
A. 缓冲区的大小为56字节
B. 在执行movq &cookie, %rdi指令时，寄存器%rsp的值是0x5566bd88
C. 当执行完movq &cookie, %rdi指令后，寄存器%rdi的值是0x5566bda0
D. 如果 cookie 的字符串表示末尾的 00 字节是为了填充对齐而添加的，hexmatch
函数在比较时会忽略该字节
/* Compare string to hex represention of unsigned value */
int hexmatch(unsigned val, char *sval)
{
    char cbuf[110];
    /* Make position of check string unpredictable */
    char *s = cbuf + random() % 100;
    sprintf(s, "%.8x", val);
    return strncmp(sval, s, 9) == 0;
}
 16 / 28

<!-- ===== page 17 ===== -->

void touch3(char *sval)
{
    vlevel = 3; /* Part of validation protocol */
    if (hexmatch(cookie, sval)) {
        printf("Touch3!: You called touch3(\"%s\")\n", sval);
        validate(3);
    } else {
        printf("Misfire: You called touch3(\"%s\")\n", sval);
        fail(3);
    }
    exit(0);
}
// phase3的一种题解
/* padding with 56 bytes */
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
/* Address of exploit code movq &cookie, %rdi */
98 bd 66 55 00 00 00 00
/* Address of a ret in exploit code, used for %rsp alignment */
9f bd 66 55 00 00 00 00
/* Address of touch3 */
98 1e 40 00 00 00 00 00
/* movq &cookie, %rdi */
48 c7 c7 a0 bd 66 55
/* ret */
c3
/* String representation of cookie */
32 64 36 66 63 32 64 35 00

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
