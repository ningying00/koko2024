'''
难度等级 I
利用面试对象的编程思想，实现下面的功能

1. 小明 体重 80kg
2. 每跑步一次  重量减去 0.5kg
3. 每吃一顿饭  重量增加 0.1kg
'''
import random
from datetime import datetime


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def running(self):
        self.weight -= 0.5

    def eating(self):
        self.weight += 0.1


# pp = Person('小明', 80)
# pp.running()
# print(pp.weight)
# pp.eating()
# print(pp.weight)
'''
难度等级 II
用面向对象的思维 实现下列需求
1. 士兵  都有 姓名和一把枪
2. 士兵  可以 用枪开火
3. 枪 能都装填子弹
4. 枪 能够发射子弹
'''


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def s_use_g(self):
        print(f'士兵{self.name}使用{self.gun}')

    @classmethod
    def g_use1(cls):
        print('枪 能都装填子弹')

    @classmethod
    def g_use2(cls):
        print('枪 能够发射子弹')


Soldier.g_use1()
Soldier.g_use2()
ss = Soldier('cc', '来福')
ss.s_use_g()
'''
难度等级 II
利用多态实现我上课说的不同的游戏角色出拳的例子
'''

'''
难度等级 III
实现一个装饰器，每次调用函数时，将函数名字 和 调用时间写入到文件 a.txt 中

1. 要求先熟悉 python 文件的操作

2. 函数名可用 __name__ 来获取，如

3. 调用时间 可以熟悉 time 模块
'''


def w(func):
    def inner():
        u_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        func()
        with open('a.txt', 'w') as f:
            f.write(u_time+func.__name__)

    return inner


@w
def ss():
    print("调用一次函数")

ss()
'''
难度等级 II
用python 模拟实现 扔1000次硬币，然后分别显示出掷出正面和反面的次数

提示：
正面，反面 可以用 0 或 1 来代替，然后统计 1000次中 1 和 0 出现的次数
'''


def count_num(num):
    num_0 = 0
    num_1 = 0
    for i in range(num):
        if random.randint(0, 1) == 0:
            num_0 += 1
        else:
            num_1 += 1
    return num_0, num_1

# print(count_num(1000))
