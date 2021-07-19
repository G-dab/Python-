# 2021/7/18  #9:52
a=0
sum=0
while a <=100:
    a+=2
    sum+=a
print(sum)
#不对
'-----------------另一种方式---------------'
a=0
sum=0
while a <=100:
    if a%2==0:  #if not bool(a%2==0)
        sum+=a
    a+=1
print(sum)
