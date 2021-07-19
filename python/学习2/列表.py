# 2021/7/13  #12:27
#创建列表 注意列表中的元素若是变量的话必须预先赋值
ms=['m1','m2','m3']
print(ms)#这样是把列表原封不动地打印出来
#访问列表元素
print(ms[0])
#title方法可以使元素的首字母大写
print('SISIS'.title())#自动把第一个字母变成大写，把其他字母都变成小写
print(ms[0].title())
#修改、添加和删除元素
ms[0]='hello everyone, i am 呆呆'
print(ms[0].title())
#append()在列表末尾添加元素  insert()在任意位置添加元素
ms.append('m4')
ms.insert(4,'m5')
print(ms)
#del语句 删除列表指定位置处的元素 pop()方法 弹出列表中的元素，但是仍然可以使用
del ms[4]
print(ms)
#pop使用
n1='你'
n2='我'
n3='他'
ns=[n1,n2,n3]
del ns[0]
ns.pop()
print(n1)
print(n3)

ms=['m1','m2','m3']
abc=ms.pop(2)#pop出的元素还可以用
print(abc)
#remove()可用于不知道元素位置但知道元素值的情况 列表.remove(元素值)

#使用列表中的元素 用f
print(f'here is the {ms[0]}')