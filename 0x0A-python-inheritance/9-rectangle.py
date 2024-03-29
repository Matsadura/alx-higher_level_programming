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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            A method that that calculates the area of the rectangle

            Return:
                The area
        """
        return self.__width * self.__height

    def __str__(self):
        """
            The string representation of Rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
