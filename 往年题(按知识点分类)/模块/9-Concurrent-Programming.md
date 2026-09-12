# 并发编程与同步

> **英文模块名**：`Concurrent Programming and Synchronization`  

> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，
> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。

## 一、清单

共 74 道题，来自 18 份材料。

| 年份 | 试卷 | 类别 | 题号 | 考什么 |
|---|---|---|---|---|
| 2013 | 2013期末-带答案 | 期末 | 第一题 19 | pthread_create 程序输出判断 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 20 | 信号量 PV 序列与死锁判定 |
| 2013 | 2013期末-带答案 | 期末 | 第八题 | 用信号量实现单双号限行（PV 操作填空） |
| 2014 | 2014期末-带答案 | 期末 | 第一题 19 | Pthread_detach 与 Pthread_create 用法 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 20 | 并发轨迹线安全/不安全判定 |
| 2014 | 2014期末-带答案 | 期末 | 第九题 | 水果盘问题的信号量设计与 PV 填空 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 19 | 多线程可共享的变量（全局/静态局部） |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 20 | 信号量 PV 序列的死锁判定 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第八题 | 双缓冲区生产者-消费者信号量设计与 PV 填空 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 19 | 基于进程的并发服务器父子资源共享关系 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 20 | 信号量 PV 下多线程输出的可能性 |
| 2016 | 2016期末-带答案 | 期末 | 第八题 | 多线程 cnt++ 竞态分析与 PV 实现司机售票员同步 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 19 | 死锁定义、信号量顺序与线程安全 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 20 | 主线程与线程1交错执行的输出种类 |
| 2017 | 2017期末-无答案 | 期末 | 第八题 | 并发 echo 服务器 P/T 代码找错与信号量同步 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 13 | 线程安全与可重入的包含关系 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 14 | 进程与线程的资源共享与上下文切换 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 15 | 对等线程引用的变量集合判定 |
| 2018 | 2018期末-带答案 | 期末 | 第七题 2-4 | i++/j++ 竞态的输出可能性与信号量死锁 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 22 | 线程间共享与私有数据 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 23 | 锁/解锁/信号顺序的最优全序 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 24 | pthread_exit 与 exit 的差别 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 25 | 加锁顺序相反导致的死锁 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 解答题五 | 哲学家就餐死锁与信号量实现互斥 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 8 | 并行与并发的关系 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 18 | 线程安全与可重入函数 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 19 | 对等线程赋值与 accept 的竞争 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 20 | sem 与 pthread_mutex 阻塞范围 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 解答题六 | 读者优先读写锁的竞争 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 8 | 进程并发与并行的区别 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 17 | 死锁现象的判定 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 18 | 线程安全与可重入函数 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 19 | 多线程 echo 服务器中 connfd 的竞争 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 20 | 信号量与 P/V 操作语义 |
| 2019 | 2019期末-无答案 | 期末 | 第七题 | 第一类读者-写者问题的执行流程分析 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 22 | 同进程内不同线程共享的资源 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 23 | 指令重排以消除共享变量竞争 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 24 | 主线程退出导致对等线程终止 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 25 | 信号量执行轨迹中的死锁 |
| 2020 | 2020期末-无答案 | 期末 | 第六题 | 圆桌信号量：死锁、加锁顺序与二元信号量实现 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 20 | 进程与线程的上下文、栈与地址空间 |
| 2021 | 2021期末-无答案 | 期末 | 第六题 | 生产者-消费者：信号量解法与等待计数解法 |
| 2021 | chap 11-12 解析 | 期末 | 选择题 1 | 进程与线程模型：上下文、线程栈、地址空间 |
| 2021 | chap 11-12 解析 | 期末 | 大题 小题1 | 生产者-消费者信号量解法1：代码与子问题 |
| 2021 | chap 11-12 解析 | 期末 | 大题 小题2 | 信号量模拟条件变量解法2：代码与子问题 |
| 2021 | chap 11-12 题目 | 期末 | 选择题 1 | 进程与线程模型：上下文、线程栈、地址空间 |
| 2021 | chap 11-12 题目 | 期末 | 大题 小题1 | 信号量解法1：P/V 顺序、死锁饥饿、rand 线程安全 |
| 2021 | chap 11-12 题目 | 期末 | 大题 小题2 | 信号量模拟条件变量：while 换 if 的同步错误 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 14 | 主线程创建对等线程后两线程并发运行 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 15 | 以互斥为目的的二元信号量即互斥锁 |
| 2022 | 2022期末-无答案 | 期末 | 第七题 1 | 第一类读者-写者（读者优先）信号量 P/V 填空 |
| 2022 | 2022期末-无答案 | 期末 | 第七题 2 | 第二类读者-写者（写者优先）信号量 P/V 填空 |
| 2022 | 2022期末-答案 | 期末 | 第一题 14 | 对等线程 |
| 2022 | 2022期末-答案 | 期末 | 第一题 15 | 互斥锁 |
| 2022 | 2022期末-答案 | 期末 | 第七题 | 信号量实现读者-写者与互斥 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 13 | 线程栈与 pthread_join/detach |
| 2024 | 2024期末-带答案 | 期末 | 第五题 Part A | 读者-写者与信号量代码补全、饥饿 |
| 2024 | 2024期末-带答案 | 期末 | 第五题 Part B | 线程/信号共享变量、竞态与信号安全 |
| 2025 | 2025期末-带答案 | 期末 | 二 25 | 进程与线程资源共享与寄存器独立 |
| 2025 | 2025期末-带答案 | 期末 | 四 1 | 共享变量识别及参考答案 |
| 2025 | 2025期末-带答案 | 期末 | 四 2 | Lightswitch 读者-写者两问及答案 |
| 2025 | 2025期末-带答案 | 期末 | 四 3 | 生产者-消费者订单缓冲区空白答案 |
| 2025 | 2025期末-无答案 | 期末 | 二 25 | 进程与线程的资源共享与切换开销 |
| 2025 | 2025期末-无答案 | 期末 | 四 1 | 多线程代码中的共享变量识别 |
| 2025 | 2025期末-无答案 | 期末 | 四 2 | Lightswitch 读者-写者与到达时刻状态分析 |
| 2025 | 2025期末-无答案 | 期末 | 四 3 | 服务员-厨师订单缓冲区的生产者-消费者 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2015 第八题 | 两 mutex 初值应为 1 与 PB 代码订正 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2016 第一题 第20问 | 非 volatile 变量的寄存器缓存与加锁 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2018 第一题 第13问 | 使用全局变量导致线程不安全 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2018 第七题 第4问 | 信号量初值≥2 时锁失效 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2019 第七题 | 读者-写者 while 循环的竞争含义 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2020 第一题 第25问 | a、d 加锁顺序相反导致死锁 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2020 第六题 | 哲学家就餐加锁顺序与 sem 的 value/zero |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2021 第六题 2.b | 生产者-消费者中 if 与 while 的区别 |

## 二、题目原文

### 2013期末-带答案 · 第一题 19

> 出处：`原文/期末/2013期末-带答案.md` 第 278–305 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：pthread_create 程序输出判断

19、在Pthread线程包使用中，下列代码输出正确的是：（     ）
void *th_f(void * arg)
{
 printf("Hello World") ;
  pthread_exit(0) ;
}
int main(void)
{
8

<!-- ===== page 9 ===== -->

   pthread_t tid;
   int st;
   st = pthread_create(&tid,NULL,th_f,NULL);
   if(st<0) {
      printf("Oops, I can not create thread\n");
      exit(-1);
   }
   sleep(1);
   exit(0);
}
A. Oops, I can not create thread
B. Hello World
  Oops, I can not create thread
C. Hello World
D. 不输出任何信息
答案：C

---

### 2013期末-带答案 · 第一题 20

> 出处：`原文/期末/2013期末-带答案.md` 第 306–319 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量 PV 序列与死锁判定

20、有四个信号量，初值分别为：a=1,  b=1,  c=1,  d=1
线程1：  线程2：  线程3：
① P(a);   ⑨ P(c);  ⑮ P(d);
② P(b);  ⑩ P(b);  ⑯ P(a);
③ P(d);   ⑪ V(c);  ⑰ V(d);
④ P(c);  ⑫ V(b);  ⑱ P(b);
⑤ V(d);  ⑬ P(a);  ⑲ V(a);
⑥ V(a);  ⑭ V(a);  ⑳ V(b);
⑦ V(b);
⑧ V(c);
上面的程序执行时，下列哪些执行轨迹不会产生死锁?
A. ①②③⑨⑩⑮④      B. ⑨①②③⑩
C. ①②⑮⑨③          D. ⑨①⑮②③
答案：实际上四个选项都有问题，无正确答案，因此批卷时本题直接算作得分

---

### 2013期末-带答案 · 第八题

> 出处：`原文/期末/2013期末-带答案.md` 第 629–683 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：用信号量实现单双号限行（PV 操作填空）

第八题（10分）
某个城市为了解决市中心交通拥堵的问题，决定出台一项交通管制措施，对进
入市中心区的机动车辆实行单双日限制行驶的办法。具体要求是，逢单日，只允许
车辆牌号号码为单数的机动车进入市中心区；同样，逢双日，只允许车辆牌号号码
为双数的机动车进入市内中心区。有一个进入市中心区的交通路口，进入该路口的
道路有一条，离开该路口的道路有两条，其中一条是通往市中心区的道路，而另一
条是绕过市中心区的环路，在进入路口处设置了自动识别车辆牌号的识别设备与放
行栅栏控制设备。在单日，遇到单号车辆进入路口车辆号码识别区，号码识别设备
打开通往市中心区道路的放行栅栏；而遇到双号车辆，则打开绕过市中心区环路的
放行栅栏。反之亦然。显然，只有在该路口车辆号码识别区中无车时，才允许一辆
车进入车辆号码识别区。同时为了防止有车辆混过路口，两个放行栅栏平时处于关
闭状态，只有在车辆号码识别区中的车辆已被识别出单双号之后，放行栅栏才会在
识别设备的控制下，打开对应的放行栅栏，在车辆通过之后，该放行栅栏自行关闭。
vehicle_n  int；         /* 车辆号码 */
检查车辆牌号线程T1：
  while (1) {
车辆到达识别区路口；
①
车辆进入号码识别区；
if  (vehicle_n == 奇数)
{    ②        }
   else
{    ③        }
 }；
市区放行栅栏线程T2：
  while (1) {
④
允许车辆进入市中心区；
⑤
 }；
21

<!-- ===== page 22 ===== -->

环路放行栅栏线程T3：
  while (1) {
⑥
允许车辆绕行环路；
⑦
}；
1）请设计若干信号量，给出每一个信号量的作用和初值。（3分）
参考答案：
Check：指示可否在车辆号码识别区中进入一辆汽车，由于只能进入一辆，其
初值为1。
Odd：指示汽车号码是否为奇数，其初值为0，表示不是奇数。
Even：指示汽车号码是否为偶数，其初值为0，表示不是偶数。
2）请将信号量上对应的PV操作填写在代码中适当位置。（7分）
  参考答案：
① P(Check)；
② V(Odd)；
③ V(Even)；
④ P(Odd)；
⑤ V(Check)；
⑥ P(Even)；
⑦ V(Check)；

---

### 2014期末-带答案 · 第一题 19

> 出处：`原文/期末/2014期末-带答案.md` 第 272–298 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：Pthread_detach 与 Pthread_create 用法

19. 对于如下C语言程序：
#include "csapp.h"
void *thread (void * arg)
{
       printf("Hello World") ;
       Pthread_detach(pthread_self()) ;
}
int main(void)
{
8

<!-- ===== page 9 ===== -->

       pthread_t tid;
       int sta ;
       sta = Pthread_create(&tid, NULL, thread, NULL);
       if (sta==0)
            printf("Oops, I can not create thread\n");
       exit(NULL);
}
在上述程序中，Pthread_detach函数的作用是(      )
A．使主线程阻塞以等待线程thread结束
B．线程thread运行结束后会自动释放所有资源
C．线程thread运行后主动释放CPU给其他线程
D．线程thread运行后成为僵尸线程
【答案】B
【说明】考查对Posix线程包Pthreads函数功能的理解。

---

### 2014期末-带答案 · 第一题 20

> 出处：`原文/期末/2014期末-带答案.md` 第 299–321 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：并发轨迹线安全/不安全判定

20. 两个线程中共享如下一段C代码：
         for (j = 0;  j < N;  j++)
                count + = 2;
假设其对应的汇编代码如下：
    movq  (%rdi), %rcx
    testq %rcx,%rcx
    jle   .L2                       Hi
    movl  $0, %eax
.L3:
    movq  count(%rip),%rdx       Li
    addq  $2, %rdx                 Ui
    movq  %rdx, count(%rip)      Si
addq  $1, %rax
    cmpq  %rcx, %rax              Ti
    jne   .L3
.L2:
请问在下列指令顺序对应的轨迹线中，哪一个是安全轨迹线？(      )
A. H1，H2，L2，L1，U2，U1，S1，S2，T1，T2
B. H1，L1，U1，H2，L2，S1，T1，U2，S2，T2
C. H2，L2，U2，H1，S2，L1，T2，U1，S1，T1
D. H2，L2，H1，L1，U1，U2，S2，T2，S1，T1
【答案】Ｃ
【说明】考查两个并发线程指令执行序列是否会导致不安全轨迹线。

---

### 2014期末-带答案 · 第九题

> 出处：`原文/期末/2014期末-带答案.md` 第 792–846 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：水果盘问题的信号量设计与 PV 填空

