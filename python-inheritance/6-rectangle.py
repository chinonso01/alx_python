#!/usr/bin/python3
"""Same object module"""


class BaseGeometry:
    """Base class for"""
    def area(self):
        """Returns the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Returns the integer"""
        if not isinstance(value, int):
            """Returns"""
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """Returns"""
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Base class for"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
