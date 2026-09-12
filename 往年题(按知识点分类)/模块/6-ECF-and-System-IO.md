# 异常控制流与系统级 I/O

> **英文模块名**：`ECF and System IO`  

> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，
> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。

## 一、清单

共 110 道题，来自 23 份材料。

| 年份 | 试卷 | 类别 | 题号 | 考什么 |
|---|---|---|---|---|
| 2013 | 2013期末-带答案 | 期末 | 第一题 9 | 信号的基本性质（待处理、SIGKILL） |
| 2013 | 2013期末-带答案 | 期末 | 第一题 10 | 非局部跳转 setjmp/longjmp |
| 2013 | 2013期末-带答案 | 期末 | 第一题 15 | open/read/write 后文件偏移与内容 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 16 | open 与 dup 的文件描述符/open file table |
| 2013 | 2013期末-带答案 | 期末 | 第五题 Part I | fork 与父子进程输出交错的可能顺序 |
| 2013 | 2013期末-带答案 | 期末 | 第五题 Part II | signal/kill 驱动 handler 输出 Fibonacci |
| 2014 | 2014期末-带答案 | 期末 | 第一题 10 | fork 次数与 hello 输出个数 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 11 | 中断/异常/故障/陷阱的同步异步性质 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 12 | SIGCHLD 处理程序与输出顺序 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 15 | open/dup/read/write 与文件长度 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 16 | 标准I/O、RIO 与缓冲区 |
| 2014 | 2014期末-带答案 | 期末 | 第六题 1 | fork/dup2/read/write 后文件内容与输出 |
| 2014 | 2014期末-带答案 | 期末 | 第六题 2 | 用 signal/alarm/pause 实现 sleep 的缺陷 |
| 2014 | 2014期末-带答案 | 期末 | 第七题 | 描述符表/打开文件表/v-node 表与 dup2 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 6 | 阻塞信号与待处理信号只处理一次 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 7 | 异常的定义与同步/异步性质 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 8 | 信号捕获/忽略、SIGCONT、系统调用中断 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 9 | 嵌套 fork 的输出可能 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 10 | Unix I/O：文件偏移、read、dup2/close |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 11 | printf 缓冲与 write 无缓冲的输出顺序 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第五题 | fork/signal/sigprocmask/管道中信号处理的输出 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 9 | fork 父子进程输出交错与 ++/-- |
| 2016 | 2016期末-带答案 | 期末 | 第一题 10 | 哪些事件会导致信号发送到进程 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 14 | dup2 共享文件偏移导致的内容变化 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 15 | RIO 交叉调用、fd 分配与打开文件表 |
| 2016 | 2016期末-带答案 | 期末 | 第五题 | fork/exit 输出排列与信号处理程序填空 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 9 | 嵌套 fork 的输出顺序可能性 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 10 | 信号语义、signal 与 SIGSTOP/SIGKILL |
| 2017 | 2017期末-无答案 | 期末 | 第一题 14 | dup/RIO/fork 与打开文件表的关系 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 15 | dup/dup2/O_APPEND 组合后的文件内容 |
| 2017 | 2017期末-无答案 | 期末 | 第五题 | fork/信号/sleep 与文件读取的输出行数及内容 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 5 | 模式位、waitpid、execve 与 signal |
| 2018 | 2018期末-带答案 | 期末 | 第一题 6 | dup2 链式重定向后的文件引用关系 |
| 2018 | 2018期末-带答案 | 期末 | 第四题 | signal/kill 交替打印与描述符表/v-node 表分析 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 9 | fork 次数与 printf 行缓冲 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 10 | 外部 I/O 触发中断 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 12 | 缺页故障与系统调用陷阱 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 13 | 信号处理程序中 printf 死锁与重定向 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 解答题三 | fork/open/dup/wait 与文件指针 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 7 | 故障/中断/异常的同步异步分类 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 9 | fork/setjmp/longjmp/execve 返回次数 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 17 | 信号处理程序中 printf 死锁 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 解答题三 | 文件描述符分配、dup 与文件指针 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 7 | 同步/异步异常与异常返回行为 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 9 | fork/setjmp/longjmp/execve 返回次数 |
| 2019 | 2019期末-无答案 | 期末 | 第四题 | open/dup/fork/waitpid 的文件描述符与文件内容 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 9 | fork() && fork() 的进程数与输出 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 10 | 网络报文到达触发的异常类型 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 11 | Ctrl+C 的 SIGINT 与前台进程组 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 12 | 缺页异常与系统调用的异同 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 13 | 并发流、/proc、execve 重定向与信号处理函数（兼 Concurrency） |
| 2020 | 2020期末-无答案 | 期末 | 第四题 | signal/fork/dup/open 的输出与 counter |
| 2021 | 2021期末-无答案 | 期末 | 第一题 12 | waitpid、信号与用户态/内核态转换 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 13 | Unix I/O、文件描述符与 RIO |
| 2021 | 2021期末-无答案 | 期末 | 第一题 14 | open 标志与 O_APPEND 对文件内容的影响 |
| 2021 | 2021期末-无答案 | 期末 | 第四题 | fork/信号/waitpid 的顺序输出与信号处理 |
| 2021 | 2021期末-无答案 | 期末 | 第五题 4 | double fault 异常的成因（不定项） |
| 2021 | chap 10 解析 | 期末 | 选择题 1 | Unix I/O：RIO、描述符重定向、open file table |
| 2021 | chap 10 解析 | 期末 | 选择题 2 | O_APPEND 与共享文件偏移下的写入顺序结果 |
| 2021 | chap 7 解析 | 期末 | 第 4 题 Part C | execve 加载后的入口点 _start 与运行在用户态 |
| 2021 | chap 8 解析 | 期末 | 第 1 题 | waitpid 选项组合、signal 例外、用户态与内核态切换、中断同步性 |
| 2021 | chap 8 解析 | 期末 | 第 2 题 | 异常四分类：中断/陷阱/故障/终止的判别 |
| 2021 | chap 8 解析 | 期末 | 大题 PART A | 父进程 fork 两个子进程，用信号在兄弟进程间同步输出奇偶数 |
| 2021 | chap 8 解析 | 期末 | 大题 PART B | 信号检测时机、相同信号只记一次、结合处理器给出可能输出 |
| 2021 | chap 9 解析 | 期末 | 大题 4 | 缺页故障处理程序不在主存时引发 double fault（兼 VM） |
| 2021 | chap 9 题目 | 期末 | 大题 4 | double fault：缺页处理程序再次触发故障 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 7 | 进程上下文切换与信号递送流程填空（含图） |
| 2022 | 2022期末-无答案 | 期末 | 第一题 8 | Shell 解析命令行后以 fork/execve 执行外部命令 |
| 2022 | 2022期末-无答案 | 期末 | 第四题 1(1) | 信号传随机数程序填空 A~F（含程序上下文） |
| 2022 | 2022期末-无答案 | 期末 | 第四题 1(2) | 第 43 行阻塞信号是否必需的后果分析 |
| 2022 | 2022期末-无答案 | 期末 | 第四题 2 | 处理函数加计数条件后子进程输出值推导 |
| 2022 | 2022期末-答案 | 期末 | 第一题 7 | 异常切内核态与信号处理程序 |
| 2022 | 2022期末-答案 | 期末 | 第一题 8 | fork/execve 进程控制 |
| 2022 | 2022期末-答案 | 期末 | 第四题 | 信号屏蔽与 sigsuspend 同步 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 7 | 进程调度/fork/异常返回/信号辨析 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 8 | stdio 缓冲区、SIGKILL 与 fork 缓冲区 |
| 2024 | 2024期末-带答案 | 期末 | 第三题 Part A | open/dup2/fork/write 与文件偏移 |
| 2024 | 2024期末-带答案 | 期末 | 第三题 Part B | 信号处理函数注册、kill 与 sigprocmask |
| 2024 | 2024期末-带答案 | 期末 | 第三题 Part C | fork 父子进程 buffer 与文件写结果 |
| 2025 | 2025期末-带答案 | 期末 | 二 15 | 异常四分类与返回行为 |
| 2025 | 2025期末-带答案 | 期末 | 二 16 | 进程上下文切换的时机与地址空间 |
| 2025 | 2025期末-带答案 | 期末 | 二 17 | fork 后共享 open file description 的 read |
| 2025 | 2025期末-带答案 | 期末 | 二 18 | SIGCHLD 合并递送、waitpid 回收与 zombie |
| 2025 | 2025期末-带答案 | 期末 | 二 19 | 阻塞期间同类信号 pending 不排队 |
| 2025 | 2025期末-带答案 | 期末 | 二 20 | execve 成功后 PID 与地址空间语义 |
| 2025 | 2025期末-无答案 | 期末 | 二 15 | 异常四分类与返回行为 |
| 2025 | 2025期末-无答案 | 期末 | 二 16 | 进程上下文切换的时机与寄存器保存 |
| 2025 | 2025期末-无答案 | 期末 | 二 17 | fork 后共享文件偏移下的 read 结果 |
| 2025 | 2025期末-无答案 | 期末 | 二 18 | SIGCHLD 不排队、waitpid 回收与 zombie |
| 2025 | 2025期末-无答案 | 期末 | 二 19 | 阻塞信号 pending 不排队与 sigprocmask |
| 2025 | 2025期末-无答案 | 期末 | 二 20 | execve 成功后的语义与 fd 保持 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2016 第一题 第10问 | SIGPIPE 与 I/O 多路复用（兼 Network） |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2018 第一题 第6问 | dup2 对未打开描述符也合法 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2018 第四题 | fork 后 fd 与信号竞争导致的输出 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2021 第三题 Part C | 可替换代码段的函数运行在用户态（存疑） |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第16/17讲 22 | 除 0 异常属 Faults 能否在处理器中修正后继续 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第16/17讲 23 | fork 程序的输出次数与输出顺序判断 |
| 2025 | 2025第2次阶段测验-带答案 | 阶段测验 | 第16/17讲 24 | 含 fork/wait/sleep 的程序进程数与输出行数 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 1 | ls -a 显示隐藏文件（L0 命令行） |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 2 | cd 的 - 参数表示上次所在目录 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 3 | chmod 755 的文件权限位 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 4 | tar/gcc/rm/rmdir/grep 命令用法辨误 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 16 | GDB 断点通过 INT3 触发陷阱实现 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 21 | hex2raw 用法与 shell 管道/输入输出重定向 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 35 | getopt 解析命令行参数（Unix API，CacheLab 语境） |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 36 | ShellLab tsh 与真实 shell 的功能对比 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 37 | 为避免竞态的信号屏蔽与解除时机 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 38 | ShellLab 内建命令 jobs/bg/kill/nohup |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 39 | sigchld_handler 中 WIFSTOPPED/WIFCONTINUED 判断 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 40 | waitfg 前台等待的正确实现（sigsuspend） |

## 二、题目原文

### 2013期末-带答案 · 第一题 9

> 出处：`原文/期末/2013期末-带答案.md` 第 126–134 行　·　模块判定：ECF and System IO
> 考什么：信号的基本性质（待处理、SIGKILL）

9、关于信号的描述，以下不正确的是哪一个？答：（        ）
A. 在任何时刻，一种类型至多只会有一个待处理信号
B. 信号既可以发送给一个进程，也可以发送给一个进程组
C. SIGTERM和SIGKILL信号既不能被捕获，也不能被忽略
D. 当进程在前台运行时，键入Ctrl-C，内核就会发送一个SIGINT信号给
这个前台进程
答案：C
说明：考察信号的基本了解，C应该为“SIGKILL和SIGSTOP信号既不能被捕获，
也不能被忽略”

---

### 2013期末-带答案 · 第一题 10

> 出处：`原文/期末/2013期末-带答案.md` 第 135–145 行　·　模块判定：ECF and System IO
> 考什么：非局部跳转 setjmp/longjmp

10、下面关于非局部跳转的描述，正确的是（        ）
A. setjmp可以和siglongjmp使用同一个jmp_buf变量
B. setjmp必须放在main()函数中调用
C. 虽然longjmp通常不会出错，但仍然需要对其返回值进行出错判断
4

<!-- ===== page 5 ===== -->

D. 在同一个函数中既可以出现setjmp，也可以出现longjmp
答案：D
说明：考察非局部跳转的基本了解；D选项：可以采用不同的jmp_buf

---

### 2013期末-带答案 · 第一题 15

> 出处：`原文/期末/2013期末-带答案.md` 第 183–197 行　·　模块判定：ECF and System IO
> 考什么：open/read/write 后文件偏移与内容

15、考虑如下代码，假设result.txt的初始内容是“123”。
int main(int argc, char** argv)
{
int fd1 = open("result.txt", O_RDWR);
char str[] = "abc";
char c;
write(fd1, str, 1);
read(fd1, &c, 1);
write(fd1, &c, 1);
return 0;
}
在这段代码执行完毕之后，result.txt 的内容是什么？（假设所有的系
统调用都会成功）答：（      ）
A．a22     B．a21     C．a13     D．abb
答案：A。考察文件操作过程中指针的移动情况。

---

### 2013期末-带答案 · 第一题 16

> 出处：`原文/期末/2013期末-带答案.md` 第 198–231 行　·　模块判定：ECF and System IO
> 考什么：open 与 dup 的文件描述符/open file table

16、已知如下代码段
write(fd1, str1, strlen(str1));
write(fd2, str2, strlen(str2));
可以在原本为空的文件ICS.txt中写下字符串 I love ICS!
对于下面这些对于变量fd1, fd2, str1, str2的定义：
(1)
int fd1 = open("ICS.txt", O_RDWR);
int fd2 = open("ICS.txt", O_RDWR);
char *str1 = "I love ";
char *str2 = "ICS!";
(2)
int fd1 = open("ICS.txt", O_RDWR);
int fd2 = dup(fd1);
6

<!-- ===== page 7 ===== -->

char *str1 = "I love ";
char *str2 = "ICS!";
(3)
int fd1 = open("ICS.txt", O_RDWR);
int fd2 = open("ICS.txt", O_RDWR);
char *str1 = "I love ";
char *str2 = "I love ICS!";
(4)
int fd1 = open("ICS.txt", O_RDWR);
int fd2 = dup(fd1);
char *str1 = "I love ";
char *str2 = "I love ICS!";
下面哪一个组合是正确的：（       ）
A．(1)(4)       B．(2)(3)       C．(1)(2)(3)(4)    D．都不正确
答案：B
说明：考察两种不同文件描述符指向同一文件v的不同，一种是指向了同一的open
file table，一种是指向了同一的v-node table。

---

### 2013期末-带答案 · 第五题 Part I

> 出处：`原文/期末/2013期末-带答案.md` 第 429–447 行　·　模块判定：ECF and System IO
> 考什么：fork 与父子进程输出交错的可能顺序

 第五题（10分）
