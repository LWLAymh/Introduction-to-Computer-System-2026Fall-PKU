## 第十章I/O部分选择（4分）

1\. 下列关于系统I/O的说法中，正确的是（）：

A. Linux shell创建的每个进程开始时都有三个打开的文件：标准输入（描述符为0），标准输出（描述符为1），标准错误（描述符为2），这使得程序始终不能使用保留的描述符0,1,2读写其他文件。

B. Unix I/O的read/write函数是异步信号安全的，故可以在信号处理函数中使用。

C. RIO函数包的健壮性保证了对于同一个文件描述符，任意顺序调用RIO包中的任意函数不会造成问题。

D. 使用int fd1 = open(“ICS.txt”, O_RDWR); 打开ICS.txt文件后，再用int fd2 = open(“ICS.txt”, O_RDWR); 再次打开文件，会使得fd1对应的打开文件表中的引用计数refcnt加一。

答案：B（简单）

1.  描述符0，1，2可以重定向到其他文件。

2.  正确，教材P534。

3.  有缓冲区和无缓冲区的不可以交叉使用，教材P629。

4.  多次打开文件应该对应着多个打开文件表，教材P635。

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

答案：D（中等）
