#!/usr/bin/python3
"""
    A module that contains the class Rectangle

    Methods:
        __init__
        width()
        height()
        x()
        y()
        area()
        display()
        __str__
        update()
        to_dictionary()

"""
from models.base import Base


class Rectangle(Base):
    """
        A class that inherits from the class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Class constructor

            Args:
                width (int): The width of the Rectangle
                height (int): The height of the Rectangle
                x (int, optional): The horizental postion
                y (int, optional): The verstical position
                id (int, optional): The id of the object

            Raises:
                TypeError: if width, height, x or y isn't an integer
                ValueError: if width, height < 0 or x, y <= 0
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
        """
            A getter for the width instance attribute

            Returns:
                The width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            A setter method for the width instance attribute

            Args:
                width: The new width value

            Raises:
                TypeError: if width is not an integer
                ValueError: if width < 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
            A getter method the height instance attribute

            Return:
                The height value
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            A setter method for the height instance attribute

            Args:
                height: The new height value

            Raises:
                TypeError: if height is not an integer
                ValueError: if height < 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
            A getter method the x instance attribute

            Return:
                The x value
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            A setter method for the x instance attribute:

            Args:
                x: The new value
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
            A getter method for the y instance attribute

            Returns:
                The y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
            A method that calculate the area of the Rectangle

            Returns:
                The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            A method that displays the Rectangle using #
        """
        print('\n' * self.__y + (
              ' ' * self.__x + '#' * self.__width + '\n') * self.__height,
              end="")

    def __str__(self):
        """
            A method that returns the string representation of a Rectangle

            Returns:
                The string representation
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
            A method that assigns an argument to each attribute:

            Args:
                *args (tuple): Non-keyworded argumental list
                **kwargs (Dictionary): Keyworded argumental list
        """
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
        """
            A method that returns the dictionary representation of a Rectangle

            Return:
                The dictionary representation
        """
        attrs = {}
        names = ['x', 'y', 'id', 'height', 'width']
        values = [self.x, self.y, self.id, self.height, self.width]
        for name, value in zip(names, values):
            attrs[name] = value
        return attrs
