#!/usr/bin/python3
from . import rectangle
"""Defines the Square class"""


class Square(rectangle.Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square object"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets or sets the size of the Square object"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square object

        Order: id, size, x, y
        """

        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the
        Square object"""

        rdict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y}
        return rdict