第九题（10分）并发
桌子上有一个水果盘，能容纳一个水果。一家四口人：爸爸、妈妈、儿子、女
儿。爸爸专门往盘子里放苹果，妈妈专门往盘子里放桔子；儿子专等盘子里的苹果
吃，女儿专等盘子里的桔子吃。
dad() {
   while(1) {
      准备好一个苹果；
          ①
      往果盘中放苹果；
          ②
   }
}
mom() {
   while(1) {
      准备好一个桔子；
          ③
      往果盘中放桔子；
          ④
   }
}
boy() {
   while(1) {
          ⑤
      从果盘中拿走苹果；
          ⑥
      吃苹果；
   }
}
girl() {
   while(1) {
          ⑦
      从果盘中拿走桔子；
          ⑧
      吃桔子；
   }
}
26

<!-- ===== page 27 ===== -->

1．(2分)请设计若干信号量，给出每一个信号量的作用和初值。
参考答案（答对两条给2分）：
plate：互斥信号量，标识能否往果盘中放入水果，其初值为1。
apple：信号量，标识果盘中是否有苹果，其初值为0。
orange：信号量，标识果盘中是否有桔子，其初值为0。
2．(8分)请将信号量上对应的PV操作填写在代码中适当位置。
  参考答案：
①P(plate)；
②V(apple)；
③P(plate)；
④V(orange)；
⑤P(apple)；
⑥V(plate)；
⑦P(orange)；
⑧V(Plate)；

---

### 2015期末-20160104-带答案 · 第一题 19

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 262–293 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：多线程可共享的变量（全局/静态局部）

19. 有如下代码：
int counter = 0;
void * thread(void * vargp)
{
  intthread_var = ((int *) vargp);
  staticintthread_counter = 0;
  thread_internal(thread_var);
  thread_counter ++;
8

<!-- ===== page 9 ===== -->

  return NULL;
}
int main (intargc, const char ** argv)
{
  int tid1, tid2;
  intvar = atoi(argv[1]);
  Pthread_create(&tid1, NULL, thread, (void *)var);
  Pthread_create(&tid2, NULL, thread, (void *)var);
  Pthread_join(tid1, NULL);
  Pthread_join(tid2, NULL);
  return 0;
}
则，线程 tid1 与线程 tid2 可以共享的变量是
A.  counter, var
B.  counter, thread_counter
C.  var, thread_counter
D.  thread_var, thread_counter
答案：B
（本题考查对线程中共享变量的概念的理解。因为 counter 是全局变量；
thread_counter是静态局部变量，所以两个线程可以共享它们）

---

### 2015期末-20160104-带答案 · 第一题 20

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 294–317 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量 PV 序列的死锁判定

20. 有四个信号量，初值分别为：a=1，b=1，c=1，d=1。
线程①  线程②  线程③
P(a);  P(d);  P(d);
P(d);  P(a);  P(c);
P(c);  P(c);  P(b);
P(b);  P(b);  P(a);
V(c);  V(d);  V(c);
V(b);  P(d);  V(b);
V(d);  V(a);  V(a);
9

<!-- ===== page 10 ===== -->

V(a);  V(b);  V(d);
V(c);
V(d);
下列哪两个线程并发执行时，一定不会发生死锁？
A.  ①, ②
B.  ①, ③
C.  ②, ③
D.  以上选项均不正确
答案：D
（本题考查对死锁概念的理解，本题的情况是任意两个线程并发执行，都会产生死
锁）

---

### 2015期末-20160104-带答案 · 第八题

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 686–770 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：双缓冲区生产者-消费者信号量设计与 PV 填空

第八题（10分）并发
有三个线程 PA、PB、PC 协作工作以解决文件打印问题：PA 将记录从磁盘读
入内存缓冲区 Buff1，每执行一次读一个记录；PB 将缓冲区 Buff1 的内容复制
到缓冲区Buff2，每执行一次复制一个记录； PC将缓冲区Buff2的内容打印出
来，每执行一次打印一个记录。缓冲区 Buff1 可以放 4 个记录；缓冲区 Buff2
可以放8个记录。请用信号量及P、V操作实现上述三个线程以保证文件的正确打
印。
PA() {
while(1)  {
      ①
    从磁盘读入一个记录
      ②
    将记录放入Buff1
      ③
  }
}
PB() {
while(1)  {
      ④
    从Buff1中取出一个记录
      ⑤
    将记录放入Buff2
      ⑥
}
}
PC() {
while(1)  {
      ⑦
    从Buff2中取出一个记录
      ⑧
    打印
}
}
1．请设计若干信号量，给出每一个信号量的作用和初值。
26

<!-- ===== page 27 ===== -->

 2．请将信号量上对应的 PV操作填写在代码中适当位置。注意：每一标号处可
以不填入语句（请标记成 X），或填入一条或多条语句。
标号  对应的操作
①
②
③
④
⑤
⑥
⑦
⑧
 答  案：（本大题总得分按四舍五入取整数）
27

<!-- ===== page 28 ===== -->

1．3分，答对1个0.5分
empty1，初值4；
full1，初值0；
empty2，初值8；
full2，初值0；
mutex1，初值1；
mutex2，初值2
2．7分
标号  对应的操作
①    X
P(&empty1);
②  P(&mutex1);
注意：顺序不能错，各0.5分
V(&full1);
③  V(&mutex1);
各0.5分
P(&full1);
④  P(&mutex1);
注意：顺序不能错，各0.5分
P(&empty2);
⑤  P(&mutex2);
注意：顺序不能错，各0.5分
V(&mutex2)
⑥  V(&full2)
各0.5分
P(&full2);
⑦  P(&mutex2);
注意：顺序不能错，各0.5分
V(&mutex2)
⑧  V(&empty2)
各0.5分

---

### 2016期末-带答案 · 第一题 19

> 出处：`原文/期末/2016期末-带答案.md` 第 251–256 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：基于进程的并发服务器父子资源共享关系

19. 下列关于“基于进程的并发服务器”的叙述中，哪一个是错误的？
A. 父子进程共享文件表
B. 父子进程共享文件描述符
C. 父子进程不共享用户地址空间
D. 进程控制和进程间通信开销大
答案：B（考核对基于进程的并发服务器优缺点的理解）

---

### 2016期末-带答案 · 第一题 20

> 出处：`原文/期末/2016期末-带答案.md` 第 257–285 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量 PV 下多线程输出的可能性

20. 请阅读如下代码：
sem_t s;
int main()
{
int i;
pthread_t tids[3];
sem_inti(&s, 0, 1);
for (i=0; i <3; i++) {
    pthread_create(&tids[i], NULL, justdoit, NULL);
}
for (i=0; i <3; i++) {
    pthread_join(&tids[i], NULL);
}
return 0;
}
int j=0;
void *justdoit(void *arg)
{
    P(&s);
j = j + 1;
    V(&s);
printf(“%d\n”, j);
}
  下列哪一个输出结果是不可能的？
A. （1，3，2）
B. （2，3，2）
C. （3，3，2）
D. （2，1，2）
答案：D（本题考查对多线程、信号量使用的掌握）

---

### 2016期末-带答案 · 第八题

> 出处：`原文/期末/2016期末-带答案.md` 第 751–815 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：多线程 cnt++ 竞态分析与 PV 实现司机售票员同步

 第八题（12分）
1/*. 请Gl阅ob读al下 s列ha代re码d bvaadrcianbtl.ec ：*/
vi{on lta tmialien (lionntg  acrngtc ,=  c0h;a r/ ** *Caorugnvt)e r */
            lpnotinhtgre ernasid t_=et r astt;iodi 1(,a rtgivd[21;]) ;
            PPPttthhhrrreeeaaaddd___ccjrroeeiaantt(eet((i&&dtt1ii,dd 12N,,U  LNNLUU)LL;LL ,,  tthhrreeaadd,,  &&nniitteerrss));;
            P/it*fh  rC(ehcaendct_k j !or=ie ns((u2tl it*d  2*n,/i t  NeUrLsL)));
            e    l  s  epp rr iinnttff((""BOOKO Mc!n tc=n%tl=d%\lnd"\, nc"n, t)cn;t );
 }     exit(0);
/v{*o   iTdh r*etahdr eraodu(tvionied  **/v a rgp)
         lfoonrg  (ii,  =n i0t;e ris  <=  n*i(t(elrosn;g  i*+)+v)a rgp);
   }        r  e t ucrnnt +N+U;L L;
 运li行nu后x>可 .能/b产ad生cn如t 下10结00果0 ：
O或lKi者 ncu：nxt> = 2.0/0b0a0d cnt 10000
Bl OiOnMu!x >c  nt=13051
为什么会产生不同的结果？请分析产生不同结果的原因。
24

<!-- ===== page 25 ===== -->

2.某辆公交车的司机和售票员为保证乘客的安全，需要密切配合、协调工作。司
机和售票员的工作流程如下所示。请编写程序，用P、V操作来实现司机与售票员
之间的同步。
      司机进程：                 售票员进程：
         while(1) {                 while(1) {
            ①                          ⑤
启动车辆；                   关门；
            ②                          ⑥
正常行驶；                   报站名或维持秩序；
            ③                          ⑦
到站停车；                   到站开门；
            ④                          ⑧
         }                            }
（1）请设计若干信号量，给出每一个信号量的作用和初值。
（2）请将信号量对应的PV操作填写在代码中适当位置。
注：每一标号处可以不填入语句（请标记成 X），或填入一条或多条语句。
标号  对应的操作
①
②
③
④
⑤
⑥
⑦
⑧
答案：
25

<!-- ===== page 26 ===== -->

1. （4分）
cnt++ 在汇编里会被分成加载、更新、写回三个步骤（2分）。线程1把cnt读
入寄存器，寄存器加1，在未写回时，若线程2把cnt读入自己的寄存器，寄存
器加1，最终两个线程都是把cnt+1写入cnt，这就造成了错误。（2分）
2. （8分）
（1）设置两个信号量s1=0、s2=1（2分）。s1用于司机进程是否能启动车辆（1
分），s2用于售票员进程是否能开门（1分）。
（2） ① P(s1)
② X
③ X
④ V(s2)
⑤ X
⑥ V(s1)
⑦ P(s2)
⑧ X
评分：每空0.5分，共4分。

---

### 2017期末-无答案 · 第一题 19

> 出处：`原文/期末/2017期末-无答案.md` 第 209–215 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：死锁定义、信号量顺序与线程安全

19. 下列关于死锁的叙述中，不正确的是：
A. 所谓死锁是指一组线程被阻塞，等待一个永远不会为真的条件
B. 在用信号量及 PV 操作解决生产者消费者问题（多个缓冲区、多个生产者，多
个消费者）时，如果先给缓冲区加锁 P(&sp->mutex)，再申请可用的缓冲区槽
P(&sp->slots)；则可能出现死锁
C. printf()是线程安全函数
D. 在信号处理函数中使用printf()不会导致死锁

---

### 2017期末-无答案 · 第一题 20

> 出处：`原文/期末/2017期末-无答案.md` 第 220–221 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：主线程与线程1交错执行的输出种类

20. 某s i{  进en mt程_ ipsf}f的tmnteoo  athmrr主si r_  pen线iei((tm(;aniih程;)di== r  _t00和et(;;a对 &  dtsii_等ie<<cdm33线rs,;;e程[   a30iit的],++e; ++代(1)) &码)  t;{{i如   d 下s[所i]示,： N ULL, thread, NULL);
 A    . 1执1} iv{}行 no   ti上  d}rPyVp述y e( (r  *t&=&i代 =tus snp h码reyett1rnm mfh后B5e ))(-r.;a0;;" ，e d ;% 3 a1 会d; d2( \_产 vnjo"生 oi,id多 n y (少 *)&a;种tr ig不Cd).s同  [1的i3]输 , 出 N？UL  L);D . 14

---

### 2017期末-无答案 · 第八题

> 出处：`原文/期末/2017期末-无答案.md` 第 524–575 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：并发 echo 服务器 P/T 代码找错与信号量同步

1.  基于进程的并发Echo服务器代码（简称P代码）和基于线程的并发Echo服
  务器代码（简称T代码）如下所示：
P#i代nc码l：ud e “csapp.h”
void ec ho(int cnnfd);
v{o  id sigchld_handler(int sig)
if (waitpid(-1, 0, WNOHANG) > 0)
return;;   }
i{n  ti nmta ilni(sitnetn fadr,g cc,o ncnhfadr;  **argv)
      ssotcrkulcetn _sto ccklaidednrt_lsetno;ra ge clientaddr;
      lwhiislteen f(d1 )=  {O pen_listenfd(argv[1]);
            ccloinennftdl e=n  A=c cseipzte(olfi(sstternufcdt, (sSoAc*k)a&dcdlri_esnttoardadgre,)&;cl ientlen);
      if (Fork() == 0) {
 echo(connfd);
 Close(connfd);
      }  exit(0);
      Close(connfd);
   }
}
19

<!-- ===== page 20 ===== -->

T#vv i{               ioon 代        niit  ssplwi码cdd   ottihnl m   ：crhsitccu*aekurtl lodtic lceeelinehnhetan ien r(on df(snf“ei(_s_d1ttdcanitot )el1sdtn c = ne a( t=ckt {fnpva  laiO dA porciddp,c=.igned;e chdcn nrn ce” ,fst__op* d ilslntvc)zetin(ah;enosflrao ;rtdigrfae 1sp (gn;t)*sef e;*t dnar c(fruladgcir,vteg () nvSs t[Aoa1*cd])kd)&ar;cd; ld ire_nsttaodrdarg,e )&;c lientlen);
  } v{     } 问       o          ：i      }d iPeCr以   ntcleP*上thhottt rosuhhPce(errroac(n代eendoc aan_noN码ddfdnnU_(和defnLcv2tdfLro a2d;Tei=c)2 ad代 h;)t *(; 码e*(p (v(t中&aihtr存nrigte在dp a,)*d几  )_N处vsUae错LrlLgf误,p( ，))t;)请h; r 指e a出d出, 错co的n位nf置d1（)请; 按照①、②等
符        号标注位置），解释出错的原因并给出2修0 正错误的解决方案。

<!-- ===== page 21 ===== -->

