#认识字符串
# 单引号
a = 'hello'  #单引号不支持回车换行
print(a)
print(type(a))
b = "TOM"
print(type(b))

# 三引号
e = '''i am TOM'''
print(type(e))
f = """I am TOM"""    # 三引号支持回车换行
print(type(f))
print(f)   

#I`m TOM
c = "I'm TOM"
q = 'i\'m TOM'   #加上转义符号
print(c)
print(q)

#字符串输出
name = 'Tom'
print('我的名字是%s'%name)
print(f'我的名字是{name}')

#字符串输入
#input() 接受用户输入  输入的任何类型数据都会转变成字符串类型数据
password = input('请输入您的密码：')
print(f'您输入的密码是：{password}')
print(type(password))