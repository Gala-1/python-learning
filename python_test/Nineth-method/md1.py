#运算符
#1.+ 合并   --支持的容器类型（字符串、列表、元组）
str1 = 'aa'    #--字符串
str2 = 'bb'
print(str1+str2)
list1 = [1,2]  #--列表
list2 = [3,4]
print(list1+list2)
tuple1 = (1,2) #--元组
tuple2 = (3,4)
print(tuple1+tuple2)

#2.* 复制   --支持的容器类型（字符串、列表、元组）
str3 = 'a'
list3 = ['hello']
t3 = ('world',)    #元组一个元素需要加逗号

print(str3*5)
print(list3*5)
print(t3*5)
 
#3.in       --支持的容器类型（字符串、列表、元组、字典）
#4.not in   --支持的容器类型（字符串、列表、元组、字典）