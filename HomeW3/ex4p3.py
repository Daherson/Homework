#exponentiation
"""
def my_funct(x, y):
    return x**y
print(my_funct(2,-2))
"""

#--------------------------------------------Version2-()------------------------------------------------------------------

def my_funct (x, y):
    x = int(x)
    y = int(y)
    if y < 0:
        n = x
        i = 0
        while i > y+1:
            x = n*x
            i = i-1
    a = 1/x
    return(a)
print(my_funct(2, -4))

#-------------------------------------------Version3--------------------------------------------------------------------
"""def my_funct(x, y):
    return pow(x, y)
print(my_funct(2, -4))
"""









