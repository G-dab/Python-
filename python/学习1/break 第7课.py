# 2021/7/19  #7:34
'录入密码，最多录入三次，若正确则结束循环'
real_passwd = '123'
for item in range(3):
    passwd = input('请输入密码')
    if passwd == real_passwd:
        print('密码输入正确'）
        break
    else:
        print('密码输入错误，请重新输入')
'-----------------------while语句---------------------------'
a=0
while a<3:
    '条件执行体（循环体）'
    pwd = input('请输入密码')
    if pwd == '123':
        print('密码输入正确')
        break
    else:
        print('密码输入错误，请重新输入')

    '改变变量'
    a+=1