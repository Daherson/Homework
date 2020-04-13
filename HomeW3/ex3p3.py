#Вопрос: как сделать аргументы целочисленными? Как корректно применить int к аргументам функции в данном варианте?
def my_func(val_1, val_2, val_3):
    if (val_1 > val_2 < val_3):
        print(sum(val_1, val_3))
    elif(val_2 > val_1 < val_3):
        print(sum(val_2, val_3))
    elif(val_1 > val_3 < val_2):
        print(sum(val_1, val_2))
    else:
        print("Numbers don't have to be the same!")

my_func(2, 3, 4)


