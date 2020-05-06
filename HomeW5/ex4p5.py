dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("дз4.txt", "a") as rus:
    with open("rus_file.txt") as my_f:
        line = my_f.read().split("\n")
        for i in line:
            i = i.split(" - ")
            rus.writelines(dict[i[0]] + " - " + i[1] + "\n")