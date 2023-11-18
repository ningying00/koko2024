'''
难度等级 II
实现选择排序

实现原理：
　设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换
　重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序

算法描述：
1. 在一个长度为 N 的无序数组中，第一次遍历 n-1 个数找到最小的和第一个数交换。
2. 第二次从下一个数开始遍历 n-2 个数，找到最小的数和第二个数交换。
3. 重复以上操作直到第 n-1 次遍历最小的数和第 n-1 个数交换，排序完成。

'''

# 学习后复习
from collections import Counter


def choose_range(l=[1, 3, 7, 2, 4, 0]):
    min_index = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                min_index = i
                l[min_index], l[j] = l[j], l[min_index]
    return l


# print(choose_range())
'''
难度等级 II
实现用户登录系统，用户名密码正确，提示登录成功，用户名密码不匹配，提示密码错误，你还有几次登录机会    当用户输入三次密码时，提示不能登录,
用户名，密码存放在字典中 user_dict= {"cc":"123123","小牛":"123123"}
'''


def user_login1():
    user_dict = {"cc": "123123", "小牛": "123123"}
    for i in range(3):
        username = input('请输入账号')
        password = input('请输入密码')
        if username in user_dict and password == user_dict[username]:
            print("登录成功")
            break
        elif i < 2:
            print(f"密码错误,你还有{2 - i}次机会")
        elif i == 2:
            print("超过次数，不能登录")


# user_login1()

'''
难度等级 II
有文件 a.txt(内容不为空，且有多行)
要求：找出出现次数最多的字符
'''
# 查资料Counter
with open('a.txt', 'r') as f:
    rr = f.readlines()
rr = "".join(rr)
r1 = Counter(rr)
print(r1.most_common())
'''
难度等级 III
实现算法，找出 列表中第二大的数, 
如列表 [3,5,2,8,4,7,9] 第二大的数是 8
'''


# 学习后复习
def range_sce(l=[3, 5, 2, 8, 4, 7, 9]):
    max_index = 0
    sec_index = 1
    if l[0] < l[1]:
        l[0], l[1] = l[1], l[0]
    for i in range(2, len(l)):
        if l[i] > l[max_index]:
            sec_index = max_index
            max_index = i
        elif l[i] > l[sec_index]:
            sec_index = i
    return l[sec_index]


print(range_sce())
'''
难度II
自习部分

1. 掌握 python 中的文件操作
'''
