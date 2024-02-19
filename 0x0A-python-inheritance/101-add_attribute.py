#!/usr/bin/python3
"""
    A module that contains a the add_attribute function
"""


def add_attribute(obj, attribute, value):
    """
        A function that adds a new attribute to an object

        Args:
            obj: The object
            attribute: The attribute's name
            value: The attribute's value

        Raises:
            TypeError: if the object can't have a new attribute
    """
    if "__dict__" in dir(obj):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
