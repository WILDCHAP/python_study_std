'''
单例设计模式
利用__new__(cls)  # 只分配一个空间
一定要返回
super().__new__(cls)
'''
class MusicPlayer(object):

    def __init__(self):
        print("播放器初始化")

    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 一定要返回分配的内存空间
        instance = super().__new__(cls)
        return instance

player = MusicPlayer()

print(player)