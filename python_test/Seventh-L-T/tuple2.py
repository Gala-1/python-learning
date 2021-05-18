#元组的常见操作
#元组数据不支持修改，只支持查找
tuple1 = ('aa','bb','cc')
#1.下标
print(tuple1[0])          #aa
#2.index()
print(tuple1.index('bb')) #1
#3.count()
print(tuple1.count('cc')) #1
#4.len()
print(len(tuple1))        #3

#元组数据的修改
#tuple[0] = 'aaa'   元组对象不支持修改

#元组内的列表数据依然可以被修改
t2 = ('aa','bb',['cc','dd','ee'])
print(t2[2])
print(t2[2][0])
t2[2][0] = 'fff'
print(t2)        


