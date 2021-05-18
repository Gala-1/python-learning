# 5.修改  
name_list = ['TOM','lily','Rose']

#修改指定下标数据
name_list[0] = 'change'
print(name_list) 

#逆序 reverse()
list1 = [1,5,3,4,7,6]
list1.reverse()
print(list1)

#排序 sort() 升序与降序
list1.sort()  #默认reverse=False(升序排列)  reverse=True(降序)
print(list1)  
list1.sort(reverse=True)  #降序排列
print(list1)



