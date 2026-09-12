# 网络编程

> **英文模块名**：`Network`  

> 本文件由 `_tools/build_modules.py` 生成：分类结果只记录行号区间，
> 题目正文全部从 `原文/` 按行号**逐字切出**，未经转述或改写。

## 一、清单

共 75 道题，来自 19 份材料。

| 年份 | 试卷 | 类别 | 题号 | 考什么 |
|---|---|---|---|---|
| 2013 | 2013期末-带答案 | 期末 | 第一题 17 | 计算机网络与端口/域名基本概念 |
| 2013 | 2013期末-带答案 | 期末 | 第一题 18 | client-server connection socket pair |
| 2013 | 2013期末-带答案 | 期末 | 第七题 | socket 连接数上限与 listenfd/connfd 填空 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 17 | 不同协议局域网互连设备 |
| 2014 | 2014期末-带答案 | 期末 | 第一题 18 | TCP/UDP/HTTP 基础概念 |
| 2014 | 2014期末-带答案 | 期末 | 第八题 | socket 数量、Connection socket pair、Echo/Tiny Server |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 17 | HTTP 命令与静态/动态内容 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第一题 18 | HUB/帧头/IP 地址分类与动态分配 |
| 2015 | 2015期末-20160104-带答案 | 期末 | 第七题 | 协议栈数据包类型与软件实现、互联网概念 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 16 | IP 协议特性与域名到 IP 的映射 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 17 | HTTP 端口、TCP 可靠性与连接语义 |
| 2016 | 2016期末-带答案 | 期末 | 第一题 18 | HTTPS 取文件时各层协议的必要性 |
| 2016 | 2016期末-带答案 | 期末 | 第七题 | 并发 echo server 套接字程序填空 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 16 | 本地端口、私有 IP 与服务器端口 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 17 | 交换机/HUB、UDP 实时音视频、校验 |
| 2017 | 2017期末-无答案 | 期末 | 第一题 18 | localhost、套接字地址与 IPv4/IPv6 |
| 2017 | 2017期末-无答案 | 期末 | 第七题 | Echo 客户端/服务器流程填空与协议判断 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 10 | Internet/IP 递送与帧头剥离封装 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 11 | 套接字接口 API 与描述符读写 |
| 2018 | 2018期末-带答案 | 期末 | 第一题 12 | 打开网页所涉及的协议栈层次 |
| 2018 | 2018期末-带答案 | 期末 | 第六题 | 协议分层/面向连接判断与套接字连接流程填空 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 20 | accept 建立连接与 read 阻塞 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2020 选择题 21 | 主机名解析与网络字节序 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 14 | 迭代服务器 read 阻塞 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 15 | 网络字节序即大端 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 选择题 16 | CGI 文件名与参数用 ? 分隔 |
| 2019 | 2019、2020期末-答案解析 | 期末 | 2019 解答题五 | RIO/套接字 API 调用顺序 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 14 | 迭代 echo 服务器中客户端阻塞位置 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 15 | IP 地址、套接字地址与网络字节序 |
| 2019 | 2019期末-无答案 | 期末 | 第一题 16 | Web 服务器 CGI 动态内容 |
| 2019 | 2019期末-无答案 | 期末 | 第六题 | client-server echo 框架与 open_listenfd 补全 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 20 | 套接字接口函数与迭代 echo 服务器阻塞 |
| 2020 | 2020期末-无答案 | 期末 | 第一题 21 | IPv4 地址、字节序与主机名命令 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 17 | TCP 协议的可靠传输与全双工特性 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 18 | TCP 套接字接口函数语义 |
| 2021 | 2021期末-无答案 | 期末 | 第一题 19 | Web 服务、URL 与 HTTP 状态码 |
| 2021 | chap 11-12 解析 | 期末 | 选择题 1 | TCP 协议特性判断 |
| 2021 | chap 11-12 解析 | 期末 | 选择题 2 | TCP 套接字接口 connect/bind/listen 辨析 |
| 2021 | chap 11-12 解析 | 期末 | 选择题 3 | Web 服务、HTTP 状态码与域名映射 |
| 2021 | chap 11-12 解析 | 期末 | 备选题 4 | 全球 IP 因特网：字节序/DNS/套接字说法正误 |
| 2021 | chap 11-12 解析 | 期末 | 备选题 5 | 网络基本概念说法正误 |
| 2021 | chap 11-12 题目 | 期末 | 选择题 1 | TCP 协议特性：可靠/全双工/基于IP/DNS |
| 2021 | chap 11-12 题目 | 期末 | 选择题 2 | TCP 套接字接口 connect/bind/listen/socket 辨析 |
| 2021 | chap 11-12 题目 | 期末 | 选择题 3 | Web 服务、HTTP 状态码、URL 与域名映射 |
| 2021 | chap 11-12 题目 | 期末 | 备选题 4 | 网络字节序、DNS、域名与套接字概念 |
| 2021 | chap 11-12 题目 | 期末 | 备选题 5 | 网络基本概念：客户端服务器指进程、以太网 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 12 | IPv4 地址十六进制转点分十进制 |
| 2022 | 2022期末-无答案 | 期末 | 第一题 13 | 客户端-服务器套接字流程填空（accept/bind/listen/socket） |
| 2022 | 2022期末-无答案 | 期末 | 第六题 1 | Open_listenfd 中 hints.ai_socktype 取值（含服务器代码） |
| 2022 | 2022期末-无答案 | 期末 | 第六题 2 | Getnameinfo 用途：由 IP 地址查主机名 |
| 2022 | 2022期末-无答案 | 期末 | 第六题 3 | 由 log.out 客户端端口推断命令行缺失参数（含客户端代码） |
| 2022 | 2022期末-无答案 | 期末 | 第六题 4 | GOAL 增大后客户端报错的原因 |
| 2022 | 2022期末-无答案 | 期末 | 第六题 5 | 在客户端补一行代码以支持更大的 GOAL |
| 2022 | 2022期末-无答案 | 期末 | 第六题 6 | 两客户端并发连服务器时结果分析 |
| 2022 | 2022期末-无答案 | 期末 | 第六题 3（第 14 页重复） | 操作流程与端口推断题面，扫描重复页 |
| 2022 | 2022期末-无答案 | 期末 | 第六题 4（第 14 页重复） | GOAL 增大报错原因，扫描重复页 |
| 2022 | 2022期末-无答案 | 期末 | 第六题 5（第 14 页重复） | 补代码支持大 GOAL，扫描重复页 |
| 2022 | 2022期末-无答案 | 期末 | 第六题 6（第 14 页重复） | 多客户端并发结果分析，扫描重复页 |
| 2022 | 2022期末-答案 | 期末 | 第一题 12 | 点分十进制 IP 地址 |
| 2022 | 2022期末-答案 | 期末 | 第一题 13 | bind 绑定套接字 |
| 2022 | 2022期末-答案 | 期末 | 第六题 | SOCK_STR 与客户端 fd 泄漏 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 11 | IP 递送机制、TCP 与域名映射 |
| 2024 | 2024期末-带答案 | 期末 | 第一题 12 | 套接字接口 bind/listen/connect |
| 2025 | 2025期末-带答案 | 期末 | 二 24 | 并发网络服务器 listenfd/connfd 与 SIGCHLD |
| 2025 | 2025期末-无答案 | 期末 | 二 24 | 并发网络服务器 listenfd/connfd 与 SIGCHLD |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2015 第一题 第17问 | GET/POST/PUT 均可获取动态内容（判为废题） |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2018 第一题 第11问 | socket fd 可用标准 IO 读写 |
| — | 期末往年题勘误、详解 by Arthals | 期末 | 2019 第一题 第14问 | connect 返回与 accept 的时序区别 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 5 | ssh-keygen 公钥/私钥的存放位置（兼 Unix 工具） |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 6 | scp 指定端口复制文件到远程主机 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 46 | IPv4/IPv6 地址长度 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 47 | TCP 与 UDP 的区别 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 48 | /24 子网可用主机地址数量 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 49 | 10.7.74.125 的地址类别与私有地址 |
| 2025 | 2025Lab测验-无答案 | Lab测验 | Lab 任务 50 | 域名映射、IP 可靠性与 getaddrinfo/freeaddrinfo |

## 二、题目原文

### 2013期末-带答案 · 第一题 17

> 出处：`原文/期末/2013期末-带答案.md` 第 232–246 行　·　模块判定：Network
> 考什么：计算机网络与端口/域名基本概念

