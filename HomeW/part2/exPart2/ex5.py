 #--------------------------------------Версия после исправления---------------------------------------------------------
#the_list = [9, 8, 7, 6, 6, 6, 4, 3, 2, 2, 1]
#number = int(input("Write new rating item:"))
#i = 0
#for k in the_list:
#    if number <= k:
#        i+=1
#the_list.insert(i, number)
#print(the_list)
#--------------------------------------Версия изначальная(с ошибкой)----------------------------------------------------
the_list = [9, 8, 7, 6, 6, 6, 4, 3, 2, 2, 1]
number = int(input("Write new rating item"))
for i in the_list:
    if the_list[i+1] == i:
        the_list.insert(i+1, number)
    else:
        i += 1
print(the_list)