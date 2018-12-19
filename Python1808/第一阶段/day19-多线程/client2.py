import socket
client=socket.socket()
client.connect(("10.7.187.67",6666))
while True:
    message =input("自己：")
    client.send(message.encode("utf-8"))