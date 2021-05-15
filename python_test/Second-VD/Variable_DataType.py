# print('python test')  #单行注释
# print('happy ending')
'''fd
多行注释
fasdf'''


'''
# 定义一个变量
my_name="LHR"
print(my_name) 
# 定义另一个变量
schoolName="HZAU"
print(schoolName)
'''


'''
# 认识数据类型
num1=1 
num2=1.1
type(num1)
print(type(num1))  #int --整型
print(type(num2))  #float --浮点型
s='hel'
print(type(s))     #string --字符串
b=True
print(type(True))  #bool  --布尔型
c=[10,34,23,34,34]
print(type(c))     #list --列表
d=(1,23,34)
print(type(d))     #tuple --元组
e={23,23,43}
print(type(e))     #set --集合
f={'name':'lhr','age':18}
print(type(f))     #dict --字典
'''


'''
# 输出（格式化符号）
# %s --字符串
# %d --有符号的十进制整数
# %f --浮点数
# %c --字符
age=18
name='LHR'
weight=74.5
stu_id=3
print("今年我的年龄是%d岁"%age)
print("我的名字是%s"%name)
print("我的体重是%.2f公斤"%weight)
print("我的学号是%03d"%stu_id)
print("我的名字是%s,我的年龄是%d岁"%(name,age))
print("我的名字是%s,明年是%d岁"%(name,age+1))
print("今年我的年龄是%d岁，我的名字是%s，我的体重是%.3f公斤，我的学号是%05d"%(age,name,weight,stu_id))
'''


'''   f'dd{变量名}dd{变量名}'
age=18
name='LHR'
weight=74.5
print("我的名字是%s,我的年龄是%s岁,我的体重是%s公斤"%(name,age,weight))
print(f'我的名字是{name},今年{age}岁了')
'''

'''
# 转义字符
print("hello\npython")
print('ab\tcd')
print('\tabcd')
print('dfsf',end='\t')
print('dfsfs')
print('dfsf',end='....')
print('abcd')
'''