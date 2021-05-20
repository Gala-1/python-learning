# 2.修改 --用函数的形式修改字符串中的数据
# replace（）、split（）、join()、capitalize()
# 1.replace（）语法 -- 字符串序列.replace(旧子串，新子串，替换次数)
        # 注意：替换次数如果超过出现次数，则替换所有出现子串即可  
mystr = 'hello world and itcast and itheima and Python'
newstr = mystr.replace('and','和')  #替换次数默认是全部替换
print(newstr)  
# 字符串是不可变数据类型

newstr2 = mystr.replace('and','和',1)
print(newstr2)
newstr3 = mystr.replace('and','和',10)
print(newstr3)

# 2.split（）语法 -- 字符串序列.split(分割字符，num)  注意：num表示分割字符出现的次数，即返回n+1个数据形成的列表
    # 按照指定字符分割字符串   split()默认是按照空格分割
list1 = mystr.split('and')  #分割字符会丢失
print(list1)
list2 = mystr.split('and',2)  #分割2次
print(list2)

#3.join() 语法 -- 合并列表里面的字符串数据为一个大字符串  字符或子串.join(多字符串组成的序列)
mylist = ['aa','bb','cc']
#aa...bb...cc
new_str = '...'.join(mylist)
print(new_str)  

#4.capitalize():将字符串第一个字符转换成大写,其余转小写
print(mystr.capitalize())
# title() 将字符串每个单词首字母转换成大写
print(mystr.title())
# lower():大写转小写   upper():小写转大写
print(mystr.upper())
print(mystr.lower())


#5. lstrip() 删除字符串左侧空白字符
  # rstrip() 删除字符串右侧空白字符
  # strip()  删除字符串两侧空白字符
st = "  hello  world  and  itcast  and  Python  "
print(st)
print(st.lstrip())
print(st.rstrip())
print(st.strip())

# 6. ljust(长度，填充字符) 使字符串左对齐  默认填充字符是空格
#    rjust() 使字符串右对齐
#    center() 中间对齐
bab = 'ddd'
print(bab.ljust(10,'.'))  #在10个字符内左对齐，剩余用空格填充

