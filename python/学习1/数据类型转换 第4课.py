# 2021/7/12  #17:18
name='张三'
age=38
#print('我叫'+name+'今年'+age+'岁') 不同的数据类型相连接会报错
#只能通过数据类型转换来实现
#用str函数转换
print('我叫'+name+'今年'+str(age)+'岁')
#注意，int()函数是可转浮点数，而不能转浮点数的字符串
print(str(True))
print(int(True))
print(float(True))