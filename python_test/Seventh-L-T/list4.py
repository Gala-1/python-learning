# 4.删除
# del 目标
name_list = ['TOM','lily','Rose']
del name_list     #删除整个列表
# print(name_list)
name_list = ['TOM','lily','Rose']
del name_list[0]  #删除列表指定位置的数据
print(name_list)  

# 数据列表.pop(下标)   #删除指定位置的数据，默认是删除最后一个数据，但都会返回被删除的数据
name_list = ['TOM','lily','Rose']
print(name_list.pop())  #删除最后一个数据，并返回删除值
print(name_list)
print(name_list.pop(1)) #删除下标为1的数据，并返回删除值
print(name_list)

# 数据列表.remove(数据) 
name_list = ['TOM','lily','Rose']
name_list.remove('Rose')
print(name_list)

# clear() --清空列表
name_list.clear()  #剩余一个空列表
print(name_list)