P请a阅rt读 以I 下程序，然后回答问题（假设程序中的函数调用都可以正确执行）：
int main() {
   pirfi (nftofr(k"(A\)n "=)=;  0) {
    }  printf("B\n");
   e lsep r{i ntf("C\n");
    A
   }p rintf(“D\n");
 }  exit(0);
（1） 如果程序中的A位置的代码为空，列出所有可能的输出结果：（1分）
 4个：分别是ABDCD ABCDD ACBDD ACDBD（错一个扣半分，多了也扣半分，最
多扣1分）
 （2）如果程序中的A位置的代码为：
列出所wa有it可p能id的(-输1出, 结NU果L：L（, 20分);）
 3个：分别是ABDCD ABCDD ACBDD（每个半分，多了扣一分，最多扣2分）
 （3）如果程序中的A位置的代码为：
列出所pr有in可t能f(的“E输\出n”结);果 ：（2分）
7个： 分别是ABDCED ABCEDD ACEBDD ACEDBD ACBEDD ACBDED ABCDED（错
一  个扣半分，多了扣一分）

---

### 2013期末-带答案 · 第五题 Part II

> 出处：`原文/期末/2013期末-带答案.md` 第 452–491 行　·　模块判定：ECF and System IO
> 考什么：signal/kill 驱动 handler 输出 Fibonacci

Part II
请阅读以下程序，然后回答问题（假设程序中的函数调用都可以正确执行，且
每条语句都是原子动作）：
pid_t pid;  1). 完成程序，使得程序在输出前20个
int even = 0;  斐波那契(Fibonacci)数列，即 F0=0,
int counter1 = 0;  F1=1, …, Fn=Fn-1+Fn-2。（如果存在对本
ivnoti dc ohuanntdelre2r 1=( i1n;t  sig) {  次程序执行结果没有影响的语句，请在相
  if (even % 2 == 0) {  应位置填写“无关”）（3分）
  printf(“%d\n”,
counter1);    A: ___counter1 + counter2__
    counter1 =      A       ;
    } else {    B: ___counter1 + counter2__
  printf(“%d\n”,
counter2);    C: ___even + 1____________
    counter2 =      B      ;
    }    D: ____无关__________
    even =      C      ;
}    E: ___SIGUSR1___________
void handler2(int sig) {
    if (_____D_____) {    F: ___SIGUSR1___________
    counter1 = even * even;
    } else {  2). 完成程序，其中A, B处保持不变，
    counter2 = even * even;  使得程序可以分别输出前几个奇数或偶
    }  数的平方和。（如果存在对本次程序执行
}  结果没有影响的语句，请在相应位置填写
int smiaginna(l)( S{I GUSR1, handler1);  “无关”）（2分）
signal(SIGUSR2, handler2);  其中：
if ((pid = fork()) == 0) {    若要输出奇数的平方和：even的初
while (1) {};  始值为3；
    }    若要输出偶数的平方和，even的初
    while (even < 20) {  始值为2。
      kill(pid,     E   );
      sleep(1);    C: ____even + 2__________
      kill(pid,     F   );
      sleep(1);    D: ____even % 2 == 1______
      even += 2;
    }    E: ____SIGUSR2__________
kill(pid, SIGKILL);
exit(0);    F: ____SIGUSR1__________
}

---

### 2014期末-带答案 · 第一题 10

> 出处：`原文/期末/2014期末-带答案.md` 第 149–166 行　·　模块判定：ECF and System IO
> 考什么：fork 次数与 hello 输出个数

10. 在系统调用成功的情况下，下列代码会输出几个hello？(      )
void doit()
{
if ( fork() == 0 ) {
        printf("hello\n");
        fork();
    }
    return ;
}
int main()
{
    doit();
    printf("hello\n");
    exit(0) ;
}
A. 3    B. 4    C. 5    D. 6
【答案】B
【说明】考查学生对fork执行机制的理解和掌握。

---

### 2014期末-带答案 · 第一题 11

> 出处：`原文/期末/2014期末-带答案.md` 第 167–173 行　·　模块判定：ECF and System IO
> 考什么：中断/异常/故障/陷阱的同步异步性质

11. 下列说法中哪一个是错误的？(      )
A． 中断一定是异步发生的
B． 异常处理程序一定运行在内核模式下
C． 故障处理一定返回到当前指令
D．陷阱一定是同步发生的
【答案】C
【说明】

---

### 2014期末-带答案 · 第一题 12

> 出处：`原文/期末/2014期末-带答案.md` 第 178–197 行　·　模块判定：ECF and System IO
> 考什么：SIGCHLD 处理程序与输出顺序

12. 下列这段代码的输出不可能是(      )
void handler()
{
    printf("h");
}
int main()
{
    signal(SIGCHLD, handler) ;
    if ( fork() == 0 ) {
        printf("a") ;
    } else {
        printf("b") ;
    }
    printf("c") ;
    exit(0) ;
}
A. abcc   B. abch    C. bcach    D. bchac
【答案】Ｄ
【说明】SIGCHLD信号只有在fork的子进程结束时产生，因此h只会出现在ac
之后。

---

### 2014期末-带答案 · 第一题 15

> 出处：`原文/期末/2014期末-带答案.md` 第 222–243 行　·　模块判定：ECF and System IO
> 考什么：open/dup/read/write 与文件长度

15. ICS.txt中包含3000个字符，考虑如下代码段：
int main(int argc, char** argv) {
int fd = open("ICS.txt", O_CREAT | O_RDWR, S_IRUSR |
S_IWUSR);
write(fd, "ICS", 3);
char buf[128];
int i;
for (i = 0; i < 10; i++) {
int fd1 = open("ICS.txt", O_RDWR);
int fd2 = dup(fd1);
int cnt = read(fd1, buf, 128);
write(fd2, buf, cnt);
}
return 0;
}
上述代码执行完后，ICS.txt 中包含多少个字符（假设所有系统调用都成功）？
（     ）
A．3        B．256          C．3000        D．3072
【答案】Ｃ
【说明】主要考查open函数的用法。open不像fopen，不设置O_TRUNC并不
会清空文件。所以只会反复把文件中字符1-128写到字符129-256，字符数不变。
几个干扰项分别考查dup的作用以及buf大小对于程序功能的影响。

---

### 2014期末-带答案 · 第一题 16

> 出处：`原文/期末/2014期末-带答案.md` 第 244–256 行　·　模块判定：ECF and System IO
> 考什么：标准I/O、RIO 与缓冲区

16. 下列系统I/O的说法中，正确的是(      )
7

<!-- ===== page 8 ===== -->

A． C语言中的标准I/O函数在不同操作系统中的实现代码一样
B． 对于同一个文件描述符，混用RIO包中的rio_readnb和rio_readn两个
函数不会造成问题
C． C语言中的标准I/O函数是异步线程安全的
D． 使用I/O缓冲区可以减少系统调用的次数，从而加快I/O的速度
【答案】D
【说明】A中在不同操作系统需要用到不同系统调用。B中两个函数一个从buffer
读一个直接读，混用会造成错误。C不是线程安全的。D正确。

---

### 2014期末-带答案 · 第六题 1

> 出处：`原文/期末/2014期末-带答案.md` 第 607–638 行　·　模块判定：ECF and System IO
> 考什么：fork/dup2/read/write 后文件内容与输出

 第六题（10分）ECF
 1 .（5 分）以下程序运行时系统调用全部正确执行，buffer.txt 文件的内容为
pekinguniv。请给出代码运行后打印输出的结果，并给出程序运行结束后
buffer.txt文件的内容。
##iinncclluuddee  <<ssttddiloi.bh.>h>
##iinncclluuddee  <<fucnnitslt.dh.>h>
 int main() {
        cihnat r fci;le 1 = open("buffer.txt", O_RDWR);
     int file2;
        rfeialde(2f i=l ed1u,p (&fci,l e11));;
        wprriitnet(ff("i1le 2=, % c&\cn," 1,) ;c) ;
     int pid = fork() ;
         i f   (rpeiadd (=f=i l0e)1 ,{  &c, 1);
                wprriitnet(ff("i2l e=2 ,% c&\cn," 1, );c) ;
        read(file1, &c, 1);
                        pcerlxioinstte(0f()(f";i3l  e=1 )%;c \n", c);
         }   e lwsaei t{p id(pid, NULL, 0);
                cdluops2e((ffiillee12,) ;fi le2);
                rweraidt(ef(ifliel2e,2 ,& c&,c ,1 )1;);
         }    printf("4 = %c\n", c);
    return 0;
}
19

<!-- ===== page 20 ===== -->

答案：
1 = p
2 = k
3 = n
4 = g
buffer.txt文件内容为ppkknggniv

---

### 2014期末-带答案 · 第六题 2

> 出处：`原文/期末/2014期末-带答案.md` 第 639–667 行　·　模块判定：ECF and System IO
> 考什么：用 signal/alarm/pause 实现 sleep 的缺陷

2.（5分）某程序员实现了一个课程实验用的操作系统ICSNIX，其系统函数sleep
用以下代码实现。请分析该代码存在哪些问题。
1 #include    <signal.h>
2 #include    <unistd.h>
3 static void sig_alrm(int signo)
4 {
5    /* nothing to do, just return to wake up the pause */
6 }
7
8 unsigned int sleep(unsigned int seconds)
9 {
10    if (signal(SIGALRM, sig_alrm) == SIG_ERR)
11       return(seconds);
12
13    alarm(seconds); /* start the timer */
14    pause(); /* next caught signal wakes us up */
15    return(alarm(0)); /* turn off timer, return unslept time */
16}
答案：（三个问题若只回答了1个或2个则每个2分，全部回答了得5分）
问题1) 由于操作系统调度的原因，alarm信号触发时，pause可能还未执行，
导致sleep调用永不会返回。
问题 2) 如果应用程序在调用 sleep 之前已经调用了 alarm，则 sleep 中的
alarm 调用会取消之前设置的 alarm 闹钟。（若用户调用 alarm(5);
sleep(10); 则第 5 秒 sleep 就应该唤醒；若用户调用 alarm(20);
sleep(10); 则 sleep 在 10 秒返回后，再过 10 秒应继续产生一个 SIGALRM
信号。）
问题 3) sleep的signal调用改变了整个程序的SIGALRM信号处理方式。因
此sleep应该保留signal的返回值（旧的SIGALRM信号处理程序），并在返回
前恢复该值。

---

### 2014期末-带答案 · 第七题

> 出处：`原文/期末/2014期末-带答案.md` 第 673–721 行　·　模块判定：ECF and System IO
> 考什么：描述符表/打开文件表/v-node 表与 dup2

第七题（10分）系统I/O
（用作试卷题目时，请把红字和红色箭头全部删去）
请阅读下面的代码：
1:  int main(int argc, char** argv) {
2:  int  fd1  =  open("ICS.txt",  O_CREAT|O_RDWR,
3:  S_IRUSR|S_IWUSR);
4:  write(fd1, "abc", 3);
5:
6:      int fd2 = fd1;
7:      int fd3 = dup(fd2);
8:      int fd4 = open("ICS.txt", O_APPEND|O_RDWR);
9:      write(fd2, "defghi", 6);
10:      write(fd4, "xyz", 3);
11:
12:      int fd5 = fd4;
13:      dup2(fd3, fd5);
14:      write(fd4, "pqr", 3);
15:
16:      close(fd1);
17:
18:      return 0;
19:  }
1.请填写在第16行代码刚刚执行完之后，下面的打开文件表和v-node表中表项
的部分值，并画出表项之间的指向关系。（6分）
初始时，ICS.txt文件不存在。程序执行时，所有的系统调用均会成功，所有
表项均会从上到下依次分配，描述符表一开始被占用掉前3个表项。对于已经释放
的打开文件表表项，请填写释放前那一刻的值和指向的v-node表表项。
对于多余的表项，请直接忽略。
21

<!-- ===== page 22 ===== -->

  描述符表  打开文件表    v-node表
Descriptor table  Open file table  v-node table
...    pos  refcnt  释放？    文件名
3  12  2  N  ICS.txt
4  12  0  Y
5
6
7
 说明：考查三层表结构的基本概念，以及Unix I/O的基本用法。因为第8章
出题会融合第10章内容，所以没涉及到第8章内容。
错一空或者多/少填一空，扣1分。多画/少画一个箭头扣1分。扣完为止。
2. 请填写在第16行代码刚刚执行完之后，下列变量的值（2分）
fd1  fd2  fd3  fd4  fd5
  说明：错3 1空扣1分，3扣 完为止。 4  5  5
 3.请写出程序执行完之后，ICS.txt文件中的内容（2分）
a说b明cd：e写fg成hiapbqcrx yzghipqr给1分，出现此错误是因为不熟悉O_APPEND用
法。

---

### 2015期末-20160104-带答案 · 第一题 6

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 86–93 行　·　模块判定：ECF and System IO
> 考什么：阻塞信号与待处理信号只处理一次

6.  一段程序中阻塞了SIGCHLD和SIGUSR1信号。接下来，向它按顺序发送
SIGCHLD，SIGUSR1，SIGCHLD信号，当程序取消阻塞继续执行时，将处理
这三个信号中的哪几个？
A.  都不处理
B.  处理一次SIGCHLD
C.  处理一次SIGCHLD，一次SIGUSR1
D.  处理所有三个信号
答案：C。

---

### 2015期末-20160104-带答案 · 第一题 7

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 94–104 行　·　模块判定：ECF and System IO
> 考什么：异常的定义与同步/异步性质

7.  学完本课程后，几位同学聚在一起讨论有关异常的话题，请问你认为他们中谁
学习的结果有错误？
3

<!-- ===== page 4 ===== -->

A.  发生异常和异常处理意味着控制流的突变。
B.  与异常相关的处理是由硬件和操作系统共同完成的。
C.  异常是由于计算机系统发生了不可恢复的错误导致的。
D.  异常的发生可能是异步的，也可能是同步的。
答案：C。异常不一定是不可恢复的，也可能是可恢复的、甚至是有意产生的。

---

### 2015期末-20160104-带答案 · 第一题 8

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 105–113 行　·　模块判定：ECF and System IO
> 考什么：信号捕获/忽略、SIGCONT、系统调用中断

8.  下列说法正确的是：
A．SIGTSTP信号既不能被捕获，也不能被忽略
B．存在信号的默认处理行为是进程停止直到被SIGCONT信号重启
C．系统调用不能被中断，因为那是操作系统的工作
D．子进程能给父进程发送信号，但不能发送给兄弟进程
答案：B
A：SIGTSTP可以被忽略；既不能被捕获又不能被忽略的是SIGKILL和SIGSTOP
C：系统调用可以被中断，如read这样的慢速系统调用
D：可以通过kill(0, …)给整个组的进程发送信号

---

### 2015期末-20160104-带答案 · 第一题 9

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 114–138 行　·　模块判定：ECF and System IO
> 考什么：嵌套 fork 的输出可能

9.  在系统调用成功的情况下，下面哪个输出是可能的？
int main() {
  intpid = fork();
  if (pid == 0) {
    printf("A");
  } else {
    pid = fork();
    if (pid == 0) {
      printf("A");
    } else {
      printf("B");
    }
  }
  exit(0);
}
A. AAB
B. AAA
C. AABB
D. AA
4

<!-- ===== page 5 ===== -->

答案：A
总共产生3个子进程，共输出2个A和1个B

---

### 2015期末-20160104-带答案 · 第一题 10

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 139–151 行　·　模块判定：ECF and System IO
> 考什么：Unix I/O：文件偏移、read、dup2/close

10. 以下四句都是关于Unix I/O的说法。其中正确的是：
A. 从网络套接字（socket）读取内容时，可以通过反复读的方式处理不足值
问题，直到读完所需要的数量或遇到EOF为止。
B. 以O_RDWR方式打开文件后，文件会有两个指针，分别记录读文件的当前位
置和写文件的当前位置。
C. 用read函数直接读取控制台输入的文本行，会自动在行末追加‘\0’字符。
D. 使用 dup2(4, 1)成功进行重定向后执行 close(4)，会导致 1号文件描
述符也不可用。
参考信息：O_RDWR表示文件可读可写；dup2(oldfd, newfd)表示将oldfd
重定向给newfd。
答案：A。
说明：B. 并没有两个指针，读写操作是共用一个指针的；C. read 操作不会追
加‘\0’字符；D. close(4)后1号描述符仍然可用。

---

### 2015期末-20160104-带答案 · 第一题 11

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 152–183 行　·　模块判定：ECF and System IO
> 考什么：printf 缓冲与 write 无缓冲的输出顺序

