the_list = [1, 2, 2, 3, 3, 5, 4, 6, 6]
new_list = [el for el in the_list if the_list.count(el) < 2]
print(new_list)