'''
一般不需要用到类方法，也不要用到对象方法
就把他设置为一个静态方法
静态方法不需要self

@staticmethod
'''
class Dog(object):
    @staticmethod
    def fun():
        print("dog play")

Dog.fun()