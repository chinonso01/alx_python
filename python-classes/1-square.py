#!/usr/bin/python3
"""A square module"""


class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """Validate that size is an integer"""
        if not isinstance(size, int):
            """Check that size is an integer"""
            raise TypeError("size must be an integer")

        if size < 0:
            """Check that size is non-negative"""
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Return"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"Square with size {self.__size}"
