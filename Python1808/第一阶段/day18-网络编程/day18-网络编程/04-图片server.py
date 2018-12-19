"""__author__ = 余婷"""
import socket

# 1.创建套接字对象
server = socket.socket()

# 2.绑定ip和端口
server.bind(('10.7.187.149', 9093))

# 3.监听
server.listen(512)
print('开始监听!')

while True:
    # 4.接收请求
    conversation, addr = server.accept()
    print(addr)
    # ==========2.保持通话==============
    while True:
        # 接收消息
        data = conversation.recv(1024)
        print('客户端:', data.decode('utf-8'))

        # 发送消息
        message = input('服务器:')
        conversation.send(message.encode('utf-8'))

    # ===========1.发送图片=============
    # with open('luffy.png', 'br') as f:
    #     content = f.read()
    #     conversation.send(content)
    #
    # conversation.close()


