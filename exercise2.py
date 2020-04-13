#TimeConverter
#Demonstrates sting format
sec = int(input("Whelcom to the TimeConverter! How many seconds would you like to convert? Please, don't write more 86399 seconds."))
hours = ((sec // 3600)) % 24
min = (sec // 60) % 60
sec_ = sec % 60

print('{0}:{1:=02}:{2:=02}'.format(hours, min, sec_))