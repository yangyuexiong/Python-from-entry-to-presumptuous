# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 下午6:19
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : 06_01.inherit_demo1.py
# @Software: PyCharm

class A:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('name:{}'.format(self.name))


class B(A):
    def __init__(self, name, age):  # 先继承 A 类的 name, 再重写 B 类 age
        """
        调用格式一:
            父类名.方法名（对象）

        调用格式二:
            super(子类名， 对象）.方法名（）

        调用格式三:
            super().方法名（）

        :param name:
        :param age:
        """
        super().__init__(name)
        self.age = age

    def get_name(self):  # 重写 A 类 get_name()
        print('name:{},age:{}'.format(self.name, self.age))


class C:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<%s:%s:%s>' % (self.__class__.__name__, self.name, self.age)


class D(C):

    def __init__(self, name, sex):
        super().__init__(name, 99)
        self.sex = sex

    def __str__(self):
        return '<{}:{}>'.format(self.__class__.__name__, self.__dict__)


if __name__ == '__main__':
    a = A(name='okc')
    a.get_name()

    b = B(name='yyx', age='1')
    b.get_name()

    d = D(name='lol', sex='man')
    print(d)
