# for循环
'''
for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2
'''

str1 = 'itheima'
for i in str1:
    print(i,end=',')
print()
print()

# break 退出for循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print()
        print('遇到e不打印')
        break   
    print(i,end='')
print()


# continue 跳出当前循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        continue   #遇到e跳过
    print(i,end='')
print()
print('跳过e')