#!/usr/bin/python3
"""
    A module that contains the Square class

    Methods:
        __init__
        size()
        to_dictionary()
        update()
"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """
        A class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Class constructor

            Args:
                size (int): The size of the square
                x (int, optional): The horizental position
                y (int, optional): The vertical position
                id (int, optional): The object's ID
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            A method that returns the string representation of a square

            Returns:
                The string representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}"

    @property
    def size(self):
        """
            A getter method for the size instance attribute

            Return:
                The size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            A setter method for the size instance attribute

            Args:
                value (int): The new size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            A method that assigns an argument to each attribute:

            Args:
                *args (tuple): Non-keyworded argumental list
                **kwargs (Dictionary): Keyworded argumental list
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for k, arg in enumerate(args):
                setattr(self, attrs[k], arg)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
            A method that returns the dictionary representation of a Rectangle

            Return:
                The dictionary representation
        """
        attrs = {}
        names = ['id', 'x', 'size', 'y']
        values = [self.id, self.x, self.size, self.y]
        for name, value in zip(names, values):
            attrs[name] = value
        return attrs
