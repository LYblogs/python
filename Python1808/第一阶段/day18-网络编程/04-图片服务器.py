import socket
#1.创建套接字
server =socket.socket()
#2.绑定ip和端口
server.bind(("10.7.187.67",6666))
#3.开始监听
server.listen(1024)
#让服务器处于运行状态
while True:
    conversation,addr =server.accept()
    #打开图片对象
    with open("files/1.jpg","rb")as f:
        count=f.read()
        conversation.send(count)