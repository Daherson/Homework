class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return str((([str[i] for i in k]).split("\t") for i in self.matr).split("\n"))

    def __add__(self, other):
        return Matrix([sum([self.matr[i][k]], [self.other[i][k]]) for i in range(len(self.matr))]
                      for k in range(len(self.matr[0])))

try:
    stroki = int(input("Введите кол-во строк и столбцов матрицы"))
    stolbiki = stroki
    matrix1 = ([[i * k for k in range(stroki)] for i in range(stolbiki)])
    matrix2 = ([[i + k for k in range(stroki)] for i in range(stolbiki)])
   # print("\n", matrix1, "\n")
    #print("\n", matrix2, "\n")
except:
    ValueError
    print("Пожалуйста, введите 1 число.")