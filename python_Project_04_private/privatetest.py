# 前面加两个下划线就变成了私有
class person:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
    def hellow(self):
        print("hellow")
    def __getid(self):
        print(self.__id)
    def getId(self):
        print(self.__id)
a = person(10086, "小明")
print(a.name)
# print(a.__id)
a.hellow()
#a.__getid()
a.getId()


