def demo(*args, **kwargs):
    print(args)
    print(kwargs)

gl_nums = (1, 2, 3)
gl_dict = {'name':'小明', 'age':18}

demo(gl_nums, gl_dict)      #这样会全赋值给args
demo(gl_nums, name = '1')   #这样kwargs就可以得到值

#