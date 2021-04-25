# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午4:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : threading_condition_demo.py
# @Software: PyCharm

import time

from concurrent.futures import ThreadPoolExecutor


def func_1(t):
    print('func_1 start')
    time.sleep(t)
    print('func_1 end')
    return t


def func_2(t):
    print('func_2 start')
    time.sleep(t)
    print('func_2 end')
    return t


executor = ThreadPoolExecutor(max_workers=2)

if __name__ == '__main__':
    task_1 = executor.submit(func_1, (0))  # 通过 submit() 提交执行的函数到线程池中
    task_2 = executor.submit(func_2, (2))

    print('=== done ===')
    print(task_1.done())  # done() 用于判定某个任务是否完成
    print(task_2.done())

    print('=== result ===')
    print(task_1.result())  # result() 获取任务的返回值
    print(task_2.result())

    print('=== cancel ===')
    print(task_1.cancel())  # cancel() 关闭任务(必须在任务未开始时才会生效)
    print(task_2.cancel())
