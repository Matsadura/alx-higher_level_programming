#!/usr/bin/python3
"""
    A module that contains the class Rectangle
"""


class Rectangle:
    """
        A class that defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
            A public instance method that returns
            the rectangle's area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            A public instance method that returns
            the rectangle's perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
            Prints the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
            The string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
            Destructor of the instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            A static method that returns the biggest
            rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
            A class method that returns a new Rectangle instance
            with width == height == size
        """
        return cls(cls.size, cls.size)