11. 下面是一段C程序代码：
#include <stdio.h>
#include "csapp.h"
int main()
{
  printf("2");
  if (Fork())
  {
    printf("33");
    Write(STDOUT_FILENO, "lol", 3);
  }
  else
  {
    Sleep(1);
    printf("233");
    Write(STDOUT_FILENO, "hhhh", 4);
5

<!-- ===== page 6 ===== -->

  }
  fflush(stdout);
  return 0;
}
编译后运行程序，程序正常退出。那么程序的输出是：
A.  233lol233hhhh
B.  lol233hhhh2233
C.  233lol2233hhhh
D.  2lol33hhhh233
答案：B。
说明：printf 所属的标准 IO 是有缓冲区的，直到关闭文件、遇到换行符或者
fflush时才会输出；write则没有缓冲区立刻输出。

---

### 2015期末-20160104-带答案 · 第五题

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 524–553 行　·　模块判定：ECF and System IO
> 考什么：fork/signal/sigprocmask/管道中信号处理的输出

 第五题（10分）异常
 以 下程序运行时系统调用全部正确执行，且每个信号都被处理到。请给出代码运行
后所有可能的输出结果。
###iiinnncccllluuudddeee   <<<ssuttnddiilsoit.bdh..>hh>>
# include <signal.h>
i nt c = 1;
void handler1(int sig) {
   cp+r+i;nt f("%d", c);
}
i nt main() {
   ssiiggnsaelt(_StI GsU;S R1, handler1);
   ssiiggeamdpdtsyeste(t&(s&,s )S;IG USR1);
   sigprocmask(SIG_BLOCK, &s, 0);
   intpid = fork()?fork():fork();
  if (kpiildl (=g=e t0p)p i{d (), SIGUSR1);
    printf("S");
      } elsesixegi pt{r( o0c)m;a sk(SIG_UNBLOCK, &s, 0);
19

<!-- ===== page 20 ===== -->

      wshiiglper o(cwmaaistkp(iSdI(G_-U1N,B LNOUCLKL,,  &0s),  !0=) ;-1 );
    }  printf("P");
 }  return 0;
 答  ：
 答案：
共5种：
SSS2S2P2SSP222PPPP
S2SP2P
   SS22PP

---

### 2016期末-带答案 · 第一题 9

> 出处：`原文/期末/2016期末-带答案.md` 第 150–162 行　·　模块判定：ECF and System IO
> 考什么：fork 父子进程输出交错与 ++/--

9.  对于以下一段代码，可能的输出为：
   int count = 0;
    int pid = fork();
    if (pid == 0){
        printf("count = %d\n",--count);
    }
    else{
        printf("count = %d\n",++count);
    }
    printf("count = %d\n",++count);
A.1 2 -1 0       B.0 0 -1 1
C.1 -1 0 0       D.0 -1 1 2
答案:A(printf从后向前处理，注意fork出的子进程与父进程执行顺序不确定)

---

### 2016期末-带答案 · 第一题 10

> 出处：`原文/期末/2016期末-带答案.md` 第 163–168 行　·　模块判定：ECF and System IO
> 考什么：哪些事件会导致信号发送到进程

10. 下列哪一事件不会导致信号被发送到进程？
A. 新连接到达监听端口
B. 进程访问非法地址
C. 除零
D. 上述情况都不对
答案:A(考察对各种情况的理解)

---

### 2016期末-带答案 · 第一题 14

> 出处：`原文/期末/2016期末-带答案.md` 第 192–208 行　·　模块判定：ECF and System IO
> 考什么：dup2 共享文件偏移导致的内容变化

14. 考ch虑ar以 *下st代r1码 =， "假66设66"r;e sult.txt中的初始内容为“666666”
    cchhaarr  **ssttrr23  ==  ""2h3h3h3h"";;
   int fd1, fd2, fd3, i;
   ffdd12  ==  ooppeenn((""rreessuulltt..ttxxtt"",,  OO__RRDDWWRR));;
  dup2(fd1, fd2);
    f or f(di3  ==  0o;p ein (<" r5e;s u+l+ti.)t x{t ", O_RDWR);
      wwrriittee((ffdd12,,  ssttrr12,,  44));;
    write(fd3, str3, 4);
     }  close(fd3);
  close(fd1); close(fd2);
  假设所有系统调用均成功，则这段代码执行结束后，result.txt 的内容中
有（）个“6”
  A. 6
  B. 16
  C. 20
  D. 22
答  案：B (考察文件读写位置的理解)

---

### 2016期末-带答案 · 第一题 15

> 出处：`原文/期末/2016期末-带答案.md` 第 213–220 行　·　模块判定：ECF and System IO
> 考什么：RIO 交叉调用、fd 分配与打开文件表

15. 关于IO操作，以下说法中正确的是（）
  A. 由于RIO包的健壮性，所以RIO中的函数都可以交叉调用
  B. 成功调用open函数后，返回一个不小于3的文件描述符
  C. 调用Unix I/O开销较大，标准I/O库使用缓冲区来加快I/O的速度
  D. 和描述符表一样，每个进程拥有独立的打开文件表
答案：C  (RIO中带缓冲的函数不应与无缓冲的函数交叉调用，A错误。若标准输
入、标准输出或标准错误被关闭，则会返回一个小于3的文件描述符，B错误。打
开文件表是所有进程共享的，D错误)

---

### 2016期末-带答案 · 第五题

> 出处：`原文/期末/2016期末-带答案.md` 第 475–559 行　·　模块判定：ECF and System IO
> 考什么：fork/exit 输出排列与信号处理程序填空

 第五题（10分）
P请a阅rt读 I以 下程序，然后回答问题。假设程序中的函数调用都可以正确执行，并默认
pinrti nmtafin执()行 {完 会调用fflush。
    iipnnittd  _cp1ni=tdf=_o11r;,k p(i)d;_ 2;
    i  f(ppiiifdd(__p12i==d=f_0o2)r! k=(0)){;     {
          }  wpariitn(tpfi(d"_B2",)N;U LL,0);
      }  perxiintt(f0()";F ");
    e  lseAB   {
        wpiaifid(t_p(2ip=dif_do2_r=1k=,(0N))U ; L L,{0 );
          }  pcrnitn-t=f1(;" D");
        i efl(sce n p tr=i=n0t)f ("E");
      }   exitp(r0i)n;t f("G");
}（ 1）如果程序中的A、B位置的代码为空，列出所有可能的输出结果：
（FFBB1FFGD分DG）EE  3个，全对才得分
（2）如FB果FD程EG序 中的A、B位置的代码为：
15

<!-- ===== page 16 ===== -->

    A:   printf("C");
    B：   exit(0);
列出所有可能的输出结果：
（2分）4个，对1~3个给1分，全对给2分
CFBF
FCBF
FBCF
FBFC
Part II
请阅读以下程序，然后回答问题（假设程序中的函数调用都可以正确执行，且
每条语句都是原子动作）：
pid_t pid;
int even = 0;
int counter1 = 0;
int counter2 = 1;
void handler1(int sig) {
  if (even % 2 == 0) {
  printf("%d\n", counter1);
    counter1 =      A       ;
    } else {
    printf("%d\n", counter2);
      counter2 =      B      ;
    }
    even = even+    C       ;
  }
void handler2(int sig) {
    if (_____D_____) {
    counter1 = even*even;
    } else {
    counter2 = even*even;
    }
}
int main() {
signal(SIGUSR1, handler1);
signal(SIGUSR2, handler2);
if ((pid = fork()) == 0) {
while (1) {};
  }
    while (even < 30) {
      kill(pid,     E   );
      sleep(1);
16

<!-- ===== page 17 ===== -->

      kill(pid,     F   );
      sleep(1);
      even = even+    G      ;
    }
kill(pid, SIGKILL);
exit(0);
}
（1）完成程序，使得程序在输出的数字为以下Q队列的前30项，Q队列定义如下：
𝑄𝑛+1,   n%2=0
𝑄0=0, 𝑄1=1, 𝑄𝑛+2={     (𝑛=0,1,2,3,...)
𝑄𝑛×2,   n%2≠0
（若某个位置中的程序内容，对本次程序执行结果没有影响，请在相应位置填写“无
关”）
（7分）7个，对1个给1分
  A:                          counter1+1
  B:                         counter2*2
  C:                              1
  D:                             无关
  E:                         SIGUSR1
  F:                         SIGUSR1
  G:                              2

---

### 2017期末-无答案 · 第一题 9

> 出处：`原文/期末/2017期末-无答案.md` 第 117–129 行　·　模块判定：ECF and System IO
> 考什么：嵌套 fork 的输出顺序可能性

9.  下列程序输出的数字顺序可能是：
int count = 1;
if (fork() == 0) {
  if (fork() == 0) {
    printf("%d\n", ++count);
  }
  else {
    printf("%d\n", --count);
  }
}
printf("%d\n", ++count);
A. 0 1 3 2 2     B. 0 3 2 2 1
C. 2 0 1 3 2     D. 2 1 0 2 3

---

### 2017期末-无答案 · 第一题 10

> 出处：`原文/期末/2017期末-无答案.md` 第 130–135 行　·　模块判定：ECF and System IO
> 考什么：信号语义、signal 与 SIGSTOP/SIGKILL

10. 下列关于信号的说法不正确的是：
A. 在键盘上输入Ctrl-C会导致内核发送一个SIGINT信号到前台进程组中的每
个进程
B. 每种类型最多只能有一个未处理的信号
C. SIGINT的处理函数不能被另一个SIGINT信号中断
D. 进程可以通过使用signal函数修改和SIGSTOP相关联的默认行为

---

### 2017期末-无答案 · 第一题 14

> 出处：`原文/期末/2017期末-无答案.md` 第 156–164 行　·　模块判定：ECF and System IO
> 考什么：dup/RIO/fork 与打开文件表的关系

14. 以下关于文件I/O的说法中，正确的是：
A. 文件重定向（dup 和 dup2）操作仅仅改变了文件描述符的指向，不会改变打
开文件表中的内容
B. 进程调用fork()时，可能对文件描述符表和打开文件表采用写时拷贝（Copy
on Write）机制
C. 对同一描述符，rio_readlineb 和 rio_readnb 可以任意交叉使用，
rio_readn和rio_writen也可以任意交叉使用
D. RIO中包括无缓冲的输入输出函数和带缓冲的输入输出函数，使用带缓冲的输
入输出函数时，要先声明一个rio_t类型变量并调用rio_readinitb函数

---

### 2017期末-无答案 · 第一题 15

> 出处：`原文/期末/2017期末-无答案.md` 第 165–184 行　·　模块判定：ECF and System IO
> 考什么：dup/dup2/O_APPEND 组合后的文件内容

15. 以下程序执行完成后，ICS.txt文件中的内容是：
int main(int argc, char** argv) {
int fd1 = open("ICS.txt", O_CREAT|O_RDWR,
 S_IRUSR|S_IWUSR);
write(fd1, "ics ", 4);
int fd2 = fd1;
int fd3 = dup(fd2);
int fd4 = open("ICS.txt", O_APPEND|O_RDWR);
write(fd2, "segmentation fault ", 19);
write(fd4, "tao", 3);
int fd5 = fd4;
dup2(fd3, fd5);
write(fd4, "lab", 3);
close(fd1);
return 0;
}
A. ics segmentation fault tao
B. ics segmentation fault lab
C. ics taomentation fault lab
D. tao segmentation fault lab

---

### 2017期末-无答案 · 第五题

> 出处：`原文/期末/2017期末-无答案.md` 第 354–408 行　·　模块判定：ECF and System IO
> 考什么：fork/信号/sleep 与文件读取的输出行数及内容

 第五题（10分）
代  码如下：（仅为示例代码，答题时不考虑任何出错的情况）
#include <stdio.h>
##iinncclluuddee  <<sutndilsitbd..hh>>
##iinncclluuddee  <<fscynst/lt.yhp>es .h>
# include <sys/wait.h>
ii nntt  ccoouunntteerr12  ==  11;;
void handler(int sig) {
                iiff  ((ssiigg  ====  SSIIGGUUSSRR12))          ccoouunntteerr12++++;;
} in t main(int argc, char **argv)
{         int i;
                piindt_ tf dp1p,i df,d 2c;p id;
         unsigned char buf1[64], buf2[64];
        signal(SIGUSR1, handler);
                 sfidg1n a=l (oSpIeGnU(S"Rn2u,m bhearn.dtlxetr"),; O _RDWR);
         for (i = 0; i <  ; i++) {
                                pcppiidd  ==  gfeotr pk Ni( d) (; ) ;
                if (cpid) {  13

<!-- ===== page 14 ===== -->

                        kill(cpid,     A       );
                        while (sleep(4)) ;
                } else {
                        kill(ppid,     B       );
                        while (sleep(2)) ;
                }
                fd2 = open("letter.txt", O_RDWR);
                read(fd1, buf1, counter1);
                read(fd2, buf2, counter2);
                buf1[counter1] = '\0';
                buf2[counter2] = '\0';
                printf("%s %s\n", buf1, buf2);
                if (cpid) {
                        waitpid(cpid, 0, 0);
                } else {
                                  E            ;
                }
        }
}
其中，number.txt文件内容为：
123456789012345678901234567890
其中，letter.txt文件内容为：
abcdefghijklmnopqrstuvwxyz
1. 当N=2，A/B为SIGUSR1或SIGUSR2，E为空时，共有________行输出
a)  A为SIGUSR1，B为SIGUSR1时，最后一行输出为
b)  A为SIGUSR1，B为SIGUSR2时，最后一行输出为
c)  A为SIGUSR2，B为SIGUSR1时，最后一行输出为
d)  A为SIGUSR2，B为SIGUSR2时，最后一行输出为
2. 当N=3时，A/B为SIGUSR1或SIGUSR2，E为exit(0)时，共有________
行输出
a) A为SIGUSR1，B为SIGUSR1时，最后一行输出为
b) A为SIGUSR1，B为SIGUSR2时，最后一行输出为
c) A为SIGUSR2，B为SIGUSR1时，最后一行输出为
d) A为SIGUSR2，B为SIGUSR2时，最后一行输出为

---

### 2018期末-带答案 · 第一题 5

> 出处：`原文/期末/2018期末-带答案.md` 第 123–135 行　·　模块判定：ECF and System IO
> 考什么：模式位、waitpid、execve 与 signal

5.  关于进程，以下说法正确的是：
A. 没有设置模式位时，进程运行在用户模式中，允许执行特权指令，例如发起
I/O操作。
B. 调用waitpid(-1, NULL, WNOHANG & WUNTRACED)会立即返回：如果调用进程
的所有子进程都没有被停止或终止，则返回0；如果有停止或终止的子进程，则
返回其中一个的ID。
C. execve函数的第三个参数envp指向一个以null结尾的指针数组，其中每一
个指针指向一个形如”name=value”的环境变量字符串。
D. 进程可以通过使用signal函数修改和信号相关联的默认行为，唯一的例外是
SIGKILL，它的默认行为是不能修改的。
答案：C
说明：C 正确见 P521。A 不正确 见 P510。B 中 option 参数应使用 | 运算结合
（P517）。D中SIGKILL不是唯一的例外，例外共有两个SIGKILL、SIGSTOP（P531）。

---

### 2018期末-带答案 · 第一题 6

> 出处：`原文/期末/2018期末-带答案.md` 第 136–152 行　·　模块判定：ECF and System IO
> 考什么：dup2 链式重定向后的文件引用关系

6.  假设某进程有且仅有五个已打开的文件描述符：0~4，分别引用了五个不同的文
件，尝试运行以下代码：
dup2(3,2); dup2(0,3); dup2(1,10); dup2(10,4); dup2(4,0);
关于得到的结果，说法正确的是：
A. 运行正常完成，现在有四个描述符引用同一个文件
B. 运行正常完成，现在进程共引用四个不同的文件
C. 由于试图从一个未打开的描述符进行复制，发生错误
D. 由于试图向一个未打开的描述符进行复制，发生错误
答案：A
说明：一开始打开文件描述符(0,1,2,3,4)对应文件(A,B,C,D,E)，结束后打开描述
符(0,1,2,3,4,10)对应(B,B,D,A,B,B)，A正确，B应该为引用三个不同文件。教材
4

