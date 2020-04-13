#Profile
#--------------------------------------------Version1-------------------------------------------------------------------
def profile(name, surname, year, city, email, number):
    print(name, surname, year, city, email, number)
profile("Masha", "Ivanova", "1910", "Moskow", "MI@mail.ru", "89102223322" )

#--------------------------------------------Version2-------------------------------------------------------------------
def profile(name, surname, year, city, email, number):
    print(name, surname, year, city, email, number)
name1 = input("Input your name")
surname1 = input("Input your surname")
year1 = input("Input year")
city1 = input("Input city")
email1 = input("Input email")
number1 = input("Input your phone number")
profile(name1, surname1, year1, city1, email1, number1)