2.  假设有3个线程，代码如下所示。已声明了三个信号量s1、s2和s3，其初
值分别为1、0、0。请将信号量S1、S2、S3对应的P()和V()操作填写在
三个线程中的标号处（每空至多填写1个操作），要求三个线程并发执行的结
果只能是x = 10。
x = 1;
void thread1()
{
①
x = x * 5;
②
}
void thread2()
{
③
x = x + 3;
④
}
void thread3()
{
  ⑤
x = x / 2;
21
⑥
}

---

### 2018期末-带答案 · 第一题 13

> 出处：`原文/期末/2018期末-带答案.md` 第 223–228 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：线程安全与可重入的包含关系

13. 下面关于线程安全和可重入的描述中，哪一个是正确的？
A. 如果一个函数的所有参数都是值传递的且无返回值，该函数一定是可重入的
B. 函数的可重入版本一定比不可重入版本高效
C. 可重入函数一定是线程安全的
D. 以上说法都不正确
答案：C

---

### 2018期末-带答案 · 第一题 14

> 出处：`原文/期末/2018期末-带答案.md` 第 229–234 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程与线程的资源共享与上下文切换

14. 下列关于进程与线程的描述中，哪一个是不正确的？
A. 一个进程可以包含多个线程
B. 进程中的各个线程共享进程的代码、数据、堆和栈
C. 进程中的各个线程拥有自己的线程上下文
D. 线程的上下文切换比进程的上下文切换快
答案：B

---

### 2018期末-带答案 · 第一题 15

> 出处：`原文/期末/2018期末-带答案.md` 第 235–256 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：对等线程引用的变量集合判定

15. 给定下列代码片段：
char **ptr;  /* global var */
int main(int main, char *argv[]) {
  long i;  pthread_t tid;
  char *msgs[2] = {" Hello from foo", " Hello from bar" };
    ptr = msgs;
    for (i = 0; i < 2; i++)
        Pthread_create(&tid, NULL, thread,(void *)i);
    Pthread_exit(NULL);}
void *thread(void *vargp)
{
  long myid = (long)vargp;
  static int cnt = 0;
  printf("[%ld]:  %s (cnt=%d)\n", myid, ptr[myid], ++cnt);
  return NULL;
}
下列哪一组变量集合是对等线程1引用的？
A. ptr，cnt，i.m，msgs.m，myid.p0，myid.p1
B. ptr，cnt，msgs.m，myid.p0
C. ptr，cnt，msgs.m，myid.p1
D. ptr，cnt，i.m，msgs.m，myid.p1
答案：C

---

### 2018期末-带答案 · 第七题 2-4

> 出处：`原文/期末/2018期末-带答案.md` 第 727–807 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：i++/j++ 竞态的输出可能性与信号量死锁

2.  （4分）请回答该程序是否有可能输出如下结果，并简述原因。
(a) 2000, 2000
(b) 1500, 1500
(c) 1000, 1000
(d) 2, 2
3.  （2分）卜廷江同学在学习了信号量之后，决定要让程序能稳定输出2000, 2000，
于是对程序进行了如下改写。
1.  #include <stdio.h>
2.  #include <pthread.h>
3.  int i = 0;
4.  int j = 0;
5.  sem_t si;
6.  sem_t sj;
7.  void *do_stuff1(void * arg __attribute__((unused))) {
8.  int a;
9.    for (a = 0; a < 1000; a++) {
10. P(&si);
11. P(&sj);
12. i++;
13. j++;
14. V(&si);
15. V(&sj);
16. }
17. return NULL;
18. }
19. void *do_stuff2(void * arg __attribute__((unused))) {
20. int a;
21. for (a = 0; a < 1000; a++) {
22. P(&sj);
23. P(&si);
24. j++;
25. i++;
26. V(&si);
27. V(&sj);
28. }
25

<!-- ===== page 26 ===== -->

29. return NULL;
30. }
31. int main() {
32. pthread_t tid1, tid2;
33. Sem_init(&si, 0, 1);
34. Sem_init(&sj, 0, 1);
35. pthread_create(&tid1, NULL, do_stuff1, NULL);
36. pthread_create(&tid2, NULL, do_stuff2, NULL);
37. pthread_join(tid1, NULL);
38. pthread_join(tid2, NULL);
39. printf("%d\n", i);
40. return 0;
41. }
请问卜廷江同学的程序有什么潜在问题？为什么？
4.  （2 分）如果对卜廷江同学的程序改动一处数字来消除上述问题，同时仍然保
证输出结果稳定为2000, 2000，应该如何改动？
回答：将_____（填行号）行的_________（填数字）改为__________（填数字）。
答案
1.  (a)(c)(d)
(b)(e)(d)
(a)(d)(c)
（写错任意一个不得分）
2.  (a) 可能，do_stuff俩函数全串行执行即可
(b) 可能，do_stuff1先执行了读取i的操作，然后do_stuff2执行500次循
环，接下来do_stuff1写回i完成该次循环，则i变成1，j变成501。之后
do_stuff2 执行了读取 j 的操作，然后 do_stuff1 执行 500 次循环，接下来
do_stuff2完成该次循环，则i变成501，j变成501。然后两个线程串行执行
剩下的499次循环即可。
(c) 不可能。可以证明程序结束时一定有i+j>=2002。只能当某线程先执行了
读i (j)操作，之后另一个线程执行了若干次i++ (j++)，然后h该线程执行
了写i (j)操作可以将另一个线程的i++ (j++)效果抵消掉。这个过程中，抵
消掉的加法次数一定不会多于执行的加法次数。同时，由于两个线程交错执行
i++和j++的顺序相反，所以头尾一定存在一次i++或j++无法被抵消，因此增
加的总次数大于等于2002。
(d) 不可能。理由同上。
26

<!-- ===== page 27 ===== -->

（前一半对，后一半解释大致差不多得分，否则不得分。）
3.  死锁。两个线程分别执行到11行和23行时会发生。
4.  将33行或34行中的1改为任意大于2的数。（错任意一空不得分）

---

### 2019、2020期末-答案解析 · 2020 选择题 22

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 67–68 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：线程间共享与私有数据

22. C。a)是共享的（在数据段），b)也是共享的（栈是私有的），c)是共享的，属于书上原话，或
者从同一进程的概念中读解出，d)是特别的上下文，是私有的。所以有3个。

---

### 2019、2020期末-答案解析 · 2020 选择题 23

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 73–77 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：锁/解锁/信号顺序的最优全序

23. C。此题意义不大。主要的困难在于最终的正确顺序并不是确定的一个全序，所以需要找
一个“最优”的全序。大概估计一下，𝐿2,𝑈2,𝑆2和𝐿4,𝑈4,𝑆4之间不能有重叠，𝐿1,𝑈1,𝑆1和
𝐿3,𝑈3,𝑆3之间亦然，所以可能是
𝐿2,𝐿1,𝑈1,𝑆1,𝐿3,𝑈2,𝑆2,𝐿4,𝑈4,𝑈3,𝑆4,𝑆3.
数出逆序数为12。实际上，合法的全序只有十几种，可以枚举验证答案正确性。

---

### 2019、2020期末-答案解析 · 2020 选择题 24

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 78–80 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：pthread_exit 与 exit 的差别

24. B。注意主线程如果调用诸如pthread_exit的函数退出，是不会引发其他线程退出的，所
以A为一错误描述。但是如果主线程调用了exit（或者return）,则整个进程都会结束，
自然其他线程也结束。

---

### 2019、2020期末-答案解析 · 2020 选择题 25

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 81–83 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：加锁顺序相反导致的死锁

25. B。首先1和2分别获得a和c的锁，然后2再获得b的锁，1和3分别等d的锁和a的锁。
此时如果2释放c和b的锁，1和3无论如何都将出现互相等待（a、d）的情况，因此发生了
死锁。

---

### 2019、2020期末-答案解析 · 2020 解答题五

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 143–152 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：哲学家就餐死锁与信号量实现互斥

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

---

### 2019、2020期末-答案解析 · 2019 选择题 8

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 170–170 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：并行与并发的关系

8. 未解之谜，CD。并行一定并发。

---

### 2019、2020期末-答案解析 · 2019 选择题 18

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 189–190 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：线程安全与可重入函数

18. B。保持跨越多个调用的状态的函数不是线程安全的，而C项是隐式可重入函数，如果合理
使用就是线程安全的。

---

### 2019、2020期末-答案解析 · 2019 选择题 19

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 191–192 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：对等线程赋值与 accept 的竞争

19. C。否则会在对等线程的赋值和主线程的accept之间引入竞争，如果赋值在accept之后
完成，描述符值就错了。

---

### 2019、2020期末-答案解析 · 2019 选择题 20

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 193–194 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：sem 与 pthread_mutex 阻塞范围

20. D。D是超纲选项，sem型指令会阻塞整个进程，而pthread_mutex型指令只会阻塞相应
线程，后者的效率更高。A、B、C都是容易看出正确的，所以可以用排除法做出。

---

### 2019、2020期末-答案解析 · 2019 解答题六

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 270–275 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：读者优先读写锁的竞争

解答题六
1. 7, 14, 7, 2, 0。这时两个读者都在正常读，因为是读者优先，所以写者在14行阻塞等
待，写锁的值是0。
2. 14, 7, 3, 0。完全同理。
3. 会出现竞争的错误。例如两位读者同时进入，由于readcnt的写不是原子的，可能导致进入
后readcnt=1，当一位读者离开后，写者就错误进入了。

---

### 2019期末-无答案 · 第一题 8

> 出处：`原文/期末/2019期末-无答案.md` 第 99–109 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程并发与并行的区别

8.  考虑4个具有如下开始和结束时间并运行在不同处理器上的进程，
进程  开始时间  结束时间  运行处理器
A  5  7  P0
B  2  4  P1
C  3  6  P0
D  1  8  P1
下面那个判断是正确的。
A. 进程A和B不是并发运行的，但是并行运行的；
B. 进程A和C是并发运行的，并且是并行运行的；
C. 进程B和D是并发运行的，但不是并行运行的；
D. 进程A和D是并发运行的，并且是并行运行的；

---

### 2019期末-无答案 · 第一题 17

> 出处：`原文/期末/2019期末-无答案.md` 第 183–195 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：死锁现象的判定

17. 并发程序执行时会遇到下列各种情况：
①   程序执行结果的正确性依赖于一个线程要在另一个线程到达y点之
前到达其控制流的x点
② 程序员使用P和V操作顺序不当
③ 外部事件和/或系统调度决策阻止了任务进度
④ 不合理的资源分配策略导致程序难以向前运行
⑤ 程序的执行结果取决于系统的调度决策
⑥ 在信号处理函数中调用printf()
请问下列哪些情况表示可能产生死锁现象？
A.  ①、②和⑤
B.  ②、③和④
C.  ③、④和⑥
D.  ②、④和⑥

---

### 2019期末-无答案 · 第一题 18

> 出处：`原文/期末/2019期末-无答案.md` 第 196–202 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：线程安全与可重入函数

18. 称一个函数为线程安全的（thread-safe），当且仅当该函数被多个并
发线程反复调用时会一直产生正确的结果。下列哪些函数不是线程安全
的？
A.  利用P、V操作保护了共享变量的函数
B.  保持跨越多个调用的状态的函数
C.  包括了调用者传递存放结果变量的地址的函数
D.  可重入函数

---

### 2019期末-无答案 · 第一题 19

> 出处：`原文/期末/2019期末-无答案.md` 第 203–228 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：多线程 echo 服务器中 connfd 的竞争

19. 在以下基于线程的并发Echo服务器代码中，哪一个代码片段会潜在引发
不正确的程序执行结果？
A.  int main(int argc, char **argv)
{                              /*假设有配对的”}”
        int listenfd, connfd;
5

<!-- ===== page 6 ===== -->

        socklen_t clientlen;
        struct sockaddr_storage clientaddr;
        pthread_t tid;
B. listenfd = Open_listenfd(argv[1]);
C. while (1) {
      connfd = Accept(listenfd, (SA *) &clientaddr,
&clientlen);
      Pthread_create(&tid, NULL, thread, &connfd);
    }
D. void *thread(void *vargp)
{
      int connfd = *((int *)vargp);
      Pthread_detach(pthread_self());
      echo(connfd);
      Close(connfd);
      return NULL;
}

---

### 2019期末-无答案 · 第一题 20

> 出处：`原文/期末/2019期末-无答案.md` 第 229–236 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量与 P/V 操作语义

20. 下列关于信号量及P、V操作的叙述中，哪一个是不正确的？
A.  信号量是一个非负整数，对信号量只能执行P操作和V操作
B.  当信号量的值为0时，调用P操作的线程被挂起
C.  P(s)的实现代码中语句：while (s == 0)  wait(); s--; 应
该由内核保证其执行的不可分割性
D.  在保护临界区的解决方案中使用 sem_wait()和 sem_post()比使
用 pthread_mutex_lock()和 pthread_mutex_unlock()性能
好

---

### 2019期末-无答案 · 第七题

> 出处：`原文/期末/2019期末-无答案.md` 第 530–572 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：第一类读者-写者问题的执行流程分析

解决第一类读者-写者问题的代码如下：
int readcnt;    /* Initially 0 */
sem_t mutex, w; /* Both initially 1 */
void reader(void)
{
(1)    while (1) {
(2)      P(&mutex);
(3)      readcnt++;
(4)      if (readcnt == 1) /* First in */
(5)        P(&w);
(6)      V(&mutex);
(7)         /* Reading happens here, need 7 time unit */
(8)      P(&mutex);
(9)      readcnt--;
(10)     if (readcnt == 0) /* Last out */
(11)        V(&w);
(12)     V(&mutex);
        }
}
void writer(void)
{
(13)  while (1) {
(14)    P(&w);
(15)       /* Writing here, need 8 time unit */
(16)    V(&w);
      }
}
假设有5个读者或写者到来，到达时刻和所需的时间如下：
线程  到达时刻  读写时间
R1  0  7
W1  1  8
R2  2  7
W2  4  8
R3  5  7
注意，为简单起见，只考虑读写时间，忽略所有其他时间（包括代码中其
他语句的执行时间、线程切换、调度等等），亦假设没有更多的读者或写者或
其他线程。
（1）在时刻3时，R1、W1和R2所处的位置，请标出对应的代码行号。此刻，
readcnt和w的值分别是多少？R1: ；W1: ；R2: ；readcnt: ；w: 。
（2）在时刻6时，W2和R3所处的位置，请标出对应的行号。此刻，readcnt
和w的值分别是多少？W2: ；R3: ；readcnt: ；w: 。
（3）如果不使用P(&mutex)和V(&mutex)，程序执行会不会出错？如果出
错，会出什么错？

---

### 2020期末-无答案 · 第一题 22

> 出处：`原文/期末/2020期末-无答案.md` 第 209–214 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：同进程内不同线程共享的资源

22.  同一个进程内的不同线程共享以下几项？
a)  函数体内部的静态变量
b)  堆
c)  文件描述符表
d)  条件码
A.  1  B. 2   C. 3   D. 4

