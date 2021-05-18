# 综合应用 --随机分配办公室
# 需求：8位老师，3个办公室，将他们随机分配到三个办公室中
'''
步骤：
1.准备数据
    1.1 8位老师   --列表
    1.2 3个办公室  --列表嵌套
2.分配老师办公室
    ***随机分配
    就是把老师的名字写入到办公室列表 -- 办公室列表追加老师名字数据
3.验证是否分配成功
    打印办公室详细信息：每个办公室的人数和对应的老师名字
'''

# 1.准备数据
teachers = ['A','B','C','D','E','F','G','H']  #存储列表
offices = [[],[],[]]      #嵌套列表
# 2.分配老师到办公室
import random
for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)    #列表中添加数据
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}人,老师分别是：')
    s = []
    for name in office:
        s.append(name)
    print(','.join(s))    #合并s列表内的各个字符串为一个大字符串，以逗号分隔
    i += 1   
    print()
   

