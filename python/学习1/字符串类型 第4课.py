# 2021/7/12  #9:21
#字符串可以用单引号，双引号，三引号表示  而三引号可以换行写
str1='人生苦短，我用python'
str2="人生苦短，我用python"
str3="""人生苦短，
我用python"""

str4='''人生苦短，
我用python'''

str5="人生苦短，" \
     "我用python"   #这个最后展现出来的是一行
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))
print(str5,type(str5))
