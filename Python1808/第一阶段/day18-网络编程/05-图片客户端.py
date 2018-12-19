import socket
client =socket.socket()
client.connect(("10.7.187.100",6060))
#不断接收数据，直到接收完为止
# 创建一个空额二进制数据
data =bytes()
while True:
    # message = input("客户端:")
    # client.send(bytes(message, encoding="utf-8"))
    #
    re_data =client.recv(1024)
    # print("服务器：",re_data.decode("utf-8"))

    data+=re_data
    print("接收数据")
    if not re_data:
        break
print("接收完了")
with open("files/2.jpg","wb")as f:
    f.write(data)