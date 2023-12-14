#!/usr/bin/python3
"""Same object module"""


def inherits_from(obj, a_class):
    """Inherits from"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
