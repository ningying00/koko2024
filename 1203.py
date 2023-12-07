class Animal:
    def __new__(cls, *args, **kwargs):
        # 重写__new__
        print('__new__ is called')
        return super(Animal, cls).__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 属性赋值时调用__setattr__()
    def __setattr__(self, key, value):
        print('_' * 10)
        print(self.__dict__)
        # 如果没有下面这个不会在dict里赋值
        # self.__dict__[key] = str(value).upper()

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age > other.age

    def __ne__(self, other):
        return self.name != other.name


# a1 = Animal("aa", 12)
# # a2 = Animal("bb", 10)
# # a3 = Animal("aa", 12)
#
# print(a1.name)


# print(a1 == a3)
# print(a1 > a2)
# print(a1 >= a3)
# print(a1 != a2)


class Iter_demo:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[len(self.data) - self.index - 1]


a = Iter_demo('abc')
for i in a:
    print(i)
