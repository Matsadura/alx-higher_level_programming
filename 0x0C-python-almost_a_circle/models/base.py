#!/usr/bin/python3
"""
    A module for the class Base
"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        list_to_print = []
        if list_objs:
            list_to_print = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_to_print))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            inst = cls(1, 1)
        elif cls.__name__ == 'Square':
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + '.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                dict_json = cls.from_json_string(f.read())
            list_of_inst = [cls.create(**inst) for inst in dict_json]
            return list_of_inst
        return []