17、下列关于计算机网络概念的说法中，哪一项是正确的？答：（     ）
A. 全球最大的计算机网络是互联网 Internet，所以计算机网络协议是
Internet Protocol即IP协议。
B. 计算机之间的网络通信是一个机器上的一个 process (如 client
process) 与另一个机器上的 process (如 server process) 之间
的通信。
C. 网络应用程序有默认的端口号，大部分应用的端口号可以修改，而少部分
知名应用如Web服务程序的端口号80是无法修改的。
D. 一个域名只能对应一个IP地址；而一个IP地址可以对应多个域名。
答案：B
解释：考察第一部分
A. IP只是计算机网络众多协议中的一种；IP是具有代表性的一种协议；但还有
其他很多协议。
C. 端口号是可以修改的，默认端口号只是为了方便
D. 一个域名可以对应多个IP；一个IP也可以对应多个域名。

---

### 2013期末-带答案 · 第一题 18

> 出处：`原文/期末/2013期末-带答案.md` 第 247–277 行　·　模块判定：Network
> 考什么：client-server connection socket pair

18、在 client-server 模型中，一个连接（connection）可以由 IP 地址，
7

<!-- ===== page 8 ===== -->

端口号的组合来表示。假设一个访问网页服务器的应用，客户端 IP 地址为
128.2.194.242，目标服务器端 IP 地址为 208.216.181.15，用户设置的代
理服务器 IP 地址为 155.232.108.39。目标服务器同时提供网页服务（默认端
口80），和邮件服务（默认端口25）。当客户端向目标服务器发送访问网页的请求
时，下面connection socket pairs 正确的一组是？答：（       ）
  客户端请求  代理请求
(128.2.194.242:25,  (128.2.194.242:51213,
A  155.232.108.39:80)  208.216.181.15:80)
(128.2.194.242:51213,  (128.2.194.242:12306,
B  155.232.108.39:80)  208.216.181.15:80)
(128.2.194.242:25,  (155.232.108.39:51213,
C  208.216.181.15:80)  208.216.181.15:80)
D  (128.2.194.242:51213,  (155.232.108.39:12306,
208.216.181.15:80)  208.216.181.15:80)
答案：D
解释：考察所有三部分内容
（客户端请求）这一段，客户端发送的请求，源地址是客户自己地址
128.2.194.242，端口号是临时端口号；目标地址仍是服务器地址
208.216.181.15:80默认端口80
（代理请求）这一段，代理发送的请求，源地址是代理自己地址155.232.108.39，
端口号是临时端口号；目标地址仍是服务器地址208.216.181.15:80默认端口
80。
所以，选项D正确。
（选项A/B中，目标地址不是代理的地址，而是目标服务器的地址。）
（选项C中，端口号25属于电子邮件应用默认端口号，不作为客户端的临时端口
号。）

---

### 2013期末-带答案 · 第七题

> 出处：`原文/期末/2013期末-带答案.md` 第 571–623 行　·　模块判定：Network
> 考什么：socket 连接数上限与 listenfd/connfd 填空

第七题（10分）
（1） 一个服务器拥有两个独立的固定IP地址，那么它在web应用端口80上最
多可以监听多少个独立的 socket 连接？（2分）
答案：2*248
服务器端  客户端  结果
2个独立固定IP  任意32位IP  2*232+16
任 意 16 位   port
number
（2） 该服务器在所有有web应用端口上最多可以监听多少个独立的 socket 连
接？（2分）
答案：2*264
服务器端  客户端  结果
2个独立固定IP  任意32位IP  2*216+32+16
任意16位port number  任 意 16 位   port
number
（3） 在下图中连线上填入正确的目标服务器的socket 标识符（2分）
19

<!-- ===== page 20 ===== -->

答案：
128.2.194.242:80
128.2.194.242:7
4) 在Echo server 范例中，server端通过accept函数接受了一个 client
的连接请求，从而将网络描述符与该网络连接、socket绑定，然后进行网络数据
传输。在下面的空格处填写正确的网络描述符，每个空填写listenfd 或connfd
（共4分，每空1分）。
int main(int argc, char **argv) {
int listenfd, connfd, port, clientlen;
struct sockaddr_in clientaddr;
struct hostent *hp;
char *haddrp;
unsigned short client_port;
…………
while (1) {
clientlen = sizeof(clientaddr);
_________ = Accept(_________, (SA *)&clientaddr,
&clientlen);
hp = Gethostbyaddr((const char*)
&clientaddr.sin_addr.s_addr,
sizeof(clientaddr.sin_addr.s_addr), AF_INET);
haddrp = inet_ntoa(clientaddr.sin_addr);
client_port = ntohs(clientaddr.sin_port);
printf("server connected to %s (%s), port %u\n",
hp->h_name, haddrp, client_port);
echo(_________);
Close(_________);
    }
}
答案：connfd, listenfd, connfd, connfd
accept 之后把参数里的listenfd 转交给 connfd
server 无法支持多个 connections，因为只有一个文件描述符（listenfd）
考察学生对 网络文件描述符、listenfd、connfd的理解。

---

### 2014期末-带答案 · 第一题 17

> 出处：`原文/期末/2014期末-带答案.md` 第 257–264 行　·　模块判定：Network
> 考什么：不同协议局域网互连设备

17. 如果两个局域网高层分别采用TCP/IP协议和SPX/IPX协议，那么可以选择
的互连设备应是(      )
A. 网桥
B. 集线器
C. 路由器
D. 交换机
【答案】Ｃ
【说明】

---

### 2014期末-带答案 · 第一题 18

> 出处：`原文/期末/2014期末-带答案.md` 第 265–271 行　·　模块判定：Network
> 考什么：TCP/UDP/HTTP 基础概念

18. 下面说法正确的是（     ）
A. TCP是一种可靠的无连接协议
B. UDP是一种不可靠的无连接协议
C. Web浏览器与web服务器通信采用的协议是HTML
D. 数字数据只能通过数字信号传输
【答案】B
【说明】Ａ应该是连接协议，Ｃ应该是HTTP，Ｄ应该还包括模拟信号

---

### 2014期末-带答案 · 第八题

> 出处：`原文/期末/2014期末-带答案.md` 第 727–786 行　·　模块判定：Network
> 考什么：socket 数量、Connection socket pair、Echo/Tiny Server

第八题（10分）网络
1．（1分）以下问题默认为IPv4协议。一个服务器拥有四个独立的固定IP地址，
那么它在 web 应用端口 80，理论上可以最多再监听______个来自一个客户端独
立的 socket 连接（客户端只有一个固定IP地址）。
答案： 4*216 – 4
服务器端  客户端  结果
4个独立固定IP  一个32位固定IP  （4*216 – 4），因为80端口本
身已用于监听端口
任意16位 port number
或者
（4*216 – 4*well-known 端
口数）
2．（2 分）在 client-server 模型中，一个连接（connection）可以由 IP
地址，端口号的组合来表示。假设客户端 IP 地址为 162.105.192.178，内网
IP为192.168.100.121。HTTP服务器端IP地址为208.216.181.15。
服务器使用的是默认监听端口号。
指出下面这个网页浏览器应用的 Connection socket pair 有什么错误，
并简要说明原因？
客户端IP：端口号  服务器端IP：端口号
192.168.100.121:15321  208.216.181.15:25
答案：
192.168.100.121不对，原因：不能用内网IP；
25应该是80，原因：网页浏览器应用的默认监听端口是80端口。
3.(4分)在Echo Server程序中，客户端（Client）与服务器端（Server）
通过 socket进行一系列的命令和数据交互。
23

<!-- ===== page 24 ===== -->

注意：客户端Connect命令包含在其Open_clientfd命令中。
请在下图中用单向箭头标出这些交互步骤。例如，当 Client给Server端
发送某个命令或者数据时，则需要在 Client 端相应代码行，朝向 Server 端相
应代码行画一条单向箭头。
答案：
clientfd = Open_clientfd(host, port); --------à
connfd=Accept(listenfd, (SA*)&clientaddr, &clientlen);
Rio_writen(clientfd, buf, strlen(buf)); --------à
while((n=Rio_readlineb(&rio,buf, MAXLINE)) != 0)
Rio_readlineb(&rio, buf, MAXLINE); ß-----------
Rio_writen(connfd, buf, n);
Close(clientfd); -----------à Close(connfd);
24

<!-- ===== page 25 ===== -->

