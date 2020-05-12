class Stationery:
    def _init_(self,title):
        self.title = title
    def draw(self):
        print("Draw is starting")
class Pen:
    def draw(self):
        print(f"{self.title}The Pen is starting draw")
class Pencil:
    def draw(self):
        print(f"{self.title} The Pencil is starting draw")
class Handle:

    def draw(self):
        print(f"{self.title} The Handle is starting draw")
st = Stationery()
st.draw()
pen = Pen("Corvina 51")
pen.draw()
pencil = Pencil(" Kohinor")
pencil.draw()
handle = Handle("Blue")
handle.draw()
