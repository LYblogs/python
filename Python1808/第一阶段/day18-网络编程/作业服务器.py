import socket
import  requests
server =socket.socket()
server.bind(("10.7.187.67",6666))
server.listen(100)
print("开始监听！")
while True:
    #addr请求的地址  conversation建立的会话
    conversation, addr = server.accept()
    while True:
        re_data=conversation.recv(1024)
        print("客户端:",re_data.decode("utf-8"))
        if re_data.decode("utf-8")=="3":
            message = "拜拜"
            conversation.send(message.encode("utf-8"))
            break
        if re_data.decode("utf-8")=="1":
            with open("files/222.jpg","rb")as f:
                image=f.read()
                conversation.send(image)
        if re_data.decode("utf-8") == "2":
            url = "https://www.apiopen.top/satinApi"
            response = requests.get(url, {"type": 1, "page": 1})
            json= response.content
            conversation.send(json)