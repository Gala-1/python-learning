# Condition2:continue  退出当前循环，执行下一次循环
i = 1
while i <= 5:
    if i == 3:
        print('吃了条虫子，就不用吃了')
        i += 1     #在continue之前使变量发生变化
        continue   #如果使用了continue，需要在continue之前使循环控制变量发生改变
    print(f'吃了{i}个')
    i += 1


