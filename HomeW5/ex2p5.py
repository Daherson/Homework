with open("filedz2.txt", "r") as file_1:
    i = 0
    for line in file_1:
        i += 1
        words = line.split(" ")
        print(line, "Слов в строке: ", len(words))
    print(f"Кол-во строк: {i}")
