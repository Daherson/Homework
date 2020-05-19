class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * '*'

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return self.quantity - other.quantity
        else:
            print("Number less then 0")

    def __mul__(self, other):
        return int(self.quantity * other.quantity)

    def __truediv__(self, other):
        return round(self.quantity // other.quantity)


    def make_order(self, stroki):
        stroki = " "
        for i in range(int(self.quantity / stroki)):
            stroki += f"{'*' * stroki} \n"
        stroki += f"{'*' * (self.quantity % stroki)}"
        return stroki

cell_1 = Cell(23)
cell_2 = Cell(12)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_2.make_order(9))
print(cell_1.make_order(15))
print(cell_1 / cell_2)