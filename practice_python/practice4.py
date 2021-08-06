import math
import random
import re


class Practice4:

    @staticmethod
    def show_menu():
        print("PRATICE 4".center(50, "="))
        print("1. Applying Discounts")
        print("2. Words that Start with a Vowel")
        print("3. The DECIMATOR")
        print("4. Instant JAZZ")
        print("5. Same Parity?")
        print("6. Compare by ASCII Codes")
        print("7. Edabit Experience Points")
        print("8. Fix the Error: Vowel Edition")
        print("9. Type of Value")
        print("10. Sort Numbers in Descending Order")
        print("0. Exit")
        print("".center(50, "="))

    def get_discounts(self, nums, d):
        int_d = int(d[:-1])
        return [i * (int_d / 100) for i in nums]

    def retrieve(self, txt):
        lst = []
        # return [i.lower() for i in lst if re.search("[a, e, u, o, i]", i)]
        for i in txt.split():
            str = ""
            if re.search("[a, e, u, o, i]", i[0].lower()):
                for j in i:
                    if j.isalpha():
                        str += j.lower()
                lst.append(str)
        return lst

    def DECIMATOR(self, txt):
        n = math.ceil(len(txt) / 10)
        return txt[:-n]

    def jazzify(self, lst):
        new_lst = []
        for i in lst:
            if re.search("[7]", i[-1]):
                new_lst.append(i)
            else:
                i += "7"
                new_lst.append(i)
        return new_lst

    def parity_analysis(self, num):
        str_num = str(num)
        sum = 0
        for i in str_num:
            sum += int(i)
        if num % 2 != 0 and sum % 2 != 0:
            return True
        if num % 2 == 0 and sum % 2 == 0:
            return True
        return False

    def ascii_sort(self, lst):
        sum_lst = []
        for i in lst:
            sum = 0
            for j in range(len(i)):
                sum += ord(i[j])
            sum_lst.append(sum)
        return lst[sum_lst.index(min(sum_lst))]

    def get_xp(self, d):
        sum_xp = 0
        for key in d.keys():
            if key == "Very Easy":
                sum_xp += d[key] * 5
            if key == "Easy":
                sum_xp += d[key] * 10
            if key == "Medium":
                sum_xp += d[key] * 20
            if key == "Hard":
                sum_xp += d[key] * 40
            if key == "Very Hard":
                sum_xp += d[key] * 80
        return f"{sum_xp}XP"

    def remove_vowels(self, string):
        return "".join(re.findall("[^a, ^e, ^i, ^u, ^o]", string))

    def get_type(self, value):
        return type(value).__name__       #Convert a python 'type' object to a string

    def sort_descending(self, num):
        lst = [int(i) for i in str(num)]
        lst.sort(reverse=True)
        return int("".join([str(i) for i in lst]))

if __name__=="__main__":
    p = Practice4()
    p.show_menu()
    choose = int(input("Enter your chooses: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Applying Discounts".center(40, "-"))
            nums = [2, 4, 6, 11]
            d = "50%"
            print("Given nums = {}, d = {}".format(nums, d))
            print("Result = {}".format(p.get_discounts(nums, d)))

        if choose == 2:
            print("Words that Start with a Vowel".center(40, "-"))
            txt = "Exercising is a healthy way to burn off energy."
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.retrieve(txt)))

        if choose == 3:
            print("The DECIMATOR".center(40, "-"))
            txt = "1234567890AB"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.DECIMATOR(txt)))

        if choose == 4:
            print("Instant JAZZ".center(40, "-"))
            lst = ["Dm", "G", "E", "A7"]
            print("Given lst = {}".format(lst))
            print("Result = {}".format(p.jazzify(lst)))

        if choose == 5:
            print("Same Parity?".center(40, "-"))
            num = random.randint(1, 999)
            print("Given num = {}".format(num))
            print("Result = {}".format((p.parity_analysis(num))))

        if choose == 6:
            print("Compare by ASCII Codes".center(40, "-"))
            lst = ["victory", "careless"]
            print("Given lst = {}".format(lst))
            print("Result = {}".format(p.ascii_sort(lst)))

        if choose == 7:
            print("Edabit Experience Points".center(40, "-"))
            d = {
                "Very Easy": 11,
                "Easy": 0,
                "Medium": 2,
                "Hard": 0,
                "Very Hard": 27
            }
            print("Given d = {}".format(d))
            print("Result = {}".format(p.get_xp(d)))

        if choose == 8:
            print("Fix the Error: Vowel Edition".center(40, "-"))
            string = "hello"
            print("Given string = {}".format(string))
            print("Result = {}".format(p.remove_vowels(string)))

        if choose == 9:
            print("Type of Value".center(40, "-"))
            value = 1
            print("Given value = {}".format(value))
            print("Result = {}".format(p.get_type(value)))

        if choose == 10:
            print("Sort Numbers in Descending Order".center(40, "-"))
            num = 123
            print("Given num = {}".format(num))
            print("Result = {}".format(p.sort_descending(num)))

        choose = int(input("\nEnter your chooses: "))
        print()
    print("EXIT PRACTICE 4".center(50, "="))



