# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 上午10:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : 04_01.method_use.py
# @Software: PyCharm


def y():
    pass


class User:
    test_str = 'test_str'
    test_int = 33
    test_tuple = ("t1", "t2", "t3")
    test_list = ['a', 'b', 'c']
    test_dict = {
        "key_1": "value_1",
        "key_2": "value_2"
    }
    test_list_01 = ['x', 'y', 'z']
    test_dict_01 = {"yyx": "okc"}
    test_func = y

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def func_01(self):
        """func_01"""
        print('>>> 调用实例方法:{}'.format(self.func_01.__doc__))
        print('>>> 打印属性\n')
        print('{}\n{}\n'.format(type(self.test_str), self.test_str))
        print('{}\n{}\n'.format(type(self.test_int), self.test_int))
        print('{}\n{}\n'.format(type(self.test_tuple), self.test_tuple))
        print('{}\n{}\n'.format(type(self.test_list), self.test_list))
        print('{}\n{}\n'.format(type(self.test_dict), self.test_dict))
        print('{}\n{}\n'.format(type(self.test_func), id(self.test_func)))
        print('{}\n{}\n'.format(type(self.test_list_01), self.test_list_01))
        print('{}\n{}\n'.format(type(self.test_dict_01), self.test_dict_01))
        print('>>> 调用实例方法结束:{}'.format(self.func_01.__doc__))

    @classmethod
    def func_02(cls):
        """func_02"""
        print('>>> 调用类方法:{}'.format(cls.func_02.__doc__))
        print('>>> 打印属性\n')
        print('{}\n{}\n'.format(type(cls.test_str), cls.test_str))
        print('{}\n{}\n'.format(type(cls.test_int), cls.test_int))
        print('{}\n{}\n'.format(type(cls.test_tuple), cls.test_tuple))
        print('{}\n{}\n'.format(type(cls.test_list), cls.test_list))
        print('{}\n{}\n'.format(type(cls.test_dict), cls.test_dict))
        print('{}\n{}\n'.format(type(cls.test_func), id(cls.test_func)))
        print('{}\n{}\n'.format(type(cls.test_list_01), cls.test_list_01))
        print('{}\n{}\n'.format(type(cls.test_dict_01), cls.test_dict_01))
        print('>>> 调用类方法结束:{}'.format(cls.func_02.__doc__))

    @staticmethod
    def func_03():
        """func_03"""
        print('>>> 调用静态方法:{}'.format(User.func_03.__doc__))
        print('>>> 打印属性\n')
        print('{}\n{}\n'.format(type(User.test_str), User.test_str))
        print('{}\n{}\n'.format(type(User.test_int), User.test_int))
        print('{}\n{}\n'.format(type(User.test_tuple), User.test_tuple))
        print('{}\n{}\n'.format(type(User.test_list), User.test_list))
        print('{}\n{}\n'.format(type(User.test_dict), User.test_dict))
        print('{}\n{}\n'.format(type(User.test_func), id(User.test_func)))
        print('{}\n{}\n'.format(type(User.test_list_01), User.test_list_01))
        print('{}\n{}\n'.format(type(User.test_dict_01), User.test_dict_01))
        print('>>> 调用静态方法结束:{}'.format(User.func_03.__doc__))

    def __repr__(self):
        return '我是 __repr__'


if __name__ == '__main__':
    def demo_001():
        new_user = User(name='yyx', sex='man')
        print('\n===修改前【实例】通过【实例方法】调用属性===')
        new_user.func_01()

        print('\n===修改后【实例】通过【实例方法】调用属性===')
        new_user.test_str += '-new'
        new_user.test_int += 33
        new_user.test_tuple += ('t4', 't5')
        new_user.test_list.append('d')
        new_user.test_dict['key_3'] = 'value_3'
        new_user.test_func = y
        new_user.test_list_01 = []
        new_user.test_dict_01 = {}
        new_user.func_01()

        print('\n===对比【实例】通过【类方法】调用属性===')
        new_user.func_02()

        print('\n===对比【类】通过【类方法】调用属性===')
        User.func_02()

        print('\n===对比【实例】通过【静态方法】调用属性===')
        new_user.func_03()

        print('\n===对比【类】通过【静态方法】调用属性===')
        User.func_03()


    def demo_002():
        print('\n===修改前【类】通过【类方法】调用属性===')
        User.func_02()

        print('\n===修改后【类】通过【类方法】调用属性===')
        User.test_str += '-new'
        User.test_int += 33
        User.test_tuple += ('t4', 't5')
        User.test_list.append('d')
        User.test_dict['key_3'] = 'value_3'
        User.test_func = y
        User.test_list_01 = []
        User.test_dict_01 = {}
        User.func_02()

        new_user = User(name='yyx', sex='man')
        print('\n===对比【实例】通过【实例方法】调用属性===')
        new_user.func_01()

        print('\n===对比【实例】通过【类方法】调用属性===')
        new_user.func_02()


    demo_001()
    demo_002()
