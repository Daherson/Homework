#The seasons
month = int(input("Enter your favorite month. Use 1-12 numbers."))
month_dict = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                6:"June", 7:"July", 8:"August",9:"September", 10:"October", 11:"November", 12:"December"}
month_list=["january", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
description=["It's time when  weatheris snowy", "It's time when birds are singing",
                  "It's time when sun is shining", "It's time when trees are color"]
desk=""
for key in month_dict:
    if month == 1 or 2 or 12:
        desk=description[0]
    elif month == 3 or 4 or 5:
        desk=description[1]
    elif month == 6 or 7 or 8:
        desk=description[2]
    elif month == 9 or 10 or 11:
        desk=description[3]
    if key == month:
       print(f"{month} month is {month_dict[key]} {desk}")
       print(f"{month} month is {month_list[month-1]} {desk}")

print("Month isn't correct.")
