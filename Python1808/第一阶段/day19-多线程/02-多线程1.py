"""
python中提供了threading模块

默认创建的线程叫主线程，其他的线程叫子线程。如果希望代码在子线程中执行，必须手动创建线程对象。
"""
import threading
import time,datetime

def download(film_name):
    print("开始下载%s"%film_name,datetime.datetime.now())
    time.sleep(5)#程序执行到这个地方，线程会阻塞（停5s），再执行后面的代码
    print("%s下载结束"%film_name,datetime.datetime.now())
    print(threading.current_thread())


if __name__ == '__main__':

    # 1.创建线程对象
    """
    Thread - 线程类
    Thread(target=函数名,args=参数列表） - 直接创建线程对象 - 返回线程对象
     函数名 - 需要在当前创建的子线程中执行的函数的函数变量
     参数列表 - 元组，元组的元素
     """
    t1 = threading.Thread(target=download,args=("海绵宝宝",))
    t2 = threading.Thread(target=download,args=("花园宝宝",))
    # 2.在子线程中执行任务
    """
    在这儿就是在调用ti对应的线程中调用download函数，并且传递参数“海绵宝宝”
    """
    t1.start()
    t2.start()