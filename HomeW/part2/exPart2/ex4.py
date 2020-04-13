#----------------------------------Исправленное решение
#Welcom to the competitor's list
competitors=input("Enter the name of each member in your team in the list. Use Space").split()

for i, k in enumerate(competitors,1):
    print(f"{i}){k[:10]}")
#-------------------------------------------Изначальное решение( с ошибкой)-----------------------------------------
#Welcom to the competitor's list
competitors = input("Enter the name of each member in your team in the list. Use Space").split()
for i in range(len(competitors)):
    for j in competitors:
        i+=1
        print(f"{i} {j})")

