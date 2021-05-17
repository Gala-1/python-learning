# 星型符号的梯形排列
# 重复打印5行星星
j = 0
while j < 5:
    # 一行星星的打印
    i = 0
    while i <= j:
        # 一行内的星星不能换行，取消print默认结束符\n
        print('*', end='')
        i += 1
    # 每行结束要换行，借助一个print（）
    print()
    j += 1


# 九九乘法表
j = 1
while j <= 9:
    i=1
    while i <= j:
        s = i * j
        print(f'{i}*{j}={s}',end='\t')
        i += 1
    print()
    j += 1
    