4.关于Tiny Server 程序，请回答下列问题。
a.（1分）下面这段服务器代码用来生成内容的文件是哪个参数？
b.（1分）所生成的内容是静态还是动态？请简述原因。
c.（1分）如果支持多个客户端请求，下面程序需要添加一个什么功能？
/* Return first part of HTTP response */
    sprintf(buf, "HTTP/1.0 200 OK\r\n");
        Rsipor_iwnrtift(ebnu(ff,d ," Sbeurfv,e rs:t rTlienny( bWuefb) )S;e rver\r\n");
    Rio_writen(fd, buf, strlen(buf));
     /* Real server would set all CGI vars here */
   sDeutpe2n(vf(d",Q USETRDYO_USTT_RFIINLGE"N,O )c;g i/a*rRgesd,i r1e)c;t   stdout to socket and
client */
  Execve(filename, emptylist, environ);/* Run CGI prog  */
  答案
ab..  动fi态le，n因am为e调  用了exec函数启动新的程序（execve执行文件），而非静态
fci.l 可e 以na通m过e 多进程、多线程或IO多路复用进行更改

---

### 2015期末-20160104-带答案 · 第一题 17

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 245–251 行　·　模块判定：Network
> 考什么：HTTP 命令与静态/动态内容

17. HTTP协议中，哪个命令可以用来获取动态内容？
A.  HEAD
B.  GET
C.  POST
D.  PUT
答案：B或C都正确
说明：POST只能用于获得静态内容

---

### 2015期末-20160104-带答案 · 第一题 18

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 252–261 行　·　模块判定：Network
> 考什么：HUB/帧头/IP 地址分类与动态分配

18. 下列关于计算机网络概念的说法中，哪一项是正确的？
A.  HUB会把它任意端口上接收到的帧只转发到它的目的地去
B.  当在不同的LAN中的主机A和主机B通信的过程中，他们的数据包中的
LAN frame header不会变化
C.  162.105.0.0是一个B类地址
D.  同一台主机每次进入相同的网络，通过动态地址分配的到的IP地址总是
相同的
答案：C
说明：HUB会广播它任意端口上接收到的帧；LAN frame header的目的地地址
在经历的不同的LAN中会不断调整；动态分配地址和主机地址没有唯一映射关系

---

### 2015期末-20160104-带答案 · 第七题

> 出处：`原文/期末/2015期末-20160104-带答案.md` 第 649–680 行　·　模块判定：Network
> 考什么：协议栈数据包类型与软件实现、互联网概念

第七题（10分）网络
1. 请根据 web 应用在计算机网络中的定义以及其在协议栈自上而下在软件中的
实现，把以下关键字填入表格
注：同一个关键词可能被填入多次；不是每一个关键词都必须被填入
Streams (end to end), Datagrams, web content, IP, TCP, UDP, K
ernel code, User code
协议  数据包类型  软件实现
HTTP
答案：（每空1分，共8分）
协议  数据包类型  软件实现
HTTP  Web content  User code
TCP  Streams  Kernel code
IP  Datagrams  Kernel code
2. 以下关于互联网的说法中哪些是正确的？并简要说明原因
A. 在client-server模型中，server通常使用监听套接字listenfd和多
个client同时通信
B. 在client-server模型中，套接字是一种文件标识符
C. 准确地说，IP地址是用于标识主机的adapter (network interface ca
rd)，并非主机
D. Web是一种互联网协议
E. 域名和IP地址是一一对应的
F. Internet是一种internet
答：
答案：B, C, F（全对得2分，有错得0分，部分对得1分）
说明的原因供评分时参考
24

<!-- ===== page 25 ===== -->

说明：server会为每一个client单独创建一个套接字进行通信；Web是一种基
于HTTP协议的互联网应用；一个域名可以对应多个IP地址，一个IP地址也可
以对应多个域名

---

### 2016期末-带答案 · 第一题 16

> 出处：`原文/期末/2016期末-带答案.md` 第 221–228 行　·　模块判定：Network
> 考什么：IP 协议特性与域名到 IP 的映射

16. 关于IP，以下说法正确的是：
A.  IP协议提供了可信赖的主机与主机之间的数据包传输能力
B.  IP地址的长度固定为32位
C.  一个域名可以映射到多个IP，但一个IP不能被多个域名映射
D.  一个域名可以不映射到任何IP
答案：D
A错误，不可信赖；B错误，如IPv6地址就是128位的；C错误，存在多个域名
映射到一个IP的情况

---

### 2016期末-带答案 · 第一题 17

> 出处：`原文/期末/2016期末-带答案.md` 第 229–236 行　·　模块判定：Network
> 考什么：HTTP 端口、TCP 可靠性与连接语义

17. 关于以下说法，以下说法正确的是：
A.  HTTP协议规定服务器端使用80端口提供服务
B.  使用TCP来实现数据传输一定是可靠的
C.  Internet上的两台的主机要通信必须先建立端到端连接
D.  在Linux中只能通过Socket接口进行网络编程
答案：B
A错误，80是默认端口而非必须；C错误，IP协议本身不基于连接，传输层中的
UDP协议便不基于连接；D错误，可以通过网卡驱动接口直接收发数据。

---

### 2016期末-带答案 · 第一题 18

> 出处：`原文/期末/2016期末-带答案.md` 第 237–246 行　·　模块判定：Network
> 考什么：HTTPS 取文件时各层协议的必要性

18. 假设有一个 HTTPS（基于 HTTP 的一种安全的应用层协议）客户端程序想要
通过一个 URL 连接一个电子商务网络服务器获取一个文件，并且这个服务器
URL的IP地址是已知的，以下哪种协议是一定不需要的？
A.  HTTP
B.  TCP
C.  DNS
D.  SSL/TLS
答案：C
DNS的作用是返回URL对应的IP地址，因为已知，所以不需要。其他协议都是必
须的，因为HTTPS是基于HTTP，SSL以及TCP一种协议。

---

### 2016期末-带答案 · 第七题

> 出处：`原文/期末/2016期末-带答案.md` 第 687–745 行　·　模块判定：Network
> 考什么：并发 echo server 套接字程序填空

第七题（12分）
下面是一个基于进程的并发echo server的主要代码（省略了与本题无关的部分），
每段代码都注释了相应的功能，请补充空缺的代码（可能是0行或多行）。请确保
任何由你打开的文件描述符都被显式地关闭。
int open_listenfd(char *port) {
  struct addrinfo hints, *listp, *p;
  int listenfd, optval = 1;
  /* Get a list of potential server addresses */
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_flags = AI_PASSIVE | AI_ADDRCONFIG;
  hints.ai_flags |= AI_NUMERICSERV;
  Getaddrinfo(NULL, port, &hints, &listp);
  /* Walk the list for one that we can bind to */
  for (p = listp; p; p = p->ai_next) {
    /* Create a socket descriptor. If failed, try the next */
    if ((listenfd = socket(p->ai_family,
      p->ai_socktype, p->ai_protocol)) < 0)
          (1)
    /* Eliminates error from bind */
    Setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR,
      (const void *)&optval, sizeof(int));
    /* Bind the descriptor to the address */
    if (bind(listenfd, p->ai_addr, p->ai_addrlen) == 0)
          (2)     else /* Success, use the current one */
          (3)          /* Bind failed, try the next */
  }
      (4)
  if (!p) return -1; /* No address worked */
  /* Make it a listening socket*/
  if (listen(listenfd, LISTENQ) < 0) {
        (5)
    return -1;
  }
  return listenfd;
}
22

<!-- ===== page 23 ===== -->

vvooiidd  ehcahnod(leirn(t inftd) ;si g/*)  {se rvice a client via fd */
   wrheitluern (;w aitpid(-1, 0, WNOHANG) > 0);
}in t main(int argc, char **argv) {
   isnotck lleins_tte ncfldi,e nctolnennf;d;
   struct sockaddr_storage clientaddr;
   Sliigsntaeln(fd    =  (O1p0e)n _ l i s,t ehnafndd(laerrg)v;[ 1]);
   w hilec l(i1e)n t{le n = sizeof(struct sockaddr_storage)
       i f( 6()F o r k=( )A c=c=e p0t)(  {  (7)  , (SA *)&clientaddr, &clientlen);
         /  *   C(h8i)l d   s e rvices client and close fd */
       }  exit(0); /* Child exits */
    }      (9)
}
（  第(9)空3分，其余每空1分; 共12分）
答(1案) ： continue;
((23))  bCrleoaske(; listenfd);
((45))   FCrleoesaed(dlriisntfeon(fldi)s;t  p);
(6)   connfd
((78))   lCilsotseen(fldi stenfd); echo(connfd); Close(connfd);
((190))   CSlIoGsCeH(LcDo nnfd);

---

### 2017期末-无答案 · 第一题 16

> 出处：`原文/期末/2017期末-无答案.md` 第 189–195 行　·　模块判定：Network
> 考什么：本地端口、私有 IP 与服务器端口

16. 一台处于校园网内的笔记本电脑访问一台处于公网上的服务器上的网页服务。
网页服务使用默认的80端口。以下答案有三项一定不正确，可能正确的那一
项是：
A. 笔记本在通信过程中，本地使用的端口号是80
B. 笔记本的IP地址是192.168.1.101
C. 服务器向笔记本传送网页内容时，使用的服务器端口号是80
D. 服务器的IP地址是192.168.1.102

---

### 2017期末-无答案 · 第一题 17

