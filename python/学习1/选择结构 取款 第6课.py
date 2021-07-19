# 2021/7/16  #9:51
money = 1000
a = int(input('请输入取款金额'))
if money >= a:
    money = money -a
    print('取款成功，余额为',a)