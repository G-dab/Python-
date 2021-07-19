
#print函数可以输出数字 字符串 含运算符的表达式
print(1)
print('hello world')
print(1+1+1)
#输出到文件
#a+代表用读写的方式输出，若文件不存在就创建，若文件存在就在原文件上追加
fp=open('C:\Users\ASUS\Desktop','a+')
print('hello world',file=fp)
fp.close()
#在一行输出
print(1,1,1,1)