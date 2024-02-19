#!/usr/bin/python3
"""
    A module that contains the function inherits_from
"""


def inherits_from(obj, a_class):
    """
        A function that checks of the object is an instance of a class
        that inherited (directly or indirectly) from the specified class

        Args:
            obj: The object
            a_class: The specified class

        Returns:
            True if yes
            False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
