# 2.判断（指定数据是否存在列表中）
name_list = ['TOM','lily','Rose']
# (1). in 判断指定数据是否在列表
print('TOM' in name_list)
print('TOMS' in name_list)

# (2). not in 判断指定数据是否不在列表
print('TOM' not in name_list)
print('TOMS' not in name_list)

#案例
name = input('请输入您的的名字：')
if name in name_list:
    print('您输入的名称已存在')
else:
    print(f'您的昵称：{name}创建成功')

    