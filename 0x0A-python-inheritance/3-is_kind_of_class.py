#!/usr/bin/python3
"""
    A module that contains the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
        A function that checks if the object is an instance of,
        or an instance of a class that inherited from the specified class

        Args:
            obj: The object
            a_class: The specified class

        Return:
            True: If the object is an instance of, or of the class
            False: otherwise
    """
    return isinstance(obj, a_class)
