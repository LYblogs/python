"""
一个线程默认有一个线程，这个线程叫主线程，默认情况下所有的任务（代码）都是在主线程中执行的

"""
import time,datetime

def download(film_name):
    print("开始下载%s"%film_name,datetime.datetime.now())
    time.sleep(5)#程序执行到这个地方，线程会阻塞（停5s），再执行后面的代码
    print("%s下载结束"%film_name,datetime.datetime.now())

if __name__ == '__main__':
    download("喜洋洋与灰太狼")
    download("花园宝宝")