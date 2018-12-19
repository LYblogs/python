import socket
import requests
import json

client = socket.socket()
client.connect(("10.7.187.67", 6666))
while True:
    message = input("客户端：")
    client.send(message.encode("utf-8"))
    if message == "1":
        data_image = bytes()
        while True:
            re_data = client.recv(1024)
            data_image += re_data
            print("接收数据")
            if len(re_data) < 1024:
                break
        print("接收完成")
        with open("files/4.jpg", "wb")as f:
            f.write(data_image)
    if message == "2":
        data = bytes()
        while True:
            re_data = client.recv(1024)
            data += re_data
            print("aaa", re_data)
            print("接收数据")
            if len(re_data) < 1024:
                break
        print("接收完成")
        with open("files/a.json", "w", encoding='utf-8')as f:
            f.write(data.decode(encoding='utf-8'))
    if message == "3":
        re_data = client.recv(1024)
        print("服务器：", re_data.decode("utf-8"))
        break
