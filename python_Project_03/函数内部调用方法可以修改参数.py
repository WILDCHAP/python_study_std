def demo(num_list):
    #用方法可以修改
    num_list.append(9)
    num_list[1] = 8
    num_list.remove(3)
    #直接赋值不行
    num_list = [4, 5, 6]
    print('函数执行完成')

gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)