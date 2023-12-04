#!/usr/bin/python3
""" A module that contains a class Rectangle """


class BaseGeometry:
    """ A class based on 6-base_geometry.py """

    def area(self):
        """
            A public instance method that raises
            an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A method that validates Value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
        A class Rectangle that inherits frm BaseGeometry
    """
    def __init__(self, width, height):
        """
            Instantiation with width and height
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
