import socket
from threading import Thread
class Receive(Thread):
    def __init__(self,addr,conversation):
        super().__init__()
        self.conversation=conversation
        self.addr = addr
    def run(self):
        while True:
            message = self.conversation.recv(1024).decode("utf-8")
            print(self.addr, ":" + message, sep="")
server =socket.socket()
server.bind(("10.7.187.67",6666))
server.listen(100)
while True:
    conversation,addr=server.accept()
    #给服务器发送请求的客户端连接创建一个子线程。在子线程中处理每个请求
    r1 = Receive(addr,conversation)
    r1.start()