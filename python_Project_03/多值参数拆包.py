def demo(*args, **kwargs):
    print(args)
    print(kwargs)

gl_nums = (1, 2, 3)
gl_dict = {'name':'小明', 'age':18}

demo(gl_nums, gl_dict)      #这样会全赋值给args
demo(gl_nums, name = '1')   #这样kwargs就可以得到值

'''
在调用带有多值参数的函数时，如果希望:
    。将一个元组变量，直接传递给args
    。将一个字典变量，直接传递给kwargs
·就可以使用拆包，简化参数的传递，拆包的方式是:
    。在元组变量前，增加一个*
    。 在字典变量前，增加两个
'''
demo(*gl_nums, **gl_dict)