# break and continue 
# Condition1：break  终结循环
# 方法一
i = 1
while i <= 5 :
    if i <= 3:
        print(f'完成了{i}个')
        i += 1
    else:
        print('够了')
        break

# 方法二
j = 1
while j <= 5:
    if j == 4:
        print('够了')
        break
    print(f'完成了{j}个')
    j += 1


