#storage
"""
print("Welcome to the Amagon storage! Hear you can check availability of the product in stock.")
goods = []
features ={"Name": "", "Cost": "", "Quantity": "", "unit": ""}
analytics ={"Name": [], "Cost": [], "Quantity": [], "unit": []}
number = 0
while True:
    if input("Press end to exit:").lower() == "end":
        break
    number += 1
    for i in features.keys():
        a = input(f"Press name {i}:")
        features[i] = int(a) if (i == "cost" or i == "quantity") else a
        analytics[i].append(features[i])
    goods.append((number, features))
    print(f"\n Product in stock: ")
    for key, value in analytics.items():
        print(f"{key[:20]>25}:{value}")
"""

#--------------------------------------------------Начальный вариант----------------------------------------------------
#storage
print("Welcome to the Amagon storage! Hear you can check availability of the product in stock.")
goods = []
features ={"Name": "", "Cost": "", "Quantity": "", "unit": ""}
analytics ={"Name": [], "Cost": [], "Quantity": [], "unit": []}
number = 0
while True:
    if input("Press end to exit:") == "end":
        break
    number += 1
    for i in features.keys():
        user_enter = input(f"Press name {i}:")
        analytics[i].append(features[i])
    goods.append((number, features))
    print(f"\n Product in stock: ")
    for key, value in analytics.items():
        print(f"{key[:20]}:{value}")

