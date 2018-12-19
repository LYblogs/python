from threading import  Thread,current_thread

"""
创建子线程除了直接创建Thread的对象，还可以创建这个类的子类对象

注意：一个进程中有多个线程，进程会在所有的线程结束才会结束；
     线程中的任务执行完了线程就结束了
"""
#1.声明一个类继承Thread
class DownloadThread(Thread):
    def __init__(self,file_name):
        super().__init__()
        self.file_name =file_name
    #2.重写run方法
    def run(self):
        #这个方法中的代码会在子线程当中执行
        print("开始下载：%s"%self.file_name)
        print(current_thread())

# 3.创建线程对象
d1=DownloadThread("滴滴滴")
d1.start()
d2 =DownloadThread("啊啊啊")
d2.start()
# d1.run()#直接调用run方法，会在主线程中执行


