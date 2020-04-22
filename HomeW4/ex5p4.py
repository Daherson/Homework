from functools import reduce

def my_funct(prev_el, el):
    return prev_el*el


the_list = [el for el in  range(100, 1001) if el % 2 == 0 ]
print(reduce(my_funct, the_list))