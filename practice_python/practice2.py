import random
import re


class Practice2:

    @staticmethod
    def show_menu():
        print("PRACTICE 2".center(50, "="))
        print("1. Sum of Two Digit Numbers")
        print("2. Frequency Distribution")
        print("3. Alphanumeric Restriction")
        print("4. Factor Chain")
        print("5. Multi-division")
        print("6. Transforming Words into Binary Strings")
        print("7. Apples and Bananas")
        print("8. Reverse Words Starting With a Particular Letter")
        print("9. Flatten the Curve")
        print("10. Video Length in Seconds")
        print("0. Exit")
        print("".center(50, "="))

    def two_digit_sum(self, n):
        str_n = str(n)
        sum = 0
        for i in str_n:
            sum += int(i)
        return sum

    def get_frequencies(self, lst):
        d = {i: lst.count(i) for i in lst}
        return d

    def alphanumeric_restriction(self, s):
        if s == "":
            return False
        if all(i.isalpha() for i in s):
            return True
        if all(i.isdigit() for i in s):
            return True
        return False

    def factor_chain(self, lst):
        for i in range(len(lst) - 1):
            if lst[i+1] % lst[i] == 0:
                continue
            else:
                return False
        return True

    def abcmath(self, a, b, c):
        sum = a
        for i in range(b):
            sum += sum
        return sum % c == 0

    def convert_binary(self, string):
        lst = []
        for i in string:
            if re.search("[a-mA-M]", i):
                lst.append("0")
            if re.search("[n-zN-Z]", i):
                lst.append("1")
        return "".join(lst)

    def vow_replace(self, word, vowel):
        new_word = ""
        for w in word:
            if w in ["a", "o", "u", "e", "i"]:
                new_word += vowel
            else:
                new_word += w
        return new_word

    def special_reverse(self, s, c):
        return " ".join([i[::-1] if i[0] == c else i for i in s.split()])

    def flatten_the_curve(self, lst):
        if lst == []:
            return []
        avg = round(sum(lst) / len(lst), 1)
        return [avg for i in lst]

    def minutes_to_seconds(self, time):
        lst = time.split(":")
        sum = 0
        if int(lst[1]) >= 60:
            return False
        sum += int(lst[0]) * 60 + int(lst[1])
        return sum

if __name__=="__main__":
    p = Practice2()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Sum of Two Digit Numbers".center(40, "-"))
            n = random.randint(10, 99)
            print("Given n = {}".format(n))
            print("Result = {}".format(p.two_digit_sum(n)))

        if choose == 2:
            print("Frequency Distribution".center(40, "-"))
            lst = ["A", "B", "A", "A", "A"]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.get_frequencies(lst)))

        if choose == 3:
            print("Alphanumeric Restriction".center(40, "-"))
            s = "ed@bit"
            print("Given str = {}".format(s))
            print("Result = {}".format(p.alphanumeric_restriction(s)))

        if choose == 4:
            print("Factor Chain".center(40, "-"))
            lst = [2, 4, 6, 7, 12]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.factor_chain(lst)))

        if choose == 5:
            print("Multi-division".center(40, "-"))
            a, b, c = random.sample(range(1, 10), 3)
            print("Given a {}, b = {}, c = {}".format(a, b, c))
            print("Result = {}".format(p.abcmath(a, b, c)))

        if choose == 6:
            print("Transforming Words into Binary Strings".center(40, "-"))
            str = "house"
            print("Given strig = {}".format(str))
            print("Result = {}".format(p.convert_binary(str)))

        if choose == 7:
            print("Apples and Bananas".center(40, "-"))
            word = "apples and bananas"
            vowel = "u"
            print("Given word = {}, vowel = {}".format(word, vowel))
            print("Result = {}".format(p.vow_replace(word, vowel)))

        if choose == 8:
            print("Reverse Words Starting With a Particular Letter".center(40, "-"))
            s = "word searches are super fun"
            c = "s"
            print("Given s = {}, c = {}".format(s, c))
            print("Result = {}".format(p.special_reverse(s, c)))

        if choose == 9:
            print("Flatten the Curve".center(40, "-"))
            lst = [1, 2, 3, 4, 5]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.flatten_the_curve(lst)))

        if choose == 10:
            print("Video Length in Seconds".center(40, "-"))
            time = "121:59"
            print("Given time = {}".format(time))
            print("Result = {}".format(p.minutes_to_seconds(time)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PRACTICE 2".center(50, "="))