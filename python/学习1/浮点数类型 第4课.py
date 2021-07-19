# 2021/7/12  #8:59
#浮点数
a=3.14159
print(type(a))
#浮点数储存不精确，一下为一个例子
n1=1.1
n2=2.2
print(n1+n2)#所以对于浮点数的计算要格外的小心
#通过导入模板decimal来解决这个问题
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))





