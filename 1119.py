"""
1. 难度等级 I
如何实现 "1,2,3" 变成 ['1','2','3'] ?
"""
a1 = "1,2,3"
b1 = a1.split(",")
# print(b1)
"""
2. 难度等级 II
将列表[['a','b','c'],['d','e','f'],['g','h']]中的元素依次展开，得到 ⼀个新的列表
['a','b','c','d','e','f','g','h']
"""
a2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
b2 = []
[b2.extend(i) for i in a2]
# print(b2)
"""
3. 难度等级 III
假设今天的上课时间为5678秒，编程计算今天上课时间是多少时，多少分，多
少秒，以“xx时xx分xx秒”的形式表示出来。
"""


def time_change(time_a3=5678):
    b31 = time_a3 // (60 * 60)
    b32 = time_a3 % (60 * 60) // 60
    b33 = time_a3 % 60
    print(f"{b31}时{b32}分{b33}秒")


# time_change()
"""
4. 输⼊字符串，将字符串的开头和结尾变成'+'，产⽣⼀个新的字符串
"""
# a4 = input("请输入：")
# a4 = list(a4)
# a4[0] = "+"
# a4[-1] = "+"
# a4 = "".join(a4)
# print(a4)
"""
5. 猜数
给定⼀个定值，⽐如说 99
让⽤户输⼊数字，给⽤户三次机会，如果三次之内猜对了(输⼊的值等于99)，
显示猜测正确
如果三次之内没有猜对，退出循环，显示'stupid' 要求，⽤2种⽅式实现
"""


def compare1(a=99):
    for i in range(3):
        aa = int(input("请输入:"))
        if aa == a:
            print("猜测正确")
            break
        else:
            if i == 2:
                print("stupid")
            else:
                print("猜错啦")


def compare2(a=99):
    aaa = 3
    while aaa:
        aa = int(input("请输入:"))
        if aa == a:
            print("猜测正确")
            break
        elif aaa == 1:
            print('stupid')
            aaa -= 1
        else:
            print("猜错啦")
            aaa -= 1


# compare1()
# compare2()
"""
6. 输⼊某年某⽉某⽇，判断这⼀天是这⼀年的第⼏天？ 这边简单考虑，不考虑 闰
年的情况。
"""
date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def date_1(dd="2024年01月01日"):
    if dd[5:7] == "01":
        return f"{dd}是{dd[:4]}年第{(int(dd[-3:-1]))}天"
    else:
        d = []
        for i in range(1, int(dd[5:7])):
            d.append(date_dict[i])
        return f"{dd}是{dd[:4]}年第{(sum(d) + int(dd[-3:-1]))}天"

# print(date_1("2024年01月01日"))
# print(date_1("2024年01月31日"))
# print(date_1("2024年03月01日"))
# print(date_1("2024年12月31日"))
"""
7. 输出 101~200 之间的所有素数 素数，就是 只能被 1 和 ⾃⼰整除的数， 判断素
数的⽅法：⽤⼀个数分别去除2到这个数的平⽅根，如果能被整除，则表明此数
不是素数，反之是素数。
"""
num_list = [i for i in range(101, 200)]


def prime_number(num_list):
    a = []
    for ii in num_list:
        for j in range(2, int(pow(ii, 0.5)) + 1):
            if ii % j == 0:
                a.append(ii)
                break
    return set(num_list) - set(a)


print(prime_number(num_list))
