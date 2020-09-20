card_list = []  # 空列表记录所有名片字典


def show_main():
    '''显示主菜单'''
    print('*' * 50)
    print('欢迎使用[名片管理系统]v1.0'.center(50))
    print('1. 新增名片'.center(50))
    print('2. 显示全部'.center(50))
    print('3. 查询名片'.center(50))
    print('4. 修改名片'.center(50))
    print('5. 删除名片'.center(50))
    print('0. 退出'.center(50))
    print('*' * 50)


def add_card():
    '''新增名片'''
    name = input('姓名：')
    phone = input('电话：')
    qq = input('QQ：')
    email = input('邮箱：')
    # 创建字典
    new = {'姓名': name,
           '电话': phone,
           'QQ': qq,
           '邮箱': email}
    card_list.append(new)
    a = input('添加成功！按回车继续')


def show_card():
    '''显示名片'''
    if len(card_list) != 0:
        print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
        for temp_dict in card_list:
            for val in temp_dict.values():
                print(val , end='\t\t\t')
            print()
        print()
    else:
        print('没有任何记录存在')
    input('按回车继续')

def search_card():
    '''搜索名片'''
    name = input('请输入要搜索名片的姓名：')
    for temp_dict in card_list:
        if temp_dict['姓名'] == name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            for val in temp_dict.values():
                print(val, end='\t\t\t')
            print()
            break
    else:
        print('没有找到名片')
    input('按回车继续')

def alter_card():
    '''修改名片'''
    name = input('请输入要修改名片的姓名：')
    for temp_dict in card_list:
        if temp_dict['姓名'] == name:
            temp_dict['姓名'] = input('姓名：')
            temp_dict['电话'] = input('电话：')
            temp_dict['QQ'] = input('QQ：')
            temp_dict['邮箱'] = input('邮箱：')
            print("修改名片成功")
            break
    else:
        print('没有找到名片')
    input('按回车继续')

def del_card():
    '''删除名片'''
    name = input('请输入要删除名片的姓名：')
    for temp_dict in card_list:
        if temp_dict['姓名'] == name:
            card_list.remove(temp_dict)
            print("删除名片成功")
            break
    else:
        print('没有找到名片')
    input('按回车继续')