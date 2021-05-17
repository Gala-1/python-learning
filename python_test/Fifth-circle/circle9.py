# else --循环可以和else配合使用
# while ... else   (else下方缩进的代码指的是当循环正常结束后，要执行的代码)
i = 1
while i <= 5:
    if i == 3:
        print('这次不真诚')
        i += 1      #注意continue上方i要增加
        continue    #这里是break的话，循环非正常结束，else下方的代码将不会被执行
    print('我错了')
    i += 1
else:
    print('原谅我了')

