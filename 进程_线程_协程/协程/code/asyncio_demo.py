# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午2:49
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : asyncio_demo.py
# @Software: PyCharm

import time
import asyncio


async def task_001(i):
    print('hello:{}'.format(i))
    result = await asyncio.sleep(1)
    print('world:{}'.format(i))
    return result


async def main_01():
    """
    单个任务
    :return:
    """
    task = asyncio.create_task(task_001(99))  # 创建任务
    await task


async def main_02():
    """
    多个任务
    :return:
    """
    # gather
    t1 = asyncio.create_task(task_001(1))
    t2 = asyncio.create_task(task_001(2))
    t3 = asyncio.create_task(task_001(3))
    t4 = asyncio.create_task(task_001(4))
    task_1 = [t1, t2]
    task_2 = [t3, t4]
    group1 = asyncio.gather(*task_1)  # 分组
    group2 = asyncio.gather(*task_2)  # 分组
    await asyncio.gather(group1, group2)  # 创建多个任务

    # wait
    task = [asyncio.create_task(task_001(i)) for i in range(3)]  # 创建多个任务
    await asyncio.wait(task)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main_01())  # 启动协程
    print(time.time() - start_time, '\n')

    start_time = time.time()
    asyncio.run(main_02())
    print(time.time() - start_time)
