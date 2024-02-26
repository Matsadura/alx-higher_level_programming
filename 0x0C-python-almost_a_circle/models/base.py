#!/usr/bin/python3
"""
    A module for the class Base
"""
import json
import csv
import os
import turtle
import random


class Base:
    """
        The base class for all other classes
        It's purpose is to manage ID attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Class constructor

            Args:
                id (int, optional): The id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            A static method that serializes a json

            Args:
                list_dictionaries (list): A list of dictionaries

            Returns:
                The JSON string representattion of list_dictionaries
                or [] if list_dictionaries is None or Empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            A class method that writes the JSON string representation
            of list_obj to a file

            Args:
                list_objs (list): A list of instances who inherits of Base
        """
        list_to_print = []
        if list_objs:
            list_to_print = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_to_print))

    @staticmethod
    def from_json_string(json_string):
        """
            A static method that deserializes a JSON

            Args:
                json_string (str): The JSON string representation

            Returns:
                The list of the JSON string representation of json_string
                or [] if json_string is None or Empty
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            A class method that returns an instance will all attributes
            already set

            Args:
                **dictionary (dict): Keyworded argument list

            Returns:
                inst: The instance
        """
        if cls.__name__ == 'Rectangle':
            inst = cls(1, 1)
        elif cls.__name__ == 'Square':
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """
            A class method that returns a list of instances from a file

            Return:
                list_of_inst (list): The list of instances
        """
        file_name = cls.__name__ + '.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                dict_json = cls.from_json_string(f.read())
            list_of_inst = [cls.create(**inst) for inst in dict_json]
            return list_of_inst
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            A class method that serializes in CSV

            Args:
                list_objs (list): List of instances that inherits of Base
        """
        if list_objs:
            list_of_dict = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + '.csv', 'w') as f:
            if cls.__name__ == 'Rectangle':
                names = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                names = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=names)

            writer.writeheader()
            if list_objs:
                for line in list_of_dict:
                    writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        """
            A class method that deserializes in CSV

            Returns:
                list_of_inst (list): List of instances
        """

        with open(cls.__name__ + '.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            list_objs = [row for row in reader]
            json_str = cls.to_json_string(list_objs)
            dict_json = cls.from_json_string(json_str)
            new_dict = []
            for mini_dict in dict_json:
                for key, value in mini_dict.items():
                    mini_dict[key] = int(value)
                new_dict.append(mini_dict)
            list_of_inst = [cls.create(**inst) for inst in new_dict]
            return list_of_inst

    @staticmethod
    def draw(list_rectangle, list_square):
        """
            A static method that opens a window and draws
            all the Rectangles and Squares

            Args:
                list_rectangle (list): The list of rectangles to draw
                list_squares (list): The list of squares to draw
        """
        list_colors = ['red', 'blue', 'green', 'purple', 'brown', 'yellow',
                       'orange', 'cyan', 'violet']
        drawing = turtle.Turtle()
        for rect in list_rectangle:
            drawing.color(random.choice(list_colors))
            drawing.fillcolor(random.choice(list_colors))
            drawing.forward(rect.x)
            drawing.right(90)
            drawing.forward(rect.y)
            drawing.pd()
            drawing.begin_fill()
            drawing.fd(rect.width)
            drawing.right(90)
            drawing.fd(rect.height)
            drawing.right(90)
            drawing.fd(rect.width)
            drawing.right(90)
            drawing.fd(rect.height)
            drawing.end_fill()
            drawing.pu()

        for sqr in list_square:
            drawing.color(random.choice(list_colors))
            drawing.fillcolor(random.choice(list_colors))
            drawing.forward(sqr.x)
            drawing.right(90)
            drawing.forward(sqr.y)
            drawing.pd()
            drawing.begin_fill()
            drawing.fd(sqr.size)
            drawing.right(90)
            drawing.fd(sqr.size)
            drawing.right(90)
            drawing.fd(sqr.size)
            drawing.right(90)
            drawing.fd(sqr.size)
            drawing.end_fill()
            drawing.pu()

        turtle.done()