> 出处：`原文/期末/2017期末-无答案.md` 第 196–201 行　·　模块判定：Network
> 考什么：交换机/HUB、UDP 实时音视频、校验

17. 下列关于计算机网络概念的说法中，正确的是：
A. HUB与交换机都会转发从任意端口上收到的帧，区别在于交换机转发速度更快
B. UDP是无连接的协议，而实时音视频一般需要先呼叫对方建立连接，因此这些
应用不能基于UDP传输音视频数据
C. 处于数据链路层的以太网协议和处于传输层的TCP协议都对数据进行了校验
D. HTML是互联网上应用最为广泛的超文本传输协议

---

### 2017期末-无答案 · 第一题 18

> 出处：`原文/期末/2017期末-无答案.md` 第 202–208 行　·　模块判定：Network
> 考什么：localhost、套接字地址与 IPv4/IPv6

18. 下列关于计算机网络的说法中，错误的是：
A. 在Linux系统中，每台主机都有本地定义的域名localhost，这个域名总是
被映射为IP地址127.0.0.1
B. 在套接字编程中，既可以用网卡地址作为地址，也可以用IP地址作为地址
C. Web客户端和服务器间的交互采用的是基于文本的无连接协议
D. IPv4中的IP地址是一个32位无符号整数，IPv6中的IP地址是一个128
位无符号整数

---

### 2017期末-无答案 · 第七题

> 出处：`原文/期末/2017期末-无答案.md` 第 486–517 行　·　模块判定：Network
> 考什么：Echo 客户端/服务器流程填空与协议判断

第七题（12分）
1. 请根据Echo server/client应用的标准程序填空。
2.(cid:9)Start(cid:9)client 1.(cid:9)Start(cid:9)server
Client Server
1 2 Sockets(cid:9)
Interface
socket socket
open_listenfd
open_clientfd 3
4
Connection
5 request 6
3.(cid:9)Exchange
Client(cid:9)/(cid:9) 7 8 data
Server
Session rio_readlineb rio_writen Arewqauiet(cid:9)scto(cid:9)fnrnoemction
next(cid:9)client
close EOF 9
5.(cid:9)Drop(cid:9)client
4.(cid:9)Disconnect(cid:9)client close
1. ______________  2. ______________  3. ______________
4. ______________  5. ______________  6. ______________
7. ______________  8. ______________  9. ______________
2. 不定项选择题（全对得分，有错得0分）
A. TCP是一种实现在用户态的端到端可靠数据传输协议
B. 每一个连接在网络上的主机都会被分配一个固定的IP地址
C. IP包在网际互联时通过其帧头（LAN frame header）和包头（Internet
packet header）信息共同决定路由
D. HTTP1.0支持在同一个连接里进行多个transaction
E. Web代理作为网络缓存功能的时候对用户是显式存在的
F．10.0.0.0/12和172.16.0.0/16和192.168.0.0/20属于私有地址字段
上述正确的有：_________________

---

### 2018期末-带答案 · 第一题 10

> 出处：`原文/期末/2018期末-带答案.md` 第 176–197 行　·　模块判定：Network
> 考什么：Internet/IP 递送与帧头剥离封装

10. 下面有关计算机网络概念的叙述中，正确的是
A.  大写字母的Internet用来描述互联网的一般概念，而小写字母的internet用
来描述一种具体的实现，也就是全球IP互联网。
B.  在一个基于集线器(hub)的以太网(Ethernet)中，如果往一台主机发送一段数
据帧(frame)，那么其他主机无法看到这个帧。
C.  IP协议提供基本的命名方法和递送机制，因此我们能够借助IP协议，从一台
主机往另一台主机发送包，即使两台主机不在同一个LAN内。
D.  当一段数据通过路由器，从LAN1被发送到LAN2时，附加的互联网络包头和局
5

<!-- ===== page 6 ===== -->

域网帧头保持不变。
答案：C
  A选项出自书本645页，考察互联网的基本概念。internet应该是描述一般概
念，Internet应该是特指一个具体实现
  B选项出自书本 643-644页，考察 Ethernet协议的概念和实现形式。早期的
Ethernet协议使用Hub来连接网络主机，所有的帧传送都是广播形式。
  C选项出自书本647页，考察IP协议在网络协议栈中的角色。
  D选项出自书本645-646页，考察网络协议的基本概念。在通过路由器将数据
从一个局域网传送到另一个局域网的过程中，原来的局域网帧头会被剥离，然后附
加新的局域网帧头

---

### 2018期末-带答案 · 第一题 11

> 出处：`原文/期末/2018期末-带答案.md` 第 198–209 行　·　模块判定：Network
> 考什么：套接字接口 API 与描述符读写

11. 下面有关套接字接口(Socket API)的叙述中，错误的是
A.  套接字接口常常被用来创建网络应用
B.  Windows 10系统没有实现套接字接口
C.  getaddrinfo()和getnameinfo()可以被用于编写独立于特定版本的IP协议的
程序
D.  socket()函数返回的描述符，可以使用标准Unix I/O函数进行读写
答案：B
  A选项是套接字的基本概念
  B选项出自书本652页，考察对套接字接口的理解。几乎所有的现代操作系统
都实现了套接字接口。
  C选项出自书本656页，考察套接字接口中协议无关的设计思想。
  D选项考察对Socket API和Linux文件描述符的基本理解

---

### 2018期末-带答案 · 第一题 12

> 出处：`原文/期末/2018期末-带答案.md` 第 210–218 行　·　模块判定：Network
> 考什么：打开网页所涉及的协议栈层次

12. 使用浏览器打开网页www.pku.edu.cn的过程中，下列网络协议中，可能会被用
到的网络协议有___个
①  DNS  ② TCP  ③ IP  ④ HTTP
A.   1    B.  2    C.  3    D.  4
答案：D
  考察对于网络的整体理解。按照书上涉及的内容，要解析域名必须用到DNS协
议，要传输网页必须用到HTTP协议，HTTP协议构建于TCP/IP协议之上，因此，所
有的协议都可能会被用到。因为存在诸如HTTPS，QUIC等其他传输网页的协议，故
加了可能两字。

---

### 2018期末-带答案 · 第六题

> 出处：`原文/期末/2018期末-带答案.md` 第 652–687 行　·　模块判定：Network
> 考什么：协议分层/面向连接判断与套接字连接流程填空

第六题（10分）
1.  请在以下的表格中填入相应的内容，每个空格仅需填一项。其中第1列可填
选项包括：网络层、传输层、应用层；第2列可填选项IP、UDP、TCP、HTT
P；第3列可填选项包括：是、否。
（说明：面向连接的协议保障数据按照发送时的顺序被接收）
协议层次  协议名称  是面向连接的吗？
网络层
  HTTP
  TCP
答案：（每空1分，共6分）
协议层次  协议名称  是面向连接的吗？
网络层  IP  否
应用层  HTTP  否
传输层  TCP  是
2.  下图描述了客户端与服务器套接字连接和通信的过程，请在空格处补充相关
步骤。
22

<!-- ===== page 23 ===== -->

(cid:23)(cid:19)(cid:12)(cid:16)(cid:14)(cid:24) (cid:23)(cid:19)(cid:12)(cid:16)(cid:14)(cid:24)
(cid:1)
(cid:2)
(cid:5)(cid:19)(cid:18)(cid:18)(cid:14)(cid:12)(cid:24)(cid:15)(cid:19)(cid:18)
(cid:22)(cid:14)(cid:21)(cid:25)(cid:14)(cid:23)(cid:24)
(cid:3) (cid:10)(cid:12)(cid:12)(cid:14)(cid:20)(cid:24)
(cid:22)(cid:15)(cid:19)(cid:9)(cid:26)(cid:22)(cid:15)(cid:24)(cid:14)(cid:18) (cid:22)(cid:15)(cid:19)(cid:9)(cid:22)(cid:14)(cid:10)(cid:13)(cid:17)(cid:15)(cid:18)(cid:14)(cid:11)
(cid:22)(cid:15)(cid:19)(cid:9)(cid:22)(cid:14)(cid:10)(cid:13)(cid:17)(cid:15)(cid:18)(cid:14)(cid:11) (cid:22)(cid:15)(cid:19)(cid:9)(cid:26)(cid:22)(cid:15)(cid:24)(cid:14)(cid:18)
(cid:6)(cid:8)(cid:7)
(cid:12)(cid:17)(cid:19)(cid:23)(cid:14) (cid:4)
(cid:12)(cid:17)(cid:19)(cid:23)(cid:14)
答案：（每空1分，共4分）
1：   bind
2：   listen
3：   connect
4：   rio_readlineb

---

### 2019、2020期末-答案解析 · 2020 选择题 20

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 64–64 行　·　模块判定：Network
> 考什么：accept 建立连接与 read 阻塞

