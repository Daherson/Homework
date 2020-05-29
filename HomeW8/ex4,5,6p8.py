# К сожалению не успеваю исправить некорректное добавление в (printer, scanner, xerox) в total.

class OE:
    def __init__(self, type, paper_index, size_index):

        self.type = type
        self.paper_index = paper_index
        self.size_index = size_index
        print(type, paper_index, size_index)
        printer = []
        scanner = []
        xerox = []
        print("Weclome to the office equipment, please, input type. Please input first variable only from list and check:\n"
              " printer, scanner, xerox.")
        my_dict_1 = {1: "Canon", 2: "Brother", 3: "Epson"}
        my_dict_2 = {1: "black", 2: "white", 3: "gray"}
        my_dict_3 = {1: "5", 2: "1", 3: "20"}
        total = []



        try:
            name = int(input(f"Chose the name. Input only numbers:{my_dict_1}"))
            color = int(input(f"Choose the color. Input only numbers: {my_dict_2}"))
            quantity = int(input(f"Choose the paper index. Input only numbers: {my_dict_3}"))
            if (0 > name >= 4) or (0 > color >= 4) or (0 > quantity >= 4):
                print("You have to input only numbers from the list!")
            else:
                if type == "printer" or "Printer":
                    printer.append(name)
                    printer.append(color)
                    printer.append(quantity)
                    print(f"The printer list: {printer}")
                    i = 0
                    for i in printer:

                        if printer[0] == 1:
                            total.append(my_dict_1.setdefault(1, "Canon"))
                        if printer[0] == 2:
                            total.append(my_dict_1.setdefault(2, "Brother"))
                        if printer[0] == 3:
                            total.append(my_dict_1.setdefault(3, "Epson"))
                        if printer[1] == 1:
                            total.append(my_dict_2.setdefault(1, "black"))
                        if printer[1] == 2 :
                            total.append(my_dict_2.setdefault(2, "white"))
                        if printer[1] == 3:
                            total.append(my_dict_3.setdefault(3, "gray"))
                        if printer[2] == 1:
                            total.append(my_dict_3.setdefault(1, "5"))
                        if printer[2] == 2:
                            total.append(my_dict_3.setdefault(2, "10"))
                        if printer[2] == 3:
                            total.append(my_dict_3.setdefault(3, "20"))
                    print(total)



                elif type == "scanner" or "scaner" or "Scanner":
                    scanner.append(name)
                    scanner.append(color)
                    scanner.append(quantity)
                    print(f"{printer}")
                    i = 0
                    for i in scanner:
                        if scanner[0] == 1:
                            total.append(my_dict_1.setdefault(1, "Canon"))
                        if scanner[0] == 2:
                            total.append(my_dict_1.setdefault(2, "Brother"))
                        if scanner[0] == 3:
                            total.append(my_dict_1.setdefault(3, "Epson"))
                        if scanner[1] == 1:
                            total.append(my_dict_2.setdefault(1, "black"))
                        if scanner[1] == 2:
                            total.append(my_dict_2.setdefault(2, "white"))
                        if scanner[1] == 3:
                            total.append(my_dict_3.setdefault(3, "gray"))
                        if scanner[2] == 1:
                            total.append(my_dict_3.setdefault(1, "5"))
                        if scanner[2] == 2:
                            total.append(my_dict_3.setdefault(2, "10"))
                        if scanner[2] == 3:
                            total.append(my_dict_3.setdefault(3, "20"))

                    print(total)
                elif type == "xerox" or "Xerox":
                    xerox.append(name)
                    xerox.append(color)
                    xerox.append(quantity)
                    print(f"The xerox list:{xerox}")
                    i = 0
                    for i in xerox:
                        if xerox[0] == 1:
                            total.append(my_dict_1.setdefault(1, "Canon"))
                        if xerox[0] == 2:
                            total.append(my_dict_1.setdefault(2, "Brother"))
                        if xerox[0] == 3:
                            total.append(my_dict_1.setdefault(3, "Epson"))
                        if xerox[1] == 1:
                            total.append(my_dict_2.setdefault(1, "black"))
                        if xerox[1] == 2:
                            total.append(my_dict_2.setdefault(2, "white"))
                        if xerox[1] == 3:
                            total.append(my_dict_3.setdefault(3, "gray"))
                        if xerox[2] == 1:
                            total.append(my_dict_3.setdefault(1, "5"))
                        if xerox[2] == 2:
                            total.append(my_dict_3.setdefault(2, "10"))
                        if xerox[2] == 3:
                            total.append(my_dict_3.setdefault(3, "20"))

                    print(total)
        except ValueError:
            print("You have to input only number!")
        except TypeError:
            print("You have to input only number")





class Printer(OE):
    @staticmethod
    def printics():
        user_answ = input("Input smth you want to print:")
        return f"Yor text: {user_answ}"
class Scanner(OE):
    @staticmethod
    def scan_pages():
        try:
            user_answ2 = int(input("How many pages do you want to scan?"))
            return  f"{user_answ2} pages is scanning."
        except ValueError:
            print("You have to input a number!")
class Xerox(OE):
    @staticmethod
    def docs():
        try:
            user_answ3 = int(input("How many documents do you want to get"))
            return f"You can get your {user_answ3} documents. "
        except ValueError:
            print("You have to input a numbers!")
oe = OE
print(oe("printer", 50, "s"))
print(oe("printer", 100, "s"))
print(oe("scanner", 200, "m"))
print(oe("xerox", 300, "l"))
printer = Printer
print(printer.printics())
scanner = Scanner
print(scanner.scan_pages())
xerox = Xerox
print(xerox.docs())
