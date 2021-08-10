class Practice5:

    @staticmethod
    def show_menu():
        print("PRACTICE 5".center(50, "="))
        print("1. ")
        print("0. Exit")
        print("".center(50, "="))

if __name__=="__main__":
    p = Practice5()
    p.show_menu()
    choose = int(input("Enter your chooses: "))
    print()
    while choose != 0:
        if choose == 1:
            pass

        if choose == 2:
            pass

        if choose == 3:
            pass

        if choose == 4:
            pass

        choose = int(input("\nEnter your chooses: "))
        print()
    print("EXIT PRACTICE 5".center(50, "="))
