'''难度等级 I
定义一个函数，实现传入整数的累乘的和，比如传入5 ，实现1+2!+3!+...+5!的和。
'''
from functools import reduce


def multiplication_sum(num=5):
    multiplication_s = []
    for j in range(1, num + 1):
        num1 = [i for i in range(1, j + 1)]
        multiplication_1 = reduce(lambda x, y: x * y, num1)
        multiplication_s.append(multiplication_1)
    return reduce(lambda xx, yy: xx + yy, multiplication_s)


print(multiplication_sum())

'''
    难度等级 II
    实现一个函数，判断传入的参数是否为回文
    
    所谓 回文，就是 左右对称的字符  如  "abccba"  "abcba"
'''


def num_nn(num):
    if len(num) == 1:
        print("NO")
    if num == num[::-1]:
        print('YES')
    else:
        print('NO')


# num_nn('aab')

'''难度等级 II
    打印 所有水仙花数
    
    所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方'''


def flower_num(num=153):
    num1 = [int(i) for i in str(num)]
    num_2 = map(lambda i: i * i * i, num1)
    num_sum = reduce(lambda x, y: x + y, num_2)
    if num_sum == num:
        print(f"{num} is flower")
    else:
        print((f"{num} isn't flower"))


# flower_num(153)

'''难度等级 III
        用冒泡排序实现 一个无序列表的排序   
        
        冒泡排序原理：
        
        每一趟只能确定将一个数归位。即第一趟只能确定将末位上的数归位，第二趟只能将倒数第 2 位上的数归位，依次类推下去。如果有 n 个数进行排序，只需将 n-1 个数归位，也就是要进行 n-1 趟操作。
        而 “每一趟 ” 都需要从第一位开始进行相邻的两个数的比较，将较大的数放后面，比较完毕之后向后挪一位继续比较下面两个相邻的两个数大小关系，重复此步骤，直到最后一个还没归位的数。
'''


# 初始版本1(没有相邻的位置比）
def rang_ll(l=[1, 3, 7, 2, 4, 0]):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def rang_l1(l=[1, 3, 7, 2, 4, 0]):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# 学习后优化版本
def rang_ll1(l=[1, 3, 7, 2, 4, 0]):
    sort_range = len(l) - 1
    sort_range_len = 0
    for i in range(len(l) - 1):
        is_sort = True
        for j in range(sort_range):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                is_sort = False
                sort_range_len = j
        sort_range = sort_range_len
        if is_sort:
            break
    return l


print(rang_ll())
print(rang_l1())
print(rang_ll1())
'''难度等级 II
        实现一个 函数 get_min, 函数返回列表lst 的最小值，要求不使用 min 函数
'''


def get_min(l=[10, 3, 7, 2, 4, 10]):
    min_num = l[0]
    for i in range(len(l)):
        if min_num > l[i]:
            min_num = l[i]
    return min_num


# print(get_min())
'''难度等级 II
        实现一个函数，该函数参数为任意数量的数字，在函数中实现这样的功能：统计在参数中 出现的数字的个数
        
        如 传入的参数为 func(3,5,3)
        则打印
        数字3 出现2次
        数字 5 出现1次
'''


# 预习作业
def func(*cc):
    cc_dict = {}
    for i in cc:
        if i in cc_dict.keys():
            cc_dict[i] += 1
        else:
            cc_dict[i] = 1
    return cc_dict


# 上课后优化！！！！！
ac = 'avvffbcc'
aa = set(ac)
dict_a = {}
for i in aa:
    dict_a[i] = ac.count(i)
print(dict_a)

# print(func(3, 5, 3))
c = func(3, 5, 3)
for i in c.items():
    print(f'数字{i[0]} 出现{i[1]}次')
