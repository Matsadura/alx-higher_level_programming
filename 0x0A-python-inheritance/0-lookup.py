#!/usr/bin/python3
"""
    A module that contains the function lookup
"""


def lookup(obj):
    """
        A function that returns the list of available attributes
        and methods of an object

        Args:
            obj: The object

        Returns:
            meteor (list): The list of attributes and methodes
    """
    meteor = dir(obj)
    return meteor
