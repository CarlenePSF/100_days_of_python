"""
4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and
perimeter. Implement subclasses for different shapes like circle, triangle, and square.

https://brasilescola.uol.com.br/matematica/poligonos.htm
"""
from math import pi

class Shape:
    def find_area(self):
        pass
    def find_perimeter(self):
        pass


class RegularPoligon(Shape):
    def __init__(self, number_of_edges, length_of_edges):
        self.number_of_edges = number_of_edges
        self.length_of_edges = length_of_edges

    def find_internal_angle(self):
        sum_of_angles =  (self.number_of_edges - 2) * 180
        return sum_of_angles / self.number_of_edges

    def find_perimeter(self):
        return self.number_of_edges * self.length_of_edges

    def find_external_angles(self):
        return 360/self.number_of_edges

    def number_of_diagonals(self):
        return self.number_of_edges * (self.number_of_edges - 3)/2



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return pi * self.radius * self.radius

    def find_perimeter(self):
        return 2 * pi * self.radius


class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        self.number_of_edges = 3
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = base

    def find_area(self):
        return (self.base * self.height)/2

    def find_perimeter(self):
        return self.side1 + self.side2 + self.side3



square = RegularPoligon(4, 2)
print(square.find_internal_angle())
print(square.find_perimeter())
print(square.find_external_angles())
print(square.number_of_diagonals())

hexagonon = RegularPoligon(6, 2)
print(hexagonon.find_internal_angle())
print(hexagonon.find_perimeter())
print(hexagonon.find_external_angles())
print(hexagonon.number_of_diagonals())

triangle = Triangle(4, 2, 6, 8)
print(triangle.find_area())
print(triangle.find_perimeter())

