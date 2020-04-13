#witch's cauldron
#Demonstrates changing elements.
components = list(input("Welcom to the witch's cauldron! Write first letters of you favorite vegetables without space:"))
for i in range(1, len(components), 2):
    components[i-1], components[1] = components[1], components[i-1]
components = "".join(components)
print(f"Yor potion will be called {components}")
#--------------------------------------------Вариант 2------------------------------------------------------------------
#
#Sock's spreader
print("Welcom to the gentleman's club! If you want to be real gentelman, you have to learn how to spread your socks.")
rooms_dict ={1:"Living room", 2:"Bathroom", 3:"bedroom", 4:"cabinet", 5:"kithcen"}
print(f"Hear room's numbers.{rooms_dict}")
numbers = input("Write room's numbers. Where do you want put one of your socks?  (with space):").split()
i = 0
while i+1<len(numbers):
    if i % 2 == 0:
        numbers.insert(1, numbers.pop(i+1))
    i += 1

total = []
numbers = str(numbers)
i=0
while i != len(numbers):
    for key in rooms_dict:
        if numbers[i] == key:
            total.append(rooms_dict[key])
            i+=1
        else:
            i+=1

print(f" You have to start spread your socks in {total}.")
