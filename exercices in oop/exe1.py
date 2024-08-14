"""
1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


circle_1 = Circle(1)
circle_1_area = circle_1.area()
circle_1_perimeter = circle_1.perimeter()

print(circle_1_area)
print(circle_1_perimeter)