# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午2:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : threading_demo.py
# @Software: PyCharm


import threading
import time


def func_1(name):
    print('func_1 start')
    print(name)
    time.sleep(2)
    print('func_1 end')


def func_2(name):
    print('func_2 start')
    print(name)
    time.sleep(4)
    print('func_2 end')


class Func1(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('func_1 start')
        print(self.name)
        time.sleep(2)
        print('func_1 end')


class Func2(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('func_2 start')
        print(self.name)
        time.sleep(4)
        print('func_2 end')


if __name__ == '__main__':
    # 直接创建线程
    # thread_1 = threading.Thread(target=func_1, args=('yyx1',))
    # thread_2 = threading.Thread(target=func_2, args=('yyx2',))

    # 继承方式
    thread_1 = Func1(name='yyx1')
    thread_2 = Func2(name='yyx2')

    start_time = time.time()

    # 守护线程,当主线程结束时候,把守护线程也同时关闭
    # thread_1.setDaemon(True)
    # thread_2.setDaemon(True)

    # 启动线程
    thread_1.start()
    thread_2.start()

    # 主线程会阻塞等待这些join线程执行完成
    thread_1.join()
    thread_2.join()

    print('last time:{}'.format(time.time() - start_time))


