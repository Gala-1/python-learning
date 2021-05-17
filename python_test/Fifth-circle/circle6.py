# while循环嵌套
'''
while 条件1:
    while 条件2:
        print('aa')
    print('bb')
'''

j = 0 
while j < 3:
    i = 0
    while i < 3:
        print('Aa')
        i += 1
    print('Bb')
    j += 1