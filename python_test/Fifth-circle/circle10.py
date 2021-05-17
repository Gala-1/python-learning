# for ...else
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        # break
        continue
    print(i)
else:
    print('循环正常结束执行的代码')

