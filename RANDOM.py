import random

secert = random.randint(1,100)

times = 3

while times:
    num = input("请输入数字：")
    if num.isdigit():
        tmp = int(num)
        if tmp == secert:
            print("you r right")
            break
        elif tmp < secert:
            print("so small")
            times = times - 1
        else:
            print("so large")
            times = times - 1
    else:
        print("num")

print("end")