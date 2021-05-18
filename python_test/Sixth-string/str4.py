# 3.判断 -- 判断真假，返回结果为T或F
# (1) starstwith(): 检查字符串是否以指定子串开头，是则返回T，否则返回F。可指定范围内检查。
# 语法 字符串序列.startwith(子串,开始位置下标，结束位置下标)

mystr = 'hello world and itcast and itheima and Python'
#print(mystr.startswith('hel'))   T
#print(mystr.startswith('hels'))  F

#(2) endswith(): 检查字符串是否以指定子串结尾。
# print(mystr.endswith('s'))    F

#(3) isalpha():如果字符串是非空的并且所有字符都是字母则返回T
#    isdigit():如果字符串中都是数字则返回T
#    isalnum():一个非空字符串中所有字符都是字母或数字则返回T
#    isspace():如果字符串只包含空白，则返回T
print(mystr.isalpha())  #False
print(mystr.isdigit())  #False
print(mystr.isalnum())  #False
print(mystr.isspace())  #F
a = '   '  
print(a.isspace())      #T

