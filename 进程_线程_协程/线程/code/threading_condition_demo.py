# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午4:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : threading_condition_demo.py
# @Software: PyCharm

import threading


class Problem(threading.Thread):

    def __init__(self, cond):
        super().__init__(name='提问者')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print('{}:{}'.format(self.name, '1+1=？'))
            self.cond.notify()

            self.cond.wait()
            print('{}:{}'.format(self.name, '2+2=？'))
            self.cond.notify()

            self.cond.wait()
            print('{}:{}'.format(self.name, '=== 结束提问 ==='))
            self.cond.notify()


class Answer(threading.Thread):

    def __init__(self, cond):
        super().__init__(name='回答者')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{}: === 开始提问 ==='.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:等于 2'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:等于 4'.format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = threading.Condition()
    thread_1 = Problem(cond=cond)
    thread_2 = Answer(cond=cond)
    thread_1.start()
    thread_2.start()
