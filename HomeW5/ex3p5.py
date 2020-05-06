
def salary_counter(the_file):
    with open(the_file, 'r', encoding='utf-8') as file:
        staff = {}
        sum_sal = []
        for line in file:
            key, value = line.split()
            staff[key] = value
            if int(value) < 20000:
                print(f"{key} has salary less than 20000 ")
            sum_sal.append(value)
        new_list = []
        for i in sum_sal:
            i = int(i)
            new_list.append(i)
        print(f"{sum(new_list) / len(new_list)} is middle salary")
salary_counter("дз3.txt")
