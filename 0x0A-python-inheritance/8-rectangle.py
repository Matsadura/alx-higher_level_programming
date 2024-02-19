#!/usr/bin/python3
"""
    A module that contains a class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