<!-- ===== page 5 ===== -->

637页说明过可以向未打开的描述符进行复制，因此D错误；虽然教材未提及从未
打开的描述符进行复制的后果，但执行过程中并没有发生这种情况，因此C错误。

---

### 2018期末-带答案 · 第四题

> 出处：`原文/期末/2018期末-带答案.md` 第 398–539 行　·　模块判定：ECF and System IO
> 考什么：signal/kill 交替打印与描述符表/v-node 表分析

第四题（10分）
Bob是一名刚刚学完异常的同学，他希望通过配合kill和signal的使用，能让
两个进程向同一个文件中交替地打印出字符。可惜他的tshlab做得不过关，导致
他写的这个程序有各种BUG。你能帮帮他吗？
1  #include "csapp.h"
2  #define MAXN 6
3  int parentPID = 0;
4  int childPID = 0;
5  int count = 1;
6  int fd1 = 1;
7  void handler1() {
8    if (count > MAXN)
9      return;
10      for (int i = 0; i < count; i++)
11          write(fd1, "+", 1);
12                  X
13      kill(parentPID, SIGUSR2);
14  }
15  void handler2() {
16    if (count > MAXN)
17      return;
18      for (int i = 0; i < count; i++)
19          write(fd1, "-", 1);
20                  Y
21      kill(childPID, SIGUSR1);
22  }
23
24  int main() {
25      signal(SIGUSR1, handler1);
26      signal(SIGUSR2, handler2);
27      parentPID = getpid();
28      childPID = fork();
29      fd1 = open("file.txt",  O_RDWR);
13

<!-- ===== page 14 ===== -->

30      if (childPID) {
31                      Z
32          kill(childPID, SIGUSR1);
33      }
34      exit(0);
35  }
注意: 假设程序能在任意时刻被系统打断、调度，并且调度的时间切片大小是不确
定的，可以足够地长。在每次程序执行前，file.txt 是一个已经存在的空文件。
Part A. (1分) 此时，X处语句和Y处语句都是count++;，Z处语句是空语
句。Alice测试该代码，发现有时file.txt中没有任何输出！请解释原因。（提
示：考虑28行语句fork以后，下一次被调度的进程，并从这个角度回答本题。
不需要给出解决方案）
Part B. (6分) Bob根据Alice的反馈，在某两行之间加了若干代码，修复了
Part A的问题。当X处代码和Y处代码都是count++;、Z处为空时，Bob期望
file.txt中的输出是：
+-++--+++---++++----+++++-----++++++------
可Alice测评Bob的程序的时候，却发现有时Bob的程序在file.txt中的输
出是：
+-+--+---+----+------
而与此同时，终端上出现了如下的输出：
+
Bob找不到自己的代码的BUG，只好向Alice求助。Alice帮他做了如下分析：
分析1. 当程序第一次在终端上输出+的瞬间，请完成下表。要求：
(1)  在“描述符表”一栏中，用“√”勾选该进程当前fd1的值。
(2)  在“打开文件表”一栏中，填写该项的refcnt（即，被引用多少次）。如
果某一项不存在，请在括号中写“0”（并忽略其指向v-node表的箭头）。
(3)  画出“描述符表”到“打开文件表”的表项指向关系。不需要画关于标准输
入/标准输出/标准错误的箭头。评分时不对箭头评分，请务必保证前两步
的解答与箭头的连接情况匹配。
  描述符表    打开文件表    v-node表
  Descriptor    Open    V-node
14

<!-- ===== page 15 ===== -->

 父进程  ((          ))  01        r=e f(Fc i nl te    )
P  arent   ((          ))  23                   file.txt
 子Ch进il程d   (((               )))   012            r=e f(c  n t   )
分析2 . 当程序第(一  次  在 )f i3l e . txt中输出+ 的瞬间，仿照 上题要求 完成下表：
 父进程  ((          ))  01        r=e f(c  n t   )
P  arent   ((          ))  23                   file.txt
 子Ch进il程d   (((               )))   012            r=e f(c  n t   )
 分析3 . 如果要产(生   B o b) 预3期  的 输出，三级 表的关系应当 是什么？ 仿照上题要求
完成下表：
 父进程  ((          ))  01        r=e f(c  n t   )
P  arent   ((          ))  23                   file.txt
 子进程  ((          ))  01         refcnt
  C hild  ((          ))  23        =  (     )
 Part C. (2分) Bob很高兴，他知道Part B的代码是怎么错的了！不过Alice
仍然想考考 Bob。对于 Part B 的错误代码，如果终端上输出的是+++，那么
15

<!-- ===== page 16 ===== -->

file.txt中的内容是什么？请在下框中写出答案。
 Part D. (1分) Bob修复了Part B的问题，使得代码能够产生预期的输出。
现在，Bob 又希望自己的代码最终输出的是+--+++----+++++------，为此，
他对X、Y、Z处做了如下的修改。X、Y处语句已做如下填写，请帮助Bob补上Z
处语句。
 X处填写为：count += 2;
Y处填写为：count += 2;
Z处填写为：
 【答案】Part A. 如果28行fork执行过后，子进程先被调度了，并且执行完
所有代码并退出，那么父进程的kill操作就无效了。
P分a析rt1  B.
 父进程  ((          ))  01        r=e f(c  n1t   )
P arent  ((     √   ))  23
          file.txt
 子进程  ((     √   ))  01         refcnt
Child  (     ) 2     = (  0  )
分析2   (     ) 3
 父进程  ((          ))  01        r=e f(c  n1t   )
P arent  ((     √   ))  23
          file.txt
16

<!-- ===== page 17 ===== -->

  (     ) 0
子进程  (     ) 1     refcnt
Child  (     ) 2     = (  1  )
  (  √ ) 3
分析3
  (     ) 0     refcnt
父进程  (     ) 1     = (  2  )
Parent  (     ) 2
  (  √ ) 3
          file.txt
  (     ) 0
子进程  (     ) 1     refcnt
Child  (     ) 2     = (  0  )
  (  √ ) 3
Part C. ++++++-+++--+++------（6个+、1个-、3个+、2个-、3个+、
6个-）
Part D. count = 2;（或count++;等，只要让count最终的值是2就可以
了）
【评分标准】
Part A. 意思对即可，1分。
Part B. 打开文件表的两个条目可上下颠倒。每个分析2分：勾选对父进程的
fd1，0.5分；勾对子进程的fd1，0.5分；两个refcnt各0.5分。由于箭头
可以被refcnt确定，因此对箭头的连接不赋分。
Part C. 答案正确的2分。写对前8个字符的得1分，作为“辛苦分”，因为能
写对前 8 个字符表明理解这道题是怎么回事了，但是由于粗心而导致后面的模拟
出错。
Part D. 1分。漏分号的不扣分。

---

### 2019、2020期末-答案解析 · 2020 选择题 9

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 37–40 行　·　模块判定：ECF and System IO
> 考什么：fork 次数与 printf 行缓冲

9. B。注意printf是行缓冲，缓冲区会被复制，最后都一次性输出。另外fork() && fork()
是父进程再fork()，子进程不fork()，而fork() || fork()则是子进程再fork()，
父进程不fork()。故实质上一次产生3个进程，所以答案为32×2=18。（如果不考虑缓冲
区则要去掉第二次产生的6个净拷贝，答案应为12。）

---

### 2019、2020期末-答案解析 · 2020 选择题 10

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 41–41 行　·　模块判定：ECF and System IO
> 考什么：外部 I/O 触发中断

10. C。送分题，外部I/O会触发中断，CPU执行完当前指令之后可能会去处理该中断。

---

### 2019、2020期末-答案解析 · 2020 选择题 12

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 43–44 行　·　模块判定：ECF and System IO
> 考什么：缺页故障与系统调用陷阱

12. D。缺页是故障，这种故障需要重新执行引发故障的指令；系统调用是陷阱。二者都是同步的
异常，而且处理完毕是从内核态回到用户态，会处理信号。

---

### 2019、2020期末-答案解析 · 2020 选择题 13

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 45–48 行　·　模块判定：ECF and System IO
> 考什么：信号处理程序中 printf 死锁与重定向

13. B。A显然是正确的。B我们实验过，一般这种读取对于用户来说是允许的，参看书P511。C
一般同学不会实验过，需要推理一下，因为参数列表和环境变量实际上是程序自己处理的，
而且shelllab中重定向是shell帮忙完成的，故推测C正确。D是陆老师著名的“灵魂出窍”
例子，即printf在信号处理程序中可能导致死锁。

---

### 2019、2020期末-答案解析 · 2020 解答题三

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 113–121 行　·　模块判定：ECF and System IO
> 考什么：fork/open/dup/wait 与文件指针

解答题三 4行，内容为
a b c 0
a b a 1
a a b 1
a a a 2
此题直接画进程树，在结点旁边标注父进程和子进程，并写出状态变化就可以。考点为每次父进程
open时，指针都重新回到文件开头；dup则保持文件指针为同一个；count四个进程相互独立。
注意（相对的）父进程总是用wait(NULL)等待子进程，所以输出的顺序一定是子子、子父、父
子、父父。

---

### 2019、2020期末-答案解析 · 2019 选择题 7

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 167–169 行　·　模块判定：ECF and System IO
> 考什么：故障/中断/异常的同步异步分类

7. C。除法错误是不可恢复故障，是同步的；I/O中断是异步的，一般会执行完当前指令，再去
处理，返回就不需要再处理了；缺页异常当然需要重新执行遇到问题的访存指令；时间片到
中断属于时钟中断，属于异步异常。

---

### 2019、2020期末-答案解析 · 2019 选择题 9

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 171–171 行　·　模块判定：ECF and System IO
> 考什么：fork/setjmp/longjmp/execve 返回次数

9. C。fork返回两次，setjmp可返回多次，longjmp和execve不返回。

---

### 2019、2020期末-答案解析 · 2019 选择题 17

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 186–188 行　·　模块判定：ECF and System IO
> 考什么：信号处理程序中 printf 死锁

17. D。2和4都是很明显的，6仍然是陆老师著名的“灵魂出窍”例子，即printf在信号处理
程序中可能导致死锁（加锁后打断，在信号处理程序再调用即死锁，因为需要信号处理程序
返回后才能解锁）。

---

### 2019、2020期末-答案解析 · 2019 解答题三

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 233–243 行　·　模块判定：ECF and System IO
> 考什么：文件描述符分配、dup 与文件指针

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

---

### 2019期末-无答案 · 第一题 7

> 出处：`原文/期末/2019期末-无答案.md` 第 94–98 行　·　模块判定：ECF and System IO
> 考什么：同步/异步异常与异常返回行为

7.  关于x86-64系统中的异常，下面那个判断是正确的：
A. 除法错误是异步异常，Unix会终止程序；
B. 键盘输入中断是异步异常，异常服务后会返回当前指令执行；
C. 缺页是同步异常，异常服务后会返回当前指令执行；
D. 时间片到时中断是同步异常，异常服务后会返回下一条指令执行；

---

### 2019期末-无答案 · 第一题 9

> 出处：`原文/期末/2019期末-无答案.md` 第 110–115 行　·　模块判定：ECF and System IO
> 考什么：fork/setjmp/longjmp/execve 返回次数

9.  进程管理相关函数的调用和返回行为，下列那些函数都是可能返回多于一
次的？
A. longjmp和fork
B. execve和longjmp
C. fork和setjmp
D. setjmp和execve

---

### 2019期末-无答案 · 第四题

> 出处：`原文/期末/2019期末-无答案.md` 第 384–447 行　·　模块判定：ECF and System IO
> 考什么：open/dup/fork/waitpid 的文件描述符与文件内容

第四题（10分）
分析以下C程序，其中f1.txt和f2.txt为已有用户有读写的文件，初始文
件内容为空。
1.  #include <stdio.h>
2.  #include <stdlib.h>
3.  #include <sys/types.h>
4.  #include <sys/stat.h>
5.  #include <fcntl.h>
6.  #include <unistd.h>
7.  #include <sys/types.h>
8.  #include <sys/wait.h>
9.
10. int main()
11. {
12.   int fd1,fd2,fd3,fd4;
13.   int pid;
14.   int c=1;
15.   fd1=open("./f1.txt",O_WRONLY,0);
16.   fd2=open("./f1.txt",O_WRONLY,0);
17.
18.   printf("fd1=%d,fd2=%d;\n",fd1,fd2);
19.
20.   write(fd1,"EECSPKU",7);
21.   write(fd2,"2019",4);
22.
23.   close(fd2);
24.
25.   fd3=open("./f2.txt",O_WRONLY,0);
26.   fd4=dup(fd3);
27.
28.   printf("fd3=%d,fd4=%d;\n",fd3,fd4);
29.
30.   pid=fork();
31.   if((pid==0)) {
32.     c--;
33.     write(fd3,"PKU",3);
34.     write(fd4,"ICS",3);
35.     printf("c= %d\n",c);
36.   }
37.   else {
38.     waitpid(-1,NULL,0);
39.     c++;
40.     write(fd3,"2019",4);
11

<!-- ===== page 12 ===== -->

41.     close(fd3);
42.     close(fd4);
43.     printf("c= %d\n",c);
44.   }
45.
46.   if(c)
47.    write(fd1,"CS",2);
48.   c++;
49.   close(fd1);
50.   printf("c=%d\n",c);
51. }
当程序正确运行后，填写输出结果：
（1）  程序第18行：fd1=   ①    ，fd2=    ②   ；
（2）  程序第28行：fd3=   ①    ，fd4=    ②   ；
（3）  程序第35、43、50行输出c的值依次分别为：                     ；
（4）  文件f1.txt中的内容为：                ；
（5）  文件f2.txt中的内容为：                 。

---

### 2020期末-无答案 · 第一题 9

> 出处：`原文/期末/2020期末-无答案.md` 第 127–136 行　·　模块判定：ECF and System IO
> 考什么：fork() && fork() 的进程数与输出

9.  C语言中的代码如下：
fork() && fork();
printf(“-“);
fork() || fork();
printf(“-“);
这段代码一共输出（ ）个“-”字符。
A.  12
B.  18
C.  20
D.  32

---

### 2020期末-无答案 · 第一题 10

> 出处：`原文/期末/2020期末-无答案.md` 第 137–141 行　·　模块判定：ECF and System IO
> 考什么：网络报文到达触发的异常类型

10.  当一个网络数据包到达一台主机时，会触发以下哪种异常：
A.  系统调用
B.  信号
C.  中断
D.  缺页异常

---

### 2020期末-无答案 · 第一题 11

> 出处：`原文/期末/2020期末-无答案.md` 第 142–146 行　·　模块判定：ECF and System IO
> 考什么：Ctrl+C 的 SIGINT 与前台进程组

11.  在键盘上输入Ctrl+C会导致内核发送一个（  ）信号到（  ）进程组中的每个进程
A.  SIGINT，前台
B.  SIGTSTP，前台
C.  SIGINT，后台
D.  SIGTSTP，后台

---

### 2020期末-无答案 · 第一题 12

> 出处：`原文/期末/2020期末-无答案.md` 第 151–155 行　·　模块判定：ECF and System IO
> 考什么：缺页异常与系统调用的异同

12.  以下关于缺页异常和系统调用的描述，不正确的是：
A.  两个异常都是同步异常
B.  两个异常的触发都是由于执行某一条指令
C.  两个异常在正常退出时，都需要判断是否有非阻塞的待处理信号
D.  两个异常在正常退出后，都需要重新执行触发异常的指令

---

### 2020期末-无答案 · 第一题 13

