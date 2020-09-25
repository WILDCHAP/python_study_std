
def f():
    print("hahaha")

# 从别的文件导入此模块时就会输出
# print("小明开发的模块")
# f()

#方法，只允许他在这个文件中进行测试
if __name__ == "__main__":
    print("小明开发的模块")
    f()