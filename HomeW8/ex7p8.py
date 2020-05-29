class ComplexNum:
    def __init__(self, a, b, a1, b1):
        self.a = a
        self.b = b
        self.z = ""
        self.a1 = a1
        self.b1 = b1

    def __add__(self, a, b, a1, b1):
        return f"The sum is: z1+z2 = (a1 +a2) +(b1 +b2)i :\n z1 +z2 = {(a + a1)}+{(b+b1)} * i"

    def __mul__(self, a, b, a1, b1):
        return  f"Multiplication is: \n z = z1* z2 = {((a * a1) - (b * b1))}+{((a * b1)+(b * a1))} * i"
comlexnum = ComplexNum
print(comlexnum.__add__(2, 4, 5, 6, 8))
print(comlexnum.__mul__(2, 3, 5, 7, 8))