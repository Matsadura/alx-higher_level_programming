#!/usr/bin/python3
"""
    A module that contains the class MyInt
"""


class MyInt(int):
    """
        A class that inherits from int
    """
    def __eq__(self, value):
        """
            A rebel EQ method
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
            A rebel NEQ method
        """
        return super().__eq__(value)
