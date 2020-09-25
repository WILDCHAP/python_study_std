'''
类属性直接用类名调用

类方法里只能用类属性
@classmethod
def 类方法名(cls):
'''

class A(object):
    count = 0
    def __init__(self):
        A.count += 1
        self.name = "hahaha"
    @classmethod
    def f(cls): # 只能调用类属性
        print("你好", cls.count)
a = A()
b = A()
c = A()
print(a.count)
print(b.count)
print(c.count)
print(A.count)
a.f()
A.f()