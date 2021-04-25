# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 下午1:31
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : consume_IO_compared.py
# @Software: PyCharm

import time

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def to_sleep(t):
    time.sleep(t)
    return t


if __name__ == '__main__':
    # 多线程
    with ThreadPoolExecutor(2) as executor:
        all_task = [executor.submit(to_sleep, (t)) for t in [2] * 30]
        start_time = time.time()
        for f in as_completed(all_task):
            data = f.result()
            print('data:{}'.format(data))
        print('多线程:last time:{}'.format(time.time() - start_time))

    # 多进程
    with ProcessPoolExecutor(2) as executor:
        all_task = [executor.submit(to_sleep, (t)) for t in [2] * 30]
        start_time = time.time()
        for f in as_completed(all_task):
            data = f.result()
            print('data:{}'.format(data))
        print('多进程:last time:{}'.format(time.time() - start_time))
