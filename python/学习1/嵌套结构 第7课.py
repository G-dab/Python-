# 2021/7/19  #13:15
'输出一个三行四列的矩形'
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t') #不换行输出
    print()  # 换行
'输出一个直角三角形'
for i in range(1,10):
    for j in range(i):
        print('*', end='\t')
    print()
'输出九九乘法表'
for i in range(0,10):
    for j in range(i+1):
        print(i,'*',j,'=',i*j, end='\t')
    print()