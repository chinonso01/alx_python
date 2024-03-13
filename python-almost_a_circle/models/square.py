# models/square.py
"""Defines the Square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class representing a square.

    Inherits from Rectangle class.

    Attributes:
        size (int): The size of the square (same as width and height of the rectangle).
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
