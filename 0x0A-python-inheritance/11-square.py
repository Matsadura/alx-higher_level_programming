#!/usr/bin/python3
"""
    A module that contains the class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A class that inherits from Rectangle
    """
    def __init__(self, size):
        """
            Instances constructor

            Args:
                size: The size of the square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            A method that calculates the area of the square

            Returns:
                The area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
            The string representation of Square as Rectangle
        """
        return f"[Square] {self.__size}/{self.__size}"