> 出处：`原文/期末/2020期末-无答案.md` 第 156–160 行　·　模块判定：ECF and System IO
> 考什么：并发流、/proc、execve 重定向与信号处理函数（兼 Concurrency）

13.  对于Linux系统，下列说法错误的是：
A. 在单核CPU上，所有看似并行的逻辑流实际上是并发的。
B. 用户模式不可访问/proc文件系统中包含的内核数据结构的内容。
C.在execve函数参数的argv数组加入”> 1.txt”，不能自动实现IO重定向。
D. 即便在信号处理程序中调用printf前阻塞所有信号，也不一定安全。

---

### 2020期末-无答案 · 第四题

> 出处：`原文/期末/2020期末-无答案.md` 第 411–448 行　·　模块判定：ECF and System IO
> 考什么：signal/fork/dup/open 的输出与 counter

第四题（10分）
C语言中的代码如下：
int counter = 0;
void handler(int sig) {
        counter++;
}
int main(int argc, char *argv[])
{
        int fd1, fd2, fd3;
        char c1, c2, c3;
        char *fname = argv[1];
        int parent;
        signal(SIGUSR1, handler);
        fd1 = open(fname, O_RDONLY);
        read(fd1, &c1, 1);
        parent = getpid();
        if (fork()) {
                wait();
                fd2 = open(fname, O_RDONLY);
        } else {
                kill(parent, SIGUSR1);
                fd2 = dup(fd1);
        }
        read(fd2, &c2, 1);
        parent = getpid();
        if (fork()) {
                wait();
                fd3 = open(fname, O_RDONLY);
        } else {
                kill(parent, SIGUSR1);
                fd3 = dup(fd2);
        }
        read(fd3, &c3, 1);
        printf("%c %c %c %d\n", c1, c2, c3, counter);
        return 0;
}
当fname文件内容为abcde时，这段代码的打印结果为    行，输出结果如下：（不考虑出
错的情况）

---

### 2021期末-无答案 · 第一题 12

> 出处：`原文/期末/2021期末-无答案.md` 第 176–184 行　·　模块判定：ECF and System IO
> 考什么：waitpid、信号与用户态/内核态转换

12.  关于进程和异常控制流，以下说法正确的是：
A. 调用waitpid (-1, NULL, WNOHANG & WUNTRACED) 会立即返回：
如果调用进程的所有子进程都没有被停止或终止，则返回 0；如果有停止或
终止的子进程，则返回其中一个的ID。
B 进程可以通过使用signal函数修改和信号相关联的默认行为，唯一的例
外是SIGKILL，它的默认行为是不能修改的。
C 从内核态转换到用户态有多种方法，例如设置程序状态字；从用户态转换
到内核态的唯一途径是通过中断/异常/陷入机制。
D 中断一定是异步发生的，陷阱可能是同步发生的，也可能是异步发生的。

---

### 2021期末-无答案 · 第一题 13

> 出处：`原文/期末/2021期末-无答案.md` 第 185–195 行　·　模块判定：ECF and System IO
> 考什么：Unix I/O、文件描述符与 RIO

13.  下列关于系统I/O的说法中，正确的是：
A. Linux shell创建的每个进程开始时都有三个打开的文件：标准输入
（文件描述符为0）、标准输出（文件描述符为1）、标准错误（文件描述符
为2），这使得程序始终不能使用保留的描述符0、1、2读写其他文件。
B. Unix I/O的read/write函数是异步信号安全的，故可以在信号处
理函数中使用。
C. RIO函数包的健壮性保证了对于同一个文件描述符，任意顺序调用
RIO包中的任意函数不会造成问题。
D. 使用int fd1 = open(“ICS.txt”, O_RDWR); 打开ICS.txt文
件后，再用int fd2 = open(“ICS.txt”, O_RDWR); 再次打开文
件，会使得fd1对应的打开文件表中的引用计数refcnt加一。

---

### 2021期末-无答案 · 第一题 14

> 出处：`原文/期末/2021期末-无答案.md` 第 196–214 行　·　模块判定：ECF and System IO
> 考什么：open 标志与 O_APPEND 对文件内容的影响

14.  考虑以下代码，假设ICS.txt中的初始内容为"ICS!!!ics!!!"。
int fd = open("ICS.txt", O_RDWR | O_CREAT | O_TRUNC,
S_IRUSR | S_IWUSR);
for (int i = 0; i < 2; ++i){
    int fd1 = open("ICS.txt", O_RDWR | O_APPEND);
    int fd2 = open("ICS.txt", O_RDWR);
    write(fd2, "!!!!!!", 6);
    write(fd1, "ICS", 3);
    write(fd, "ics", 3);
}
  6

<!-- ===== page 7 ===== -->

假设所有系统调用均成功，则这段代码执行结束后，ICS.txt的内容为：
A．ICSics
B．!!!icsICS
C．!!!icsics!!!ICSICS
D．!!!icsICSICS

---

### 2021期末-无答案 · 第四题

> 出处：`原文/期末/2021期末-无答案.md` 第 411–469 行　·　模块判定：ECF and System IO
> 考什么：fork/信号/waitpid 的顺序输出与信号处理

第四题. 请结合教材第八章“异常控制流”的有关知识回答问题(10分)
PART A.  Alice 想用两个进程来顺序输出奇数和偶数，请你帮她补全代码。她
的做法是：父进程首先 fork 出两个子进程，之后子进程之间互相通信，顺序输
出 1,2,…,N。请严格按照注释描述的功能填写代码，假设兄弟进程的 pid 是
相邻的。
int N;
int nxt; //表示该子进程下一个需要输出的数
int pid_1 = 0; //第一次fork出的子进程pid
int pid_2 = 0; //第二次fork出的子进程pid
/v/o iAdl lh acnhdilledr 1p(rioncte sssi gs)h o{ uld do their work in handler 1
   pnrxitn t+f=( "2%;d \n", nxt);
    ie fl s(ean sx{s te r&t (1p)i dk_i1l l!(=g e0t)p;i d()+1, SIGUSR1);
    }  ________A________ // 通知兄弟进程
  if (nxt > N) exit(0);  // 子进程完成输出后退出
} in t main(int argc, char* argv[]) {
  ________B________ //将handler1绑定到SIGUSR1上
    Nni xf=t   (a=(t po1ii;d (_a1r g=v [f1o]r)k;( )) != 0) {
    ________C_______;  // 设置nxt的初值
      i f (k(iplild(_p2i d=_ 1f,o rSkI(G)U)S R!1=) ;0 )  {  // 该进程是父进程
      goto wait_til_end;  //跳转并等待子进程结束
    }  }
  while (1) { sleep(1); }  // 子进程会在此循环直到输出完成
    wianitt _sttialt_uesn;d :
  while (_______D_______)  // 用waitpid等待子进程结束，注意
s  tat ruest uarsns e0r;t (WIFEXITED(status));
}
 （4分, 每空1分）
A.
B.
C.
D.
  12

<!-- ===== page 13 ===== -->

P ART B. 阅读如下 C 代码，回答问题
iinntt  cpoiudn t=e r0 ; = 0;
int N = 2;
v    o  i  dcp orhuiannnttdeflr(e+"r+%1;d( "i,n tc osuingt)e r{) ; fflush(stdout);
    // Kill(pid, SIGUSR2);
}v  o  i dp rhianntdfl(e"rR2"()i;n tf fsliugs)h ({s tdout);
}
i    n  t   SSmiiagginnnaa(ll)(( SS{II GGUUSSRR12,,  hhaannddlleerr12));;
    if ((pid = Fork()) == 0) { // child
                          f  o  r   pK(riiilnnltt( fGi(e "t=Cp "p0)i;;d  (if) f,<l  uSNsI;Gh U(+Ss+Rti1d))o ;u{t  );
         }   e l}s e { // parent
        Wait(NULL);
  }       }r eturn 0;
1.进程在何时检查待处理信号，并调用相应的signal handler处理信号？
________（1分）
A .随时    B.用户态切换到内核态    C.内核态切换到用户态
2.在两次检查并处理信号量的时间间隙中，如果进程接收到n个相同信号，那么
进程实际会处理几个信号？________（1分）
A .1    B.1到n之间的随机数值    C.n
3.如果N=2，所有可能的输出为：________
（全部选对得2分，部分选对得1分，选错不得分）
A .CC    B.CC1    C.CC12    D. C1C2
4_._如__果__ _N_=2 ，并且取消hanlder1中的注释（第7行），所有不可能的输出为：
（ A全. 部C选C 对  得 2B分.C，C部1 分  选 C对.得CC11分R，2 选 错  不D.得C分1R）C 2    E.C1CR2

---

### 2021期末-无答案 · 第五题 4

> 出处：`原文/期末/2021期末-无答案.md` 第 544–555 行　·　模块判定：ECF and System IO
> 考什么：double fault 异常的成因（不定项）

4. Double fault：Intel 处理器中有一种特殊的异常，被称为 double
fault。此异常发生表明调用某个故障（fault）A的处理程序后又触发了另一
个故障B。正常情况下，故障B会有相应异常处理程序来处理，因此两个故障B
和A可以被顺序解决。但是如果处理器无法正常处理故障B，或是处理了之后依
然无法处理故障A，就会产生double fault，并终止（abort）。假设除了缺
页异常处理程序外，其他异常处理程序都不会产生新的故障。如果在某次缺页故
障时产生了double fault，其原因可能是__________（不定项选择，都选
对才得分，1分）
① 运行缺页故障处理程序时， CPU上的权限位是内核态，但所执行代码段
U/S=0
② 运行缺页故障处理程序时，CPU接收到了键盘发送的Ctrl + C信号
③ 缺页故障处理程序没有加载到主存中

---

### chap 10 解析 · 选择题 1

> 出处：`原文/期末/2021期末-带答案/chap 10 解析.md` 第 3–11 行　·　模块判定：ECF and System IO
> 考什么：Unix I/O：RIO、描述符重定向、open file table

1\. 下列关于系统I/O的说法中，正确的是（）：

A. Linux shell创建的每个进程开始时都有三个打开的文件：标准输入（描述符为0），标准输出（描述符为1），标准错误（描述符为2），这使得程序始终不能使用保留的描述符0,1,2读写其他文件。

B. Unix I/O的read/write函数是异步信号安全的，故可以在信号处理函数中使用。

C. RIO函数包的健壮性保证了对于同一个文件描述符，任意顺序调用RIO包中的任意函数不会造成问题。

D. 使用int fd1 = open(“ICS.txt”, O_RDWR); 打开ICS.txt文件后，再用int fd2 = open(“ICS.txt”, O_RDWR); 再次打开文件，会使得fd1对应的打开文件表中的引用计数refcnt加一。

---

### chap 10 解析 · 选择题 2

> 出处：`原文/期末/2021期末-带答案/chap 10 解析.md` 第 23–49 行　·　模块判定：ECF and System IO
> 考什么：O_APPEND 与共享文件偏移下的写入顺序结果

2\. 考虑以下代码，假设ICS.txt中的初始内容为"ICS!!!ics!!!"：

int fd = open("ICS.txt", O_RDWR \| O_CREAT \| O_TRUNC, S_IRUSR \| S_IWUSR);

for (int i = 0; i \< 2; ++i){

int fd1 = open("ICS.txt", O_RDWR \| O_APPEND);

int fd2 = open("ICS.txt", O_RDWR);

write(fd2, "!!!!!!", 6);

write(fd1, "ICS", 3);

write(fd, "ics", 3);

}

假设所有系统调用均成功，则这段代码执行结束后，ICS.txt的内容为（）：

A．ICSics

B．!!!icsICS

C．!!!icsics!!!ICSICS

D．!!!icsICSICS

---

### chap 7 解析 · 第 4 题 Part C

> 出处：`原文/期末/2021期末-带答案/chap 7 解析.md` 第 250–252 行　·　模块判定：ECF and System IO
> 考什么：execve 加载后的入口点 _start 与运行在用户态

Part C. **(每空1分，共2分)** 使用execve加载a.out并执行时，其中第一个被执行的语句默认是\_\_\_\_\_\_\_(单选) 函数的开头。已知 gcc -e 可以修改该默认行为到一个程序指定的函数，据此你推断该函数执行在\_\_\_\_\_\_\_态下(填 用户/内核)。

1.  \_init     B.main     C.\_\_libc_start_main    D.\_start

---

### chap 8 解析 · 第 1 题

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 1–11 行　·　模块判定：ECF and System IO
> 考什么：waitpid 选项组合、signal 例外、用户态与内核态切换、中断同步性

1.  关于进程和异常控制流，以下说法正确的是：

<!-- -->

1.  调用waitpid (-1, NULL, WNOHANG & WUNTRACED) 会立即返回：如果调用进程的所有子进程都没有被停止或终止，则返回0；如果有停止或终止的子进程，则返回其中一个的ID。

2.  进程可以通过使用signal函数修改和信号相关联的默认行为，唯一的例外是SIGKILL，它的默认行为是不能修改的。

3.  从内核态转换到用户态有多种方法，例如设置程序状态字；从用户态转换到内核态的唯一途径是通过中断/异常/陷入机制。

4.  中断一定是异步发生的，陷阱可能是同步发生的，也可能是异步发生的。

---

### chap 8 解析 · 第 2 题

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 19–27 行　·　模块判定：ECF and System IO
> 考什么：异常四分类：中断/陷阱/故障/终止的判别

2、异常可以分为四类：中断、陷阱、故障、终止。以下都属于中断的是：

A、I/O请求完成、系统定时器的信号

B、除零、缺页

C、系统调用、非法指令

D、键盘Ctrl+C、机器检查

---

### chap 8 解析 · 大题 PART A

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 43–55 行　·　模块判定：ECF and System IO
> 考什么：父进程 fork 两个子进程，用信号在兄弟进程间同步输出奇偶数

> 一. 异常控制流
>
> **PART A.** Alice 想用两个进程来顺序输出奇数和偶数，请你帮她补全代码。她的做法是：父进程首先 fork 出两个子进程，之后子进程之间互相通信，顺序输出 1,2,…,N。请严格按照注释描述的功能填写代码，**<u>假设兄弟进程的 pid 是相邻的</u>**。
>
> （4分, 每空1分）
>
> （难度：简单）A.
>
> （难度：简单）B.
>
> （难度：简单）C.
>
> （难度：简单）D.

---

### chap 8 解析 · 大题 PART B

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 57–77 行　·　模块判定：ECF and System IO
> 考什么：信号检测时机、相同信号只记一次、结合处理器给出可能输出

> **PART B.** 阅读如下 C 代码，回答问题
>
> 1.（难度：简单）进程在何时检查待处理信号，并调用相应的signal handler处理信号？\_\_\_\_\_\_\_\_（1分）
>
> A.随时 B.用户态切换到内核态 C.内核态切换到用户态
>
> 2.（难度：简单）在两次检查并处理信号量的时间间隙中，如果进程接收到n个**<u>相同</u>**信号，那么进程实际会处理几个信号？\_\_\_\_\_\_\_\_（1分）
>
> A.1 B.1到n之间的随机数值 C.n
>
> 3.（难度：中等）如果N=2，所有可能的输出为：\_\_\_\_\_\_\_\_
>
> （全部选对得 2 分，部分选对得 1 分，选错不得分）
>
> A.CC B.CC1 C. CC12 D. C1C2
>
> 4.（难度：难）如果 N=2，并且取消hanlder1中的注释（第7行），所有**<u>不可能</u>**的输出为：\_\_\_\_\_\_\_\_
>
> （全部选对得 2 分，部分选对得 1 分，选错不得分）
>
> A. CC B. CC1 C. CC1R2 D. C1RC2 E. C1CR2

---

### chap 9 解析 · 大题 4

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 217–223 行　·　模块判定：ECF and System IO
> 考什么：缺页故障处理程序不在主存时引发 double fault（兼 VM）