20. C。服务器端的进程通过accept来建立已连接套接字。D应阻塞在read，参看课程投影片。

---

### 2019、2020期末-答案解析 · 2020 选择题 21

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 65–66 行　·　模块判定：Network
> 考什么：主机名解析与网络字节序

21. D。送分题，根据这个命令的字面意思也能看出获得的是主机名，参数-i表示返回点分十进
制的IP地址。网络字节顺序和大端法是一回事。

---

### 2019、2020期末-答案解析 · 2019 选择题 14

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 183–183 行　·　模块判定：Network
> 考什么：迭代服务器 read 阻塞

14. B。参看课程投影片，迭代服务器的第二个客户端会在read阻塞。

---

### 2019、2020期末-答案解析 · 2019 选择题 15

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 184–184 行　·　模块判定：Network
> 考什么：网络字节序即大端

15. C。网络字节序规定为大端序，在不同的主机中可能需要转换。

---

### 2019、2020期末-答案解析 · 2019 选择题 16

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 185–185 行　·　模块判定：Network
> 考什么：CGI 文件名与参数用 ? 分隔

16. A。文件名和参数应该用?分隔。

---

### 2019、2020期末-答案解析 · 2019 解答题五

> 出处：`原文/期末/2019、2020期末-答案解析.md` 第 266–269 行　·　模块判定：Network
> 考什么：RIO/套接字 API 调用顺序

解答题五
1. bind, connect, accept, writen, readlineb, readlineb, writen。容易读解，
但注意RIO包的API名称不能记错。
2. bind, listp, listenfd。

---

### 2019期末-无答案 · 第一题 14

> 出处：`原文/期末/2019期末-无答案.md` 第 159–169 行　·　模块判定：Network
> 考什么：迭代 echo 服务器中客户端阻塞位置

14. 采用迭代的Echo 服务器服务多个客户端，假设client1 先完成连接，
并且没有结束，那么 client2 向服务器发出连接请求后，会被阻塞在下
列哪个函数上？
A. connect
4

<!-- ===== page 5 ===== -->

B. read
C. write
D. socket

---

### 2019期末-无答案 · 第一题 15

> 出处：`原文/期末/2019期末-无答案.md` 第 170–174 行　·　模块判定：Network
> 考什么：IP 地址、套接字地址与网络字节序

15. 下列关于全球IP因特网的各种概念叙述中，哪一个是错误的？
A. 一个套接字是连接的一个端点，对应了一个套接字地址
B. IPv4的因特网中，一个IP地址是一个32位无符号整数
C. 因特网主机的字节顺序与TCP/IP定义的网络字节顺序是一致的
D. IP协议提供了一种不可靠的从一台主机向其他主机的递送机制

---

### 2019期末-无答案 · 第一题 16

> 出处：`原文/期末/2019期末-无答案.md` 第 175–182 行　·　模块判定：Network
> 考什么：Web 服务器 CGI 动态内容

16. 下列关于Web服务器向客户端提供动态内容（遵从CGI标准）的叙述
中，哪一个是错误的？
A.  客户端提出的GET请求的参数在URI中传递，并用“&”字符分隔文
件名和多个参数
B.  接到客户端的请求，Web 服务器创建一个子进程执行相应的 CGI 程
序
C.  通过设置环境变量，Web服务器将URI中传递的参数传递给子进程
D.  CGI程序将动态内容重定向到与客户端关联的已连接描述符connfd

---

### 2019期末-无答案 · 第六题

> 出处：`原文/期末/2019期末-无答案.md` 第 477–523 行　·　模块判定：Network
> 考什么：client-server echo 框架与 open_listenfd 补全

第六题（10分）
下图是一个基于echo服务器的client-server框架
（1）  请给图中的编号填写相应的函数名。
（2）  请补全下面server端open_listenfd函数中缺失的操作（Line 21, Line
26和Line 34）
Line 1:  int open_listenfd(char *port)
Line 2:  {
Line 3:     struct addrinfo hints, *listp, *p;
Line 4:     int listenfd, optval=1;
Line 5:     /* Get a list of potential server addresses */
Line 6:     memset(&hints, 0, sizeof(struct addrinfo));
Line 7:     hints.ai_socktype = SOCK_STREAM;
Line 8:     hints.ai_flags = AI_PASSIVE | AI_ADDRCONFIG;
Line 9:     hints.ai_flags |= AI_NUMERICSERV;
Line 10:    Getaddrinfo(NULL, port, &hints, &listp);
14

![图](../../assets/期末/2019期末-无答案/p14-img1.jpg)

<!-- ===== page 15 ===== -->

Line 11:
Line 12:     for (p = listp; p; p = p->ai_next) {
Line 13:         /* Create a socket descriptor */
Line 14:        if ((listenfd = socket(p->ai_family, p->ai_socktype,
Line 15:                                    p->ai_protocol)) < 0)
Line 16:           continue;  /* Socket failed, try the next */
Line 17:         /* Eliminates "Address already in use" error from
bind */
Line 18:         Setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR,
Line 19:                    (const void *)&optval , sizeof(int));
Line 20:
Line 21:         if (_⑧_(listenfd, p->ai_addr, p->ai_addrlen) == 0)
Line 22:           break;  /* Success */
Line 23:         Close(listenfd);
Line 24:     }
Line 25:     /* Clean up */
Line 26:     Freeaddrinfo(___⑨___);
Line 27:     if (!p) /* No address worked */
Line 28:         return -1;
Line 29:
Line 30:     if (listen(listenfd, LISTENQ) < 0) {
Line 31:         Close(listenfd);
Line 32:         return -1;
Line 33:     }
Line 34:     return __⑩___;
Line 35:  }

---

### 2020期末-无答案 · 第一题 20

> 出处：`原文/期末/2020期末-无答案.md` 第 196–203 行　·　模块判定：Network
> 考什么：套接字接口函数与迭代 echo 服务器阻塞

20.  按照课程中的描述，套接字socket接口是一组函数，它们与UNIX I/O函数一起使用可
以构建网络应用。下列关于socket的描述中，哪一个是错误的？
A. 因特网的套接字地址存放在socketaddr_in结构中
B. 在使用套接字接口函数时，要将对应协议的特定结构指针转换成通用结构sockaddr
C. 当客户端通过connect()发起连接请求时，由服务器端的服务进程通过listen()捕获该请
求并建立监听套接字listenfd
D. 对于迭代 echo 服务器，当client1 连接到该服务器且尚未断开连接时，client2 若想要
连接该服务器会阻塞在从服务器读结果的操作上

---

### 2020期末-无答案 · 第一题 21

> 出处：`原文/期末/2020期末-无答案.md` 第 204–208 行　·　模块判定：Network
> 考什么：IPv4 地址、字节序与主机名命令

21.  下列关于全球IP因特网的描述中，哪一个是不正确的？
A. IPV4协议中，一个IP地址是一个32位无符号整数
B. IP地址结构中存放的地址总是以大端法存放的
C. 网络字节顺序是采用大端法的
D. 在Linux系统上，用hostname -i命令可以确定自己主机的域名

---

### 2021期末-无答案 · 第一题 17

> 出处：`原文/期末/2021期末-无答案.md` 第 249–252 行　·　模块判定：Network
> 考什么：TCP 协议的可靠传输与全双工特性

17.  以下符合对TCP协议描述的是
①可靠传输         ②在主机间传输     ③可以基于IP协议
④全双工           ⑤可以基于DNS
A. ①②④    B. ③④⑤    C. ①③④    D. ②④

---

### 2021期末-无答案 · 第一题 18

> 出处：`原文/期末/2021期末-无答案.md` 第 253–261 行　·　模块判定：Network
> 考什么：TCP 套接字接口函数语义

18.  对于建立客户端与服务器的TCP连接，以下关于套接字接口，正确的是：
A. 对于TCP连接而言，其可以由连接双方的套接字对四元组（双方的IP
地址和端口号）唯一确定。
B. connect函数用于客户端建立与服务器的连接，其参数中的套接字地址
结构需要指明本客户端使用的端口号
C. socket函数返回的套接字描述符，可以立即使用标准 Unix I/O 函
数进行读写
D. bind 函数用于将用于客户端的主动套接字转化为用于服务器的监听套
接字

---

### 2021期末-无答案 · 第一题 19

> 出处：`原文/期末/2021期末-无答案.md` 第 262–270 行　·　模块判定：Network
> 考什么：Web 服务、URL 与 HTTP 状态码

19.  下列有关Web服务错误的是：
A. Web服务使用客户端-服务器模型，使用了HTTP协议，可以传输文本，
HTML页面，二进制文件等多种内容
B. HTTP响应会返回状态码，它指示了对响应的处理状态
C. Web服务使用URL来标明资源，这提供了一层抽象，使得客户端仿佛在
访问远端的文件目录，而服务器处理了URL资源和具体文件/动态内容的映
射关系
D. 多个域名可以映射到同一个IP地址，但一个域名不可以映射到多个IP
地址

