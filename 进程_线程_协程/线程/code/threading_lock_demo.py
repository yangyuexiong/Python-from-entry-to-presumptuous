# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午4:32
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : threading_lock_demo.py
# @Software: PyCharm

import threading
from threading import Lock, RLock

total = 0
lock = Lock()
r_lock = RLock()


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


def add_02():
    global total
    global r_lock
    for i in range(1000000):
        r_lock.acquire()
        r_lock.acquire()
        total += 1
        r_lock.release()
        r_lock.release()


def desc_02():
    global total
    global r_lock
    for i in range(1000000):
        r_lock.acquire()
        r_lock.acquire()
        total -= 1
        r_lock.release()
        r_lock.release()


if __name__ == '__main__':
    thread_1 = threading.Thread(target=add)
    thread_2 = threading.Thread(target=desc)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print(total)

    thread_3 = threading.Thread(target=add_02)
    thread_4 = threading.Thread(target=desc_02)
    thread_3.start()
    thread_4.start()
    thread_3.join()
    thread_4.join()
    print(total)