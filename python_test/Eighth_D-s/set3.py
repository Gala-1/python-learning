#2.删除数据
#remove() --删除集合中的指定数据，如果数据不存在则报错
#discard() --删除集合中的指定数据，如果数据不存在也不会报错
#pop() --随机删除某个数据，并返回这个数据

s1 = {10,20,30,40,50}

#(1) remove()
s1.remove(10)
print(s1)

#s1.remove(10)   #报错
#print(s1)

#(2) discard()
s1.discard(20)
print(s1)

'''s1.discard(20)
print(s1)       #不存在也不会报错'''

#(3) pop()
del_num = s1.pop()
print(del_num)
print(s1)

