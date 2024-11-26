# Abstarction method doesn't have definition and overridden is compulsory in derive classes
# Abstract class are those class can't create object
# Meta class
# ABC abstract base class

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def formula(self):
        pass


class Rectangle(Shape):

    def formula(self, height, width):
        return height * width


class Circle(Shape):

    def formula(self, radius):
        return 3.14 * radius * radius


rect = Rectangle()
area = rect.formula(23, 45)
cir = Circle()
circleofarea = cir.formula(20)
print("Area of rectangle is ", area)
print("Area of circle is ", circleofarea)
