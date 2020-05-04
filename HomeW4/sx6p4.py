"""from itertools import count
def counting(first_number,end):
    for el in count(first_number):
        if el > end:
            break
        else:
            print(el)
print(counting(3, 6))
"""

from itertools import cycle

the_list = list(input("Enter some numbers without space: "))
cycling = cycle(the_list)
i = 0
while i <= 25:
    print(next(cycling))
    i = i+1