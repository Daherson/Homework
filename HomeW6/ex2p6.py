class Road:
    _length = 3000
    _width = 25
    mass = 21
    thickness = 2


    def _init_(self, length, width):
        _length = length
        _width = width

    def counter(self):
        total = ((self._length * self._width) * self.mass * self.thickness) / 1000
        print(f"{total}")

the_road = Road()
print(the_road.counter())