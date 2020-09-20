def f1():
    '''
    打印九九乘法表
    '''
    for i in range(1, 10):  # i: 1-9
        for j in range(1, i + 1):  # j: 1-i+1
            print("%d * %d = %d " % (j, i, i * j), end='\t')
        print("\n")


f1()


def f2(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)


a = 5
b = 6
f2(a, b)
print(a, b)
name = "hahaha"
