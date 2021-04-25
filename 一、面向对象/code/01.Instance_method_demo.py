# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 上午10:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : 01.Instance_method_demo.py
# @Software: PyCharm


class User:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def instance_method(self):
        print('实例:{}'.format(self.name))

    def __str__(self):
        return '名称:{},性别:{},年龄:{}'.format(self.name, self.sex, self.age)


if __name__ == '__main__':
    new_user = User(name='yyx', sex='man', age=18)
    print(new_user)
    new_user.instance_method()
