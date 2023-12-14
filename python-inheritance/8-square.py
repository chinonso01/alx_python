#!/usr/bin/python3
"""Same object module"""


class BaseGeometry:
    """Base class for"""
    def area(self):
        """Returns the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"Returns the integer"""
        if not isinstance(value, int):
            """Returns"""
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """Returns the"""
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Base class for"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns"""
        return self.__width * self.__height

    def __str__(self):
        """Returns"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Base class for square rectangles"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of"""
        return f"[Square] {self.__width}/{self.__height}"