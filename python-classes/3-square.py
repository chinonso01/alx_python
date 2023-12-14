#!/usr/bin/python3
"""A square module"""


class Square:
    """A square module"""
    def __init__(self, size=0):
        """Construct"""
        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            """Set the size of the square"""
            raise TypeError("size must be an integer")

        if value < 0:
            """Set the size of the square"""
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2