---

### 2020期末-无答案 · 第一题 23

> 出处：`原文/期末/2020期末-无答案.md` 第 215–220 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：指令重排以消除共享变量竞争

23.  令 Li表示加载共享变量到寄存器的指令，Ui表示更新寄存器的指令，Si表示将更新值
存回到共享变量的指令，指令L1、S1、U3、S3操作共享变量cnt，指令L2、S2、L4、S4
操作共享变量num，假定每次只允许交换相邻的两条指令，则将下列指令序列变为正确
的至少需要交换多少次：
L2、L1、U1、L3、L4、U4、U3、S1、U2、S4、S3、S2
A.10   B.11   C.12   D.13

---

### 2020期末-无答案 · 第一题 24

> 出处：`原文/期末/2020期末-无答案.md` 第 225–242 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：主线程退出导致对等线程终止

24.  以下程序在输出有限行之后就终止了，请问最有可能的原因是（假定所有函数都正常执
行）
#include "csapp.h"
void *thread(void *dummy){
while (1){
printf("hello, world!\n");
Sleep(1);
}
}
int main(){
pthread_t tid;
Pthread_create(&tid, NULL, thread, NULL);
Sleep(3);
}
A.  主线程结束必然引发所有对等线程结束
B.  主线程结束时调用了_exit导致进程结束
C.  主线程结束后，内核发送SIGKILL杀死进程
D.  主线程结束后，内核观察到对等线程运行时间过长，将其杀死

---

### 2020期末-无答案 · 第一题 25

> 出处：`原文/期末/2020期末-无答案.md` 第 243–256 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量执行轨迹中的死锁

 25.  有四个信号量，初值分别为：a=1,  b=1,  c=1,  d=1
  线程1：  线程2：  线程3：
① P(a);   ⑨ P(c);   P(d);
② P(b);  ⑩ P(b);  ⑮ P(a);
③ P(d);    V(c);  ⑯ V(d);
④ P(c);  ⑪ V(b);  ⑰ P(b);
⑤⑥  VV((da));;   ⑫  VP((aa));;     ⑱  VV((ba));;
⑦ V(b);    ⑬   ⑲
⑧ V(c);  ⑭ ⑳
 上面的程序执行时，下列哪一个执行轨迹执行后已经出现死锁?
A. ⑨①⑩②
B. ①⑨⑩②⑪⑮
DC..  ①①②⑨③⑩④⑮⑨②⑯
  ⑮ ⑯⑮

---

### 2020期末-无答案 · 第六题

> 出处：`原文/期末/2020期末-无答案.md` 第 498–627 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：圆桌信号量：死锁、加锁顺序与二元信号量实现

第六题（10分）
1. 火锅洞洞主终于要请吃火锅啦！由于防疫规定，洞主决定分批邀请，Alice、
Bob、……、Zach这26位同学顺理成章地成为了第一批受到邀请的同学。他们围坐在
一张圆桌旁，按照首字母顺序排列（即Alice的右边是Bob，Bob的右边是
Carol，……，Zach的右边是Alice）。吃饭之前，洞主想要验证他们的身份，他提出了
这样的要求：
1） 每位同学有一个编号，即字母序号减1，也就是说，Alice是0号，Bob是1
号，以此类推。
2） 每位同学需要同时拿着旁边两位同学的手机去找洞主（不必带上自己的手
机），按照洞主的要求在树洞里发信息以验证身份。
3） 可以同时有多位同学找洞主验证（也就是说，Alice需要拿着Zach和Bob的
手机找洞主，并且在同一时间，Bob也可以拿着Alice和Carol的手机找洞
主。但是，如果Alice还没同时拿到Zach和Bob的手机，就只能坐在座位上
等待。）
所幸，在座有多位字母君学过ICS，他们决定采用信号量解决问题。
1.1 Alice给出了这样的代码，其中thread函数的参数指明了字母君的编号：
1.  #include "csapp.h"
2.  #define N 26
3.  #define UP(i) ((i + 1) % N)
4.  #define DOWN(i) ((i - 1 + N) % N)
5.  sem_t sem[N];
6.
7.  void *thread(void *i){
8.      int num = (int)i;
9.      P(&sem[UP(num)]);
10.     P(&sem[DOWN(num)]);
11.
12.     /* verify identity */
13.
14.     V(&sem[UP(num)]);
15.     V(&sem[DOWN(num)]);
16. }
17. int main(){
18.     for (int i = 0; i < N; i++)
19.         Sem_init(&sem[i], 0, 1);
20.     pthread_t tid[N];
21.     for (int i = 0; i < N; i++)
22.         Pthread_create(&tid[i], NULL, thread, (void *)i);
23.     Pthread_exit(0);
24. }
Bob一看，皱起了眉头。请问这段代码可能会发生什么问题（用一个专用名词表
述即可）？
14

<!-- ===== page 15 ===== -->

1.2 Carol把thread函数换成了下面这样：
1.  void *thread(void *i){
2.      int num = (int)i;
3.      for (int i = 0; i < N; i++)
4.          P(&sem[i]);
5.      /* verify identity */
6.      for (int i = 0; i < N; i++)
7.          V(&sem[i]);
8.  }
Dave指出，这段代码固然正确，但是效率太低了，他认为只要把第3、4行的代
码换成一个P操作，把第6、7行的代码换成一个V操作，就能实现同样的效果。
请问Dave的方法是：
1.2.1 P操作：P(&sem[         ]);
1.2.2 V操作：V(&sem[         ]);
1.3 Eve看了Dave的方案还是摇头，这样执行效率太低了，没能利用同时可以有多位
同学找洞主验证的条件。借助“互斥锁加锁顺序规则”，他给出了自己的代码。你能
把代码补全吗？
1.  void *thread(void *i)
2.  {
3.      int num = (int)i;
4.      if (UP(num) < DOWN(num)){
5.          P(&sem[  A  ]);
6.          P(&sem[  B  ]);
7.      }
8.      else{
9.          P(&sem[  C  ]);
10.         P(&sem[  D  ]);
11.     }
12.     /* verify identity */
13.     V(&sem[UP(num)]);
14.     V(&sem[DOWN(num)]);
15. }
A:             B:             C:             D:
以上4空均填序号：
①  UP(num)
②  DOWN(num)
③  num
2. Hungary Alice发现自己没吃上第一场的火锅，一怒之下，给上面的26位字母君出了一
道难题：用二元信号量实现信号量（也就是值可以是任意非负整数的信号量）。精通ICS的
你自然认为这是小儿科，迅速补全了以下代码。
15

<!-- ===== page 16 ===== -->

1.  #include "csapp.h"
2.  typedef struct{
3.      int value;
4.      sem_t mutex;
5.      sem_t zero;
6.  } my_sem_t;
7.  void my_sem_init(my_sem_t *sem, unsigned int value){
8.      sem->value = value;
9.      Sem_init(&sem->mutex, 0,   A  );
10.     Sem_init(&sem->zero, 0,   B  );
11. }
12. void my_P(my_sem_t *sem){
13.     P(&sem->mutex);
14.     sem->value--;
15.     if (sem->value   C   0)
16.     {
17.           D  ;
18.           E  ;
19.     }
20.     else
21.         V(&sem->mutex);
22. }
23. void my_V(my_sem_t *sem){
24.     P(&sem->mutex);
25.     sem->value++;
26.     if (sem->value   F   0)
27.     {
28.         V(&sem->mutex);
29.         V(&sem->zero);
30.     }
31.     else
32.         V(&sem->mutex);
33. }
A:             B:             C:
D:             E:             F:
D和E请填序号：
①  P(&sem->mutex)
②  P(&sem->zero)
③  V(&sem->mutex)
④  V(&sem->zero)

---

### 2021期末-无答案 · 第一题 20

> 出处：`原文/期末/2021期末-无答案.md` 第 271–279 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程与线程的上下文、栈与地址空间

20.  下列关于C语言中进程模型和线程模型的说法中，错误的是：
A.每个线程都有它自己独立的线程上下文，包括线程 ID、程序计数器、条
件码、通用目的寄存器值等
B.每个线程都有自己独立的线程栈，任何线程都不能访问其他对等线程的栈
空间
C.不同进程之间的虚拟地址空间是独立的，但同一个进程的不同线程共享同
一个虚拟地址空间
D.一个线程的上下文比一个进程的上下文小得多，因此线程上下文切换要比
进程上下文切换快得多

---

### 2021期末-无答案 · 第六题

> 出处：`原文/期末/2021期末-无答案.md` 第 561–806 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：生产者-消费者：信号量解法与等待计数解法

第六题. 请结合教材第十二章“并发编程”的有关知识回答问题(15分)
“生产者-消费者”问题是并发编程中的经典问题。本题中，考虑如下场景：
a.  所有生产者和所有消费者共享同一个buffer
b.  生产者、消费者各有NUM_WORKERS个（大于一个）
c.  buffer的容量为BUF_SIZE，初始情况下buffer为空
d.  每个生产者向 buffer 中添加一个 item；若 buffer 满，则生产者等待
buffer中有空槽时才能添加元素
e.  每个消费者从 buffer 中取走一个 item；若 buffer 空，则消费者等待
buffer中有item时才能取走元素
1. 阅读以下代码并回答问题（代码阅读提示：主要关注producer和consumer
两个函数）
1. /* Producer–Consumer Problem (Solution 1) */
2.
3. #include "csapp.h"
4.
5. #define BUF_SIZE 3
6. #define NUM_WORKERS 50
7. #define MAX_SLEEP_SEC 10
8.
9. volatile
static int items = 0; /* How many items are there in t
he buffer */
10.
11.  static sem_t mutex; /* Mutual Exclusion */
12.  static sem_t empty; /* How many empty slots are there
in the buffer */
13.  static sem_t full;  /* How many items are there in the
 buffer */
14.
15.  static void sync_var_init() {
16.      Sem_init(&mutex, 0, 1);
17.
18.      /* Initially, there is no item in the buffer */
19.      Sem_init(&empty, 0, BUF_SIZE);
20.      Sem_init(&full, 0, 0);
21.  }
22.
23.  static void *producer(void *num) {
24.      ①;
25.      ②;
26.
27.      /* Critical section begins */
28.      Sleep(rand() % MAX_SLEEP_SEC);
29.      items++;
30.      /* Critical section ends */
31.
32.      V(&mutex);
33.      V(&full);
  16

<!-- ===== page 17 ===== -->

34.
35.      return NULL;
36.  }
37.
38.  static void *consumer(void *num) {
39.      ③;
40.      ④;
41.
42.      /* Critical section begins */
43.      Sleep(rand() % MAX_SLEEP_SEC);
44.      items--;
45.      /* Critical section ends */
46.
47.      V(&mutex);
48.      V(&empty);
49.
50.      return NULL;
51.  }
52.
53.  int main() {
54.      sync_var_init();
55.
56.      pthread_t pid_producer[NUM_WORKERS];
57.      pthread_t pid_consumer[NUM_WORKERS];
58.
59.      for (int i = 0; i < NUM_WORKERS; i++) {
60.          Pthread_create(&pid_producer[i], NULL, produce
r, (void *)i);
61.          Pthread_create(&pid_consumer[i], NULL, consume
r, (void *)i);
62.      }
63.
64.      for (int i = 0; i < NUM_WORKERS; i++) {
65.          Pthread_join(pid_producer[i], NULL);
66.          Pthread_join(pid_consumer[i], NULL);
67.      }
68.  }
a)  补全代码（请从以下选项中选择，可重复选择，每个1分，共4分）
①    （24行）
②    （25行）
③    （39行）
④    （40行）
选项：
A.  P(&mutex)
B.  P(&empty)
C.  P(&full)
b)  如果交换24行与25行（两个P操作），      （单选，2分）
A.  有可能死锁
B.  有可能饥饿
C.  既不会死锁，也不会饥饿
  17

<!-- ===== page 18 ===== -->

c)  交换32、33行（两个V操作）是否可能造成同步错误？    （2分）
A.  可能
B.  不可能
d)  rand函数是不是线程安全的？   （1分）
A.  是
B.  不是
28行与43行对rand函数的使用是否会导致竞争？   （1分）
A.  会
B.  不会
已知rand函数的实现如下
来源：
https://github.com/begriffs/libc/blob/master/stdlib.h
https://github.com/begriffs/libc/blob/master/stdlib.c
1.  #define RAND_MAX 32767
2.
3.  unsigned long _Randomseed = 1;
4.
5.  int rand() {
6.      _Randomseed = _Randomseed * 1103515425 + 12345;
7.      return (unsigned int)(_Randomseed>>16) & RAND_MAX;
8.  }
9.
10. void srand(unsigned int seed) {
11.     _Randomseed = seed;
12. }
2. 考虑“生产者-消费者”问题的另一种解法（代码阅读提示：12-69 行之外
均与上一种解法相同）
1.  /* Producer–Consumer Problem (Solution 2) */
2.
3.  #include "csapp.h"
4.
5.  #define BUF_SIZE 3
6.  #define NUM_WORKERS 50
7.  #define MAX_SLEEP_SEC 10
8.
9.  volatile
static int items = 0; /* How many items are there in t
he buffer */
10.
11. static sem_t mutex;                /* Mutual Exclusion */
12. static sem_t sem_waiting_producer; /* Wait for empty slots *
/
13. static sem_t sem_waiting_consumer; /* Wait for available ite
ms */
14.
15. volatile static int num_waiting_producer = 0;
16. volatile static int num_waiting_consumer = 0;
  18

