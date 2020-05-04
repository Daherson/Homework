from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)
generator = fibo_gen()
y = 0
for i in generator:
    if y < 23:
        print(i)
        y+=1
    else:
        break