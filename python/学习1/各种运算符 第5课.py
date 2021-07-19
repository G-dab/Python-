# 2021/7/14  #8:42
#赋值运算符
a=20
b=c=20 #链式赋值
print(a,type(a),id(a))    #id就是内存地址
print(b,type(b),id(b))
print(c,type(c),id(c))
print('-------------参数赋值--------------')
a+=30 #相当于a=a+30
print(a)
print('--------系列解包赋值---------')
a,b,c=1,2,3
print(a)
print(b)
print(c)

#比较运算符
a,b=10,20
print('a>b吗？',a>b) #比较运算符的结果为bool类型
print('a>b吗？',a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


'''  =   赋值运算符
     ==  比较运算符

一个变量由三部分组成：标识，类型，值
==比较的是值
is 比较的是标识
'''
print('------------------------')
a=b=1
print(a == b)
print(a is b)
print('------------------------')
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1 == lst2)#True
print(lst1 is lst2)#False

'--------------------布尔运算符-----------------'
a,b=1,2
print(a==1 and b==2)

f1= True
print(not f1)

c='hello world '
print('w' in c)
'--------------------位运算符-----------------'
print(4&8)#按位与%
print(4|8)#按位或|
print(4>>1)#右移一位   相当于整除2
print(1>>1)
print(4<<2)#左移两位   相当于乘以4