<!-- ===== page 19 ===== -->

17.
18. static void sync_var_init() {
19.     Sem_init(&mutex, 0, 1);
20.
21.     Sem_init(&sem_waiting_producer, 0, ①);
22.     Sem_init(&sem_waiting_consumer, 0, ①);
23. }
24.
25. static void *producer(void *num) {
26.     P(&mutex);
27.     while (items == BUF_SIZE) {
28.         num_waiting_producer++;
29.         ②;
30.         ③;
31.         P(&mutex);
32.     }
33.
34.     /* Critical section begins */
35.     Sleep(rand() % MAX_SLEEP_SEC);
36.     items++;
37.     /* Critical section ends */
38.
39.     if (num_waiting_consumer > 0) {
40.         num_waiting_consumer--;
41.         V(&sem_waiting_consumer);
42.     }
43.     V(&mutex);
44.
45.     return NULL;
46. }
47.
48. static void *consumer(void *num) {
49.     P(&mutex);
50.     while (items == 0) {
51.         num_waiting_consumer++;
52.         ④;
53.         ⑤;
54.         P(&mutex);
55.     }
56.
57.     /* Critical section begins */
58.     Sleep(rand() % MAX_SLEEP_SEC);
59.     items--;
60.     /* Critical section ends */
61.
62.     if (num_waiting_producer > 0) {
63.         num_waiting_producer--;
64.         V(&sem_waiting_producer);
65.     }
66.     V(&mutex);
67.
68.     return NULL;
69. }
70.
71. int main() {
72.     sync_var_init();
73.
  19

<!-- ===== page 20 ===== -->

74.     pthread_t pid_producer[NUM_WORKERS];
75.     pthread_t pid_consumer[NUM_WORKERS];
76.
77.     for (int i = 0; i < NUM_WORKERS; i++) {
78.         Pthread_create(&pid_producer[i], NULL, producer, (vo
id *)i);
79.         Pthread_create(&pid_consumer[i], NULL, consumer, (vo
id *)i);
80.     }
81.
82.     for (int i = 0; i < NUM_WORKERS; i++) {
83.         Pthread_join(pid_producer[i], NULL);
84.         Pthread_join(pid_consumer[i], NULL);
85.     }
86. }
a)  补全代码（请从以下选项中选择，④⑤无需填写，每个 1 分，共 3 分）
①    （21、22行）
②    （29行）
③    （30行）
选项：
A.  0
B.  1
C.  P(&sem_waiting_producer)
D.  V(&mutex)
b)  如果27行和50行的while换成if，是否可能造成同步错误？
   （2分）
A.  可能
B.  不可能

---

### chap 11-12 解析 · 选择题 1

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 123–131 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程与线程模型：上下文、线程栈、地址空间

1.下列关于C语言中进程模型和线程模型的说法中，错误的是：

A.每个线程都有它自己独立的线程上下文，包括线程ID、程序计数器、条件码、通用目的寄存器值等

B.每个线程都有自己独立的线程栈，任何线程都不能访问其他对等线程的栈空间

C.不同进程之间的虚拟地址空间是独立的，但同一个进程的不同线程共享同一个虚拟地址空间

D.一个线程的上下文比一个进程的上下文小得多，因此线程上下文切换要比进程上下文切换快得多

---

### chap 11-12 解析 · 大题 小题1

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 137–363 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：生产者-消费者信号量解法1：代码与子问题

大题

并发编程（15分）

“生产者-消费者”问题是并发编程中的经典问题。本题中，考虑如下场景：

1.  所有生产者和所有消费者**共享同一个buffer**

2.  生产者、消费者各有NUM_WORKERS个（**大于一个**）

3.  buffer的容量为BUF_SIZE，**初始情况下buffer为空**

4.  每个生产者向buffer中添加一个item；若buffer满，则生产者等待buffer中有空槽时才能添加元素

5.  每个消费者从buffer中取走一个item；若buffer空，则消费者等待buffer中有item时才能取走元素

<!-- -->

1.  阅读以下代码并回答问题（**代码阅读提示：主要关注producer和consumer两个函数**）

<!-- -->

1.  */\* Producer–Consumer Problem (Solution 1) \*/*

2.  

3.  \#include "csapp.h"

4.  

5.  \#define BUF_SIZE 3

6.  \#define NUM_WORKERS 50

7.  \#define MAX_SLEEP_SEC 10

8.  

9.  volatile static int items = 0; */\* How many items are there in the buffer \*/*

10. 

11. static sem_t mutex; */\* Mutual Exclusion \*/*

12. static sem_t empty; */\* How many empty slots are there in the buffer \*/*

13. static sem_t full;  */\* How many items are there in the buffer \*/*

14. 

15. static void sync_var_init() {

16.     Sem_init(&mutex, 0, 1);

17. 

18.     */\* Initially, there is no item in the buffer \*/*

19.     Sem_init(&empty, 0, BUF_SIZE);

20.     Sem_init(&full, 0, 0);

21. }

22. 

23. static void \*producer(void \*num) {

24.     ①;

25.     ②;

26. 

27.     */\* Critical section begins \*/*

28.     Sleep(rand() % MAX_SLEEP_SEC);

29.     items++;

30.     */\* Critical section ends \*/*

31. 

32.     V(&mutex);

33.     V(&full);

34. 

35.     return NULL;

36. }

37. 

38. static void \*consumer(void \*num) {

39.     ③;

40.     ④;

41. 

42.     */\* Critical section begins \*/*

43.     Sleep(rand() % MAX_SLEEP_SEC);

44.     items--;

45.     */\* Critical section ends \*/*

46. 

47.     V(&mutex);

48.     V(&empty);

49. 

50.     return NULL;

51. }

52. 

53. int main() {

54.     sync_var_init();

55. 

56.     pthread_t pid_producer\[NUM_WORKERS\];

57.     pthread_t pid_consumer\[NUM_WORKERS\];

58. 

59.     for (int i = 0; i \< NUM_WORKERS; i++) {

60.         Pthread_create(&pid_producer\[i\], NULL, producer, (void \*)i);

61.         Pthread_create(&pid_consumer\[i\], NULL, consumer, (void \*)i);

62.     }

63. 

64.     for (int i = 0; i \< NUM_WORKERS; i++) {

65.         Pthread_join(pid_producer\[i\], NULL);

66.         Pthread_join(pid_consumer\[i\], NULL);

67.     }

68. }

    1)  补全代码（请从以下选项中选择，可重复选择，每个1分，共4分）

① （24行）

> ② （25行）
>
> ③ （39行）
>
> ④ （40行）
>
> 选项：

1.  P(&mutex)

2.  P(&empty)

3.  P(&full)

    1)  如果交换24行与25行（两个P操作）， （单选，2分）

        1.  有可能死锁

        2.  有可能饥饿

        3.  既不会死锁，也不会饥饿

    2)  交换32行与33行（两个V操作）是否可能造成同步错误？ （2分）

        1.  可能

        2.  不可能

    3)  rand函数是不是线程安全的？ （1分）

        1.  是

        2.  不是

> 28行与43行对rand函数的使用是否会导致竞争？ （1分）

1.  会

2.  不会

> 已知rand函数的实现如下（来源：<https://github.com/begriffs/libc/blob/master/stdlib.h> 和<https://github.com/begriffs/libc/blob/master/stdlib.c>）：

1.  \#define RAND_MAX 32767

2.  

3.  unsigned long \_Randomseed = 1;

4.  

5.  int rand() {

6.    \_Randomseed = \_Randomseed \* 1103515425 + 12345;

7.    return (unsigned int)(\_Randomseed \>\> 16) & RAND_MAX;

8.  }

9.  

10. void srand(unsigned int seed) {

11.   \_Randomseed = seed;

12. }

---

### chap 11-12 解析 · 大题 小题2

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 377–577 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量模拟条件变量解法2：代码与子问题

2.  考虑“生产者-消费者”问题的另一种解法（**代码阅读提示：12-69行之外均与上一种解法相同**）

<!-- -->

1.  */\* Producer–Consumer Problem (Solution 2) \*/*

2.  

3.  \#include "csapp.h"

4.  

5.  \#define BUF_SIZE 3

6.  \#define NUM_WORKERS 50

7.  \#define MAX_SLEEP_SEC 10

8.  

9.  volatile static int items = 0; */\* How many items are there in the buffer \*/*

10. 

11. static sem_t mutex;                */\* Mutual Exclusion \*/*

12. static sem_t sem_waiting_producer; */\* Wait for empty slots \*/*

13. static sem_t sem_waiting_consumer; */\* Wait for available items \*/*

14. 

15. volatile static int num_waiting_producer = 0;

16. volatile static int num_waiting_consumer = 0;

17. 

18. static void sync_var_init() {

19.     Sem_init(&mutex, 0, 1);

20. 

21.     Sem_init(&sem_waiting_producer, 0, ①);

22.     Sem_init(&sem_waiting_consumer, 0, ①);

23. }

24. 

25. static void \*producer(void \*num) {

26.     P(&mutex);

27.     while (items == BUF_SIZE) {

28.         num_waiting_producer++;

29.         ②;

30.         ③;

31.         P(&mutex);

32.     }

33. 

34.     */\* Critical section begins \*/*

35.     Sleep(rand() % MAX_SLEEP_SEC);

36.     items++;

37.     */\* Critical section ends \*/*

38. 

39.     if (num_waiting_consumer \> 0) {

40.         num_waiting_consumer--;

41.         V(&sem_waiting_consumer);

42.     }

43.     V(&mutex);

44. 

45.     return NULL;

46. }

47. 

48. static void \*consumer(void \*num) {

49.     P(&mutex);

50.     while (items == 0) {

51.         num_waiting_consumer++;

52.         ④;

53.         ⑤;

54.         P(&mutex);

55.     }

56. 

57.     */\* Critical section begins \*/*

58.     Sleep(rand() % MAX_SLEEP_SEC);

59.     items--;

60.     */\* Critical section ends \*/*

61. 

62.     if (num_waiting_producer \> 0) {

63.         num_waiting_producer--;

64.         V(&sem_waiting_producer);

65.     }

66.     V(&mutex);

67. 

68.     return NULL;

69. }

70. 

71. int main() {

72.     sync_var_init();

73. 

74.     pthread_t pid_producer\[NUM_WORKERS\];

75.     pthread_t pid_consumer\[NUM_WORKERS\];

76. 

77.     for (int i = 0; i \< NUM_WORKERS; i++) {

78.         Pthread_create(&pid_producer\[i\], NULL, producer, (void \*)i);

79.         Pthread_create(&pid_consumer\[i\], NULL, consumer, (void \*)i);

80.     }

81. 

82.     for (int i = 0; i \< NUM_WORKERS; i++) {

83.         Pthread_join(pid_producer\[i\], NULL);

84.         Pthread_join(pid_consumer\[i\], NULL);

85.     }

86. }

    1)  补全补全代码（请从以下选项中选择，④⑤无需填写，每个1分，共3分）

> ① （21、22行）
>
> ② （29行）
>
> ③ （30行）
>
> 选项：

1.  0

2.  1

3.  P(&sem_waiting_producer)

4.  V(&mutex)

<!-- -->

2)  如果27行和50行的while换成if，是否可能造成同步错误？ （2分）

    1.  可能

    2.  不可能

---

### chap 11-12 题目 · 选择题 1

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 63–71 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程与线程模型：上下文、线程栈、地址空间

1.下列关于C语言中进程模型和线程模型的说法中，错误的是：

A.每个线程都有它自己独立的线程上下文，包括线程ID、程序计数器、条件码、通用目的寄存器值等

B.每个线程都有自己独立的线程栈，任何线程都不能访问其他对等线程的栈空间

C.不同进程之间的虚拟地址空间是独立的，但同一个进程的不同线程共享同一个虚拟地址空间

D.一个线程的上下文比一个进程的上下文小得多，因此线程上下文切换要比进程上下文切换快得多

---

### chap 11-12 题目 · 大题 小题1

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 77–299 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量解法1：P/V 顺序、死锁饥饿、rand 线程安全

“生产者-消费者”问题是并发编程中的经典问题。本题中，考虑如下场景：

1.  所有生产者和所有消费者**共享同一个buffer**

2.  生产者、消费者各有NUM_WORKERS个（**大于一个**）

3.  buffer的容量为BUF_SIZE，**初始情况下buffer为空**

4.  每个生产者向buffer中添加一个item；若buffer满，则生产者等待buffer中有空槽时才能添加元素

5.  每个消费者从buffer中取走一个item；若buffer空，则消费者等待buffer中有item时才能取走元素

<!-- -->

1.  阅读以下代码并回答问题（**代码阅读提示：主要关注producer和consumer两个函数**）

<!-- -->

1.  */\* Producer–Consumer Problem (Solution 1) \*/*

2.  

3.  \#include "csapp.h"

4.  

5.  \#define BUF_SIZE 3

6.  \#define NUM_WORKERS 50

7.  \#define MAX_SLEEP_SEC 10

8.  

9.  volatile static int items = 0; */\* How many items are there in the buffer \*/*

10. 

11. static sem_t mutex; */\* Mutual Exclusion \*/*

12. static sem_t empty; */\* How many empty slots are there in the buffer \*/*

13. static sem_t full;  */\* How many items are there in the buffer \*/*

14. 

15. static void sync_var_init() {

16.     Sem_init(&mutex, 0, 1);

17. 

18.     */\* Initially, there is no item in the buffer \*/*

19.     Sem_init(&empty, 0, BUF_SIZE);

20.     Sem_init(&full, 0, 0);

21. }

22. 

23. static void \*producer(void \*num) {

24.     ①;

25.     ②;

26. 

27.     */\* Critical section begins \*/*

28.     Sleep(rand() % MAX_SLEEP_SEC);

29.     items++;

30.     */\* Critical section ends \*/*

31. 

32.     V(&mutex);

33.     V(&full);

34. 

35.     return NULL;

36. }

37. 

38. static void \*consumer(void \*num) {

39.     ③;

40.     ④;

41. 

42.     */\* Critical section begins \*/*

43.     Sleep(rand() % MAX_SLEEP_SEC);

44.     items--;

45.     */\* Critical section ends \*/*

46. 

47.     V(&mutex);

48.     V(&empty);

49. 

50.     return NULL;

51. }

52. 

53. int main() {

54.     sync_var_init();

55. 

56.     pthread_t pid_producer\[NUM_WORKERS\];

57.     pthread_t pid_consumer\[NUM_WORKERS\];

58. 

59.     for (int i = 0; i \< NUM_WORKERS; i++) {

60.         Pthread_create(&pid_producer\[i\], NULL, producer, (void \*)i);

61.         Pthread_create(&pid_consumer\[i\], NULL, consumer, (void \*)i);

62.     }

63. 

64.     for (int i = 0; i \< NUM_WORKERS; i++) {

65.         Pthread_join(pid_producer\[i\], NULL);

66.         Pthread_join(pid_consumer\[i\], NULL);

67.     }

68. }

    1)  补全代码（请从以下选项中选择，可重复选择，每个1分，共4分）

① （24行）

> ② （25行）
>
> ③ （39行）
>
> ④ （40行）
>
> 选项：

1.  P(&mutex)

2.  P(&empty)

3.  P(&full)

    1)  如果交换24行与25行（两个P操作）， （单选，2分）

        1.  有可能死锁

        2.  有可能饥饿

        3.  既不会死锁，也不会饥饿

    2)  交换32行与33行（两个V操作）是否可能造成同步错误？ （2分）

        1.  可能

        2.  不可能

    3)  rand函数是不是线程安全的？ （1分）

        1.  是

        2.  不是

> 28行与43行对rand函数的使用是否会导致竞争？ （1分）

1.  会

2.  不会

> 已知rand函数的实现如下（来源：<https://github.com/begriffs/libc/blob/master/stdlib.h> 和<https://github.com/begriffs/libc/blob/master/stdlib.c>）：

1.  \#define RAND_MAX 32767

2.  

3.  unsigned long \_Randomseed = 1;

4.  

5.  int rand() {

6.    \_Randomseed = \_Randomseed \* 1103515425 + 12345;

7.    return (unsigned int)(\_Randomseed \>\> 16) & RAND_MAX;

8.  }

9.  

10. void srand(unsigned int seed) {

11.   \_Randomseed = seed;

12. }

---

### chap 11-12 题目 · 大题 小题2

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 303–503 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量模拟条件变量：while 换 if 的同步错误

2.  考虑“生产者-消费者”问题的另一种解法（**代码阅读提示：12-69行之外均与上一种解法相同**）

<!-- -->

1.  */\* Producer–Consumer Problem (Solution 2) \*/*

2.  

3.  \#include "csapp.h"

4.  

5.  \#define BUF_SIZE 3

6.  \#define NUM_WORKERS 50

7.  \#define MAX_SLEEP_SEC 10

8.  

9.  volatile static int items = 0; */\* How many items are there in the buffer \*/*

10. 

11. static sem_t mutex;                */\* Mutual Exclusion \*/*

12. static sem_t sem_waiting_producer; */\* Wait for empty slots \*/*

13. static sem_t sem_waiting_consumer; */\* Wait for available items \*/*

14. 

15. volatile static int num_waiting_producer = 0;

16. volatile static int num_waiting_consumer = 0;

17. 

18. static void sync_var_init() {

19.     Sem_init(&mutex, 0, 1);

20. 

21.     Sem_init(&sem_waiting_producer, 0, ①);

22.     Sem_init(&sem_waiting_consumer, 0, ①);

23. }

24. 

25. static void \*producer(void \*num) {

26.     P(&mutex);

27.     while (items == BUF_SIZE) {

28.         num_waiting_producer++;

29.         ②;

30.         ③;

31.         P(&mutex);

32.     }

33. 

34.     */\* Critical section begins \*/*

35.     Sleep(rand() % MAX_SLEEP_SEC);

36.     items++;

37.     */\* Critical section ends \*/*

38. 

39.     if (num_waiting_consumer \> 0) {

40.         num_waiting_consumer--;

41.         V(&sem_waiting_consumer);

42.     }

43.     V(&mutex);

44. 

45.     return NULL;

46. }

47. 

48. static void \*consumer(void \*num) {

49.     P(&mutex);

50.     while (items == 0) {

51.         num_waiting_consumer++;

52.         ④;

53.         ⑤;

54.         P(&mutex);

55.     }

56. 

57.     */\* Critical section begins \*/*

58.     Sleep(rand() % MAX_SLEEP_SEC);

59.     items--;

60.     */\* Critical section ends \*/*

61. 

62.     if (num_waiting_producer \> 0) {

63.         num_waiting_producer--;

64.         V(&sem_waiting_producer);

65.     }

66.     V(&mutex);

67. 

68.     return NULL;

69. }

70. 

71. int main() {

72.     sync_var_init();

73. 

74.     pthread_t pid_producer\[NUM_WORKERS\];

75.     pthread_t pid_consumer\[NUM_WORKERS\];

76. 

77.     for (int i = 0; i \< NUM_WORKERS; i++) {

78.         Pthread_create(&pid_producer\[i\], NULL, producer, (void \*)i);

79.         Pthread_create(&pid_consumer\[i\], NULL, consumer, (void \*)i);

80.     }

81. 

82.     for (int i = 0; i \< NUM_WORKERS; i++) {

83.         Pthread_join(pid_producer\[i\], NULL);

84.         Pthread_join(pid_consumer\[i\], NULL);

85.     }

86. }

    1)  补全补全代码（请从以下选项中选择，④⑤无需填写，每个1分，共3分）

> ① （21、22行）
>
> ② （29行）
>
> ③ （30行）
>
> 选项：

1.  0

2.  1

3.  P(&sem_waiting_producer)

4.  V(&mutex)

<!-- -->

2)  如果27行和50行的while换成if，是否可能造成同步错误？ （2分）

    1.  可能

    2.  不可能

---

### 2022期末-无答案 · 第一题 14

> 出处：`原文/期末/2022期末-无答案.md` 第 123–123 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：主线程创建对等线程后两线程并发运行

14. 多线程的执行模型在某些方面和进程的执行模型是相似的。每个进程开始生命周期时都是单一进程，这个线程称为主线程（main thread）。在某一时刻，主线程创建一个____________，从这个时间点开始，两个线程就并发地运行。

---

### 2022期末-无答案 · 第一题 15

> 出处：`原文/期末/2022期末-无答案.md` 第 125–125 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：以互斥为目的的二元信号量即互斥锁

15. 以提供互斥为目的的二元信号量常常也称为______：

---

### 2022期末-无答案 · 第七题 1

> 出处：`原文/期末/2022期末-无答案.md` 第 645–685 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：第一类读者-写者（读者优先）信号量 P/V 填空

1、第一类读者-写者问题（读者优先：总是给读者优先权，只要写者当前没有进行写操作，读者就能获得访问权；这种情况存在于读者很多，写者不经常更新的时候使用）

```c
int readcnt;    /* Initially 0 */
sem_t mutex, w; /* Both initially 1 */

