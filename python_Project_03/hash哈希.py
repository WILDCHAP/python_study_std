'''
Python中内置有一个名字叫做hash(o)的函数
。接收一个不可变类型的数据作为参数
。返回结果是一个整数
'''

# 无论什么时候输出都一样
print(hash(1))
print(hash("hellow"))
print(hash((1,)))
# 不能列表(因为可变)
# print(hash([1, 2]))
# 不能字典(因为可变)
# print(hash({1: 2}))