---

### chap 11-12 解析 · 选择题 1

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 5–11 行　·　模块判定：Network
> 考什么：TCP 协议特性判断

1.  以下符合对TCP协议描述的是

①可靠传输 ②在主机间传输 ③可以基于IP协议

④全双工 ⑤可以基于DNS

1.  ①②④ B. ③④⑤ C. ①③④ D. ②④

---

### chap 11-12 解析 · 选择题 2

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 29–37 行　·　模块判定：Network
> 考什么：TCP 套接字接口 connect/bind/listen 辨析

2\. 对于建立客户端与服务器的TCP连接，以下关于套接字接口，正确的是：

A. 对于TCP连接而言，其可以由连接双方的套接字对四元组（双方的IP地址和端口号）唯一确定。

B. connect函数用于客户端建立与服务器的连接，其参数中的套接字地址结构需要指明本客户端使用的端口号

C. socket函数返回的套接字描述符，可以立即使用标准 Unix I/O 函数进行读写

D. bind 函数用于将用于客户端的主动套接字转化为用于服务器的监听套接字

---

### chap 11-12 解析 · 选择题 3

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 53–61 行　·　模块判定：Network
> 考什么：Web 服务、HTTP 状态码与域名映射

3\. 下列有关Web服务错误的是

A. Web服务使用客户端-服务器模型，使用了HTTP协议，可以传输文本，HTML页面，二进制文件等多种内容

B. HTTP响应会返回状态码，它指示了对响应的处理状态

C. Web服务使用URL来标明资源，这提供了一层抽象，使得客户端仿佛在访问远端的文件目录，而服务器处理了URL资源和具体文件/动态内容的映射关系

D. 多个域名可以映射到同一个IP地址，但一个域名不可以映射到多个IP地址

---

### chap 11-12 解析 · 备选题 4

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 79–89 行　·　模块判定：Network
> 考什么：全球 IP 因特网：字节序/DNS/套接字说法正误

4.  下列关于全球IP因特网的说法中，正确的是

<!-- -->

1.  TCP/IP协议规定网络字节顺序取决于不同主机的字节顺序，从而方便主机和网络之间收发数据

2.  域名集合和IP地址集合的映射关系目前由http来维护

3.  多个域名可以映射到同一个IP地址，但一个域名不可以映射到多个IP地址

4.  从内核的角度来看，套接字是通信的一个端点；从用户程序的角度来看，套接字是一个有相应描述符的打开文件

---

### chap 11-12 解析 · 备选题 5

> 出处：`原文/期末/2021期末-带答案/chap 11-12 解析.md` 第 101–111 行　·　模块判定：Network
> 考什么：网络基本概念说法正误

5.  下列关于网络的说法中，错误的是

<!-- -->

1.  在TCP连接中，客户端和服务器都是指主机

2.  网络按照覆盖范围的大小可以分成局域网和广域网，其中一种流行的局域网技术是以太网

3.  网络可以被主机认为是一种I/O设备，是数据源和数据接收方

4.  路由器可以把多个不兼容的网络连接起来组成一个互联网络

---

### chap 11-12 题目 · 选择题 1

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 5–11 行　·　模块判定：Network
> 考什么：TCP 协议特性：可靠/全双工/基于IP/DNS

1.  以下符合对TCP协议描述的是

①可靠传输 ②在主机间传输 ③可以基于IP协议

④全双工 ⑤可以基于DNS

1.  ①②④ B. ③④⑤ C. ①③④ D. ②④

---

### chap 11-12 题目 · 选择题 2

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 13–21 行　·　模块判定：Network
> 考什么：TCP 套接字接口 connect/bind/listen/socket 辨析

2\. 对于建立客户端与服务器的TCP连接，以下关于套接字接口，正确的是：

A. 对于TCP连接而言，其可以由连接双方的套接字对四元组（双方的IP地址和端口号）唯一确定。

B. connect函数用于客户端建立与服务器的连接，其参数中的套接字地址结构需要指明本客户端使用的端口号

C. socket函数返回的套接字描述符，可以立即使用标准 Unix I/O 函数进行读写

D. bind 函数用于将用于客户端的主动套接字转化为用于服务器的监听套接字

---

### chap 11-12 题目 · 选择题 3

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 23–31 行　·　模块判定：Network
> 考什么：Web 服务、HTTP 状态码、URL 与域名映射

3\. 下列有关Web服务错误的是

A. Web服务使用客户端-服务器模型，使用了HTTP协议，可以传输文本，HTML页面，二进制文件等多种内容

B. HTTP响应会返回状态码，它指示了对响应的处理状态

C. Web服务使用URL来标明资源，这提供了一层抽象，使得客户端仿佛在访问远端的文件目录，而服务器处理了URL资源和具体文件/动态内容的映射关系

D. 多个域名可以映射到同一个IP地址，但一个域名不可以映射到多个IP地址

---

### chap 11-12 题目 · 备选题 4

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 35–45 行　·　模块判定：Network
> 考什么：网络字节序、DNS、域名与套接字概念

4.  下列关于全球IP因特网的说法中，正确的是

<!-- -->

1.  TCP/IP协议规定网络字节顺序取决于不同主机的字节顺序，从而方便主机和网络之间收发数据

2.  域名集合和IP地址集合的映射关系目前由http来维护

3.  多个域名可以映射到同一个IP地址，但一个域名不可以映射到多个IP地址

4.  从内核的角度来看，套接字是通信的一个端点；从用户程序的角度来看，套接字是一个有相应描述符的打开文件

---

### chap 11-12 题目 · 备选题 5

> 出处：`原文/期末/2021期末-带答案/chap 11-12 题目.md` 第 49–59 行　·　模块判定：Network
> 考什么：网络基本概念：客户端服务器指进程、以太网

5.  下列关于网络的说法中，错误的是

<!-- -->

1.  在TCP连接中，客户端和服务器都是指主机

2.  网络按照覆盖范围的大小可以分成局域网和广域网，其中一种流行的局域网技术是以太网

3.  网络可以被主机认为是一种I/O设备，是数据源和数据接收方

4.  路由器可以把多个不兼容的网络连接起来组成一个互联网络

---

### 2022期末-无答案 · 第一题 12

> 出处：`原文/期末/2022期末-无答案.md` 第 115–115 行　·　模块判定：Network
> 考什么：IPv4 地址十六进制转点分十进制

12. IP 地址可以用十六进制表示，也可以用点分十进制表示。请写出 IPv4 地址`0x24982c5f`的点分十进制表示：________________________。

---

### 2022期末-无答案 · 第一题 13

> 出处：`原文/期末/2022期末-无答案.md` 第 117–121 行　·　模块判定：Network
> 考什么：客户端-服务器套接字流程填空（accept/bind/listen/socket）

13. 下图给出了一个典型的客户端-服务器套接字交互流程。应当填在空(2)处的函数名称是：______（accept / bind / listen / socket）。

    ![图](assets/期末/2022期末-无答案/page-03.png)

    图左为客户端流程（自上而下：getaddrinfo → socket → connect → rio_written → rio_readlineb → close），图右为服务器流程（自上而下：getaddrinfo → (1) → (2) → (3) → (4) → rio_readlineb → rio_written → rio_readlineb → close），客户端与服务器之间由"连接请求"与 EOF 箭头相连；右侧括注有"open_clientfd""open_listenfd"以及"等待来自下一个客户端的连接请求"。

---

### 2022期末-无答案 · 第六题 1

> 出处：`原文/期末/2022期末-无答案.md` 第 516–567 行　·　模块判定：Network
> 考什么：Open_listenfd 中 hints.ai_socktype 取值（含服务器代码）

学完《网络编程》一章，小明迫不及待地想搭建自己的游戏服务器。他根据课本上代码写出的《网络乒乓》服务器代码如下。他在 Class Machine 上运行代码，TCP 等协议都采用默认设置。请你根据代码回答问题。

