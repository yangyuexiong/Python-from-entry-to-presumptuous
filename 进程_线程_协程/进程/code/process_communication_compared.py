# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 下午2:38
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : process_communication_compared.py
# @Software: PyCharm

import time
from multiprocessing import Process, Queue, Manager, Pool, Pipe


def producer(q):
    print('=== 生产者 ===')
    q.put('a')
    time.sleep(1)


def consumer(q):
    print('=== 消费者 ===')
    data = q.get()
    print(data)


def producer_to_pipe(p):
    print('=== 生产者 ===')
    p.send('a')
    time.sleep(1)


def consumer_to_pipe(p):
    print('=== 消费者 ===')
    data = p.recv()
    print(data)


if __name__ == '__main__':
    """
    如果使用 from queue import Queue 会出现异常
    multiprocessing.Queue 与 queue.Queue 用法基本一致
    """
    # 多进程通信(multiprocessing.Queue())
    print('=== 多进程通信:multiprocessing.Queue() ===')
    q = Queue(10)
    new_producer = Process(target=producer, args=(q,))
    new_consumer = Process(target=consumer, args=(q,))
    new_producer.start()
    new_consumer.start()
    new_producer.join()
    new_consumer.join()

    # 进程池通信(Manager().Queue())
    print('=== 进程池通信:Manager().Queue() ===')
    m_q = Manager().Queue(10)
    pool = Pool()
    pool.apply_async(producer, args=(m_q,))
    pool.apply_async(consumer, args=(m_q,))
    pool.close()
    pool.join()

    # 进程池通信(Pipe())
    print('=== 进程池通信:Pipe() ===')
    receive_pipe, send_pipe = Pipe()
    new_producer = Process(target=producer_to_pipe, args=(send_pipe,))
    new_consumer = Process(target=consumer_to_pipe, args=(receive_pipe,))
    new_producer.start()
    new_consumer.start()
    new_producer.join()
    new_consumer.join()
