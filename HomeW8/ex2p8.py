class OwnError(Exception):
    def __init__(self, div, den):
        self.div = div
        self.den = den
    @staticmethod
    def division_by_zero(div,den):
        try:
            return (div / den)
        except:
            if den == 0:
                return ("Devision by zero isn't possible!")
exeption = OwnError
print(exeption.division_by_zero(100, 0))
