import time, itertools

class TrafficLight:
    __colors = ["red", "yellow", "green", "yellow"]

    def running(self):
        for i in itertools.cycle(self.__colors):
            if i == self.__colors[0]:
                print(f"\033[31m{i}")
                time.sleep(7)
            elif i == self.__colors[1]:
                print(f"\033[33m{i}")
                time.sleep(2)
            elif i == self.__colors[2]:
                print(f"\033[32m{i}")
                time.sleep(7)
            elif i == self.__colors[3]:
                print(f"\033[33m{i}")
                time.sleep(2)
the_class = TrafficLight()
the_class.running()
