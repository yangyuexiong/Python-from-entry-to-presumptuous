# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 上午10:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : 04_01.method_use.py
# @Software: PyCharm


class A:
    a = 1
    b = 2

    def __init__(self, name):
        self.name = name

    @staticmethod
    def static_func_1():
        print('属性a:{},属性b:{}'.format(A.a, A.b))

    @staticmethod
    def static_func_2(*args):
        print(args)

    @classmethod
    def class_func(cls):
        cls.static_func_2(cls.a, cls.b)


class B(A):
    a = 100
    b = 200


class C(A):
    a = 1000
    b = 2000
    x = 3000

    @staticmethod
    def static_func_2(*args):
        print(args)
        print('yyx')

    @classmethod
    def class_func(cls):
        cls.static_func_2(cls.a, cls.b, cls.x)


if __name__ == '__main__':
    okc_b = B(name='yyx1')
    okc_b.static_func_1()
    okc_b.class_func()

    print('\n重写:类方法 与 静态方法')
    okc_c = C(name='yyx2')
    okc_c.static_func_1()
    okc_c.class_func()
