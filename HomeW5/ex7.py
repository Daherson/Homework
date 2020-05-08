import json
income = {}
pr = {}
prof = 0
averege_inc = 0
i = 0
with open("дз7txt.txt", "r") as my_file:
    for line in my_file:
        name, firm, earning, damage = line.split()
        income[name] = int(earning) - int(damage)
        if income.setdefault(name) >= 0:
            prof = prof + income.setdefault(name)
            i += 1
    if i != 0:
        averege_inc = prof / i
        print(f"Средняя прибыль {averege_inc:.2f}")
    else:
        print(f"нет прибыли")
    pr = {"средняя прибыль": round(averege_inc)}
    income.update(pr)
    print(f"Прибыль каждой из компаний", income)

with open("дз71.json", "w") as js_doc:
    json.dump(income, js_doc)

    js_str = json.dumps(income)
    print("Новый файл  json", js_str)