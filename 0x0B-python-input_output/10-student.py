#!/usr/bin/python3
""" A module that contains the class Student """


class Student:
    """ A class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrives a dictionary representation of a Student """
        # if type(attrs) is list:
            # return {attr: getattr(self, attr, None) for attr in attrs}
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr, None) for attr in attrs}
