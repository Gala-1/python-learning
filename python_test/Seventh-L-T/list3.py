# 3. 增加
# 列表序列.append(数据)  --列表结尾增加数据
name_list = ['TOM','lily','Rose']
name_list.append('xiaoming')  #列表是可变数据类型
print(name_list)
name_list.append([1,2])       #直接追加一个列表
print(name_list)

# 列表序列.extend(数据)  --列表结尾增加数据
name_list.extend([11,22])
print(name_list)              #如果追加了一个列表，会将其拆开，逐一追加

# 列表序列.insert(位置下标，数据)  --指定列表位置增加数据
name_list.insert(3,'国')
print(name_list)

