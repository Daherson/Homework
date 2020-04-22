the_list = [5, 8, 10, 3, 4, 1, 9, 22, 21]
new_list = [the_list[el] for el in range(1, len(the_list)) if the_list[el] > the_list[el - 1]]
print(new_list)
