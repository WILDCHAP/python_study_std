'''
try:
    尝试执行的代码
except 错误类型1:
    出现错误的处理
except 错误类型2:
    出现错误的处理
except Exception as 变量名:
    出现的未知错误
else:
    没有异常才会执行的代码
finally:
    无论有没有异常都会被执行

主动抛出异常：
1. 创建Exception对象
2. 用raise抛出异常

'''

try:
    num = int(input("请输入一个整数："))
    result = 8 / num
except ValueError:
    print("请输入正确的整数")
except Exception as e:
    print("出现[%s]错误" % e)
    # 主动抛出异常
    ex = Exception(e)
    raise ex
else:
    print("没有出现异常")
finally:
    print("无论是否有异常都会执行")

print("*" * 50)