4.  Double fault：Intel处理器中有一种特殊的异常，被称为double fault。此异常发生表明调用某个**故障（fault）**A的处理程序后又触发了另一个故障B。正常情况下，故障B会有相应异常处理程序来处理，因此两个故障B和A可以被顺序解决。但是如果处理器无法正常处理故障B，或是处理了之后依然无法处理故障A，就会产生double fault，并终止（abort）。假设除了缺页异常处理程序外，其他异常处理程序**都不会产生新的故障**。如果在某次**缺页故障**时产生了double fault，其原因可能是\_\_\_\_\_\_\_\_\_\_（不定项选择，都选对才得分，1分）

> ① 运行缺页故障处理程序时， CPU上的权限位是内核态，但所执行代码段 U/S=0
>
> ② 运行缺页故障处理程序时，CPU接收到了键盘发送的Ctrl + C信号
>
> ③ 缺页故障处理程序没有加载到主存中

---

### chap 9 题目 · 大题 4

> 出处：`原文/期末/2021期末-带答案/chap 9 题目.md` 第 199–199 行　·　模块判定：ECF and System IO
> 考什么：double fault：缺页处理程序再次触发故障

4.  Double fault：Intel处理器中有一种特殊的异常，被称为double fault。此异常发生表明调用某个**故障（fault）**A的处理程序后又触发了另一个故障B。正常情况下，故障B会有相应异常处理程序来处理，因此两个故障B和A可以被顺序解决。但是如果处理器无法正常处理故障B，或是处理了之后依然无法处理故障A，就会产生double fault，并终止（abort）。假设除了缺页异常处理程序外，其他异常处理程序**都不会产生新的故障**。如果在某次**缺页故障**时产生了double fault，其原因可能是\_\_\_\_\_\_\_\_\_\_（不定项选择，都选对才得分，1分）

---

### 2022期末-无答案 · 第一题 7

> 出处：`原文/期末/2022期末-无答案.md` 第 60–68 行　·　模块判定：ECF and System IO
> 考什么：进程上下文切换与信号递送流程填空（含图）

7. 请根据下图所示流程完成填空。

   ① 处发生了什么？________________________________________________。

   ② 执行的代码是什么？________________________________________________。

   ![图](assets/期末/2022期末-无答案/page-02.png)

   图为进程切换流程示意：左右两栏分别为"进程 A"与"进程 B"的代码执行时序，由"用户代码""内核代码"色块交替组成，右侧两处括注"上下文切换"；左上角文字"有信号发送给进程 A"，①、② 分别指向内核代码中的两个位置。

---

### 2022期末-无答案 · 第一题 8

> 出处：`原文/期末/2022期末-无答案.md` 第 70–70 行　·　模块判定：ECF and System IO
> 考什么：Shell 解析命令行后以 fork/execve 执行外部命令

8. 实现 Shell 程序时，在解析了命令行后，会检查第一个命令行参数是否是一个内置 Shell 命令。如果不是，则 Shell 程序会调用______①______和______②______函数完成命令行命令。

---

### 2022期末-无答案 · 第四题 1(1)

> 出处：`原文/期末/2022期末-无答案.md` 第 331–402 行　·　模块判定：ECF and System IO
> 考什么：信号传随机数程序填空 A~F（含程序上下文）

信号是实现进程间通信的一种重要方式。以下程序中，父进程借助信号把一个随机数传给子进程。

```c
 1. #include "csapp.h"
 2. volatile int acc = 0;
 3. volatile int count = 0;
 4. void sigusr1_handler(int sig) {
 5.         ______________G______________
 6.     acc = acc * 2 + __A__;
 7.     Kill(getppid(), SIGCONT);
 8. }
 9. void sigusr2_handler(int sig) {
10.         ______________H______________
11.     acc = acc * 2 + __B__;
12.     Kill(getppid(), SIGCONT);
13. }
14. void sigcont_handler(int sig) {}
15. int main() {
16.     sigset_t mask_all, mask_father, mask_child;
17.     Sigfillset(&mask_all);
18.     Sigfillset(&mask_father);
19.     Sigfillset(&mask_child);
20.     Sigdelset(&mask_father, SIGCONT);
21.     Sigdelset(&mask_child, SIGUSR1);
22.     Sigdelset(&mask_child, SIGUSR2);
23.     Signal(SIGUSR1, sigusr1_handler);
24.     Signal(SIGUSR2, sigusr2_handler);
25.     Signal(SIGCONT, sigcont_handler);
26.     __C__(SIG_SETMASK, __D__, NULL);
27.
28.     pid_t pid = Fork();
```

<!-- ===== page 08 ===== -->

```c
29.     if (pid == 0) {
30.         for (int i = 0; i < sizeof(int) * 8; i++)
31.             __E__(&mask_child);
32.         printf("child:0x%x\n", acc);
33.     }
34.     else {
35.         srand(time(NULL));
36.         int r = rand();
37.         printf("father:0x%x\n", r);
38.         for (int i = 0; i < sizeof(int) * 8; i++) {
39.             if (r & (__F__ << 31 - i))
40.                 Kill(pid, SIGUSR2);
41.             else
42.                 Kill(pid, SIGUSR1);
43.             __E__(&mask_father);
44.         }
45.         Wait(NULL);
46.     }
47. }
```

1. 假设 G. H 处都为空，该程序需要使得父进程和子进程的输出相同。（共 6 分，每空 1 分）

   (1) 程序填空：

   A:________________________________

   B:________________________________

   C:________________________________

   D:________________________________

   E:________________________________

   F:________________________________

---

### 2022期末-无答案 · 第四题 1(2)

> 出处：`原文/期末/2022期末-无答案.md` 第 404–404 行　·　模块判定：ECF and System IO
> 考什么：第 43 行阻塞信号是否必需的后果分析

   (2) 第 43 行的代码是必须的吗？如果"是"，请用一句话描述去掉了这一行代码会发生什么。（2 分）

---

### 2022期末-无答案 · 第四题 2

> 出处：`原文/期末/2022期末-无答案.md` 第 406–408 行　·　模块判定：ECF and System IO
> 考什么：处理函数加计数条件后子进程输出值推导

2. 假设 G 处填写 if (count % 3 == 0) return; 在 H 处填写 count++;

   如果第 36 行生成的随机数是 0xaaaaaaaa，则子进程的输出是 child:0x____________ （1 分），简要说明理由。（1 分）

---

### 2022期末-答案 · 第一题 7

> 出处：`原文/期末/2022期末-答案.md` 第 16–16 行　·　模块判定：ECF and System IO
> 考什么：异常切内核态与信号处理程序

7、①发生异常，从用户态切换到内核态 ②进程A的信号处理程序

---

### 2022期末-答案 · 第一题 8

> 出处：`原文/期末/2022期末-答案.md` 第 17–17 行　·　模块判定：ECF and System IO
> 考什么：fork/execve 进程控制

8、fork execve

---

### 2022期末-答案 · 第四题

> 出处：`原文/期末/2022期末-答案.md` 第 51–63 行　·　模块判定：ECF and System IO
> 考什么：信号屏蔽与 sigsuspend 同步

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

---

### 2024期末-带答案 · 第一题 7

> 出处：`原文/期末/2024期末-带答案.md` 第 229–243 行　·　模块判定：ECF and System IO
> 考什么：进程调度/fork/异常返回/信号辨析

7. 下列陈述中，错误陈述的数量为：
①进程调度的实现在一定程度上依赖于定时器中断（timer interrupts）。
②execv()函数成功调用后不会返回。
③使用fork()创建的子进程与父进程对内存的修改是共享的。
④在X86-64 Linux中，访存缺页异常属于故障。
⑤异常处理的返回行为包括：返回当前指令、返回下一条指令和终止(abort)。
⑥如果处理得当（如设置SIGFPE的信号处理函数），除以零引发的除法错误不会
导致终止(abort)。
⑦单核处理器上，可以通过不断地上下文切换交替运行并发的程序，给用户呈现一
种并发的程序在同时运行的感觉。
⑧进入信号处理函数时会创建新的进程。
A. 0个   B. 1个   C. 2个   D. 3个
答案：C， ③⑧错误。使用 fork 创建的子进程和父进程在 初始阶段 的内存内
容是相同的，但它们并不是直接共享内存。父子进程初期的内存内容是相同的，但
它们对内存的修改是 独立的，并不共享。进入信号处理函数并不会创建新的进程。

---

### 2024期末-带答案 · 第一题 8

> 出处：`原文/期末/2024期末-带答案.md` 第 244–266 行　·　模块判定：ECF and System IO
> 考什么：stdio 缓冲区、SIGKILL 与 fork 缓冲区

8. 在Ubuntu Linux 24.04环境中，关于系统级IO，下列说法正确的是：
A.在未进行特殊设置和额外操作的情况下，某进程先调用了fprintf()函数向某
文件写入数据，且返回值恰为传入数据字节数。若向该进程发送SIGKILL信号终
止进程，再打开该文件，一定能看到该进程写入的内容。
B.同一进程内的多个线程不加同步地调用fprintf()会导致程序崩溃。
C.由于慢速系统调用read()和write()会潜在地阻塞进程一段较长时间，高级
I/O函数使用缓冲区来减少对read()和write()的调用。
D.无论父进程的标准I/O缓冲区——例如printf()函数的缓冲区是否为空，执
7

<!-- ===== page 8 ===== -->

行fork()创建的子进程的缓冲区总是为空。
答案：C
A. SIGKILL会直接终止进程，此时，仍留存在用户态缓冲区的内容尚未被写入
磁盘。这里要求“未进行特殊设置和额外操作”保证了缓冲区存在且不被清空。
B. fprintf是线程安全的，内部有同步机制，不会导致程序崩溃。一个特殊情况
是如果两个竞争的fprintf调用操作同一个FILE*对象，那么文件内容的最终顺
序是不确定的。但也不会导致程序崩溃。
C. 正确
D. fork() 创建的子进程的标准 I/O 缓冲区不总是空的，它会复制父进程的标
准 I/O 缓冲区的内容。注意——COW并不会立即复制父进程的缓冲区，而是在子
进程或父进程尝试修改缓冲区时才会复制。

---

### 2024期末-带答案 · 第三题 Part A

> 出处：`原文/期末/2024期末-带答案.md` 第 444–470 行　·　模块判定：ECF and System IO
> 考什么：open/dup2/fork/write 与文件偏移

第三题（15分）
Part A: 分析下面这段代码的行为，假设file.txt文件存在，且不需要考虑
open()函数未能正常打开文件的情况。
#include <csapp.h>
int main(){
    int fd[3];
    fd[0] = open("./file.txt", O_RDWR | O_TRUNC, 0);
    fd[1] = open("./file.txt", O_RDWR | O_TRUNC, 0);
write(fd[0], "Harry", 5);
if (fork() == 0) {
    dup2(fd[0], fd[1]);
    write(fd[1], "Voldemort", 9);
    fd[2] = open("./file.txt", O_RDWR, 0);
    printf("%d\n", fd[2]);
    exit(0);
}
wait(NULL);
fd[1] = dup(fd[0]);
write(fd[0], "Hermione", 8);
write(fd[1], "Ron", 3);
fd[2] = open("./file.txt", O_RDWR, 0);
printf("%d\n", fd[2]);
}
1） 运行这段代码，在终端上可以看到两行输出，第一行的内容为          ，
第二行的内容为          。(每空1分)
2） 运行这段代码后，file.txt文件的内容为                             。
（3分）

---

### 2024期末-带答案 · 第三题 Part B

> 出处：`原文/期末/2024期末-带答案.md` 第 471–537 行　·　模块判定：ECF and System IO
> 考什么：信号处理函数注册、kill 与 sigprocmask

Part B:分析下列代码的行为，其功能是利用信号处理函数输出数列内容。
#include <csapp.h>
#define N 10
int flag = 0;
void handler1() {
    for (int i = 0; i < N; i += 2){
        printf("%d ", i)
        fflush(stdout);
15

<!-- ===== page 16 ===== -->

    }
    flag++;
}
void handler2() {
    for (int i = 1; i < N; i += 2){
        printf("%d ", i);
        fflush(stdout);
    }
    flag++;
}
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        signal(SIGUSR1, handler1);
        signal(SIGUSR2, handler2);
        while (flag < 2)
            sleep(1);
    }
else{
    kill(pid, SIGUSR1);
        kill(pid, SIGUSR2);
        wait(NULL);
    }
    return 0;
}
1） 运行这段代码后，发现程序没有输出，且陷入死循环。请简要指出其原因，并
给出解决方案。（2分）
2） 在解决上述问题之后，第一次运行得到“1	3	5	7	9	0	2	4	6	8”；但再次运行得到
的却是“1	3	0	2	4	6	8	5	7	9”，与期望不符。请结合“编写信号处理函数”的知识，补
全handler1()函数中缺失的代码，以保证运行结果的正确性。（3分）
void handler1(){
sigset_t mask, prev_mask;
      A      (       B       );
      C      (       D      , &mask, &prev_mask);
    for (int i = 0; i < N; i += 2){
        printf("%d ", i)
        fflush(stdout);
}
flag++;
      E      (       F      , &prev_mask);
}
基于下列选项选择序号填写：
16

<!-- ===== page 17 ===== -->

① Sigfillset;   ② Sigpromask;   ③ Sigemptyset;
④ SIG_BLOCK;    ⑤ SIG_UNBLOCK;   ⑥ SIG_SETMASK;
⑦ &mask;         ⑧ &prev_mask;    ⑨ NULL;
A:
B:
C:
D:
E:
F:

---

### 2024期末-带答案 · 第三题 Part C

> 出处：`原文/期末/2024期末-带答案.md` 第 538–581 行　·　模块判定：ECF and System IO
> 考什么：fork 父子进程 buffer 与文件写结果

Part C: 分析下面这段代码的行为，假设file.txt文件存在且初始内容为空，
并且不需要考虑open()函数未能正常打开文件的情况。
#include <csapp.h>
int main() {
char *numbers = "0123456789";
char buffer[100];
buffer[0] = '\0';
pid_t father_pid = getpid();
for (int i = 0; i < 10; ++i){
if (fork() != 0) {
strncat(buffer, numbers + i, 1);
}
}
int fd = open("./file.txt", O_RDWR , 0);
write(fd, buffer, strlen(buffer));
while(wait(NULL) != -1){}
if (getpid() == father_pid) {
close(fd);
fd = open("./file.txt", O_RDONLY, 0);
char content[100];
read(fd, content, 100);
printf("%c\n", content[3]);
printf("%c\n", content[6]);
}
exit(0);
}
17

<!-- ===== page 18 ===== -->

如果你不清楚string.h中strncat()函数的行为，可以参考下列说明:
strncat()函数用于将一个字符串追加到另一个字符串的末尾。它接受一个目标字符串
dest，一个源字符串src和最大追加的字符数n。在src的长度至少为n时，这个函数将
src的前n个字符拼接到dest字符串的后面。例如：
    char *dest = "Astarion";
char *src = "Shadowheart";
strncat(dest, src, 6);
printf("%s\n", dest);
这段代码将输出 AstarionShadow。
1） 运行上述代码，在终端上会看到两行输出，第一行的内容可能为            ，
第二行的内容可能为            。（ 你 需 要 列 出所有可能出现的 输 出， 每种 可能
性用逗号隔开，每空1分）
2） 在运行这段代码之后，file.txt中的内容有            种可能的结果。
（3分）（注意，字符串级别相等的内容属于同一种可能的结果）

---

### 2025期末-带答案 · 二 15

> 出处：`原文/期末/2025期末-带答案.md` 第 94–98 行　·　模块判定：ECF and System IO
> 考什么：异常四分类与返回行为

