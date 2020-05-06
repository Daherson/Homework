with open("new_file.txt", "w") as new_file:
    line = input("Enter some numbers ")
    new_file.writelines(line)
    number = line.split()
    print(f"{sum(map(int, number))}  is total")

