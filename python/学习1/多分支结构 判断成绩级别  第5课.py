# 2021/7/16  #14:54
'''
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
'''
score = int(input('请输入一个整数成绩'))
if 89<score and score <100:
    print('级别为 A')
elif 70<=score and score<90:
    print('级别为 B')
elif 60 <= score and score < 80:
    print('级别为 C')
elif 0<=score and score<60:
    print('级别为 D')
else:
    print('成绩不合法')