# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午4:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : threading_condition_demo.py
# @Software: PyCharm

import time

from concurrent.futures import ThreadPoolExecutor, as_completed, wait

t_list = [0, 3, 1]


def func(t):
    print('func start')
    time.sleep(t)
    print('func end')
    return t


executor = ThreadPoolExecutor(max_workers=2)

if __name__ == '__main__':
    # 批量创建任务
    all_task = [executor.submit(func, (t)) for t in t_list]

    # 方式一
    for f in as_completed(all_task):
        data = f.result()
        print('=== data ===')
        print(data)  # 按照完成的顺序打印

    # 方式二
    for f in executor.map(func, t_list):
        data = f  # 已经把 f.result() 也执行了
        print('=== data ===')
        print(data)  # 按照t_list的顺序打印
