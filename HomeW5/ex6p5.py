
total = {}
with open("дз6.txt", "r") as file_1:
    for line in file_1:
        all_lessons = []
        objects = ([el for el in line.split(" ")])
        for el in objects:
            all_lessons.append("".join(k for k in list(el) if k.isdigit()))
        total[line.split(":")[0]] = sum([int(k)] for k in all_lessons if k.isdigit())
print(total)


