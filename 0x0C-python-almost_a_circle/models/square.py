#!/usr/bin/python3
"""
    A module that contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}"

    def update(self, *args, **kwargs):
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for k, arg in enumerate(args):
                setattr(self, attrs[k], arg)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        attrs = {}
        names = ['x', 'y', 'id', 'size']
        values = [self.x, self.y, self.id, self.width]
        for name, value in zip(names, values):
            attrs[name] = value
        return attrs
