#divider
#---------------------------------------Version 1-----------------------------------------------------------------------
def divider(val_1, val_2):
    if val_2 == 0:
        print("You can't use 0. Press another number")
    else:
        return val_1 / val_2
a = int(input("Press your number: "))
b = int(input("Press another number:"))
print(divider(a, b))
#---------------------------------------Version 2-----------------------------------------------------------------------
def divider(val_1, val_2):
    try:
        return val_1 / val_2
    except ZeroDivisionError:
        print("Oops! Your second number can't be 0!")


userNumber1 = int(input("Print your number:"))
userNumber2 = int(input("print another number:"))
print(divider(userNumber1, userNumber2))