15.关于异常（exception）的细分类型，下列说法哪些正确？
答案：ABD
解析： trap 常见于系统调用，返回到下一条；fault 典型会重启当前指令（例如页故障
修好后重新执行触发缺页的那条访存指令），因此 C 错；page fault是 fault，不是
trap（E 错）。

---

### 2025期末-带答案 · 二 16

> 出处：`原文/期末/2025期末-带答案.md` 第 99–102 行　·　模块判定：ECF and System IO
> 考什么：进程上下文切换的时机与地址空间

16.关于“进程上下文切换（context switch）”，下列说法哪些正确？
答案：ACD
解析： B 错（不一定，有可能还在当前进程）；E 错（切换进程通常意味着切换到另一个
地址空间/页表）。

---

### 2025期末-带答案 · 二 17

> 出处：`原文/期末/2025期末-带答案.md` 第 103–107 行　·　模块判定：ECF and System IO
> 考什么：fork 后共享 open file description 的 read

17.文件t.txt的内容恰好是4字节：abcd（示意）
答案：ABE
解析： 父子进程共享同一个 open file description，因此 4 次 read 总体按顺序
消耗 a,b,c,d。某个进程读到的两字节一定是“先后顺序递增”的组合（如
ab/ac/bd/cd/...），但不可能倒序（ca）或重复（aa）。

---

### 2025期末-带答案 · 二 18

> 出处：`原文/期末/2025期末-带答案.md` 第 108–112 行　·　模块判定：ECF and System IO
> 考什么：SIGCHLD 合并递送、waitpid 回收与 zombie

18.观察下面的C程序代码
答案：AB
解析： SIGCHLD 可能合并递送；一次进入 handler 用 while(waitpid...) 可回收
多个已退出子进程，因此 A 对。reap==2 意味着两个子都已被回收，通常不会有 zombie
（B 对）。C/D/E 都不成立。

---

### 2025期末-带答案 · 二 19

> 出处：`原文/期末/2025期末-带答案.md` 第 113–116 行　·　模块判定：ECF and System IO
> 考什么：阻塞期间同类信号 pending 不排队

19.观察下面的C程序代码：
答案：B
解析： 普通信号（非实时信号）通常不排队：阻塞期间同种信号 pending 只记一次，因
此解除阻塞后 handler 只会跑一次（B/E 对），解除阻塞前不会递送（D 错）。

---

### 2025期末-带答案 · 二 20

> 出处：`原文/期末/2025期末-带答案.md` 第 117–123 行　·　模块判定：ECF and System IO
> 考什么：execve 成功后 PID 与地址空间语义

20.关于 execve()成功执行后的语义，下列说法哪些正确？
3

<!-- ===== page 4 ===== -->

答案：ABD
解析： exec 是“在同一进程里换程序”，PID 不变（C 错），也不会创建新进程（E 错）

---

### 2025期末-无答案 · 二 15

> 出处：`原文/期末/2025期末-无答案.md` 第 205–210 行　·　模块判定：ECF and System IO
> 考什么：异常四分类与返回行为

15.关于异常（exception）的细分类型，下列说法哪些正确？
A. Interrupt 通常由外部设备异步触发，处理后回到“下一条指令”
B. Trap 通常在CPU内部由执行指令触发，处理后回到“下一条指令”
C. Fault 通常表示可以恢复的错误，处理后回到“下一条指令”
D. Abort 通常表示不可恢复的错误，程序一般不会继续执行
E. 执行访存指令引发的缺页异常，属于Trap

---

### 2025期末-无答案 · 二 16

> 出处：`原文/期末/2025期末-无答案.md` 第 215–220 行　·　模块判定：ECF and System IO
> 考什么：进程上下文切换的时机与寄存器保存

16.关于“进程上下文切换（context switch）”，下列说法哪些正确？
A. 进程切换通常发生在内核态，由调度器决定下一个运行的进程
B. 显式调用 fork() 就会发生进程切换
C. 定时器中断（timer interrupt）可能触发调度，从而导致进程切换
D. 切换进程时需要保存当前进程的寄存器状态，并恢复另一个进程的寄存器状态
E. 上下文切换不会改变当前进程的虚拟地址空间映射（页表等）

---

### 2025期末-无答案 · 二 17

> 出处：`原文/期末/2025期末-无答案.md` 第 221–232 行　·　模块判定：ECF and System IO
> 考什么：fork 后共享文件偏移下的 read 结果

17.文件t.txt的内容恰好是4字节：abcd（示意）
int main(void){
int fd = open("t.txt", O_RDONLY);
char x, y;
fork();
read(fd, &x, 1);
read(fd, &y, 1);
printf("%c%c\n", x, y);
return 0;
}
下列哪些可能作为某一次 printf 打印出的那一行内容出现？
A. ab B. bd C. ca D. aa E. cd

---

### 2025期末-无答案 · 二 18

> 出处：`原文/期末/2025期末-无答案.md` 第 233–251 行　·　模块判定：ECF and System IO
> 考什么：SIGCHLD 不排队、waitpid 回收与 zombie

18.观察下面的C程序代码
volatile sig_atomic_t reap = 0;
void handler(int sig){
while (waitpid(-1, NULL, WNOHANG) > 0)
reap++;
}
int main(void){
Signal(SIGCHLD, handler);
for (int i = 0; i < 2; i++)
if (fork() == 0) _exit(0);
while (reap < 2) ;
printf("OK\n");
}
下列说法哪些正确？
A. handler 可能只被调用 1 次，但 reap 最终仍可能变为 2
B. 程序打印 OK 时，通常不会残留 zombie 子进程
C. 因为 SIGCHLD 不排队，reap 最大只能到 1
D. 若把 handler 里的 while 改为只调用一次 waitpid，则一定不会留下 zombie
E. OK 可能在任意时刻打印（包括在子进程尚未退出时）

---

### 2025期末-无答案 · 二 19

> 出处：`原文/期末/2025期末-无答案.md` 第 252–275 行　·　模块判定：ECF and System IO
> 考什么：阻塞信号 pending 不排队与 sigprocmask

19.观察下面的C程序代码：
volatile sig_atomic_t count = 0;
void h(int sig){ count++; }
int main(void){
sigset_t m;
6

<!-- ===== page 7 ===== -->

sigemptyset(&m);
sigaddset(&m, SIGINT);
Signal(SIGINT, h);
sigprocmask(SIG_BLOCK, &m, NULL);
raise(SIGINT);// raise()用于向当前进程发出指定信号
raise(SIGINT);
sigprocmask(SIG_UNBLOCK, &m, NULL);
printf("%d\n", (int)count);
}
该程序正常执行完，下列说法哪些正确？
A. count 一定为 0
B. count 一定为 1
C. count 可能为 2
D. 在解除阻塞之前，handler可能会运行
E. 在设置阻塞之前，handler可能会运行

---

### 2025期末-无答案 · 二 20

> 出处：`原文/期末/2025期末-无答案.md` 第 276–282 行　·　模块判定：ECF and System IO
> 考什么：execve 成功后的语义与 fd 保持

20.关于 execve()成功执行后的语义，下列说法哪些正确？
A. 成功的 execve() 不会返回到调用点（除非失败）
B. execve() 会用新程序的代码/数据替换当前进程的用户态地址空间
C. execve() 成功后，进程 PID 会改变（变成新程序的 PID）
D. execve() 成功后，默认情况下已打开的文件描述符仍然保持打开（除非设置
close-on-exec）
E. execve() 会创建一个新进程，因此父子关系会改变

---

### 期末往年题勘误、详解 by Arthals · 2016 第一题 第10问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 67–67 行　·　模块判定：ECF and System IO
> 考什么：SIGPIPE 与 I/O 多路复用（兼 Network）

第 10 问，A 是不会有信号的。在网络那一章中，只有链接异常断开会导致 SIGPIPE。A 中描述的“新连接到达监听端口”不会导致操作系统发送信号给进程，而是通过网络编程接口（如 POSIX 的 socket API）提醒应用程序有新的连接。这通常是通过 I/O 多路复用（如 select、poll、epoll 等系统调用）来实现的，其中应用程序会监控一个或多个网络端口的状态，当有新连接到来时，操作系统会唤醒正在等待的程序，而不是发送信号。

---

### 期末往年题勘误、详解 by Arthals · 2018 第一题 第6问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 91–91 行　·　模块判定：ECF and System IO
> 考什么：dup2 对未打开描述符也合法

第 6 问，执行过程中没有发生从未打开的描述符进行复制，所以错。实际测试：可以向一个未打开的描述符进行复制、从一个未打开的描述符复制（即未打开的描述符是 dup2 的第一个参数）都是合法的（但是后者一旦开始写就会报错）。

---

### 期末往年题勘误、详解 by Arthals · 2018 第四题

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 103–119 行　·　模块判定：ECF and System IO
> 考什么：fork 后 fd 与信号竞争导致的输出

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

---

### 期末往年题勘误、详解 by Arthals · 2021 第三题 Part C

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 222–222 行　·　模块判定：ECF and System IO
> 考什么：可替换代码段的函数运行在用户态（存疑）

Part C，既然这个函数是可以被换成自己指定的代码段的，那么肯定运行在用户态下。否则就构成越权了。

---

### 2025第2次阶段测验-带答案 · 第16/17讲 22

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 279–284 行　·　模块判定：ECF and System IO
> 考什么：除 0 异常属 Faults 能否在处理器中修正后继续

22.（3分）整数运算中有可能会出现“除0异常”，如果这是属于Faults类型的异常，
是否可以在异常处理程序中，将结果修改成某个特殊值，例如全为1的二进制数，然
后继续执行该程序（指整数运算那个程序）后续指令？
答：不可以（1分）。Faults类型的异常，从异常处理程序返回后，要重新执行这条
“除0”指令，导致再次发生异常。所以只能终止该进程。（2分）注：如果一开始的结论
就不对，后面如何解读都不得分。

---

### 2025第2次阶段测验-带答案 · 第16/17讲 23

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 285–307 行　·　模块判定：ECF and System IO
> 考什么：fork 程序的输出次数与输出顺序判断

23.（3分）阅读下面这段程序
#include <stdio.h>
#include <unistd.h>
int main() {
printf("A\n");
pid_t pid = fork();
if (pid == 0) {
printf("B\n");
} else {
printf("C\n");
fork();
}
printf("D\n");
return 0;
}
该程序正常运行后，问
（1）会输出几次 D：3 次
10

<!-- ===== page 11 ===== -->

（2）B和C哪个先输出：不确定
（3）ACDBDD这个输出序列是否可能：是（√）否（ ）

---

### 2025第2次阶段测验-带答案 · 第16/17讲 24

> 出处：`原文/阶段测验/2025第2次阶段测验-带答案.md` 第 308–340 行　·　模块判定：ECF and System IO
> 考什么：含 fork/wait/sleep 的程序进程数与输出行数

24.（6分）阅读下面这段程序
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
int x = 1;
int main() {
printf("start: x = %d\n", x);
pid_t pid1 = fork();
if (pid1 == 0) {
x += 1;
printf("x = %d\n", x);
sleep(1);
pid_t pid2 = fork();
if (pid2 == 0) {
x += 2;
printf("x = %d\n", x);
} else {
x += 3;
printf("x = %d\n", x);
wait(NULL);
}
} else {
x += 4;
printf("x = %d\n", x);
wait(NULL);
printf("x = %d\n", x);
}
return 0;
}
（1）（2分）这个程序正常运行，会产生几个进程？（ 3 ）
（2）（2分）总共会输出多少行？（ 6 ）
（3）（2分）最后一行输出是：D
A.x=2 B.x=3 C.x=4 D.x=5 E.x=6 F.不确定

---

### 2025Lab测验-无答案 · Lab 任务 1

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 57–61 行　·　模块判定：ECF and System IO
> 考什么：ls -a 显示隐藏文件（L0 命令行）

1.  （2分）以下哪个ls命令选项用于显示所有文件（包括隐藏文件，以.开头的文件）
A. ls -l
B. ls -a
C. ls -h
D. ls -t

---

### 2025Lab测验-无答案 · Lab 任务 2

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 62–66 行　·　模块判定：ECF and System IO
> 考什么：cd 的 - 参数表示上次所在目录

2.  （2分）使用cd命令时，哪个参数表示“上一次所在目录”
A. ~（波浪符）
B. ..（两个点）
C. -（减号）
D. /（斜杠）

---

### 2025Lab测验-无答案 · Lab 任务 3

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 71–75 行　·　模块判定：ECF and System IO
> 考什么：chmod 755 的文件权限位

3.  （2分）执行 chmod 755 file.py 后，文件 file.py 的权限是：
A. 所有者：读写执行（rwx），组和其他：读和执行（r-x）
B. 所有者：读写（rw-），组和其他：读（r--）
C. 所有者：读和执行（r-x），组和其他：读写（rw-）
D. 所有者：读写执行（rwx），组和其他：读写（rw-）

---

### 2025Lab测验-无答案 · Lab 任务 4

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 76–83 行　·　模块判定：ECF and System IO
> 考什么：tar/gcc/rm/rmdir/grep 命令用法辨误

4.  （2分）下列关于 Linux 命令和命令行的使用，说法错误的一项是：
A. 在Windows中解压tar文件可能导致权限位丢失和文件名大小写问题，因此最好
在 Linux 中使用tar命令解压
B. gcc命令可用于编译 C 语言代码，其中 -o 选项用来指定输出的文件，-O 选项
用来指定优化级别
C. rm命令用于删除单个文件或多个文件，如果要删除空目录只能用rmdir命令
D. grep命令中，-i选项的含义是“忽略大小写”，如grep -i "hello" file.txt
可匹配Hello、HELLO等

---

### 2025Lab测验-无答案 · Lab 任务 16

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 260–267 行　·　模块判定：ECF and System IO
> 考什么：GDB 断点通过 INT3 触发陷阱实现

16. （2分）GDB 中断点功能的一种实现方式是：GDB 修改目标程序断点处的机器代码，
让 CPU 执行到该位置时将控制权交给 GDB；之后 GDB 会恢复现场，包括将原指令
写回、调整 %rip 回到断点指令处等，以使程序可以继续执行。基于这一机制，下列
哪一项最符合实际情况？
A. GDB 将断点处指令修改为 NOP，CPU 执行后不做任何操作，程序会暂停并等待
B. GDB 将断点处指令修改为 INT3，CPU 执行后触发陷阱，陷入内核
C. GDB 将断点处指令修改为 sysenter，CPU 执行后陷入内核
D. GDB 将断点处指令修改为一条非法指令，类似于系统调用，CPU执行后会陷入内核

---

### 2025Lab测验-无答案 · Lab 任务 21

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 464–474 行　·　模块判定：ECF and System IO
> 考什么：hex2raw 用法与 shell 管道/输入输出重定向

21. （2分）在AttackLab中，hex2raw工具用于将表示十六进制的字符串转换为字节
序列，以便将攻击代码注入到目标程序中。假设现在有一个包含十六进制字符串的文件
hex.txt，下列哪个选项是错误的？
A. 可以使用命令cat hex.txt | hex2raw > raw.bin将hex.txt中的内容转
换为字节序列并保存到raw.bin文件中
B. 可以使用命令hex2raw < hex.txt > raw.bin将hex.txt中的内容转换为
字节序列并保存到raw.bin文件中
C. 在得到文件raw.bin后，可以使用命令./ctarget < raw.bin将raw.bin作
为输入传递给目标程序ctarget
D. 如果修改了hex.txt文件的内容，必须重新编译hex2raw工具才能正确转换新的
内容

---

### 2025Lab测验-无答案 · Lab 任务 35

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 699–704 行　·　模块判定：ECF and System IO
> 考什么：getopt 解析命令行参数（Unix API，CacheLab 语境）

35. （2分）在 CacheLab Part A 编写缓存模拟器 (csim.c) 时，推荐使用哪个 C
语言函数来解析命令行参数（如-s, -E, -b等）？
A. scanf
B. getopt
C. mmap
D. fopen

