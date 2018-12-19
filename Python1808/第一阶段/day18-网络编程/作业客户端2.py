import socket
client =socket.socket()
client.connect(("10.7.187.67",6666))
while True:
    message =input("客户端：")
    client.send(message.encode("utf-8"))
    if message =="拜拜":
        break
    re_data =client.recv(1024)
    print("服务器：",re_data.decode("utf-8"))
    if re_data.decode("utf-8")== "拜拜":
        break