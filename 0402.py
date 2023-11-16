import random
from functools import reduce

'''难度等级 II
猜数
* 给定一个定值，比如说 99
* 让用户输入数字，给用户三次机会，如果三次之内猜对了(输入的值等于99)，显示猜测正确
* 如果三次之内没有猜对，退出循环，显示'stupid'
# 要求，用2种方式实现'''


def compare1(a=99):
    for i in range(3):
        aa = input("请输入:")
        if int(aa) == a:
            print("猜测正确")
            break
        elif int(aa) != a and i == 2:
            print('stupid')
        else:
            continue


def compare2(a=99):
    aaa = 0
    while aaa < 3:
        aa = input("请输入:")
        if int(aa) == a:
            print("猜测正确")
            break
        elif int(aa) != a and aaa == 2:
            print('stupid')
            break
        else:
            aaa += 1


# compare1()
# compare2()
'''难度等级 II
输入某年某月某日，判断这一天是这一年的第几天？ 这边简单考虑，不考虑 闰年的情况。'''
date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


# dd不同格式待处理
def date_1(dd="2024年3月01日"):
    if dd[5] == "1":
        return int(dd[7:9])
    else:
        d = []
        for i in range(1, int(dd[5])):
            d.append(date_dict[i])
        return sum(d) + int(dd[7:9])


# print(date_1())
'''难度等级 III
输出 9*9 乘法口诀表'''


def cc(i=9):
    for a in range(1, i + 1):
        for b in range(1, a + 1):
            print(f"{b}*{a}={a * b}", end=" ")
        print("")


# cc()


'''难度等级 III
输出 101~200 之间的所有素数
素数，就是 只能被 1 和 自己整除的数， 
判断素数的方法：用一个数分别去除2到这个数的平方根，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 '''

num_list = [i for i in range(101, 200)]


def prime_number(num_list):
    a = []
    for ii in num_list:
        for j in range(2, int(pow(ii, 0.5)) + 1):
            if ii % j == 0:
                a.append(ii)
                break
    return set(num_list) - set(a)


#print(prime_number(num_list))

'''实现猜拳小游戏 II -- 尽量先自己完成
实现 人 和 电脑的 猜拳游戏
用户输入 数字 0 石头，1 剪刀 2 布
电脑随机产生 0 到 2 的整数，
进行输赢对比'''
aa = 1
while aa:
    a = random.randint(0, 2)
    #print(a)
    b = input("请输入0，1，2:")
    if a > int(b):
        print(f"电脑为{a}输")
        y = input('是否继续：Y or N')
        if y == 'N':
            aa = 0
    elif a == int(b):
        print(f"电脑为{a}平")
        y = input('是否继续：Y or N')
        if y == 'N':
            aa = 0
    else:
        print(f"电脑为{a}赢")
        y = input('是否继续：Y or N')
        if y == 'N':
            aa = 0
