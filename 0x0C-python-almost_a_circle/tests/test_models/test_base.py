#!/usr/bin/python3
"""
    A module that contains tests for the Base module
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class tests_base(unittest.TestCase):
    """
        A class for testing the Base module
    """
    def setUp(self):
        """ Reset __nb_objects to 0 in every test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Removes existing files after each test """
        files = ['Rectangle.json', 'Square.json', 'Rectangle.csv',
                 'Square.csv']
        for f in files:
            if os.path.exists(f):
                os.remove(f)

    # Testing ID
    def test_id1(self):
        """ Testing the __nb_objects instance & ID"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b2.id, Base._Base__nb_objects)
        b3 = Base(98)
        self.assertEqual(b3.id, 98)

    def test_id2(self):
        """ Testing ID is not None """
        b1 = Base()
        self.assertIsNotNone(b1.id, True)

    def test_type(self):
        """ Testing the type of the instance """
        b5 = Base()
        self.assertTrue(type(b5) is Base)
        self.assertIsInstance(b5, Base)

    def test_TojsonString(self):
        """ Testing the to_json_string method """
        # Testing the integritiy of to_json_string method
        var = Base.__dict__.get('to_json_string')
        self.assertIsNotNone(var, True)
        self.assertTrue(type(var) is staticmethod)

        # Testing an instance
        obj = Base()
        tmp_list = [{'key1': 1, 'key2': 2}]
        json_dict = obj.to_json_string(tmp_list)
        self.assertTrue(type(json_dict) is str)
        self.assertEqual(json_dict, '[{"key1": 1, "key2": 2}]')

        # Testing list is None
        tmp_list = None
        json_dict = obj.to_json_string(tmp_list)
        self.assertEqual(json_dict, "[]")

        # Testing an empty list
        tmp_list = []
        json_dict = obj.to_json_string(tmp_list)
        self.assertEqual(json_dict, "[]")

        dict_1 = {"x": 0, "y": 5, "width": 2, "height": 4}
        dict_2 = {"x": 1, "y": 4, "width": 3, "height": 5}
        list_1 = Base.to_json_string([dict_1, dict_2])
        str_list_1 = "[{\"x\": 0, \"y\": 5, \"width\": 2, \"height\": 4}, \
{\"x\": 1, \"y\": 4, \"width\": 3, \"height\": 5}]"
        self.assertEqual(list_1, str_list_1)

    def test_SaveToFile(self):
        """ Testing the save_to_file method """
        var = Base.__dict__.get('save_to_file')
        self.assertIsNotNone(var, True)
        self.assertTrue(type(var) is classmethod)

        # Testing a rectangle
        rec = Rectangle(1, 1, 1, 1)
        rec_str = "[{\"x\": 1, \"y\": 1, \"id\": 1, \"height\": 1, \
\"width\": 1}]"
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, rec_str)

        # Testing a square
        sqr = Square(1, 1)
        sqr_str = "[{\"id\": 2, \"x\": 1, \"size\": 1, \"y\": 0}]"
        Square.save_to_file([sqr])
        with open("Square.json", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, sqr_str)

        # Testing an empty list
        Square.save_to_file([])
        with open("Square.json", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, "[]")

        # Testing list is None
        Square.save_to_file(None)
        with open("Square.json", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, "[]")

        # Testing missing 1 argument
        with self.assertRaises(TypeError):
            Square.save_to_file()

        # Testing more argumentes provided
        with self.assertRaises(TypeError):
            Square.save_to_file([sqr], [sqr])

    def test_FromJsonString(self):
        """ Testing from_json_string method """
        # Testing the integrity of from_json_string
        tmp = Base.__dict__.get('from_json_string')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is staticmethod)

        # Testing empty list
        input_list = []
        json_list = Rectangle.to_json_string(input_list)
        output = Rectangle.from_json_string(json_list)
        self.assertEqual(output, [])

        # Testing lsit is None
        input_list = None
        json_list = Rectangle.to_json_string(input_list)
        output = Rectangle.from_json_string(json_list)
        self.assertEqual(output, [])

        # Testing list contains 2 dictionaries
        input_list = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list = Rectangle.to_json_string(input_list)
        output = Rectangle.from_json_string(json_list)
        cmp_output = [{'height': 4, 'id': 89, 'width': 10},
                      {'height': 7, 'id': 7, 'width': 1}]
        self.assertTrue(type(cmp_output) is list)
        self.assertEqual(output, cmp_output)

    def test_Create(self):
        """ Testing create method """
        # Testing the integrity of create method
        tmp = Base.__dict__.get('create')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is classmethod)

        # Testing creating a new rectangle instance
        r1 = Rectangle(1, 2, 3)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertTrue(type(r2) is Rectangle)

        # Testing creating a new square instance
        s1 = Square(1, 2, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertTrue(type(s2) is Square)

    def test_LoadFromFile(self):
        """ Testing load_from_file method """
        # Testing integrity of load_from_file
        tmp = Base.__dict__.get('load_from_file')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is classmethod)

        # Testing file doesn't exist
        rec = Rectangle.load_from_file()
        self.assertEqual(rec, [])

        # Testing loading rectangle instance
        r1 = Rectangle(1, 2, 1, 1)
        Rectangle.save_to_file([r1])
        rec = Rectangle.load_from_file()
        self.assertEqual(str(rec[0]), "[Rectangle] (1) 1/1 - 1/2")

        # Testing loading square instance
        s1 = Square(1)
        Square.save_to_file([s1])
        sqr = Square.load_from_file()
        self.assertEqual(str(sqr[0]), "[Square] (3) 0/0 - 1")

    def test_SaveToFileCsv(self):
        """ Testing save_to_file_csv method """
        # Testing integrity of save_to_file_csv
        tmp = Base.__dict__.get('save_to_file_csv')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is classmethod)

        # Testing a rectangle
        rec = Rectangle(1, 1, 1, 1)
        rec_str = 'id,width,height,x,y\n1,1,1,1,1\n'
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, rec_str)

        # Testing a square
        sqr = Square(1, 1)
        sqr_str = 'id,size,x,y\n2,1,1,0\n'
        Square.save_to_file_csv([sqr])
        with open("Square.csv", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, sqr_str)

        # Testing No Argument Passed
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

        # Testing empty list
        Square.save_to_file_csv([])
        with open("Square.csv", 'r', encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(string, 'id,size,x,y\n')

    def test_LoadFromFileCsv(self):
        """ Testing load_from_file_csv """
        # Testing integrity of load_from_file_csv
        tmp = Base.__dict__.get('load_from_file_csv')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is classmethod)

        # Testing file doesn't exist
        with self.assertRaises(FileNotFoundError):
            rec = Rectangle.load_from_file_csv()

        # Testing loading rectangle instance
        r1 = Rectangle(1, 2, 1, 1)
        Rectangle.save_to_file_csv([r1])
        rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec[0]), "[Rectangle] (1) 1/1 - 1/2")

        # Testing loading square instance
        s1 = Square(1)
        Square.save_to_file_csv([s1])
        sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqr[0]), "[Square] (3) 0/0 - 1")

    def test_Draw(self):
        """ Testing the draw method """
        # Testing integrity of draw
        tmp = Base.__dict__.get('draw')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is staticmethod)

        # Testing 1 missing argument
        with self.assertRaises(TypeError):
            Base.draw([])

        # Testing 2 missing arguments
        with self.assertRaises(TypeError):
            Base.draw()

        # Testing excesive arguments
        with self.assertRaises(TypeError):
            Base.draw([], [], [])
