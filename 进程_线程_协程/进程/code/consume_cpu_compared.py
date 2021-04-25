# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 下午1:18
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : consume_cpu_compared.py
# @Software: PyCharm

import time

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # 多线程
    with ThreadPoolExecutor(2) as executor:
        all_task = [executor.submit(fib, (n)) for n in range(25, 40)]
        start_time = time.time()
        for f in as_completed(all_task):
            data = f.result()
            print('data:{}'.format(data))
        print('多线程:last time:{}'.format(time.time() - start_time))

    # 多进程
    with ProcessPoolExecutor(2) as executor:
        all_task = [executor.submit(fib, (n)) for n in range(25, 40)]
        start_time = time.time()
        for f in as_completed(all_task):
            data = f.result()
            print('data:{}'.format(data))
        print('多进程:last time:{}'.format(time.time() - start_time))
