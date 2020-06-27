# 定义功能界面函数
def info_print():
    print('请选择功能------------')
    print('1. 添加学员')
    print('2. 删除学员')
    print('3. 修改学员')
    print('4. 查询学员')
    print('5. 显示所有学员')
    print('6. 退出系统')
    print('-' * 20)

# 等待存储所有学员的信息
info = []


# 添加学员信息的函数
def add_info():
    """添加学员函数"""
    # 1. 用户输入：学号，姓名，手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    # 2. 判断是否添加这个学员：如果学员姓名已经存在存在错误提示，如果姓名不存在，则添加数据
    global  info
    # 2.1 不允许姓名重复：判断用户输入的姓名 和 列表里面字典的name对应的值是相等  则提示
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            # return作用：退出当前函数，后面添加信息的代码不执行
            return

    # 2.2 如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)

    # 列表追加字典
    info.append(info_dict)
    print(info)


# 删除学员
def del_info():
    """删除学员"""
    # 1. 用户去输入要删除学员的姓名
    del_name = input('请输入要删除的学员姓名：')

    # 2. 判断学员是否存在：存在就删除（break），不存在就提示
    # 2.1 声明info 是个全局变量
    global info
    # 2.2 遍历列表
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)


# 修改函数
def modify_info():
    """修改函数"""
    # 1. 用户输入要修改的学员姓名
    modify_name = input('请输入要修改的学员姓名：')
    global info
    # 2. 判断学员是否存在：如果输入的姓名存在则修改手机号，否则报错提示
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')
    print(info)


# 查询学员
def search_info():
    """查询学员"""
    # 1. 输入要查找的学员姓名：
    search_name = input('请输入要查找的学员姓名：')
    global info
    # 2. 判断学员是否存在：存在则显示这位学员信息，否则报错提示
    for i in info:
        if search_name == i['name']:
            print('查找到该学员的信息如下：' + '-' * 14)
            print(f"该学员的学号是{i['id']}，姓名是{i['name']}，手机号是{i['tel']}")
            break
    else:
        print('该学员不存在')


# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


#系统功能需要循环显示，直到用户输入6才退出系统
while True:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))


    # 3. 按照用户输入的功能序号, 执行不同的功能（函数）

    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有')
        print_all()
    elif user_num == 6:
        # print('退出系统')
        # 程序要想结束，退出终止 while True ---- beak
        exit_flag = input('确定要退出吗？输入 （yes or no）   ：')
        if exit_flag == 'yes':
            break
    else:
        print('输入的功能序号有误')

