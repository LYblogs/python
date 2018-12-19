"""
socket又叫套接字，指的是实现通信过程的两个端。等待请求的一段叫服务端套接字，发送请求的叫客户端

python中有一个socket模块，来支持socket编程
"""
import socket

#===============服务器套接字==================
#1.创建套接字对象
"""
socket(family,type)
family - 设置ip类型  AF_INET - ipv4  AF_INET6 - ipv6
type - 设置传输协议类型 SOCK_STREAM - tcp协议
"""
#创建一个基于tcp和ipv4的套接字对象，
server = socket.socket()

# 2.绑定ip地址和端口
"""
bind(（ip,端口号）)
ip - 服务器对应的计算机的ip地址，字符串
端口号 - 用来区分计算机上不同的服务(应用);是一个数字，范围是（0~65535）；
但是其中1024及以下的是著名端口，用来表示一些特殊的应用
同一时间一个端口只能对应一个服务器
"""
server.bind(("10.7.187.67",8083))

#3.开始监听请求
"""
listen(最大监听数)
最大监听数 - 用来设置当前服务器一次可以处理多少个请求
"""
server.listen(100)
print("开始监听!")

#4.让服务器一直处于启动状态
while True:
    #5.接收客服端请求，返回请求地址（addr）和建立的会话；
    # 会阻塞线程（程序运行到这个地方会停下来，直到有客户端给当前服务器发送请求为止）
    conversation,addr=server.accept()
    # print("接受到请求：",addr)

    #6.接收消息（客户端发送给服务器的消息）
    re_data=conversation.recv(1024)
    print("client:",re_data.decode("utf-8"))
    """
    recv(缓存大小) -获取客 户端给服务器发送的消息，返回值是二进制
    缓存大小 - 决定一次可以接收的数据的最大字节数
    """
    #7.发送数据（服务器给客户端发送数据）
    """
    send(数据) - 将指定的数据发送给客户端
    数据 - 要求必须是二进制
    
    字符串（str）转二进制（bytes）
    a.bytes（字符串，"utf-8"）
    b.字符串.encode("utf-8")
    
    二进制转换成字符串
    a.str(二进制数据，"utf-8")
    b.二进制.decode（"utf-8"）
    """
    message =input("server:")
    conversation.send(bytes(message,encoding="utf-8"))

    #8.关闭连接
    # conversation.close()