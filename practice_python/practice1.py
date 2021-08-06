import math
import random
import re


class Practice1:

    @staticmethod
    def show_menu():
        print("PRACTICE 1".center(50, "="))
        print("1. Split a String Based on Vowels and Consonants")
        print("2. Burglary Series (10): Calculate Difference")
        print("3. Distance Between Two Points")
        print("4. Sum of all Evens in a Matrix")
        print("5. Count the Letters and Digits")
        print("6. Numbers to Arrays and Vice Versa")
        print("7. Return First and Last Parameter")
        print("8. Regex Series: String Contains at Least One Digit")
        print("9. Return Odd > Even")
        print("10. Convert Key, Values in a Dictionary to List")
        print("0. Exit")
        print("".center(50, "="))

    def split(self, txt):
        vowel = ""
        consonant = ""
        for i in txt:
            if i in ["a", "e", "u", "i", "o"]:
                vowel += i
            else:
                consonant += i
        return vowel + consonant

    def calc_diff(self, obj, limit):
        sum = 0
        for value in obj.values():
            sum += value
        return sum - limit

    def get_distance(self, a, b):
        sum = 0
        for key in a.keys():
            sum += (b[key] - a[key]) ** 2
        return round(math.sqrt(sum), 3)

    def sum_of_evens(self, lst):
        sum = 0
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] % 2 == 0:
                    sum += lst[i][j]
        return sum

    def count_all(self, txt):
        count_letter = 0
        count_digit = 0
        for i in txt:
            if re.search("[a-zA-Z]", i):
                count_letter += 1
            if re.search("[0-9]", i):
                count_digit += 1
        return {"LETTERS": count_letter, "DIGITS": count_digit}

    def to_list(self, num):
        return [int(i) for i in str(num)]

    def to_number(self, lst):
        return int("".join([str(i) for i in lst]))

    def first_arg(self, *args):
        if args == ():
            return None
        return args[0]

    def last_arg(self, *args):
        if args == ():
            return None
        return args[-1]

    def has_digit(self, txt):
        if re.search("[a-z]", txt):
            if re.search("[0-9]", txt):
                return True
        return False

    def oddeven(self, lst):
        count_odd = 0
        count_even = 0
        str_lst = str(lst[0])
        if len(lst) == 1:
            for i in str_lst:
                if int(i) % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        else:
            for i in lst:
                if i % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        return count_odd > count_even

    def dict_to_list(self, d):
        lst = [(key, value) for key, value in d.items()]
        lst.sort(key=lambda x: x[0])
        return lst


if __name__ == "__main__":
    p = Practice1()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Split a String Based on Vowels and Consonants".center(40, "-"))
            txt = input("Enter txt: ")
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.split(txt)))

        if choose == 2:
            print("Burglary Series (10): Calculate Difference".center(40, "-"))
            obj = {"baseball bat": 20}
            limit = 5
            print("Given obj = {}, limit = {}".format(obj, limit))
            print("Result = {}".format(p.calc_diff(obj, limit)))

        if choose == 3:
            print("Distance Between Two Points".center(40, "-"))
            a = {"x": -2, "y": 1}
            b = {"x": 4, "y": 3}
            print("Given a = {}, b = {}".format(a, b))
            print("Result = {}".format(p.get_distance(a, b)))

        if choose == 4:
            print("Sum of all Evens in a Matrix".center(40, "-"))
            lst = [
                [1, 0, 2],
                [5, 5, 7],
                [9, 4, 3]
            ]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.sum_of_evens(lst)))

        if choose == 5:
            print("Count the Letters and Digits".center(40, "-"))
            txt = "Hello World"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.count_all(txt)))

        if choose == 6:
            print("Numbers to Arrays and Vice Versa".center(40, "-"))
            num = 235
            lst = [2, 3, 5]
            print("Given num = {}, list = {}".format(num, lst))
            print("Result = {}".format(p.to_list(num)))
            print("Result = {}".format(p.to_number(lst)))

        if choose == 7:
            print("Return First and Last Parameter".center(40, "-"))
            print("Result = {}".format(p.first_arg(1, 2, 3)))
            print("Result = {}".format(p.last_arg(1, 2, 3)))

        if choose == 8:
            print("Regex Series: String Contains at Least One Digit".center(40, "-"))
            txt = "gnd7rksfnx0vxz"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.has_digit(txt)))

        if choose == 9:
            print("Return Odd > Even".center(40, "-"))
            lst = random.sample(range(1, 100), 10)
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.oddeven(lst)))

        if choose == 10:
            print("Convert Key, Values in a Dictionary to List".center(40, "-"))
            d = {
                "D": 1,
                "B": 2,
                "C": 3
            }
            print("Given dict = {}".format(d))
            print("Result = {}".format(p.dict_to_list(d)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT".center(50, "="))
