# 字符串常用操作方法 --查找、修改、判断
# 1. 查找  --查找子串在字符串中的位置或出现的次数
# find（）、index（）、count（）
# 语法 --字符串序列.find(子串,开始位置下标,结束位置下标)  注意：开始和结束下标可省略，默认全部字符串
# (1) find()
mystr = 'hello world and itcast and itheima and Python'
print(mystr.find('and'))  # 12 从左往右返回第一个and出现的位置
print(mystr.find('and',15,30))  #23
print(mystr.find('ands')) #-1 子串不存在

# (2) index()
print(mystr.index('and')) #12
print(mystr.index('and',15,30)) #23
# print(mystr.index('ands')) #substring not found 报错

# (3)count()
print(mystr.count('and'))  #3  and出现的次数
print(mystr.count('and',15,30)) #1
print(mystr.count('ands')) #0 

# rfind rindex --从右向左开始查找  --注意：下标仍然从左往右标记
print(mystr.rfind('and'))  #35
print(mystr.rindex('and')) #35




