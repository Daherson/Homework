from sys import argv

script_name, hours, rate_per_hour, the_prize = argv

hours = int(hours)
rate_per_hour = int(rate_per_hour)
the_prize = int(rate_per_hour)

def salary_counter():
    try:
        print("Your salary", hours * rate_per_hour + the_prize)
    except ValueError:
        print("Please, input 3 numbers!")
salary_counter()
