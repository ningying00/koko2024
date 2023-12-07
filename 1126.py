import abc
import random
import time
from functools import reduce


def out(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"运行时间为{end_time - start_time}")

    return inner


@out
def index():
    time.sleep(random.randrange(1, 5))
    print("123321")


# index()

# a = lambda x: print('big') if x > 5 else print('small')
# # a(5)

# foo = [2, 18, 9, 22, 17, 8, 21]
# a3 = filter(lambda x: x % 3 == 0, foo)
# print(list(a3))
#
# a1 = [i * 3 + 5 for i in foo]
# print(a1)
# a2 = map(lambda x: x * 3 + 5, foo)
# print(list(a2))
#
# aa = [1, 2, 3, 4, 5]
# bb = [5, 6, 7, 8, 9]
# ab = map(lambda x, y: x + y, aa, bb)
#
# print(list(ab))

# ff = [1, 2, 3, 4, 5]
#
# f1 = reduce(lambda x, y: x * 10 + y, ff)
# print(f1)

# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# c = ['1', '2']
# print(list(zip(a, b, c)))
# print(dict(zip(a, b)))


a = [1, 2, 3]
b = enumerate(a)
print(list(b))


class Car(metaclass=abc.ABCMeta):
    # def init__(self, brand, age):
    #     self.brand = brand
    #     self.age = age

    @abc.abstractmethod
    def broke(self):
        print('在刹车')

    def add(self):
        print('在加速')


class MiniCar(Car):
    def __init__(self, brand, age, weight):
        # super(MiniCar, self).__init__(brand, age)
        Car.__init__(brand, age, weight)
        self.weight = weight

    def print_weight(self):
        print(f"这是print_weight方法{self.weight}")

    def broke(self):
        print('xxx在刹车')


#cc = Car()
