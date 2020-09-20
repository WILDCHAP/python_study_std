import cards_tools as ct

tag = True

while tag:
    ct.show_main()
    choice = input('请选择希望执行的操作')
    while choice not in ['1', '2', '3', '4', '5', '0']:
        choice = input("请输入正确值:")
    if choice in ['1', '2', '3', '4', '5']:
        print('-' * 50)
        # 新增名片
        if choice == '1':
            ct.add_card()
        # 显示名片
        elif choice == '2':
            ct.show_card()
        # 查询名片
        elif choice == '3':
            ct.search_card()
        # 修改名片
        elif choice == '4':
            ct.alter_card()
        #删除名片
        else:
            ct.del_card()

    elif choice == '0':
        while True:
            ans = input('确定吗?(Y/N):')
            ans = ans.upper()
            if ans == 'Y':
                tag = False
                break
            elif ans == 'N':
                break
            else:
                print('请输入正确的值')
