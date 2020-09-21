# global num, 一般以gl_开头
gl_num = 10


def demo1():
    # 局部变量赋值99,函数结束后回收
    global gl_num  #使用global声明
    gl_num = 99
    print(gl_num)


demo1()
print(gl_num)
