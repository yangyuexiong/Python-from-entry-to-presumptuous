# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 下午2:24
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    :
# @Software: PyCharm

import time
import multiprocessing


def to_sleep(t):
    time.sleep(t)
    print('okc')
    return t


if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    # 单个任务
    # result = pool.apply_async(to_sleep, args=(2,))
    # pool.close()
    # pool.join()  # 等待所有任务完成
    # print(result.get())

    # imap:批量任务按顺序打印(对应线程池:as_completed)
    print('=== imap ===')
    for r in pool.imap(to_sleep, [2, 1, 3]):
        print(r)

    # imap_unordered:批量任务按顺序打印(对应线程池:map)
    print('=== imap_unordered ===')
    for r in pool.imap_unordered(to_sleep, [2, 1, 3]):
        print(r)