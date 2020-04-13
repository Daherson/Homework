revenue = int(input("Hello! Write your company's revenue "))
costs = int(input("Write your company's costs."))
if revenue>costs:
    print("Great job! Revenue is bigger than costs!")
    profit = revenue/costs
    print(f"Your profitability is {profit}. ")
    staff = int(input("How many staff in your company?"))
    personal_rev =revenue/staff
    print(f"revenue for person is {personal_rev}.")

elif revenue<costs
    print("Unfortunetly, buzies in your company isn't great...")
