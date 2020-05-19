from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def formula(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def formula(self):
        return round(self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def formula(self):
        return round(2 * self.height + 0.3)


coat = Coat(42)
suit = Suit(44)
print(coat.formula)
print(suit.formula)








