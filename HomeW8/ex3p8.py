"""
class ExeptElements:
    @staticmethod
    def exeptic():
        new_list = []
        while True:
            user_answ = input("Input a number: ")
            try:
                if user_answ == "stop":
                    print(new_list)
                    break
                if user_answ is int or user_answ is float:
                    new_list.append(user_answ)
            except user_answ is not int and user_answ is not float:
                print("You have to input only number")
ex = ExeptElements
print(ex.exeptic())
не работает("""


class ExeptElements:
    @staticmethod
    def exeptic():
        new_list = []
        while True:
            user_answ = int(input("Input a number: "))
            stop = str(input("Do you want to continue? (y/n"))
            try:
                if stop == "n":
                    print(new_list)
                    break
                else:
                    new_list.append(user_answ)
                    print(new_list)
            except TypeError:
                    print("You have to input only number")
            except ValueError:
                print("You have to input only number")



ex = ExeptElements
print(ex.exeptic())