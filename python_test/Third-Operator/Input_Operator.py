'''
# 输入功能的实现
password=input('请输入您的密码：')
print(f'您输入的密码是{password}') 
print(type(password))  #input接受的数据都会被当做字符串类型
'''


'''
# 数据类型的转换
num=input('请输入数字：')
print(num)
print(type(num))
print(type(int(num)))
'''


'''
# 数据类型转换函数
num1=1
str1='10'
print(type(float(num1)))
print(float(num1))
print(float(str1))
print(type(str(num1)))
list1=[1,2,3]
print(tuple(list1))
tu1=(1,2,3)
print(list(tu1))
#  eval()把字符串中的数据转换成原来的数据类型
str='1'
str2='2.2'
str3='(2,3,5)'
str4='[2,3,4]'
print(type(eval(str)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
'''


'''
# 多变量赋值
a,b,c=1,2.1,'dsf'
print(a,b,c)
# 多变量赋相同值
a=b=c=32
print(a,b,c)
# 复合赋值运算符
i,s=1,0
s+=i
print(s)
s-=i
print(s)
# 比较运算符
print(1==1)
print(1!=1)
print(2>1)
print(2<1)
# 逻辑运算符    布尔值(and or not) 且 或 非 
a=1 
b=2
c=3
print((a<b)and(c>b))   #True
# 数字之间的逻辑运算
print(1 and 0)
print(1 and 2)   #and 只要有一个值为0，则结果为0，否则结果为最后一个非零数字
print(0 or 0)
print(2 or 0)
print(0 or 2)    #or 只有所有值为0结果才为0，否则结果为第一个非0数字
'''



