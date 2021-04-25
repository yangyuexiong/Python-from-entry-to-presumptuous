# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午6:14
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : 05.private_property_demo.py
# @Software: PyCharm


class A:
    _y = '_y'
    __y = '__y'

    def _a(self):
        print('_a')

    def __a(self):
        print('__a')

    def get_y2(self):
        print(self.__y)


if __name__ == '__main__':
    a = A()
    print(A.__dict__)

    print(a._y)
    print(a._A__y)  # 正确调用双下划线的方式,在开发过程中不建议使用

    a._a()
    a._A__a()  # 正确调用双下划线的方式,在开发过程中不建议使用

    a.get_y2()  # 正确调用双下划线的方式,建议使用

    # 直接调用双下划线的属性或方法会报错
    a.__a()
    a.__y()
