#!/usr/bin/python3
"""
    Tests for the Rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """
        A class for testing Rectangle
    """

    def setUp(self):
        """
        """
        Base._Base__nb_objects = 0

    def test_init(self):
        """ Testing class constructor """
        # Testing a rectangle (1, 1)
        r1 = Rectangle(1, 1)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(type(r1) is Rectangle)
        self.assertIsInstance(r1, Base)
        self.assertEqual(r1.id, 1)

        # Testing correct ID
        r1 = Rectangle(1, 1, 1, 1, 98)
        self.assertEqual(r1.id, 98)
        r2 = Rectangle(1, 2, 3, 4, None)
        self.assertEqual(r2.id, 2)

        # Testing wrong argument types
        with self.assertRaises(TypeError):
            r1 = Rectangle('str', 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 'str')
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 'str', 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 'str')

        # Testing wrong argument value
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 1, -1)

        # Testing a rectangle without arguments
        with self.assertRaises(TypeError):
            r1 = Rectangle()

        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_GetterSetter(self):
        """ Testing getters and setters """
        # Testing integrity of getters and setters
        tmp = Rectangle.__dict__.get('width')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is property)
        tmp = Rectangle.__dict__.get('height')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is property)
        tmp = Rectangle.__dict__.get('x')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is property)
        tmp = Rectangle.__dict__.get('y')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is property)

        # Testing getter attributes
        r1 = Rectangle(4, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(4, 3, 1)
        self.assertEqual(r2.x, 1)

        r3 = Rectangle(4, 3, 1, 3)
        self.assertEqual(r3.y, 3)

        # Testing setter
        r1.width = 99
        self.assertEqual(r1.width, 99)
        r1.height = 66
        self.assertEqual(r1.height, 66)
        r1.x = 96
        self.assertEqual(r1.x, 96)
        r1.y = 69
        self.assertEqual(r1.y, 69)

        # Testing wrong setter values and types
        with self.assertRaises(TypeError):
            r1.width = 'str'
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(TypeError):
            r1.height = 'str'
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(TypeError):
            r1.x = 'str'
        with self.assertRaises(ValueError):
            r1.x = -1
        with self.assertRaises(TypeError):
            r1.y = 'str'
        with self.assertRaises(ValueError):
            r1.y = -1

    def test_area(self):
        """ Testing the area method """
        tmp = Rectangle.__dict__.get('area')
        self.assertIsNotNone(tmp, True)

        # Testing the area of a rectangle (4, 3)
        r1 = Rectangle(4, 3)
        self.assertEqual(r1.area(), 12)

    def test_display(self):
        """ Testing the display method """
        tmp = Rectangle.__dict__.get('display')
        self.assertIsNotNone(tmp, True)

    def test_Str(self):
        """ Testing the __str__ method """
        tmp = Rectangle.__dict__.get('__str__')
        self.assertIsNotNone(tmp, True)

        r1 = Rectangle(1, 2)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/2")
        self.assertTrue(type(str(r1)) is str)

        r2 = Rectangle(1, 2, 4, 3, 98)
        self.assertEqual(str(r2), "[Rectangle] (98) 4/3 - 1/2")

    def test_Update(self):
        """ Testing the update method """
        tmp = Rectangle.__dict__.get('update')
        self.assertIsNotNone(tmp, True)

        r1 = Rectangle(1, 1, 1, 1)
        r1.update(3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (3) 1/1 - 4/5")

        r2 = Rectangle(1, 1, 1, 1)
        r2.update(id=2, width=10, height=5, x=3, y=4)
        self.assertEqual(str(r2), "[Rectangle] (2) 3/4 - 10/5")

        r2.update()
        self.assertEqual(str(r2), "[Rectangle] (2) 3/4 - 10/5")

    def test_ToDictionary(self):
        """ Testing to_dictionary method """
        tmp = Rectangle.__dict__.get('to_dictionary')
        self.assertIsNotNone(tmp, True)

        r1 = Rectangle(1, 2, 3, 4)
        r1_rep = r1.to_dictionary()
        self.assertTrue(type(r1_rep) is dict)
        output_rep = {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r1_rep, output_rep)
