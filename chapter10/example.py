# Author: Jorge Rodriguez
# Date: April 12, 2017


class Robot:
    def __init__(self, make, model, year):
        self.__make = make

    def setMake(self, make):


        pass

x = Robot()
y = Robot()

x.name = "Marvin"
x.build_year = "1989"

y.name = "Caliban"
y.build_year = "1993"

print(x.name, x.build_year)
print(y.name, y.build_year)
