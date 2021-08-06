# def print_x(x):
#     return x
#
# def test_print_x():
#     assert print_x(3) == 3
#
# test_print_x()
# def split(self, txt):
#     vowel = ""
#     consonant = ""
#     for i in txt:
#         if re.search("[a, e, u, i, o]", i):
#             vowel += i
#         else:
#             consonant += i
#     return vowel + consonant
# d = {}
# for _ in range(3):
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     d[x] = y
#
# print(d)
# import re
# txt = "laeuoikpqw"
# x = re.search("[^a-e]", txt)
# print(x)
# x = "43264573658142353463158"
# c1 = 0
# c2 = 0
# for i in x:
#     if int(i) % 2 == 0:
#         c1 += 1
#     else:
#         c2 += 1
#
# print(c1 > c2)
# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# l = []
# for key, value in d.items():
#     l.append((key, value))
# print(l)
# printimport re
#
# s = "housE"
# for i in s:
#     if re.search("[a-mA-M]", i)
#     print(l)
# x = 11 // 2
# print(x)
# l1 = [1, 2, 3, 3]
# l2 = [3, 4]
# # l3 = l1 * l2
# # print(l3)
# print(list(dict.fromkeys(l1)))
# import math
#
# print(math.ceil(21/10))
# num = "2, 3"
# lst = [int(i) for i in num.split(", ")]
# tich = 1
# for i in lst:
#     tich *= i
# print(tich)
# print(type(None).__name__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age == other.age:
            return "{} is the same age as me.".format(other.name)
        if self.age > other.age:
            return "{} is younger than me.".format(other.name)
        return "{} is older than me.".format(other.name)

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
print(p1.compare_age(p2))
