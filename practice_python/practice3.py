import random
import re


class Practice3:

    @staticmethod
    def show_menu():
        print("PRACTICE 3".center(50, "="))
        print("1. Odds vs. Evens")
        print("2. Return a List of Sublists")
        print("3. Functioninator 8000")
        print("4. Apocalyptic Numbers")
        print("5. Number Split")
        print("6. Return the Highest and Lowest Numbers")
        print("7. Remove Duplicates from a List")
        print("8. Sum of Number Elements in a List")
        print("9. One Odd and One Even")
        print("10. Emotify the Sentence")
        print("0. Exit")
        print("".center(50, "="))

    def odds_vs_evens(self, num):
        sum_odd = 0
        sum_even = 0
        for i in str(num):
            if int(i) % 2 == 0:
                sum_even += int(i)
            else:
                sum_odd += int(i)
        if sum_even == sum_odd:
            return "equal"
        elif sum_even > sum_odd:
            return "even"
        return "odd"

    def matrix(self, x, y, z):
        lst = []
        for i in range(x):
            lst.append([z for _ in range(y)])
        return lst

    def inator_inator(self, inv):
        if re.search("[a, u, o, i, e, A, E, I, O, U]", inv[-1]):
            return "{}-inator {}000".format(inv, len(inv))
        return "{}inator {}000".format(inv, len(inv))

    def apocalyptic(self, n):
        str_n = str(2 ** n)
        x = str_n.find("666")
        if x != -1:
            return f"Repent! {x} days until the Apocalypse!"
        return "Crisis averted. Resume sinning."

    def number_split(self, n):
        x = n // 2
        if n % 2 == 0:
            return [x, x]
        return [x, x + 1]

    def high_low(self, txt):
        lst_num = [int(i) for i in txt.split()]
        min = lst_num[0]
        max = lst_num[0]
        for i in lst_num:
            if min > i:
                min = i
            if max < i:
                max = i
        return f"{max} {min}"

    def remove_dups(self, lst):
        return list(dict.fromkeys(lst))

    def numbers_sum(self, lst):
        sum_digit = 0
        for i in lst:
            if type(i) == int:
                sum_digit += i
        return sum_digit

    def one_odd_one_even(self, n):
        str_n = str(n)
        if int(str_n[0]) % 2 == 0 and int(str_n[1]) % 2 != 0:
            return True
        if int(str_n[0]) % 2 != 0 and int(str_n[1]) % 2 == 0:
            return True
        return False

    def emotify(self, txt):
        if re.search("smile", txt):
            return "Make me :D"
        if re.search("grin", txt):
            return "Make me :)"
        if re.search("sad", txt):
            return "Make me :("
        if re.search("mad", txt):
            return "Make me :P"

if __name__=="__main__":
    p = Practice3()
    p.show_menu()
    choose = int(input("Enter your chooses: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Odds vs. Evens".center(40, "-"))
            num = 54870
            print("Given num = {}".format(num))
            print("Result = {}".format(p.odds_vs_evens(num)))

        if choose == 2:
            print("Return a List of Sublists".center(40, "-"))
            x, y, z = random.sample(range(1, 10), 3)
            print("Given x = {}, y = {}, z = {}".format(x, y, z))
            print("Result = {}".format(p.matrix(x, y, z)))

        if choose == 3:
            print("Functioninator 8000".center(40, "-"))
            inv = "Shrink"
            print("Given inv = {}".format(inv))
            print("Result = {}".format(p.inator_inator(inv)))

        if choose == 4:
            print("Apocalyptic Numbers".center(40, "-"))
            # n = random.randint(100, 200)
            n = 157
            print("Given n = {}".format(n))
            print("Result = {}".format(p.apocalyptic(n)))

        if choose == 5:
            print("Number Split".center(40, "-"))
            n = random.randint(3, 15)
            print("Given n = {}".format(n))
            print("Result = {}".format(p.number_split(n)))

        if choose == 6:
            print("Return the Highest and Lowest Numbers".center(40, "-"))
            txt = "1 2 3 4 5"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.high_low(txt)))

        if choose == 7:
            print("Remove Duplicates from a List".center(40, "-"))
            lst = [1, 0, 1, 0]
            print("Given lst = {}".format(lst))
            print("Result = {}".format(p.remove_dups(lst)))

        if choose == 8:
            print("Sum of Number Elements in a List".center(40, "-"))
            lst = [1, 2, "13", "4", "645"]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.numbers_sum(lst)))

        if choose == 9:
            print("One Odd and One Even".center(40, "-"))
            n = 21
            print("Given n = {}".format(n))
            print("Result = {}".format(p.one_odd_one_even(n)))

        if choose == 10:
            print("Emotify the Sentence".center(40, "-"))
            txt = "Make me smile"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.emotify(txt)))

        choose = int(input("\nEnter your chooses: "))
        print()
    print("EXIT PRACTICE 3".center(50, "="))
