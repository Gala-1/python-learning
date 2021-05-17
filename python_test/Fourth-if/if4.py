# if 嵌套
'''
if 条件1:
    条件1成立执行的代码
    ...
    if 条件2:
        条件2成立执行的代码
        ...
'''

# 实例：坐公交
money=1
seat=0
if money == 1:
    print('请上车')
    if seat == 1:
        print('坐下')
    else:
        print('站着')
else:
    print('请下车')