void reader(void)
{
  while (1) {
    /* 1 */
    readcnt++;
    if (readcnt == 1) /* First in */
      /* 2 */
    /* 3 */

    /* Reading happens here */

    /* 4 */
    readcnt--;
    if (readcnt == 0) /* Last out */
      /* 5 */
    /* 6 */
  }
}

void writer(void)
{
```

<!-- ===== page 15 ===== -->

```c
  while (1) {
    /* 7 */

    /* Writing here */

    /* 8 */
  }
}
```

---

### 2022期末-无答案 · 第七题 2

> 出处：`原文/期末/2022期末-无答案.md` 第 687–730 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：第二类读者-写者（写者优先）信号量 P/V 填空

2、第二类读者-写者问题（写者优先：写者具有优先权，将后来的读者延迟到所有等待的或活动的写者都完成为止；这种情况存在于经常更新的系统，而读者的目的是获取最新的数据）

```c
int readcnt, writecnt;      // Initially 0
sem_t rmutex, wmutex;       // Initially 1
sem_t r, w;                 // Initially /* 1 */
void reader(void)
{
  while (1) {
    /* 2 */
    P(&rmutex);
    readcnt++;
    /* 3 */
    V(&rmutex);
    /* 4 */

    /* Reading happens here */

    P(&rmutex);
    readcnt--;
    /* 5 */
    V(&rmutex);
  }
}

