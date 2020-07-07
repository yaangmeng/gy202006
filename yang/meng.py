# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)
#
# a = (1,2,3,4,5)
#
# x,y,*z = a
# print(x)
# print(y)
# print(z)
#
# a = 30
# b = 20
# print(a // b)
#
# a = 30
# b = 20
# print(a % b)
#
# #循环
# # a = [23,34,53,72,73,77,99,24,53,63]
# #
# # for sc in a :
# #     if (sc >= 0 and sc < 60 ):
# #         print("不及格")
# #     elif (sc >= 60 and sc <= 70 ):
# #         print("及格")
# #     elif (sc > 70 and sc <= 80 ):
# #         print("良好")
# #     elif (sc > 80 and sc <= 100):
# #         print("优秀")
# #     else:
# #         print("请输入正确的成绩")
#
# #50的阶乘
# s = 1
# for i in range(50,0,-1):
#     s= s * i
# print(s)
#
#
#
# for i in  range(1,100):
#     if (i % 3 != 0):
#         continue
#     print(i)
#
# def ad (s,f=3):
#     if(f == 0):
#         return  None
#     else:
#         return (s//f,s%f)
#
# abc = ad (15)
#
# if abc is None:
#     print("参数错误")
# else:
#     print("商为：",abc[0],"余数为：",abc[1])
#
# c = 1,2,3,4
# a,*b = (1,2,3,4)
#
# print(b)
#
# def zxz(*args,**kwargs): #*args =*b  #*args 接收动态位置参数，**kwargs 接收动态关键字参数
#     print(kwargs)
#     s=0
#     for i in args:
#         s+=i
#     return s
#
# print(zxz(1,2,3,4,4,33,22,54,44,32,13))
# print(zxz(name="沙雕"))

#面对对象
# class adc():
# #     a=None
# #     b=None
#     res=None
#     def __init__(self,a,b):#魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b

#    def input(self,a,b):
#        self.a=a
#        self.b=b

#     def s(self):
#         self.res = self.a + self.b
#     def f(self):
#         self.res = self.a - self.b
#     def g(self):
#         self.res = self.a * self.b
#     def h(self):
#         self.res = self.a / self.b
#     def get(self):
#         print(self.res)
#
#     @classmethod
#     def get_res(cls):#类方法定义：必须添加名字为@classmethod的装饰器，第一个参数名cls cls代表当前类本身
#         print(cls.res)
#
#     @staticmethod
#     def static(self):#静态方法定义：必须使用@staticmethod装饰器，无默认参数
#         pass
#
# e =  adc(30,50)

#e.input(20,50)
# e.s()
# e.f()
#e.g()
# e.h()
#e.get()

# class Pf():
#
#     money = 1000000
#     house = 200
#     _yi_fu ='裤子'
#     __lao_po ="如花"
#
#
# class Ch(Pf):
#     ai_hao = '花钱'
#     pass
#
# c =Ch()
# print(c.ai_hao)
# print(c.house)
# print(c.money)
#


class  Liuzl():
    money = 10000000000000                #属性
    house = 10000
    _si_you = "地下城账号"                #私有变量
    __feichang_siyou="火之意志"
    def shou_yi(self):                    #实例方法
        print("抠鼻")
    def __init__(self,a1):
        self.a = a1

class Yupeng(Liuzl):                      #方法继承
    def __init__(self,*args,**kwargs):
        super(Yupeng, self).__init__(*args,*kwargs)
    ai_hao="吃屎"
    pass

y = Yupeng(1111)

print(y.ai_hao)
print(y.money)
print(y.house)
y.shou_yi()
print(y.a)