```c
 1  #include "csapp.h"
 2  #include "stdlib.h"
 3  #include "stdio.h"
 4  #define GOAL 100
 5
 6  int main(int argc, char **argv)
 7  {
 8      int listenfd, connfd;
 9      socklen_t clientlen;
10      struct sockaddr_storage clientaddr;
11      char client_hostname[MAXLINE], client_port[MAXLINE], buf[MAXLINE];
12      if (argc != 2) {
13          fprintf(stderr, "usage: %s <port>\n", argv[0]);
14          exit(0);
15      }
16      listenfd = Open_listenfd(argv[1]); // Open listen socket
17      int ball_cnt = 0;
18      while (1){
19          clientlen = sizeof(struct sockaddr_storage);
20          connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen); // Accept connection
21          Getnameinfo((SA *)&clientaddr, clientlen, client_hostname, MAXLINE,
22                      client_port, MAXLINE, 0);
23          printf("Connected to (%s, %s)\n", client_hostname, client_port);
24
25          rio_t rio;
26          Rio_readinitb(&rio, connfd);
27          Rio_readlineb(&rio, buf, MAXLINE);
28          int recv_num = atoi(buf);
29          if (recv_num == ball_cnt){
30              if (ball_cnt == GOAL){
31                  sprintf(buf, "You win!\n");
32                  Rio_writen(connfd, buf, strlen(buf));
33                  ball_cnt = 0;
34              }
35              else {
36                  sprintf(buf, "%d\n", ball_cnt+1);
37                  Rio_writen(connfd, buf, strlen(buf));
38                  ball_cnt += 2;
39              }
40          }
41          Close(connfd); // Close the connection
42      }
43      exit(0);
44  }
```

<!-- ===== page 12 ===== -->

1. 函数 Open_listenfd 要建立的是可靠的TCP连接。因此，里面有一行代码设置了 hints.ai_socktype = ______；（SOCK_STREAM / SOCK_DGRAM）。（1分）

---

### 2022期末-无答案 · 第六题 2

> 出处：`原文/期末/2022期末-无答案.md` 第 569–569 行　·　模块判定：Network
> 考什么：Getnameinfo 用途：由 IP 地址查主机名

2. 函数 Getnameinfo 的用途是查询输入的______（主机名对应的IP地址 / IP地址对应的主机名）。（1分）

---

### 2022期末-无答案 · 第六题 3

> 出处：`原文/期末/2022期末-无答案.md` 第 571–609 行　·　模块判定：Network
> 考什么：由 log.out 客户端端口推断命令行缺失参数（含客户端代码）

3. 小明的朋友们对他的游戏都不感兴趣，小明只好自己写了一个客户端来玩自己的游戏。他的客户端代码如下：

```c
 1  #include "csapp.h"
 2  #define GOAL 100
 3
 4  int main(int argc, char **argv){
 5      int clientfd;
 6      char *host, *port, buf[MAXLINE];
 7      rio_t rio;
 8
 9      if (argc != 3){
10          fprintf(stderr, "usage: %s <host> <port>\n", argv[0]);
11          exit(0);
12      }
13      host = argv[1];
14      port = argv[2];
15
16      for (int ball_cnt=0; ball_cnt<=GOAL; ball_cnt+=2){
17          clientfd = Open_clientfd(host, port);
18          Rio_readinitb(&rio, clientfd);
19          sprintf(buf, "%d\n", ball_cnt);
20          Rio_writen(clientfd, buf, strlen(buf));
21          Rio_readlineb(&rio, buf, MAXLINE);
22          Fputs(buf, stdout);
23      }
24      exit(0);
25  }
```

他在同一台主机上运行服务器和客户端。他的操作流程是：

```text
cd pingpong
nohup ./server 50000 > log.out &
./client ______ ______
```

程序正常运行完毕，"You win！"出现在了他的屏幕上。小明查看 log.out，里面的第一行是 Connected to (localhost, 33580)。请填入小明操作流程中缺失的两处信息。（2分）

---

### 2022期末-无答案 · 第六题 4

> 出处：`原文/期末/2022期末-无答案.md` 第 611–611 行　·　模块判定：Network
> 考什么：GOAL 增大后客户端报错的原因

4. 小明认为设置 #define GOAL 100 难度太低了，于是将服务器与客户端中的代码都改成了 #define GOAL 100000。他像之前一样运行服务器与客户端，结果发现客户端开始报错，并且始终没有输出"You win"。请你解释为什么修改成 100000 会让程序不能正常运行。（2分）

---

### 2022期末-无答案 · 第六题 5

> 出处：`原文/期末/2022期末-无答案.md` 第 615–615 行　·　模块判定：Network
> 考什么：在客户端补一行代码以支持更大的 GOAL

5. 请在客户端中添加一行代码，使得 #define GOAL 100000 时也能正常运行。你添加的位置是现在的第______行之后，添加的代码内容是______。（2分）

---

### 2022期末-无答案 · 第六题 6

> 出处：`原文/期末/2022期末-无答案.md` 第 617–621 行　·　模块判定：Network
> 考什么：两客户端并发连服务器时结果分析

6. 小红和小方听说了小明的高难度游戏，非常感兴趣。在小明合理配置服务器使得服务器能被访问到后，小红和小方同时在各自的电脑上运行客户端程序，与小明的服务器互动。假设小红、小方的电脑配置相同，网络延迟大小相同，并且整个过程中没有发生过重传。请推测，一段时间后，小红和小方：（ ）（2分）

- A. 有且只有一个人的屏幕上会出现"You win!"。
- B. 两个人的屏幕上都不会出现"You win!"。
- C. 两个人的屏幕上都会出现"You win!"。

---

### 2022期末-无答案 · 第六题 3（第 14 页重复）

> 出处：`原文/期末/2022期末-无答案.md` 第 625–631 行　·　模块判定：Network
> 考什么：操作流程与端口推断题面，扫描重复页

```text
cd pingpong
nohup ./server 50000 > log.out &
./client ______ ______
```

程序正常运行完毕，"You win！"出现在了他的屏幕上。小明查看 log.out，里面的第一行是`Connected to (localhost, 33580)`。请填入小明操作流程中缺失的两处信息。（2分）

---

### 2022期末-无答案 · 第六题 4（第 14 页重复）

> 出处：`原文/期末/2022期末-无答案.md` 第 633–633 行　·　模块判定：Network
> 考什么：GOAL 增大报错原因，扫描重复页

4、小明认为设置 #define GOAL 100 难度太低了，于是将服务器与客户端中的代码都改成了`#define GOAL 100000`。他像之前一样运行服务器与客户端，结果发现客户端开始报错，并且始终没有输出"You win"。请你解释为什么修改成 100000 会让程序不能正常运行。（2分）

---

### 2022期末-无答案 · 第六题 5（第 14 页重复）

> 出处：`原文/期末/2022期末-无答案.md` 第 635–635 行　·　模块判定：Network
> 考什么：补代码支持大 GOAL，扫描重复页

5、请在客户端中添加一行代码，使得`#define GOAL 100000`时也能正常运行。你添加的位置是现在的第______行之后，添加的代码内容是______。（2分）

---

### 2022期末-无答案 · 第六题 6（第 14 页重复）

> 出处：`原文/期末/2022期末-无答案.md` 第 637–641 行　·　模块判定：Network
> 考什么：多客户端并发结果分析，扫描重复页

6、小红和小方听说了小明的高难度游戏，非常感兴趣。在小明合理配置服务器使得服务器能被访问到后，小红和小方同时在各自的电脑上运行客户端程序，与小明的服务器互动。假设小红、小方的电脑配置相同，网络延迟大小相同，并且整个过程中没有发生过重传。请推测，一段时间后，小红和小方：（ ）（2分）

- A. 有且只有一个人的屏幕上会出现"You win!"。
- B. 两个人的屏幕上都不会出现"You win!"。
- C. 两个人的屏幕上都会出现"You win!"。

---

### 2022期末-答案 · 第一题 12

> 出处：`原文/期末/2022期末-答案.md` 第 21–21 行　·　模块判定：Network
> 考什么：点分十进制 IP 地址

12、36.152.44.95

---

### 2022期末-答案 · 第一题 13

> 出处：`原文/期末/2022期末-答案.md` 第 22–22 行　·　模块判定：Network
> 考什么：bind 绑定套接字

13、bind

---

### 2022期末-答案 · 第六题

> 出处：`原文/期末/2022期末-答案.md` 第 75–80 行　·　模块判定：Network
> 考什么：SOCK_STR 与客户端 fd 泄漏

 第六题 网络编程
((12))  SIPO地C址K_对S应TR的E主AM机 名
((34))  l每oc次al循ho环st 都50打00开0了  一个新的clientfd而没有关闭，导致文件数量过多，耗尽系统资源
((56))  2A2 小 C明los的e服(cl务ien器tfd在);迭  代处理两个客户端时，bal_cnt只会在某一次与其中一个客户端连
接时等于goal，之后便会设为0，而另一个客户端已经超过0，因此只会发送一次“You
win!”

---

### 2024期末-带答案 · 第一题 11

> 出处：`原文/期末/2024期末-带答案.md` 第 308–313 行　·　模块判定：Network
> 考什么：IP 递送机制、TCP 与域名映射

