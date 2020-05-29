class Data:
    """
     def __init__(self, date):
        self.date = date

    @classmethod
    def integer(cls,):
        date = str(input("Input date with space: "))
        new_date = []

        for i in date.split("-"):
            i = int(i)
            new_date.append([i])
        return new_date
    """
    def __init__(self, day_month_year):
        self.day_moth_year = str(day_month_year)

    @classmethod
    def integer(cls, day_month_year):
        date = []
        for i in day_month_year.split("-"):
            i = int(i)
            date.append([i])
        return date
    @staticmethod
    def validation(day, month, year):
        if (1 <= day <= 31) and (1 <= month <= 12) and (1 <= year <= 2020):
            return "Your date is right."
        else:
            return "Your date isn't correct!"

a = Data
print(a.integer("02-03-2000"))
print(a.validation(2, 3, 2000))
