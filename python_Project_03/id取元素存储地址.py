a = 1

print("a=1", id(a))

b = a

print("b=1", id(b))

b = 2

print("a=1", a)

print(id(a))

def f(a):       #传入引用地址
    print(id(a))
    return 2


print("函数返回a=2", f(a))
print("return 2", id(f(a)))
print("b=2", id(b))

a = {'a':1, 'b':2}