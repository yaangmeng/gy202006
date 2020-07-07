from day02 import mod_1
print(mod_1.a)
print(mod_1.name())
print(mod_1.test.name)


a = '我是模块2的a'


def name():
    print('我是模块2的name方法')


class test():
    name = "我是模块2中的tset类"