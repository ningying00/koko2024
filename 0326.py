'''
难度等级 I
'''
#  1:计算整型50乘以10再除以5的商并使用print输出。
from functools import reduce

print(int(50 * 10 / 5))
# 2：判断整型8是否大于10的结果并使用print输出。
print(8 > 10)
# 3：计算整型30除以2得到的余数并使用print输出
print(30 % 2)
# 4：使用字符串乘法实现 把字符串”我爱我的祖国”创建三遍并拼接起来最终使用print输出。
print("我爱我的祖国" * 3)

'''
难度等级 I
如何实现 "1,2,3" 变成 ['1','2','3'] ?
'''
a = ("1,2,3").split(',')
# print(a)
'''
难度等级 II
将列表[['a','b','c'],['d','e','f'],['g','h']]中的元素依次展开，得到 一个新的列表 ['a','b','c','d','e','f','g','h']
'''
b = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
bb = []


def bbb(x):
    for i in x:
        for j in range(len(i)):
            bb.append(i[j])
    return bb


print(bbb(b))

'''
难度等级 II
熟悉 列表的 sort() 方法中的key 和 reverse 参数的使用，并做demo
'''
c = [1, 5, 7, 8, 2, 3, 4]
cc = ["111", "11111", "1", "111111", "1111", "11"]
# c.sort(reverse=False)
# cc.sort(key=len, reverse=True)
# print(c)
# print(cc)
print(sorted(c, reverse=True))
'''
难度等级 III
将一个英文语句以单词为单位逆序排放，如 "i am a boy" 逆序排放后 "boy a am i"

难度等级 III
假设今天的上课时间为5678秒，编程计算今天上课时间是多少时，多少分，多少秒，以“xx时xx分xx秒”的形式表示出来。

难度等级 I
通过分片创一个与原列表实现反转的列表

难度等级 I
列表一次性追加多个值，用多种方法实现

难度II
输入字符串，将字符串的开头和结尾变成'+'，产生一个新的字符串

课堂布置的作业 字符串的count index 方法
'''
