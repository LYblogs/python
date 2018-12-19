"""__author__ = 余婷"""

import socket

# 1.创建套接字对象
client = socket.socket()

# 2.连接服务器
"""
connect((ip, 端口))
"""
client.connect(('172.21.203.2', 8088))

# 3.发送消息
message = input('>>')
client.send(message.encode('utf-8'))

# 4.接收消息
re_data = client.recv(1024)
print(re_data.decode('utf-8'))

