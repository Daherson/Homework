class Car:
    def _init_(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"{self.name} is started"

    def stop(self):
        return f"{self.name} is stopped"

    def turn_left(self):
        return f"{self.name} is terned left"

    def turn_right(self):
        return f"{self.name} is turned right"

    def show_speed(self):
        return f"{self.name} has speed {self.speed}"


class Town_car(Car):
    def show_speed(self):
        if self.speed > 90:
            return f"{self.name} - speed higher than limit"
        else:
            return f"{self.name}'s speed is {self.speed}"

class Sport_car(Car):
    def logo(self):
        return f"This is the best sport car "

class Work_car(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{self.name} - speed higher than limit"
        else:
            return f"{self.name}'s speed is {self.speed}"

class Police_car(Car):
    def _init_(self,speed, color, name, is_police = True):
        super()._init_(speed, color, name, is_police)

work_car = Work_car(120, "Grey", "Fura")
work_car.go()
work_car.stop()
work_car.turn_left()
work_car.turn_right()
print(work_car.show_speed())

sport_car = Sport_car(150, "black", "sport")
print(sport_car)
print(sport_car.show_speed())
sport_car.go()
sport_car.turn_left()
sport_car.turn_right()
sport_car.stop()

police_car = Police_car(120, "white" , "The_Police")
print(police_car.show_speed())
police_car.go()
police_car.turn_right()
police_car.turn_left()
police_car.stop()

town_car = Town_car(49, "Subaru", "Green")
print(town_car.show_speed())
town_car.go()
town_car.turn_right()
town_car.turn_left()
town_car.stop()