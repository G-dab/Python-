# 2021/7/19  #8:28
'用continue来打印输出1到50里5的倍数'
for item in range(1,51):
    if item%5 != 0:
        continue
    print(item)