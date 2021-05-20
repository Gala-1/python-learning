#公共方法
#1.len()  --计算容器中元素个数
str1 = 'abcdefg'
list1 = [10,20,30,40]
t1 = (10,20,30,40)
s1 = {10,20,30,40}
dict1 = {'name': 'Tome', 'age': 18}

print(len(str1))   #7
print(len(list1))  #4 
print(len(t1))     #4
print(len(s1))     #4
print(len(dict1))  #2

#2.del()或del --删除
# del str1
# print(str1)

# del list1
# print(list1)
# del(list1[0])
# print(list1)

# del s1
# print(s1)

# del dict1
# print(dict1)
# del(dict1['name'])
# print(dict1)

#3.max() min() --返回容器中的最大值与最小值
print(max(str1))
print(max(list1))

print(min(str1))
print(min(list1))

#4.range(start,end,step)  --生成从start到end的数字，步长为step，供for循环使用
#1 2 3 4 5 6 7 8 9 
for i in range(1,10):
    print(i,end=' ')
print()
#1 3 5 7 9
for i in range(1,10,2):
    print(i,end=' ')
print()
#0 1 2 3 4 5 6 7 8 9 
for i in range(10):    #开头默认为0，步长默认为1
    print(i,end=' ')
print()

#5.enumerate(可遍历对象，start=0)  --函数用与将一个可遍历的数据对象（如列表，字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环
list = ['a','b','c','d','e']
for i in enumerate(list):
    print(i)      #返回结果是一个元组，元组第一个对象是下标，第二个对象是数据

for i in enumerate(list,start=1):
    print(i)     #数据下标的起始值为1
