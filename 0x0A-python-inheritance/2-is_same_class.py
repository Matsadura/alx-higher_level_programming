#!/usr/bin/python3
"""
    A module that contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """
        A function that checks if the object is an instance
        of the specified class

        Args:
            obj: The object to check
            a_class: The specified class

        Returns:
            True: if the object is exactly an instance of the class
            False: if it's not
    """
    if type(obj) is a_class:
        return True
    return False