11. 下列关于全球 IP 因特网的描述中正确的是：
A. IP协议提供了一种从进程到进程的递送机制。
B. TCP协议提供了进程间可靠的全双工连接。
C. IP地址结构中地址的字节顺序是大端法还是小端法，要根据主机字节顺序来
确定。
D. 多个域名不可能被映射为同一个IP地址。

---

### 2024期末-带答案 · 第一题 12

> 出处：`原文/期末/2024期末-带答案.md` 第 314–337 行　·　模块判定：Network
> 考什么：套接字接口 bind/listen/connect

12. 套接字接口结合Unix I/O函数，可以创建网络应用。下列相关描述中，错
误的是：
A. socket函数成功返回描述符以后，还不能直接用于读写。
9

<!-- ===== page 10 ===== -->

B. TCP连接可以由连接双方的套接字对四元组（双方的IP地址和端口号）唯一
确定。
C. bind函数用于将服务端的主动套接字转化为监听套接字。
D. connect函数会阻塞，直到连接成功建立或者发生错误。
答案： C
A. socket()函数创建一个新的套接字，并返回一个文件描述符，这个套接字只
是被创建出来，并不是立即可用于读写数据。要进行读写操作，需要额外的步骤，
如调用 bind() 绑定地址、 listen() 启动监听（对于服务器端），或者
connect()建立连接（对于客户端）。
B. TCP 连接是通过四元组唯一标识的，这个四元组包括：客户端的 IP 地址、
客户端的端口号、服务器的 IP 地址、服务器的端口号。这四个信息组合在一起
能唯一确定一个 TCP 连接。
C. 错误，应为listen函数。 bind() 函数只是绑定套接字到特定的地址和端
口，套接字是否监听则是通过 listen() 来实现的。
D. connect() 函数用于建立与服务器的连接。对于客户端而言，connect()
是一个阻塞调用，直到连接成功建立或者出现错误（例如服务器不可达）时才会返
回。

---

### 2025期末-带答案 · 二 24

> 出处：`原文/期末/2025期末-带答案.md` 第 139–143 行　·　模块判定：Network
> 考什么：并发网络服务器 listenfd/connfd 与 SIGCHLD

24.并发网络服务器的这段程序代码：
答案：AC
解析： fork 后两边都持有 listenfd/connfd，子进程应关 listenfd 防泄漏；父进
程应回收子进程避免僵尸。父进程关 connfd 不影响子进程持有的 connfd（D 错）。E
错误，网络服务要一直运行。

---

### 2025期末-无答案 · 二 24

> 出处：`原文/期末/2025期末-无答案.md` 第 314–329 行　·　模块判定：Network
> 考什么：并发网络服务器 listenfd/connfd 与 SIGCHLD

24.并发网络服务器的这段程序代码：
int listenfd = open_listenfd("8080");
while (1) {
int connfd = accept(listenfd, NULL, NULL);
if (fork() == 0) {
echo(connfd);
exit(0);
}
close(connfd);
}
为使该程序更“正确/健壮”，下列哪些修改是必要或强烈建议的？
A. 子进程在 echo(connfd) 前应 close(listenfd)
B. 父进程在 fork 后应 close(listenfd)
C. 父进程应处理 SIGCHLD（或循环 waitpid）以回收子进程，避免 zombie
D. 父进程不应 close(connfd)，否则子进程会立即断开
E. while循环的判断条件应该加上连接出错时跳出循环

---

### 期末往年题勘误、详解 by Arthals · 2015 第一题 第17问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 11–13 行　·　模块判定：Network
> 考什么：GET/POST/PUT 均可获取动态内容（判为废题）

### 第一题

第 17 问，废题，现代 Web 中 GET/POST/PUT 等都可以用于获得动态内容。

---

### 期末往年题勘误、详解 by Arthals · 2018 第一题 第11问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 95–95 行　·　模块判定：Network
> 考什么：socket fd 可用标准 IO 读写

第 11 问，D 选项。题目里的意思应该是，用 socket 创建的 fd 在连接后是可以用 unix 标准 io 读写的。

---

### 期末往年题勘误、详解 by Arthals · 2019 第一题 第14问

> 出处：`原文/期末/期末往年题勘误、详解 by Arthals.md` 第 166–174 行　·　模块判定：Network
> 考什么：connect 返回与 accept 的时序区别

### 第一题

第 14 问，为什么阻塞在 `read` 而不是 `connect`？请注意，`connect` 并不是在 `accept` 之后才返回的。

连接成功意味着客户端发起的连接请求已经被服务端接受，此时 TCP 三次握手过程已经完成。在编程层面，客户端的 connect 函数会在连接成功时返回 0。所以只要服务端使用了 `listen`、当前连接数没超过 `listen` 的 backlog、网络畅通，那么客户端的 connect 就一定会返回 0。

服务端的 accept 函数用于**从监听队列中接受一个新的连接请求**。一旦客户端的 connect 请求到达服务器，服务器的操作系统会处理这个连接请求，完成三次握手过程，并将这个连接放入等待服务端 accept 的队列中。当服务器调用 accept 函数时，它会返回一个新的套接字描述符，这个描述符代表了与特定客户端的连接。

因此，从客户端的角度看，connect 返回 0 就表示连接成功。而服务端需要调用 accept 来正式接受这个连接，然后才能开始通过这个新的套接字与客户端进行通信。

---

### 2025Lab测验-无答案 · Lab 任务 5

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 84–89 行　·　模块判定：Network
> 考什么：ssh-keygen 公钥/私钥的存放位置（兼 Unix 工具）

5.  （2分）使用 ssh-keygen 命令可以生成用于 SSH 登录的密钥。该命令通常生成两
个文件：公钥 key.pub 和私钥 key。这两个文件应存放在：
A. 公钥留存在本地；私钥留存在本地
B. 公钥留存在本地；私钥上传到服务器
C. 公钥上传到服务器；私钥留存在本地
D. 公钥上传到服务器；私钥上传到服务器

---

### 2025Lab测验-无答案 · Lab 任务 6

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 90–96 行　·　模块判定：Network
> 考什么：scp 指定端口复制文件到远程主机

6.  （2分）远程主机 10.0.0.5的 SSH 服务端口为 2222（非默认 22 端口），若要
将本地文件 data.tar.gz 复制到该主机 ubuntu 用户的 ~/backup/目录，正确
的 scp命令是：
A. scp -p 2222 ubuntu@10.0.0.5:~/backup/ data.tar.gz
B. scp -P 2222 data.tar.gz ubuntu@10.0.0.5:~/backup/
C. scp ubuntu@10.0.0.5:2222:~/backup/ data.tar.gz
D. scp data.tar.gz ubuntu:2222@10.0.0.5:/backup/

---

### 2025Lab测验-无答案 · Lab 任务 46

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 848–852 行　·　模块判定：Network
> 考什么：IPv4/IPv6 地址长度

46. （2分）IPv4和IPv6的地址长度是多少位？
A. 32位，64位
B. 32位，128位
C. 64位，128位
D. 64位，256位

---

### 2025Lab测验-无答案 · Lab 任务 47

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 853–857 行　·　模块判定：Network
> 考什么：TCP 与 UDP 的区别

47. （2分）关于TCP和UDP协议的区别，以下说法正确的是：
A. TCP是面向连接的，UDP是无连接的
B. TCP不保证可靠性，UDP保证可靠性
C. TCP传输速度比UDP快
D. TCP支持广播，UDP不支持广播

---

### 2025Lab测验-无答案 · Lab 任务 48

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 858–862 行　·　模块判定：Network
> 考什么：/24 子网可用主机地址数量

48. （2分）IP地址192.168.1.100/24所在的子网中，可用的主机地址数量是：
A. 24
B. 254
C. 256
D. 2^24

---

### 2025Lab测验-无答案 · Lab 任务 49

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 863–868 行　·　模块判定：Network
> 考什么：10.7.74.125 的地址类别与私有地址

49. （2分）用个人笔记本连接北大无线网，可能获得的IP地址是10.7.74.125，这个
IP地址属于：
A. A类地址（0开头，加7位Net ID）
B. B类地址（10开头，加14位Net ID）
C. C类地址（110开头，加21位Net ID）
D. 私有地址（Unrouted IP addresses）

---

### 2025Lab测验-无答案 · Lab 任务 50

> 出处：`原文/Lab测验/2025Lab测验-无答案.md` 第 869–874 行　·　模块判定：Network
> 考什么：域名映射、IP 可靠性与 getaddrinfo/freeaddrinfo

50. （2分）以下说法正确的是：
A. 建立套接字连接的客户端和服务器端的IP地址不能相同
B. IP协议提供了可靠的主机与主机之间的数据包传输能力
C. 一个域名可以映射到多个IP，也可以不映射到任何IP
D. 为了防止内存泄漏，使用 getaddrinfo 函数获得的 addrinfo 链表只能调用
freeaddrinfo函数释放

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
