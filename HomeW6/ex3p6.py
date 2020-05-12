class Worker:
    def _init_(self, name, surname, profit, position, bonus):
      self.name = name
      self.surname = surname
      self.position = position
      self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):
    def get_full_name(self, name, surname):
        name = name
        surname = surname
        full_name = (name + " " + surname)

    def get_total_income(self):
        total = sum(self._income.values())
        return(total)
mr_worker = Position("Vasya", "Poopkin", 31000, "office_plankton", 15000)
print(f"{mr_worker.get_full_name()} is {mr_worker.position} earn {mr_worker.get_total_income()}")