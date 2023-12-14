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
            """"return"""
            raise ValueError(f"{name} must be greater than 0")