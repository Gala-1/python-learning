#容器类型转换
#1.tuple()  --将某个序列转换成元组
list1 = [1,2,3,4,5,2]
s1 = {1,2,3,4,5,3}
t1 = (1,2,3,4,5)
print(tuple(list1))
print(tuple(s1))

#2.list()  --将某个序列转换成列表
print(list(s1))
print(list(t1))

#3.set()  --将某个序列转换成集合    （集合有去重功能）
print(set(list1))
print(set(t1))