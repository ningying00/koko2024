"""
1.实现选择排序 难度等级 II
算法描述：
1. 在⼀个⻓度为 N 的⽆序数组中，第⼀次遍历 n-1 个数找到最⼩的和第⼀个数交换。
2. 第⼆次从下⼀个数开始遍历 n-2 个数，找到最⼩的数和第⼆个数交换。
3. 重复以上操作直到第 n-1 次遍历最⼩的数和第 n-1 个数交换，排序完成
"""
import time
from collections.abc import Iterable, Iterator
from functools import reduce
from sys import getsizeof


def choose_sort(l=[10, 2, 3, 5, 7, 4, 1]):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


# print(choose_sort())

"""
2. 统计⽂件内 字符串个数 难度等级I 有⽂件 a.txt(内容不为空，且有多⾏) 要求：找出出现次数最多的字符
"""
"""
本地测试验证直接读取文件会稍快，但会一次性占用内存很多；迭代读取文件稍慢，但每次占用内存很小
运行结果:
出现最多字符是 ,出现了705640次
每次循环占用内存50-600
耗时0.8579890727996826
************************************************分割线*************************************************************
出现最多字符是 ,出现了705640次
读取文件占用内存8905314
耗时0.7670009136199951
"""


def count_str():
    dict_str = {}
    size_s = ''
    with open('a.txt', 'r') as f:
        for i in f:
            for j in i[:-1]:
                if j in dict_str:
                    dict_str[j] += 1
                else:
                    dict_str[j] = 1
            # print(f"循环时每次占用内存{getsizeof(i)}")
    # print(isinstance(f, Iterable))
    # print(isinstance(f, Iterator))
    # print(dict_str)
    # 收集结果后对items，根据value排序
    sorted_items = sorted(dict_str.items(), key=lambda x: x[1], reverse=True)
    print(f"出现最多字符是{sorted_items[0][0]},出现了{sorted_items[0][1]}次")


s1 = time.time()
count_str()
s2 = time.time()
print(f"耗时{s2 - s1}")

print(
    "************************************************分割线*************************************************************")


def count_str2():
    with open('a.txt', 'r') as f2:
        content = f2.read()
    # print(type(content),content)
    dict_str2 = {}
    for x in content:
        if x in dict_str2:
            dict_str2[x] += 1
        else:
            dict_str2[x] = 1
    sorted_items2 = sorted(dict_str2.items(), key=lambda x: x[1], reverse=True)
    print(f"出现最多字符是{sorted_items2[0][0]},出现了{sorted_items2[0][1]}次")
    print(f"读取文件占用内存{getsizeof(content)}")


s3 = time.time()
count_str2()
s4 = time.time()
print(f"耗时{s4 - s3}")
"""
3.难度等级III 实现算法，找出 列表中第⼆⼤的数, 如列表 [3,5,2,8,4,7,9] 第⼆⼤的数是 8
"""


# 1、假定1号位、2号位为第一、第二大
# 2、后面的数与第一、第二比较，比第一、第二都大为第一大，原第一大为第二大
# 3、继2，比第一小比第二大，原第一不变，第二交换位置
# 4、继3，比第二还小不变
def pick_second(l=[3, 5, 2, 8, 4, 7, 9]):
    if l[0] < l[1]:
        l[0], l[1] = l[1], l[0]
    for i in range(2, len(l)):
        if l[i] > l[0] and l[i] > l[1]:
            l[i], l[0] = l[0], l[i]
            l[i], l[1] = l[1], l[i]
        elif l[i] > l[1]:
            l[i], l[1] = l[1], l[i]
    return l[1]


# print(f'第⼆⼤的数是{pick_second()}')
"""
4.难度等级I 定义⼀个函数，实现传⼊整数的累乘的和，⽐如传⼊5 ，实现1+2!+3!+...+5!的和
"""


def multip_sum1(mun=5):
    m_s = 0
    for i in range(1, mun + 1):
        m_l = [j for j in range(1, i + 1)]
        m = reduce(lambda x, y: x * y, m_l)
        m_s += int(m)
    return m_s


#print(multip_sum1())
#################################分割线############################


def multip_sum2(i):
    l1 = [i for i in range(1, i + 1)]
    m = reduce(lambda x, y: x * y, l1)
    return m


def multip_sum3(num=5):
    l1 = [i for i in range(1, num + 1)]
    m_s = map(multip_sum2, l1)
    return sum(list(m_s))


#print(multip_sum3())

"""
5.难度等级I 输⼊⼀个整数n，⽤⽣成器打印出从 0~n 中的所有偶数
"""


def pick_even_number(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


p = pick_even_number(4)

while True:
    try:
        print(next(p))
    except StopIteration:
        break

"""
6.安装好 selenium 并⽤成功打开百度⾸⻚
"""
from selenium import webdriver

# 未配置环境变量，指定驱动位置
# driver = webdriver.Chrome(executable_path='F:\python\chromedriver-win64\chromedriver-win64\chromedriver')
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.quit()
