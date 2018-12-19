import requests
import json
import re
import threading
def download(url:str):
    image_data=requests.get(url).content
    file_name=url.split("/")[-1]
    with open("images/"+file_name,"wb")as f:
        f.write(image_data)

url1 ="https://www.apiopen.top/satinApi?type=1&page=1"
response =requests.get(url1)
json1 =response.json()
data =json1["data"]
for dict1 in data:
    #拿到一个图片地址，就为他创建一个线程对象，用来在子线程中下载这种图片
    t=threading.Thread(target=download,args=(dict1["profile_image"],))
    # t.start()
# print("下载完成")

# with open("files/a.json","w",encoding="utf-8")as f:
#     f.write(json.dumps(json1,ensure_ascii=False))
url1 ="https://www.apiopen.top/satinApi?type=1&page=1"
response =requests.get(url1)
text =response.text
re_str =r'"profile_image":(.+?),'
result =re.findall(re_str,text)
print(result)
# result =re.findall(re_str,json1)
# print(result)