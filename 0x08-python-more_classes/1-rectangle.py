#!/usr/bin/python3
""" Module """


class Rectangle:
    """
        A class that defines a rectangle
        based on 0-rectangle.py
    """

    def __init__(self, width=0, height=0):
        """
            Instantiation with optional width
            and height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError("Weight must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def width(self):
        """
            getter of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter of width
        """
        if not isinstance(value, int):
            raise TypeError("Weight must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            getter of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
