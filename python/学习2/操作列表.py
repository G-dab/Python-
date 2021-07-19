# 2021/7/14  #17:16
'-------------------------------for循环----------------------------'
#for循环遍历整个列表
cars=['a','b','c']
for car in cars:
    print(car)
print('---------------------------')
for car in cars:
    print(f'hey,{car},you can run really fast')
    print(f'well,I guess {car} can be the winner\n')
'----------------------------------range()  list()-----------------------------------------'
#range()函数可以生成一组数
for value in range(1,5):
    print(value)#注意这里范围到4就停止    range(6)表示0到6
#利用list 可以将range生成的数字转换成列表
number = list(range(1,6))
print(number)
#range还可以指定步长
#打印1到10 的偶数
for a in  range(2,11,2):  #注意range一定要放在for语句里
    print(a)
#创建1到10的平方所构成的列表
squares = []     #注意先创建空列表
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
'------------------------------一些简单处理数字列表的python函数 min max sum --------------------------------------------'
digits = [1,2,3,4,4,54,13123,33,4,54,6,67,0]
min(digits)
max(digits)
sum(digits)
'--------------------------------------------列表解析---------------------------------------'
squares  = [square**2 for square in range(1,11)]
print(squares)
'------------------------------------切片--------------------------------------------'
#选取列表的2，3，4元素 注意切片和range()都是到第二个索引之前的元素停止
a = [1,2,2,21,2,1]
print(a[1:4])
#若没有第一个索引，则代表从第一个元素开始；若没有第二个索引，则表示到最后停止
#切片也可有步长
print(a[1:5:2])
