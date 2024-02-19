#!/usr/bin/python3
"""
    A module that contains a class Rectangle
"""

class BaseGeometry:
    """
        A class

        Methods:
            Area: Not yet implemented
    """
    def area(self):
        """
            A method that has not been implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A method that validates value

            Args:
                name: A string
                value: The value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
        A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
            Constructor of instances

            width (int): The width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        Rectangle.integer_validator(self, "width", width)
        self.__height = height
        Rectangle.integer_validator(self, "height", height)
