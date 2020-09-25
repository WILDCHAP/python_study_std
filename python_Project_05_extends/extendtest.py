'''
class 类名(继承类):
'''
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def __init__(self, name1, name2, sound):
        self.sound = sound
        super().__init__(name1)
        self.name = name2
    def drink(self):
        super().drink()
        print("狗喝")

'''多继承'''
class xtq(Animal, Dog):
    pass

a = Dog("haha", "wawa", "wangwang")
print(a.name)
a.eat()
a.drink()

