#字典常见操作

#1.增 --字典序列[key] = 值
#如果key存在则修改这个key对应的值，如果key不存在则新增此对应的值
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['id'] = 110   #新增一个键值对
print(dict1)      
dict1['name'] = 'Lily'  #修改已存在的key对应的值
print(dict1)

#2.删除 
#del()/ del: 删除字典或删除字典中指定键值对
'''del(dict1)       #删除整个字典
print(dict1)'''

del dict1['name']   #删除指定键值对
print(dict1)    

#clear() --清空
'''dict1.clear()    #清空字典
print(dict1)   '''

#3.修改 --字典序列[key] = 值

#4.查找 
#key值查找
#如果查找的key存在，则返回对应的值；否则则报错
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])  # Tom
#print(dict1['id'])   # 报错

#get()
#字典序列.get(key,默认值)  注意: 如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None。
print(dict1.get('name')) #Tom
print(dict1.get('id',1)) #1
print(dict1.get('id'))   #None

#keys()   --查找字典中所有的keys，返回可迭代的对象
print(dict1.keys())  #dict_keys['name','age','gender']

#values()  --查找字典中所有的值，返回可迭代的对象
print(dict1.values())  # dict_values(['Tom',20,'男'])

#items()   --查找字典中所有的键值对，返回可迭代的对象
print(dict1.items())  #内部是元组，元组有2个数据，元组数据1是字典的key，元组数据2是字典的value