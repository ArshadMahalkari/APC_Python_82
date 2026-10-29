"""Simple example of abstraction using an abstract Shape class."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class that defines a common shape interface."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


def display_shape_details(shape):
    """Use the abstract interface without knowing the concrete shape."""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


def main():
    shapes = [Rectangle(10, 5), Circle(3)]
    for shape in shapes:
        print(f"\n{type(shape).__name__}")
        display_shape_details(shape)


if __name__ == "__main__":
    main()
