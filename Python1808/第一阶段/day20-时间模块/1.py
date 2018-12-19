import socket
server = socket.socket()
server.bind(("10.7.187.67",6666))
server.listen(1024)
print("开始监听")
while True:
    conversation,addr =server.accept()
    print(addr)
    with open("aa.html","r",encoding="utf-8")as f:
        message=f.read()
    conversation.send(message.encode("utf-8"))