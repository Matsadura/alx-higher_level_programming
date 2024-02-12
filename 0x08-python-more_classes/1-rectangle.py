#!/usr/bin/python3
"""
    A module that contains the class Rectangle
"""


class Rectangle:
    """
        A class that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """
            An instance constructor for the class Rectangle

            Args:
                width (int, optional): the width of the rectangle
                height (int, optional): the height of the rectanlge

            Raises:
                TypeError: if width or height are not an integer
                ValueError: if width or height are < 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
            A property getter of height
        """
        return self.__height

    @property
    def width(self):
        """
            A property getter of width
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
            A property setter of height:

            Args:
                value (int): the new height value to set

            Raises:
                TypeError: if height is not an int
                ValueError: if height < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
            A property setter of height

            Args:
                value (int): the new width value to set

            Raises:
                TypeError: if width is not an int
                ValueError: if width < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
