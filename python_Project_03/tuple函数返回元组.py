def demo1():
    print('demo1')
    a = 3
    #return (1, 2, a) 可以省略括号
    return 1, 2, a

# 1. 直接用元组接收

a = demo1()
#a[1] = 1
print(type(a), a)
a = list(a)
a[1] = 3
print(type(a), a)
a = set(a)
print(type(a), a)
a.add(3)    #set无重复
print(type(a), a)

# 2. 用多个元素接收

a, b, c = demo1()
print(a, b, c)