void writer(void)
{
  while (1) {
    P(&wmutex);
    writecnt++;
    /* 6 */
    V(&wmutex);

    P(&w);
    /* Writing here */
    V(&w);

    P(&wmutex);
    writecnt--;
    /* 7 */
    V(&wmutex);
  }
}
```

---

### 2022期末-答案 · 第一题 14

> 出处：`原文/期末/2022期末-答案.md` 第 23–23 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：对等线程

14、对等线程

---

### 2022期末-答案 · 第一题 15

> 出处：`原文/期末/2022期末-答案.md` 第 24–24 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：互斥锁

15、互斥锁

---

### 2022期末-答案 · 第七题

> 出处：`原文/期末/2022期末-答案.md` 第 81–87 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量实现读者-写者与互斥

第七题 并发
第一类:
1、 P(&mutex);           2、 P(&w);              3、 V(&mutex);           4、 P(&mutex);
5、 V(&w);                   6、 V(&mutex);      7、 P(&w);                  8、 V(&w);
第二类:
1、1               2、 P(&r);               3、 if(readcnt==1) P(&w);   4、 V(&r);
5、 if(readcnt==0) V(&w);  6、if(writecnt==1) P(&r);   7、if(writecnt==0) V(&r);

---

### 2024期末-带答案 · 第一题 13

> 出处：`原文/期末/2024期末-带答案.md` 第 338–344 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：线程栈与 pthread_join/detach

13. 下列关于进程线程的描述中，错误的是：（多选）
A. 每个线程有自己的栈，线程运行时不能访问其他线程的栈上的数据。
B．一个进程的多个线程共享该进程的代码段、数据段和堆。
C．操作系统的调度程序选择某个线程在处理器上运行。
D．当主线程正确执行 pthread_create 后，必须使用 pthread_join 或
pthread_detach，对等线程才会运行。
答案：AD

---

### 2024期末-带答案 · 第五题 Part A

> 出处：`原文/期末/2024期末-带答案.md` 第 795–979 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：读者-写者与信号量代码补全、饥饿

第五题（20分）
Part A (12分)
北京大学南门外新开设了一家小型的电影院，由于电影院规模较小，只有两个
影厅——影厅A与影厅B，并且工作人员只有一名同时充当售票员的经理。这个影
院有一些奇怪的规定。
l  每个影厅正在放映的电影是自动续播的，只有当最后一个观众主动离开当前的
影厅时结束当前影片的放映。
l  两个影厅同时放映电影，选择观看两个影厅中任意一个正在放映的影片的观众
买票后可立即进入，且后续不能更换影厅。
l  两个影厅内的总观众人数不能超过 100 人。购票人数到达上限后，购票通道
会立即关闭。直到有观众离开影院，后续观众才可以继续购票。
l  如果有推销商来找经理推销新影片或者高级放映设施，为了能够及时接待推销
商，经理会立即关闭购票入口，新到来的观众不能购票入场。
l  每次经理只能与一名推销商会谈，后续到达的推销商需要等待。经理与已经到
达的所有推销商都会谈过后，电影院才能重新开业接待观众。
1. 这名可怜的经理希望北京大学的同学能帮他开发出一套系统，实现上面的逻辑，
从而减轻他的工作量。学过ICS的小A一眼就看出这个问题可以建模为读者-写者
问题，并且写出了代码。
1） 补全代码（5分）
#include “csapp.h”
#define MaxAudienceCount 100
int AudienceCount = 0; // 影院的观众数
int PromoterCount = 0; // 推销商的数量
信号量 MovieA = 1;
信号量 MovieB = 1;
信号量 Promote = 1;
信号量 MaxAudience = MaxAudienceCount;
信号量 AudienceMutex = 1;  // 变量AudienceCount的互斥锁
信号量 PromoterMutex = 1;  // 变量PromoterCount的互斥锁
AudienceA(){
    while(1){
        P([  A  ]);
        P(MovieA);
        P([  B  ]);
        AudienceCount++;
        if (AudienceCount == 1){
27

<!-- ===== page 28 ===== -->

            P([  C  ]);
        }
        V([  B  ]);
        V(MovieA);
        // Watch the movie
        P(AudienceMutex);
        AudienceCount--;
        if (AudienceCount == 0){
            V(Promote);
        }
        V(AudienceMutex);
        V(MaxAudience);
    }
}
AudienceB(){
    while(1){
        P([  A  ]);
        P([  D  ]);
        P([  B  ]);
        AudienceCount++;
        if (AudienceCount == 1){
            P([  C  ]);
        }
        V([  B  ]);
        V([  D  ]);
        // Watch the movie
        P(AudienceMutex);
        AudienceCount--;
        if (AudienceCount == 0){
            V(Promote);
        }
        V(AudienceMutex);
        V(MaxAudience);
    }
}
Promoter(){
    while(1){
        P(PromoterMutex);
        PromoterCount++;
        if (PromoterCount == 1){
28

<!-- ===== page 29 ===== -->

            P(MovieA);
            P(MovieB);
        }
        V(PromoterMutex);
        P([  E  ]);
        // Try to promote
        V([  E  ]);
        P(PromoterMutex);
        PromoterCount--;
        if (PromoterCount == 0){
            V(movieA);
            V([  D  ]);
        }
        V(PromoterMutex);
   }
}
A:       B:       C:
D:       E:
（选择下述编号填入字母表示的空缺内，注意不同字母也可能填入相同的数字编号）
①  MovieA
②  MovieB
③  Promote
④  MaxAudience
⑤  AudienceMutex
2） 在这个实现的逻辑下，观众有可能饥饿吗？   （1分）
A. 可能
B. 不可能
2. 让我们再次回归到最基本的第二类读者-写者问题的另一种解法，如下述代码
所示。学习了并发之后的你迅速提取出了有效信息并补全了代码。（6分）
ActiveR 表示正在读的读者的数量，WaitingR 表示正在等待的读者的数量；
ActiveW 表示正在写的写者的数量，WaitingW 表示正在等待的写者的数量。
int ActiveR = 0;
int WaitingR = 0;
int ActiveW = 0;
int WaitingW = 0;
信号量 mutex = 1;
信号量 waitingToRead = [  A  ];
29

<!-- ===== page 30 ===== -->

信号量 waitingToWrite = [  B  ];
Reader() {
    P(mutex);
    while ((ActiveW + WaitingW) > 0) {
        WaitingR++;
        [  C  ];
        [  D  ];
        P(mutex);
        WaitingR--;
    }
    ActiveR++;
    V(mutex);
    // Perform actual read-only access
    P(mutex);
    ActiveR--;
    if (ActiveR == 0 && WaitingW > 0) {
        V(waitingToWrite);
    }
    V(mutex);
}
Writer () {
    P(mutex);
    while (([  E  ]) > 0) {
        WaitingW++;
        [  C  ];
        P(waitingToWrite);
        P(mutex);
        WaitingW--;
    }
    ActiveW++;
    V(mutex);
    // Perform actual write-only access
    P(mutex);
    ActiveW--;
    if (WaitingW > 0) {
        V(waitingToWrite);
    } else if (WaitingR > 0) {
        int n = WaitingR;
        while (n--) {
            [  F  ];
        }
    }
    V(mutex);
}
30

<!-- ===== page 31 ===== -->

A:       B:       C:
D:       E:       F:
（选择下述编号填入字母表示的空缺内，注意不同字母也可能填入相同的数字编号）
①  0
②  1
③  ActiveR + ActiveW
④  ActiveR + WaitingR
⑤  ActiveW + WaitingW
⑥  P(mutex)
⑦  V(mutex)
⑧  P(waitingToRead)
⑨  V(waitingToRead)

---

### 2024期末-带答案 · 第五题 Part B

> 出处：`原文/期末/2024期末-带答案.md` 第 980–1106 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：线程/信号共享变量、竞态与信号安全

Part B (8分)
完全人格，首在体育。小北同学近日遇到了考入某体育强校的李华同学，但二
者就谁是体育世一大产生了争执，因此决定通过拔河比赛一决胜负。为了确保公平
性，小北和李华各自找来了自己的学长作为裁判进行比赛计分。作为计算机专业的
同学，你希望编写一个运行在Linux内核上的C程序模拟这个场景，以分析小北
是否遥遥领先。
为了模拟上述场景，我们用进程表示选手团和裁判团，每个进程中又用两个线
程去模拟两位选手和两位裁判。每个“选手”线程通过信号将自己视角下的比赛情
况发给对应的“裁判”线程，“裁判”线程将比赛结果记录在文件里以便最后登记
分数。
补充说明：
•  在POSIX语义下，多线程进程接收信号时将随机指定一个线程进行接收
o  但在Linux系统下，通过在主线程中BLOCK某信号、在对等线程中
UNBLOCK该信号，可以强制指定该对等线程接收该信号
o  本题利用这种方法，使两个线程judger1和judger2分别处理进
程收到的SIGUSR1和SIGUSR2信号
•  volatile 修饰关键词要求编译器对于指定的变量的每次读写都必须使
用内存中的值
•  register修饰关键词要求编译器必须将指定的变量分配在寄存器上
•  题目在Ubuntu 24.04.1上使用gcc 13.3.0 (Ubuntu 13.3.0-
6ubuntu2~24.04)进行编译，编译命令为 gcc input.c csapp.c -o
input。题目环境的内核版本5.为15.167.4。解决本题无需课程内容以外知
识，提供本信息仅为避免你臆想不必要的情况。
31

<!-- ===== page 32 ===== -->

input.c
#vionicdl usdieg n"acls_ahpapn.dhl"e r ( int signo) {
    if (signo == SIGUSR1) printf("A\n");
 }       if (signo == SIGUSR2) printf("B\r");
void *judger(void *num) {
        ././.在 省  略的代码中使用pthread_sigmask分别取消对SIGUSR1和SIGUSR2信号的阻塞
    //(int)num为1则取消 SIGUSR1的阻塞，(int)num为2则取消SIGUSR2的阻塞
 }      for (;;);
 int judger_pid = 0;
 void *player(void *arg) {
        ivnotl antuiml e=  s(tiantti)c( uiinntt 6f4l_atg) a=r g0;;
        rfeogri s(tienrt  iin t=  v1a;l  i=  <0=;  1 0 ; i++) {
                viafl  (=n ufml a=g=;  1/)/  {*  2
                        iffl a(gv a=l  v<a=l ;0  )  ++val;
            printf"(_"AP"l[avyaelr  >% d0:] )%;d   % c\n", num, val,
                 }   e lisfe  ({v a l  > 0) kill(judger_pid, SIGUSR1);
                        iffl a(gv a=l  v>a=l ;0  )  --val;
            printf"(_"BP"l[avyaelr  <% d0:] )%;d   % c\n", num, val,
            if (val < 0) kill(judger_pid, SIGUSR2);
         }      }
}
int main() {
        ././. 在  省  略的代码中使用pthread_sigmask阻塞SIGUSR1和SIGUSR2信号
    // 并设置SIGUSR1和SIGUSR2的信号处理函数为signal_handler
    pid_t player_pid;
         i f   (fprleaoypeern_(p"igda m=e .foourtk"(,) )" w{b "/,/  s*t1d o u t); //题目保证硬盘空间足够
                s/e/t 裁vb判uf团( s t dout, NULL, _IOLBF, 1024);
32

<!-- ===== page 33 ===== -->

        pthread_t judger1, judger2;
        pthread_create(&judger1, NULL, judger, (void *)1);
        pthread_create(&judger2, NULL, judger, (void *)2);
        waitpid(player_pid, NULL, 0);
        sleep(1); // 题目保证此时所有pending信号均处理完成
        _exit(0);
    } else {
        sleep(1); // 题目保证此时信号处理程序已按要求生效
        // 玩家团
        judger_pid = getppid();
        pthread_t player1, player2;
        pthread_create(&player1, NULL, player, (void *)1);
        pthread_create(&player2, NULL, player, (void *)2);
        pthread_join(player1, NULL);
        pthread_join(player2, NULL);
        return 0;
    }
}
1） 在player函数中，使用了_______个共享变量? (同一个变量多次出现算1
个) （1分）
2） 看到代码后，你很快发现：在信号处理程序里使用了不安全的printf函数！
老师在课堂上讲过著名的“灵魂出窍”死锁案例，而题目的程序同时在main函数
和信号处理程序都使用了printf。
题目中的程序_______（会／不会）出现死锁？原因包括：printf _______（是
／不是）异步信号安全的；printf _______（是／不是）线程安全的；在题目的
程序中， signal_handler 中的printf_______（可能/不会）被打断。（4
分）
3） 下面是上面代码某次运行时输出的结果：
stdout
Player 1:  1   A
Player 1:  1   A
Player 1:  1   A
Player 1:  1   A  game.out
Player 1:  1   A  A
Player 1:  1   A  A
Player 1:  1   A  A
Player 1:  1   A  A
Player 2:  0   _  B
Player 2:  0   _  A
Player 2: -1  B
Player 1:  1   A
Player 1: 0  _
Player 2: -1  B
33

<!-- ===== page 34 ===== -->

Player 2: -1  B
Player 2: -1  B
Player 2: -1  B
Player 2: -1  B
Player 2: -1  B
Player 2: -1  B
① 下列哪一项不是导致本题程序多次运行的结果不同的原因？_______（1分）
A. 操作系统调度进程具有不确定性
B. 操作系统调度线程具有不确定性
C. 操作系统下发信号的时机具有不确定性
D. 操作系统处理系统调用具有不确定性
② 下列哪一选项会导致上面的运行结果中，game.out 的 A 比 stdout 的少？
_______ （1分）
除此之外，还有哪一选项会导致上面的运行结果中，game.out的B比stdout的
少？_______（1分）
A. 多个到达的信号可能只被处理一次
B. 后面的字符可能在缓冲区内覆盖前面的字符
C. 缓冲区内的字符没有刷新到文件，程序就退出了
D. 多次相同的kill可能只有一次进入内核
E. 父进程中的两个线程产生race Condition
F. 子进程中的两个线程产生race Condition
G. 由于磁盘太慢等原因，产生写不足

---

### 2025期末-带答案 · 二 25

> 出处：`原文/期末/2025期末-带答案.md` 第 144–146 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程与线程资源共享与寄存器独立

25.关于进程(processes) 和线程 (threads) 的描述，下列说法哪些正确？
答案：ABCD
解析：线程切换会保存CPU的寄存器，E错误

---

### 2025期末-带答案 · 四 1

> 出处：`原文/期末/2025期末-带答案.md` 第 175–180 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：共享变量识别及参考答案

四 并发相关主题（15分）
1.（4分）以下是一段改编自教材上的多线程代码。对于thread函数内出现的以下8个
变量：i,niters,local_thread,static_local,cnt,index,shared_array,
dynamic_ptr，哪几个是共享变量？
答：
答案：static_local；cnt；shared_array；dynamic_ptr（每个1分）

---

### 2025期末-带答案 · 四 2

> 出处：`原文/期末/2025期末-带答案.md` 第 181–191 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：Lightswitch 读者-写者两问及答案

2.（3分）
（1）交换reader函数里的 lock(&reader_switch, &wmutex); 和 V(&empty);
两行，是否会导致竞争或死锁问题？答：（ ）[是/否]
答案：否（1分）
（2）在本题的reader和writer实现基础上，……
答：（ ）
A. (9),(8),(4),(2),(11)
B. (11),(8),(3),(3),(8)
C. (11),(11),(3),(2),(8)
D. (9),(11),(4),(3),(11)
答案：C（2分）

---

### 2025期末-带答案 · 四 3

> 出处：`原文/期末/2025期末-带答案.md` 第 192–200 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：生产者-消费者订单缓冲区空白答案

3.（8分）在现代餐饮行业中，……答案（每项1分）：
(1) 1
(2) BUF_SIZE
(3) P(&buffer.empty)
(4) P(&buffer.mutex)
(5) V(&buffer.full)
(6) P(&buffer.full)
(7) P(&buffer.mutex)
(8) V(&buffer.empty)

---

### 2025期末-无答案 · 二 25

> 出处：`原文/期末/2025期末-无答案.md` 第 330–335 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：进程与线程的资源共享与切换开销

25.关于进程(processes) 和线程 (threads) 的描述，下列说法哪些正确？
A. 同一进程内的多个线程通常共享同一虚拟地址空间（代码/全局数据/堆）
B. 同一进程内的不同线程通常有各自独立的栈（stack）
C. 进程切换往往比同进程的线程切换工作量大、耗费时间长
D. 线程之间共享文件描述符表，一个线程 close(fd) 可能影响其他线程
E. 线程之间共享寄存器状态，一个线程改 %rax 会影响另一个线程

---

### 2025期末-无答案 · 四 1

> 出处：`原文/期末/2025期末-无答案.md` 第 397–457 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：多线程代码中的共享变量识别

四 并发相关主题（15分）
1.（4分）以下是一段改编自教材上的多线程代码。对于thread函数内出现的以下8个
变量：i,niters,local_thread,static_local,cnt,index,shared_array,
dynamic_ptr。哪几个是共享变量？
答：
#define N 100
void *thread(void *vargp);
volatile long cnt = 0;
int shared_array[N];
int *dynamic_ptr;
int main(int argc, char** argv) {
long niters;
pthread_t tid1, tid2;
int local_main = 0;
if(argc!=2) {
printf("usage: %s <niters>\n", argv[0]);
exit(0);
}
niters = atoi(argv[1]);
dynamic_ptr = (int*)malloc(N * sizeof(int));
if(dynamic_ptr == NULL) {
printf("Memory allocation failed\n");
exit(1);
}
for(int i = 0; i < N; i++) {
shared_array[i] = i;
}
int thread_arg = niters;
pthread_create(&tid1, NULL, thread, &thread_arg);
pthread_create(&tid2, NULL, thread, &thread_arg);
pthread_join(tid1, NULL);
pthread_join(tid2, NULL);
if (cnt != 2 * niters) {
printf("BOOM! cnt = %ld (expected %ld)\n", cnt, 2 * niters);
} else {
printf("OK cnt = %ld\n", cnt);
}
free(dynamic_ptr);
exit(0);
10

<!-- ===== page 11 ===== -->

}
void* thread(void *arg) {
long i;
int niters = *(int *)arg;
int local_thread = 0;
static int static_local = 0;
for(i = 0; i < niters; i++) {
cnt++;
int index = i % N;
shared_array[index]++;
dynamic_ptr[index]++;
static_local++;
local_thread++;
}
printf("Thread finished: local_thread=%d, static_local=%d\n",
local_thread, static_local);
return NULL;
}

---

### 2025期末-无答案 · 四 2

> 出处：`原文/期末/2025期末-无答案.md` 第 458–555 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：Lightswitch 读者-写者与到达时刻状态分析

2.（3分）小明在学习了读者-写者问题后，编写了以下代码用来解决读者-写者问题。其
中，Lightswitch结构体封装了进入临界区的读者计数counter的操作逻辑，保证当有
读者在临界区时，其他读者仍然可以进入，但写者无法进入。请阅读下面代码（代码阅读提
示：主要关注reader和writer两个函数），回答问题：
（1）交换reader函数里的 lock(&reader_switch, &wmutex); 和 V(&empty);
两行，是否会导致竞争或死锁问题？答：（ ）[是/否]
（2）在本题的reader和writer实现基础上，考虑一共有3个读者（R1，R2，R3）和
2个写者（W1，W2）依次到来，且循环仅执行一次（NUM_OPERATIONS=1）的情况，读者
执行读操作时间为7，写者执行写操作时间为8，其到达时间如下：R1:0, R2:1, W1:2,
W2:4, R3:5。在时刻6时，R1、R2、W1、W2、R3依次处于的位置可能是：
答：（ ）
A. (9),(8),(4),(2),(11)
B. (11),(8),(3),(3),(8)
C. (11),(11),(3),(2),(8)
D. (9),(11),(4),(3),(11)
（注意，为简单起见，只考虑读写时间，忽略所有其他时间，包括代码中其他语句的执行时
间、线程切换、调度等等，亦假设没有更多的读者或写者或其他线程。）
#include “csapp.h”
#define NUM_READERS 5
#define NUM_WRITERS 10
#define NUM_OPERATIONS 100
typedef struct {
int counter;
sem_t mutex;
} Lightswitch;
void lightswitch_init(Lightswitch* ls) {
ls->counter = 0;
11

<!-- ===== page 12 ===== -->

sem_init(&ls->mutex, 0, 1);
}
void lock(Lightswitch* ls, sem_t* semaphore) {
P(&ls->mutex);
ls->counter += 1;
if (ls->counter == 1) {
P(semaphore);
}
V(&ls->mutex);
}
void unlock(Lightswitch* ls, sem_t* semaphore) {
P(&ls->mutex);
ls->counter -= 1;
if (ls->counter == 0) {
V(semaphore);
}
V(&ls->mutex);
}
void lightswitch_destroy(Lightswitch* ls) {
sem_destroy(&ls->mutex);
}
sem_t wmutex;
sem_t empty;
Lightswitch reader_switch;
void* writer(void* arg) {
(1) for (int i = 0; i < NUM_OPERATIONS; i++) {
(2) P(&empty);
(3) P(&wmutex);
(4) // writing here, need 8 time unit
(5) V(&wmutex);
(6) V(&empty);
}
return NULL;
}
void* reader(void* arg) {
(7) for (int i = 0; i < NUM_OPERATIONS; i++) {
(8) P(&empty);
(9) lock(&reader_switch, &wmutex);
(10) V(&empty);
(11) // reading here, need 7 time unit
(12) unlock(&reader_switch, &wmutex);
}
return NULL;
}
int main() {
pthread_t readers[NUM_READERS];
pthread_t writers[NUM_WRITERS];
sem_init(&wmutex, 0, 1);
sem_init(&empty, 0, 1);
lightswitch_init(&reader_switch);
12

<!-- ===== page 13 ===== -->

for (int i = 0; i < NUM_READERS; i++)
pthread_create(&readers[i], NULL, reader, NULL);
for (int i = 0; i < NUM_WRITERS; i++)
pthread_create(&writers[i], NULL, writer, NULL);
for (int i = 0; i < NUM_READERS; i++)
pthread_join(readers[i], NULL);
for (int i = 0; i < NUM_WRITERS; i++)
pthread_join(writers[i], NULL);
sem_destroy(&wmutex);
sem_destroy(&empty);
lightswitch_destroy(&reader_switch);
return 0;
}

---

### 2025期末-无答案 · 四 3

> 出处：`原文/期末/2025期末-无答案.md` 第 556–595 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：服务员-厨师订单缓冲区的生产者-消费者

3.（8分）在现代餐饮行业中，高效的订单处理系统至关重要。小红设计了一个模拟在线餐
厅的订单处理流程，其中服务员接收顾客订单，厨师处理这些订单。为最大化效率，餐厅雇
佣了多个服务员和厨师同时工作，他们通过一个共享的订单缓冲区进行协作。该场景遵循以
下规则：
 服务员有NUM_WAITERS名，厨师有NUM_COOKS名（NUM_WAITERS和NUM_COOKS
都大于1），服务员和厨师使用同一个共享订单缓冲区；
 每个服务员独立工作，每次将接收到的一个顾客订单放入共享的订单缓冲区内，当缓冲
区满时，服务员必须等待，直到有空闲位置才能放入新订单；
 每个厨师独立工作，每次从共享订单缓冲区内取出一个订单进行烹饪处理，当缓冲区为
空时，厨师必须等待，直到有新的订单被放入；
 订单缓冲区的容量为BUF_SIZE（BUF_SIZE大于0），用于存放待处理的订单，且初
始情况下订单缓冲区为空。
下面代码中，waiter函数为服务员线程，cook函数为厨师线程，init_buffer函
数为初始化函数，会在系统启动时调用一次，略去其他部分代码和无关逻辑。
请填写程序中对应空白处的代码：
#define NUM_WAITERS 4 // 服务员数量
#define NUM_COOKS 2 // 厨师数量
#define BUF_SIZE 5 // 订单缓冲区容量
typedef struct {
char* orders[BUF_SIZE];
int in;
int out;
sem_t mutex;
sem_t empty;
sem_t full;
} Buffer;
Buffer buffer;
void init_buffer() {
buffer.in = 0;
13

<!-- ===== page 14 ===== -->

bsuefmf_eirn.iotu(t&b=uf0f;er.mutex, 0, ______(1)_______);
} sseemm__iinniitt((&&bbuuffffeerr..efmupltly,,0,0,0)_;______(2)_______);
voidw*hiwl/ae/i(t1接e)r单({逻vo辑id* arg) {
c/__bh/__ua__f将r__f*__e订__ro((.单r34o放d))re__d入r__e__r缓=__s冲__[x__b区x;;uxfxf;er.in] = order;
} } bV_/u(_/f&_其fb_eu_他rf_.f(逻ie5辑nr)._略=m_u_去(t_be_ux_f);f;er.in+1) % BUF_SIZE;
voidw*hicl/__coe/__ho(__ak1从__r()__*v缓__o{o((冲ir67d区d))*e__取r__a__出r=__g订__)b__单u;;{ffer.orders[buffer.out];
} } bV_/u(_/f&_其fb_eu_他rf_.f(逻oe8辑ur)t._略m_=u_去t_(e_bx_u);f;fer.out+1) % BUF_SIZE;

---

### 期末往年题勘误、详解 by Arthals · 2015 第八题

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 35–59 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：两 mutex 初值应为 1 与 PB 代码订正

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

---

### 期末往年题勘误、详解 by Arthals · 2016 第一题 第20问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 71–71 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：非 volatile 变量的寄存器缓存与加锁

第 20 问，关键点在于，printf 的时候因为这个 j 没有 volatile 定义，所以你考虑汇编的时候，这里肯定就是一个寄存器了，上面读完是啥就是啥，而寄存器是个线程上下文里的东西，所以你 V(&s) 之后到 printf 之间哪怕被切走，切回来的时候也是会恢复的，所以不会因为在别的线程里加了 j，我这里 printf 就会知道哦原来这个 j 变了，而是依旧恢复成切走的时候的 j（寄存器版本）。所以这题前三个都是可能的，只有 D，因为线程锁保证了这个 j 一定会加到 3，而对应的线程的打印一定能打出 3，所以 D 是错的。

---

### 期末往年题勘误、详解 by Arthals · 2018 第一题 第13问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 97–97 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：使用全局变量导致线程不安全

第 13 问，A 选项，可能使用了全局变量。

---

### 期末往年题勘误、详解 by Arthals · 2018 第七题 第4问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 140–142 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：信号量初值≥2 时锁失效

### 第七题

第 4 问，信号量也可以等于 2，本质上是大于等于 2 的时候这个锁就失效了，相当于只有剩下的一个互斥锁（

---

### 期末往年题勘误、详解 by Arthals · 2019 第七题

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 180–182 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：读者-写者 while 循环的竞争含义

### 第七题

为什么读写问题要一直 while？原因是要通过两个 while 每次循环之间的竞争来模拟读者一直读写者一直写。

---

### 期末往年题勘误、详解 by Arthals · 2020 第一题 第25问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 192–192 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：a、d 加锁顺序相反导致死锁

第 25 问，选项除 D 外均会死锁。因为线程 1 和线程 3 的 a，d 锁的获得顺序刚好相反。

---

### 期末往年题勘误、详解 by Arthals · 2020 第六题

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 198–208 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：哲学家就餐加锁顺序与 sem 的 value/zero

### 第六题

第 1 问：首先你需要知道为什么会死锁？要是所有人都同时获得了 UP 的锁，那么 DOWN 的就一个都获取不到，就寄了。

然后如何保证不会发生这种情况？就需要规定获得锁的顺序，必须先获得大的，再获得小的（你可以自己思考一下正确性的原因）。所以答案是 1221 或者 2112.

第 2 问：实际上是用 value 存储你模拟的 sem 的值，用 mutex 保护 value，用 zero 实现等待。如果 value<0 了那么 P 操作就必须等待，所以 C 应该是<.

对于 F，如果 value 本来就<0，那么就需要唤醒一个 P 阻塞的线程。自增后<条件变为<=，故也填写<=.

具体的条件判断可以使用边界值判断法，就是考虑 value 为-1,0,1 三种特殊值就可以了。

---

### 期末往年题勘误、详解 by Arthals · 2021 第六题 2.b

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 224–240 行　·　模块判定：Concurrent Programming and Synchronization
> 考什么：生产者-消费者中 if 与 while 的区别

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

### chap 11-12 解析 · 11章选择题 1 答案 C 与逐项解析

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 13–27 行

答案：C

难度：简单

预计时间：小于1min

①TCP提供可靠传输

②TCP可以在两个进程间传输，包括同一个主机上的

③TCP/IP本身是一个协议族，TCP可以基于IP来实现，也存在不使用IP的实现

④TCP是全双工的，双方同时都可以进行读写

⑤TCP并不依赖DNS服务

---

### chap 11-12 解析 · 11章选择题 2 答案 A 与逐项解析

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 39–51 行

答案：A

难度：简单

预计时间：小于1min

A. TCP连接由连接双方进程的套接字唯一确定

B. connect应该指明想要连接的服务器的套接字地址结构

C. socket只是获得套接字，还不可以进行读写，需要完成连接以后才可以进行读写

D. bind 函数只是用于绑定套接字地址的，而listen函数用于将用于客户端的主动套接字转化为用于服务器的监听套接字

---

### chap 11-12 解析 · 11章选择题 3 答案 D 与解析

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 63–75 行

答案：D

难度：简单

预计时间：1min

A. 考察Web服务的基本概念

B. 考察HTTP状态码

C. 考察Web的URL机制内在的思想

D. 考察因特网域名的多对多关系

---

### chap 11-12 解析 · 备选题 4 答案 D 与 A/B/C 解析

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 91–99 行

答案：D

解析：

A：网络字节顺序是大端法

B：DNS负责维护域名集合和IP地址集合的映射关系

C：一个域名也可以被映射到多个IP地址

---

### chap 11-12 解析 · 备选题 5 答案 A 与解析

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 113–119 行

答案：A

解析：简单题，考察11.1部分内容

A：在该模型中，客户端和服务器指进程

BCD均正确

---

### chap 11-12 解析 · 12章选择题解析（答案 B，线程栈不设防）

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 133–135 行

解析：B

考察12.3 12.4线程模型，属于简单题。B选项，不同的线程栈是不对其他线程设防的。所以，如果一个线程以某种方式得到一个指向其他线程栈的指针，那么它就可以读写这个栈的任何部分。

---

### chap 11-12 解析 · 大题小题1 解析（a BACA，资源申请与死锁）

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 365–375 行

> 解析：a) BACA; b) A; c) B; d) BB
>
> 本小题是“生产者-消费者”问题用信号量的经典解法。
>
> a、b考察的是资源申请和互斥的顺序。
>
> c考察的是对死锁的分析
>
> d考察是是线程安全，以及线程不安全的函数在给定场景下是否会出错
>
> 评论：这是一道基础题，考察对基础问题的掌握程度，同学们应当能快速得到这些分数。尽管代码较长，但是代码可读性好、结构清晰，同时也是同学们熟悉的代码，阅读应当没有障碍。

---

### chap 11-12 解析 · 大题小题2 解析（a ADC; b A，while 与条件变量）

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 579–593 行

解析：a) ADC; b) A

a考察对代码理解，①涉及的两个信号量用于线程的休眠，因此在任意时刻，这两个信号量的值都是0；②③应当先释放mutex，然后再等待，注意信号量的V操作并不会丢失（信号量的值必然会加一），因此即便这两个P、V操作之间可能被打断，这个程序仍然是正确的。

b考察对控制流的分析，在如下场景下这一修改会造成同步错误：一个线程从27行的P操作中被唤醒以后，被中断，另一线程比前述线程优先获取mutex（26行），且在27行测试得到false，因此这个slot被这个新来的线程使用。

评论：本题较难，尤其是b。

本题的背景，是用信号量模拟条件变量，所以b的解法实际上是用条件变量解决“生产者-消费者”问题。

删除部分代码，还可以得到用自旋锁的解法。

b中的while是条件变量、管程中的经典问题。

本题中的代码均经过理论与实践双重验证。

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
