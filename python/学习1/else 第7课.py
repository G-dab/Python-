# 2021/7/19  #8:33
'录入密码，最多录入三次，若正确则结束循环'
real_passwd = '123'
for item in range(3):
    passwd = input('请输入密码')
    if passwd == real_passwd:
        print('密码输入正确'）
        break
    else:
        print('密码输入错误，请重新输入')
else:
    print('三次密码输入机会已经全部用完')