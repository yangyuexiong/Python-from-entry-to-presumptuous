# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午6:19
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : 06_01.inherit_demo1.py
# @Software: PyCharm


class A1:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('A1 类的 name:{}'.format(self.name))


class A2:

    def __init__(self, sex):
        self.sex = sex

    def get_name(self):
        print('A2 类的 sex:{}'.format(self.sex))


class A3:

    def __init__(self, age):
        self.age = age

    def get_name(self):
        print('A3 类的 age:{}'.format(self.age))


class Y1(A1, A2, A3):

    def __init__(self, name, sex, age):
        super().__init__(name)  # init A1
        super(A1, self).__init__(sex)  # init A2
        super(A2, self).__init__(age)  # init A3


class Y2(A1, A2, A3):

    def __init__(self, name, sex, age):
        super().__init__(name)  # init A1
        super(A1, self).__init__(sex)  # init A2
        super(A2, self).__init__(age)  # init A3

    def get_name(self):
        print('Y2 类的 name:{} sex:{} age:{}'.format(self.name, self.sex, self.age))

    def show_x(self):
        super().get_name()  # 调用 A1 类的 get_name()
        super(A1, self).get_name()  # 调用 A2 类的 get_name()
        super(A2, self).get_name()  # 调用 A3 类的 get_name()


if __name__ == '__main__':
    a1 = A1('asd')
    a1.get_name()
    a2 = A2('man')
    a2.get_name()
    a3 = A3('99')
    a3.get_name()
    print('\n')

    y1 = Y1(name='okc', sex='man', age='1')
    y1.get_name()

    print('\n')
    y2 = Y2(name='yyx', sex='man', age='2')
    y2.get_name()
    y2.show_x()

    # 查看继承顺序
    import inspect

    print(inspect.getmro(Y2))
    print(Y2.mro())
