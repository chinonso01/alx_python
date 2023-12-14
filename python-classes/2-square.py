#!/usr/bin/python3
"""A square module"""


class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """Constructor"""
        if not isinstance(size, int):
            """Check that size is an integer"""
            raise TypeError("size must be an integer")

        if size < 0:
            """Check that size is non-negative"""
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Area of the square"""
        return self.__size ** 2
