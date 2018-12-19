from threading import Thread
import time,datetime,random
"""
线程对象.join（） - 等待线程中的任务执行完成

"""
class Download(Thread):
    def __init__(self,file_name):
        super().__init__()
        self.file_name=file_name

    def run(self):
        print("开始下载%s"%self.file_name)
        a=random.randint(5,12)
        time.sleep(a)
        print("%s下载结束"%self.file_name,"耗时%d秒"%a)

if __name__ == '__main__':

    t1 =Download("花园宝宝")
    t2 =Download("海绵宝宝")
    time1 =time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time2 =time.time()
    print("耗时：",time2-time1)