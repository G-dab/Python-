# 2021/7/13  #13:06
cars=['a','c','ab','b','aa']
#sort()可对列表进行永久排序
cars.sort()#按字母进行排序
print(cars)
cars.sort(reverse=True)#按字母进行倒序排列
print(cars)

#sorted()函数可以对列表进行临时排序并显示出来，但不影响原列表的顺序
print(sorted(cars))


#倒着打印列表 用reverse()方法
print(cars)
print(cars.reverse())
#len()函数确定长度
print(len(cars))

