#!/usr/bin/python3
"""
    A module for the class Base
"""


class Base:
    """
        The base class for all other classes
        It's purpose is to manage ID attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
