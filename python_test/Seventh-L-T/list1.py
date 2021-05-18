# 列表  --一次性可以存储多个数据
# [数据1，数据2，数据3，数据4，数据5....] 这些数据可以为不同数据类型 （注意：最好一个列表放同一类型数据）
# 1.查找
name_list = ['TOM','lily','Rose']
print(name_list[0])  #TOM
print(name_list[1])  #lily
print(name_list[2])  #Rose
# 查找常用的函数
# index(数据，开始下标，结束下标) 返回指定数据所在位置的下标
# count() 统计指定数据出现的次数 
# len()   访问列表长度，即列表中数据的个数
print(name_list.index('TOM'))  #0
print(name_list.count('TOM'))  #1
print(len(name_list))          #3

