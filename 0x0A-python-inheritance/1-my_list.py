#!/usr/bin/python3
"""
    A module that contains the class MyList
"""


class MyList(list):
    """
        A class that inherist from list
    """
    def print_sorted(self):
        """
            A function that prints the list
            but sorted (ascending sort)
        """
        new_list = list(self)
        new_list.sort()
        print(new_list)
