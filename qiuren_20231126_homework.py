"""
1. 难度等级 II 实现⼀个装饰器，每次调⽤函数时，将函数名字 和 调⽤时间写⼊到⽂件 a.txt 中
tips：
要求先熟悉 python ⽂件的操作
函数名可⽤ name 来获取
调⽤时间 可以熟悉 time 模块
"""
import random
import time


def w(func):
    def inner():
        start_time = time.time()
        # 转化为时间数组,为后续格式化时间做准备
        start_time_date = time.localtime(start_time)
        func()
        end_time = time.time()
        end_time_date = time.localtime(end_time)
        used_time = end_time - start_time
        # print(start_time, end_time, used_time,start_time_date,end_time_date)
        # w:覆盖写入
        # with open("a.txt", "w") as f:
        # a:追加写入
        with open("a.txt", "a") as f:
            f.write(f"调用函数的名称为{func.__name__}\n"
                    # 格式化开始、结束时间
                    f"调用开始时间为{time.strftime('%Y-%m-%d,%H:%M:%S', start_time_date)}\n"
                    f"调用结束时间为{time.strftime('%Y-%m-%d,%H:%M:%S', end_time_date)}\n"
                    f"函数运行的时间为{used_time}\n")

    return inner


@w
def func1():
    time.sleep(1)
    print("调用一次函数")


# func1()
"""
2. 难度等级 II ⼀个实验。如果你掷硬币100次，并在每次正⾯时写下“H”,在每次反⾯时写下“T”，就会创建⼀个看起来像“TTTHHTHTTHHHH”这样的列表。如果你要求⼀个⼈进⾏100次随机掷硬币，你可能会得到正反交替的结果，例如“HHTTHTTTHHHT”。 编写⼀个程序，计算随机⽣成的正⾯和反列表中出现连续6个正⾯或者6个反⾯的频率，重复实验1000次，检查出现连续6个正⾯或者反⾯的实验次数，并计算出现的频率。 即 1000次实验中，每次回掷硬币100 次 ，然后判断 这 100次内是否有 连续6 次正⾯ 或 反⾯ 的情况"""


# 用迭代器实现外层1000次循环
def w1(param):
    def w2(func):
        def inner(num, freq):
            # 记录总的频次-
            result_sum = 0
            # 记录是否出现6次相同
            result_count = 0
            # 循环调用1000次
            for i in range(param):
                result = func(num, freq)
                # print(f"投掷100次连续出现6次相同的频次{result}")
                if result != 0:
                    result_count += 1
                    result_sum += result
            print(f"{param}次中有{result_count}次出现连续6次相同的，同出现了{result_sum}次")

        return inner

    return w2


# **********************************************************分割线******************************************************************************
# 用随机数0，1模拟一次掷硬币，0：正面（H），1：反面（T）
# 如果与这次与上一次结果相同，则记录为一次有效结果+1；否则重置为1并从这一次开始重新记录
# 记录结果每长度=6则记录一次连续6次相同，并重新开始记录，循环完成返回总共出现的次数
# 优化：从第96次(倒数第5次）开始，如果结果与上一次不一致，则无需再投掷可跳出循环

# 重新
def coin1():
    coin_result = ''
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin_result += 'H'
        else:
            coin_result += 'T'
    if "TTTTTT" in coin_result or "HHHHHH" in coin_result:
        return 1
    else:
        return 0


s_sum = 0
for j in range(1000):
    s_sum += coin1()

print(s_sum,s_sum/1000)
###########################################分割线###########################################################################
@w1(param=1000)
def toss_coin(num=100, freq=6):
    # 第一次投掷结果
    coin_result_0 = random.randint(0, 1)
    result = 1
    result_sum = 0
    for i in range(num):
        coin_result_i = random.randint(0, 1)
        # 打印投币结果验证
        # print(coin_result_i,end='')
        if coin_result_i == coin_result_0:
            result += 1
        else:
            coin_result_0 = coin_result_i
            result = 1
        if result == 6:
            result_sum += 1
            result = 1
        if i > num - freq + 1 and result == 1:
            break
    return result_sum


# toss_coin(100, 6)
"""
# 记录总的频次-
result_sum = 0
# 记录是否出现6次相同
result_count = 0
# 循环调用1000次
for i in range(1000):
    result = toss_coin()

    print(f"投掷100次连续出现6次相同的频次{result}")
    if result != 0:
        result_count += 1
        result_sum += result
print(f"1000次中有{result_count}次出现连续6次相同的，同出现了{result_sum}次")
"""

"""
3.难度等级 I 假设⼀个游戏的⻆⾊ 装备如下 goods = ['gold coin','dagger','goldcoin','gold coin','ruby',‘rope’.......] ，请写⼀个⼩程序，统计 他的装备，返回如下所
示： 3gold coin 1 rope 1 dagger 1 ruby Total number of item: 48
"""
goods = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope']


# 循环所有装备，存在数量+1，不存在记录并记录数量为1
def count_goods1(goods):
    dict_goods = {}
    for i in goods:
        if i not in dict_goods:
            dict_goods[i] = 1
        else:
            dict_goods[i] += 1
    for j in dict_goods.keys():
        print(str(dict_goods[j]) + j, end=' ')

    print(f'Total number of item: {len(goods)}')


# count_goods1(goods)


#################################################################分割线########################################################################
# 用set特性，找到种类，再根据种类统计数量
def count_goods2(goods):
    goods_set = list(set(goods))
    for i in goods_set:
        print(f"{goods.count(i)}{i}", end=' ')


# count_goods2(goods)
"""
4. 难度等级II 实现冒泡排序
"""


def bubble_sort(l=[12, 2, 3, 6, 30, 1]):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print(bubble_sort())

"""
5.难度等级II 实现⼀个函数，该函数参数为任意数量的数字，在函数中实现这样的功能：统计在参数中 出现的数字的个数如 传⼊的参数为 func(3,5,3) 则打印 数字3 出现2次 数字 5 出现1次
"""


def count_number(*num):
    num_dict = {}
    for i in num:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    for j in num_dict:
        print(f"数字{j} 出现{num_dict[j]}次", end=' ')


# count_number(3, 5, 3)

"""
6. 难度等级I 利⽤⾯试对象的编程思想，实现下⾯的功能
b. ⼩明 体重 80kg
c. 每跑步⼀次 重量减去 0.5kg
d. 每吃⼀顿饭 重量增加 0.1kg
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def running(self):
        self.weight -= 0.5

    def eating(self):
        self.weight += 0.1

# xm = Person("小明", 80)
# xm.running()
# print(xm.weight)
# xm.eating()
# print(xm.weight)
