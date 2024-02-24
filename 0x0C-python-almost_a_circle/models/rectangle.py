#!/usr/bin/python3
"""
    A module that contains the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        A class that inherits from the class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Class constructor
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        print('\n' * self.__y + (
              ' ' * self.__x + '#' * self.__width + '\n') * self.__height,
              end="")

    def __str__(self):

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.__width = args[1] if len(args) > 1 else self.__width
            self.__height = args[2] if len(args) > 2 else self.__height
            self.__x = args[3] if len(args) > 3 else self.__x
            self.__y = args[4] if len(args) > 4 else self.__y
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        attrs = {}
        names = ['x', 'y', 'id', 'height', 'width']
        values = [self.x, self.y, self.id, self.height, self.width]
        for name, value in zip(names, values):
            attrs[name] = value
        return attrs
