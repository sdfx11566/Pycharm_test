# 阶梯

x = 0
while x < 1000:
    if (x % 2 ==1)\
    and (x % 3 ==2)\
    and (x % 5 == 4)\
    and (x % 6 == 5)\
    and (x % 7 == 0):
        print(x)
        x += 1
    else:
        x += 1
print("循环结束")


# 奇数
ls = range(1,100)
for i in ls:
    if i % 2 == 1:
        print(i)