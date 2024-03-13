# models/base.py
"""Defines the Base class."""

class Base:
    """
    Base class for managing identifiers in the project.
    
    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects.
        id (int): Public instance attribute representing the identifier of the instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The identifier for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