---

### 2025Lab测验-无答案 · Lab 任务 36

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 712–721 行　·　模块判定：ECF and System IO
> 考什么：ShellLab tsh 与真实 shell 的功能对比

36. （2分）在ShellLab中，我们实现了一个简单的shell程序tsh。和真实的Linux
shell相比，下列哪一项说法是错误的？
A. tsh中不支持变量，也不支持搜索路径，无法直接运行系统程序如cat，需要输入
完整路径/bin/cat
B. tsh中不支持管道（|），但支持I/O重定向（<, >），且可以在一条命令里同时
进行输入、输出重定向
C. tsh和真实的shell一样，需要捕获SIGINT和SIGTSTP信号，然后再将这些信
号发送给前台进程组
D. tsh和真实的shell一样，支持通过&设置程序在后台执行，也支持通过fg命令
将后台任务转移到前台

---

### 2025Lab测验-无答案 · Lab 任务 37

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 722–731 行　·　模块判定：ECF and System IO
> 考什么：为避免竞态的信号屏蔽与解除时机

37. （2分）在ShellLab中，为了避免出现竞争（race），需要在特定的操作前屏蔽一
些信号。下列关于屏蔽信号与解除屏蔽的时机，说法错误的一项是？
A. sigint_handler中不需要屏蔽信号，因为只需要读取全局数据结构job_list，
而无需对其进行修改
B. sigchld_handler中需要屏蔽信号，因为需要修改全局数据结构job_list，更
新job的状态等相关信息
C. eval 中需要屏蔽信号，因为需要修改全局数据结构 job_list，在创建新任务时
添加新创建的job信息
D. fork之后需要解除屏蔽信号，解除的时机可以在执行setpgid之前，也可以在执
行setpgid 之后

---

### 2025Lab测验-无答案 · Lab 任务 38

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 736–741 行　·　模块判定：ECF and System IO
> 考什么：ShellLab 内建命令 jobs/bg/kill/nohup

38. （2 分）在 ShellLab 中，我们需要实现一系列内建命令。下列关于内建命令的说法
正确的是？
A. jobs命令中我们需要列出所有任务，且需要先屏蔽所有相关信号，避免竞争
B. bg命令中我们需要将当前运行在前台的任务变为后台运行，且不使任务停止
C. kill命令中我们需要向指定的进程或进程组发送SIGKILL信号以将其终止
D. nohup命令中我们需要在创建子进程后阻塞SIGHUP信号或设置忽略该信号

---

### 2025Lab测验-无答案 · Lab 任务 39

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 742–761 行　·　模块判定：ECF and System IO
> 考什么：sigchld_handler 中 WIFSTOPPED/WIFCONTINUED 判断

39. （2分）下面是ShellLab中sigchld_handler的一个正确实现中的部分代码（省
略了部分检查与输出）。则代码中(1)和(2)应该分别为？
A. (1) WIFSTOPPED (2) WIFCONTINUED
B. (1) WIFSTOPPED (2) WIFSIGNALED
C. (1) WIFEXITED  (2) WIFCONTINUED
D. (1) WIFEXITED  (2) WIFSIGNALED
while  ((child_pid  =  waitpid(-1,  &status,  WNOHANG  |  WUNTRACED  |
WCONTINUED)) > 0) {
    if (_____(1)_____(status)) {
        struct job_t *j = getjobpid(job_list, child_pid);
        j->state = ST;
    }
    else if (_____(2)_____(status)) {
        struct job_t *j = getjobpid(job_list, child_pid);
        if(!(j->state == FG)) {
            j->state = BG;
        }
    }
    // ...
}

---

### 2025Lab测验-无答案 · Lab 任务 40

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 766–797 行　·　模块判定：ECF and System IO
> 考什么：waitfg 前台等待的正确实现（sigsuspend）

40. （2分）在ShellLab中，我们在sigchld_handler中使用waitpid来回收子进
程，同时我们定义了waitfg函数用来等待特定pid的前台任务结束。下面waitfg
函数的实现，正确的一项是？
A.  void waitfg(pid_t pid) {
    int timeout = 0;
    struct job_t *j = getjobpid(job_list, pid);
    while (j->pid == pid && j->state == FG) {
        if (++timeout > MAX_TIME) {
            break;
        }
    }
}
B.  void waitfg(pid_t pid) {
    struct job_t *j = getjobpid(job_list, pid);
    while (j->pid == pid && j->state == FG) {
        sleep(1);
    }
}
C.  sigset_t oldmask;
void waitfg(pid_t pid) {
    struct job_t *j = getjobpid(job_list, pid);
    while (j->pid == pid && j->state == FG) {
        sigsuspend(&oldmask);
    }
}
D.  int status;
void waitfg(pid_t pid) {
    struct job_t *j = getjobpid(job_list, pid);
    while (j->pid == pid && j->state == FG) {
        waitpid(pid, &status, 0);
    }
}

---

## 三、相关试卷的参考答案 / 解析原文

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

### chap 10 解析 · 第十章选择题 1 答案 B 与逐项解析

> 出处：`原文/期末/2021期末-带答案/chap 10 解析.md` 第 13–21 行

答案：B（简单）

1.  描述符0，1，2可以重定向到其他文件。

2.  正确，教材P534。

3.  有缓冲区和无缓冲区的不可以交叉使用，教材P629。

4.  多次打开文件应该对应着多个打开文件表，教材P635。

---

### chap 10 解析 · 第十章选择题 2 答案 D

> 出处：`原文/期末/2021期末-带答案/chap 10 解析.md` 第 51–51 行

答案：D（中等）

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

### chap 8 解析 · 第 1 题答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 13–17 行

答案：C

简单

A中option参数应该使用 \| 运算结合。B中SIGKILL不是唯一的例外，例外共有两个：SIGKILL、SIGSTOP。D陷阱一定是同步发生的

---

### chap 8 解析 · 第 2 题答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 29–41 行

答案：A

中等

1.  中断、中断

2.  故障、故障

3.  陷阱、终止

4.  中断、终止

P506

---

### chap 8 解析 · 大题 PART A/B 答案与解题要点

> 出处：`原文/期末/2021期末-带答案/chap 8 解析.md` 第 79–111 行

答：

**PART A.**

A: kill(pid_1, SIGUSR1);或 kill(getpid()−1, SIGUSR1);

B: signal(SIGUSR1, handler1);

C: nxt = 2;

D: waitpid(0, &status, 0)\> 0 或 waitpid(−1, &status, 0)\> 0

**PART B.**

> 1.C
>
> 2.A
>
> <img src="media/media/image1.png" style="width:3.89687in;height:1.02812in" />3.BCD: CC1, C1C2, CC12
>
> 4.A: CC
>
> 所有可能的输出为CC1, CC1R, CC1R2, CC1R2R, C1RC2, C1RC2R, C1CR2。
>
> <img src="media/media/image2.png" style="width:6.10764in;height:1.36324in" />比如，CC1是可能的，因为子进程可以在接收到父进程的SIGUSR2之前退出。
>
> 解题要点：
>
> 1\. 进程只在内核态切换到用户态时检测并处理信号
>
> 2\. 在处理信号之前相同信号接收到多次，只按照一次计算
>
> 3\. 注意子进程可以比父进程先结束，父进程将无法发送信号给子进程

---

### chap 9 解析 · 选择题 1 答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 13–23 行

答案：D

解析：属于中等题。考察虚拟内存和高速缓存的关系，并且和进程/线程有一定联系。

A 课本原话：A TLB is a small, virtually addressed cache where each line holds a block consisting of a single PTE.

B 课本原话：Although a detailed discussion of the trade-offs is beyond our scope here, most systems opt for physical addressing.

C 线程共享虚拟地址空间，所以 TLB 中条目不会失效

D 课本原话：With physical addressing, it is straightforward for multiple processes to have blocks in the cache at the same time and to share blocks from the same virtual pages.

---

### chap 9 解析 · 选择题 2 答案与解析（COW 过程详解）

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 73–77 行

答案：A

解析：属于中等题。主要考察对私有对象COW机制及mmap函数的理解。

程序打开文件描述符fd后，使用mmap函数创建了一块映射到文本“./input.txt”所在区域的私有虚拟内存区域，其地址存储在指针bufp中。父进程创建完子进程后，首先等待子进程结束。子进程在试图对\*bufp写入‘2’时，触发了一次COW。它在物理内存中创建一个“input.txt”文本所在页面的副本，并在新的页面里完成写入操作，写入完成后子进程bufp所在地址的第一个字节值为新写入的‘2’，第二个字节值为原始值‘2’。子进程结束后，其缓冲区内”21”的值正常输出。父进程在试图对\*(bufp+1)写入‘1’，同样触发了一次COW，bufp所在地址的第一个字节为原始值‘1’，第二个字节为新写入的‘1’，故父进程输出“11”。最后父进程重新创建一块映射到“input.txt”所在页面的虚拟内存并输出。由于上述写入都是在新的物理页面下完成的，“input.txt”所在页面没有发生修改，故最后一步父进程的输出为“12”。综上，最终在终端的输出为“221112”。

---

### chap 9 解析 · 大题 1-4 的答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 225–287 行

答案：

1.  1 ②④

2.  3 0x00615000 0x48

3.  ⑴ 4 int \*y = (int \*)calloc(n, sizeof(int)); 或

> int \*y = (int \*)Calloc(n, sizeof(int));
>
> 其中 calloc/Calloc 的两个参数只要乘起来等于 n \* sizeof(int) 即算对
>
> ⑵ n \< 0（或其他等价表达）

4.  ③

解析：

1.  考察 TLB 的位划分与表项含义，属于简单题。

题目告知TLB命中且无缺页，因此只需要访问物理页，即访问一次物理内存

根据 y 的值可以得到 TLBT=0xd551，TLBI=5，查表知 y 在TLB条目的内容为0x019fa42d，R/W=0，U/S=1，因此这一页的实质权限为只读、内核模式。

参见课本第9.6和9.7节（P567-582）

2.  考察虚拟内存地址翻译，属于简单+中等题。

题目告知TLB未命中且无缺页，因此需要访问页目录、二级页表和物理页，共访问三次物理内存。

计算得x 的VPN1=1， VPN2=0，PPO =0x4d0。页目录基地址在 0x00e66000，因此相应页目录中所在条目地址为 0x00e66000+1\*4=0x00e66004，从表中按小端法读出0x00615721，因此二级页表存在，首地址为0x00615000，这恰好也是相应二级页表中所在条目的地址，从表中按小端法读出0xc0ee2d21，因此物理页存在，首地址为0xc0ee2000，因此x的物理地址为0xc0ee2000+0x4d0=0xc0ee24d0。从表中读出一个字节，为0x48。

参见课本第9.6和9.7节（P567-582）

3.  本题考查内存安全。

⑴ 考察malloc函数的性质，属于中等题。

malloc函数并不会清零所分配内存区域，因此同样的输入可能会有不同的输出，但mat_vec_mul函数别的行都不可能产生这一效果，因此只需要将第4行换为

> int \*y = (int \*)Calloc(n, sizeof(int));

Calloc是一个带错误检查的、会将所分配区域置零的函数。

参见课本第9.11.2节正文例子（P610）。

⑵ 内存安全的综合考察，属于难题。

假设malloc函数分配成功，那么y不是空指针。y\[0\]不可能在外部访问出现段错误，因此这种情况不成立，malloc一定出现了问题，导致y是空指针。但是此时 mat_vec_mul 并没有触发段错误，说明函数内部一次对y的访问都没有，这只有可能循环都没有进入，因此必须有n\<=0，根据题设，参数是非零的，所以n\<0。以上推导出了n\<0是必要条件。

下面推导n\<0是充分条件，即任何n\<0都会导致这样的错误。为此，只需要说明malloc函数一定分配失败。首先，这是Linux 64位系统，因此地址空间为64位，size_t为64位，用户虚拟地址空间为48位。注意n\*sizeof(int) 会将n的类型转为long，再转为unsigned long，而n只有32位，所以符号扩展之后最高位至少有33个1，乘sizeof(int)，即4之后，最高位还有至少29个1，因此n\*sizeof(int)\>2<sup>63</sup>\>2<sup>48</sup>，超过了用户虚拟地址空间的大小，因此无论如何，malloc函数都会分配失败。

参见课本第9.8节（P576）、9.9.1节（P588）、2.2.8节（P58-59）。

4.  本题考查对缺页故障、异常处理的综合理解，属于难题。

① 如果CPU权限位是内核态，它自然可以运行用户级代码，不会触发异常。

② 如果缺页故障处理程序运行时，收到外部中断，这不属于故障，因此不会触发。

③ 如果缺页故障处理程序不在主存，那么调用它会触发缺页故障，于是这个故障又会导致调用缺页故障处理程序，但它仍然不在主存，故这一故障无法被解决，于是触发double fault。

相关内容参见课本第8.1节（P502-507）、9.7.2节（P581-582）和Intel 64 and IA-32 Architectures Software Developer’s Manual - Volume 3: System Programming Guide 的第6.15节。

---

### chap 9 解析 · 备选题 1 答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 301–311 行

答案：A

解析：属于简单题。考察虚拟内存在管理内存方面起到的作用，主要对应中文版课本第566页。

A 程序的编译过程与使用虚拟内存还是使用物理内存的联系较小。

B 课本原话：…Such uniformity greatly simplifies the design and implementation of linkers, allowing them to produce fully linked executables that are independent of the ultimate location of the code and data in physical memory.

C. 课本原话：Virtual memory also makes it easy to load executable and shared object files into memory.

D. 课本原话：… the operating system can arrange for multiple processes to share a single copy of this code by mapping the appropriate virtual pages to in different processes to the same physical pages.

---

### chap 9 解析 · 备选题 2 答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 325–335 行

答案：A

解析：属于简单题。主要考察地址空间和虚拟内存相关的基本概念。

A. 如果运行的程序有良好的时间局部性，工作集大小（引用的页面总数）即使超过物理内存总的大小也能有较好的性能。

B. 课本原话：\[p561\] Each byte of main memory has a virtual address chosen from the virtual address space, and a physical address chosen from the physical address space.

C. 课本原话：\[p567\] When a program \[…\] requests additional heap space \[…\], the operating system allocates an appropriate number \[…\] contiguous virtual memory pages, and maps them \[…\] arbitrary physical pages located anywhere in physical memory.

D. 课本原话：\[p566\] Notice that multiple virtual pages can be mapped tothe same shared physical page.

---

### chap 9 解析 · 备选题 3 答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 347–357 行

答案：B

解析：属于中等题。考察对动态内存分配的理解，并与内存保护机制，异常有一定联系。

A 课本原话：If incr is zero, then sbrk returns the current value of brk.

B 已经分配的内存一般不会被 OS 回收，相当于用户空间正常的内存访问

C 只要不超出堆的范围，就不会触发异常。如果超出堆的范围，则触发异常

D 课本原话：While it is certainly possible to use the low-level mmap and munmap functions to create and delete areas of virtual memory, C programmers typically find it more convenient and more portable to use a dynamic memory allocator when they need to acquire additional virtual memory at run time.

---

### chap 9 解析 · 备选题 4 答案与解析

> 出处：`原文/期末/2021期末-带答案/chap 9 解析.md` 第 369–379 行

答案：C

解析：属于中等题。主要考察虚拟内存相关的理解问题。

A. 课本原话：… \[virtual memory\] works silently and automatically, without any intervention from the application programmer.

B. 课本原话：Interestingly, some early systems \[…\] supports a virtual address space that was smaller than the available physical memory.

C. 课本原话：… the operating system allocates \[…\] contiguous virtual memory pages \[…\] The pages can be scattered randomly in physical memory.

D. 课本原话：The bss area is demand-zero, mapped to an anonymous file \[…\]

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
