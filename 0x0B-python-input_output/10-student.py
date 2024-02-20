#!/usr/bin/python3
"""
    A module that contains the class Student
"""


class Student():
    """
        A class that defines a Student by:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        An attribute constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A method that retrives a dictionary repr of a Student
        """
        rep = vars(self)
        key_list = []
        if type(attrs) is list and [type(elm) is str for elm in attrs]:
            for k, v in rep.items():
                if k in attrs:
                    key_list.append((k, v))
            return dict(key_list)
        return rep
