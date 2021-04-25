# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 下午2:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : multiprocessing_demo.py
# @Software: PyCharm

import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def to_sleep(t):
    time.sleep(t)
    print('okc')
    return t


if __name__ == '__main__':
    process = multiprocessing.Process(target=to_sleep, args=(2,))
    print(process.pid)
    process.start()
    print(process.pid)
    process.join()
    print('end')
