import socket

# 1.创建套接字对象
client =socket.socket()

#2.连接服务器
"""
connect((ip,端口号))
"""
client.connect(("10.7.187.67",8083))
while True:
#3.发送消息
    message =input("client:")
    client.send(bytes(message,encoding="utf-8"))

# 4.接收消息
    re_data =client.recv(1024)
    print("server：",re_data.decode("utf-8"))