"""__author__ = 余婷"""

import socket

client = socket.socket()
client.connect(('10.7.187.149', 9092))

# ========2.保持通话=============
while True:
    # 发送消息
    message = input('客户端:')
    client.send(message.encode('utf-8'))

    # 接收消息
    data = client.recv(1024)
    print('服务器:', data.decode('utf-8'))


# ========1.接收图片==========
# 不断接收数据，直到接收完为止
# 创建一个空的二进制数据
# data = bytes()
# while True:
#     re_data = client.recv(1024)
#     data += re_data
#     print('接收到数据!')
#     if not re_data:
#         break
#
# print('数据接收完了')
# with open('new.png', 'bw') as f:
#     f.write(data)

