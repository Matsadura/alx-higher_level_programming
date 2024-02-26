#!/usr/bin/python3
"""
    Tests for the Square module
"""
import unittest
from models.base import Base
from models.square import Square


class test_Square(unittest.TestCase):
    """
        A class for testing Square
    """

    def setUp(self):
        """
        """
        Base._Base__nb_objects = 0

    def test_init(self):
        """ Testing class constructor """
        # Testing a Square (1)
        s1 = Square(1)
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(type(s1) is Square)
        self.assertIsInstance(s1, Base)
        self.assertEqual(s1.id, 1)

        # Testing correct ID
        s1 = Square(1, 1, 1, 98)
        self.assertEqual(s1.id, 98)
        s2 = Square(1, 2, 3, None)
        self.assertEqual(s2.id, 2)

        # Testing wrong argument types
        with self.assertRaises(TypeError):
            s1 = Square('str', 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, 'str')
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 'str', 1)
        with self.assertRaises(TypeError):
            s1 = Square('str')

        # Testing wrong argument value
        with self.assertRaises(ValueError):
            s1 = Square(0)
        with self.assertRaises(ValueError):
            s1 = Square(1, -1, 1)
        with self.assertRaises(ValueError):
            s1 = Square(1, 1, -1)

        # Testing a Square without arguments
        with self.assertRaises(TypeError):
            s1 = Square()

        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)

    def test_GetterSetter(self):
        """ Testing getters and setters """
        # Testing integrity of getters and setters
        tmp = Square.__dict__.get('size')
        self.assertIsNotNone(tmp, True)
        self.assertTrue(type(tmp) is property)

        # Testing getter attributes
        s1 = Square(4)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(4, 3)
        self.assertEqual(s2.x, 3)

        r3 = Square(4, 3, 1)
        self.assertEqual(r3.y, 1)

        # Testing setter
        s1.size = 99
        self.assertEqual(s1.size, 99)
        s1.x = 96
        self.assertEqual(s1.x, 96)
        s1.y = 69
        self.assertEqual(s1.y, 69)

        # Testing wrong setter values and types
        with self.assertRaises(TypeError):
            s1.size = 'str'
        with self.assertRaises(ValueError):
            s1.size = 0
        with self.assertRaises(TypeError):
            s1.x = 'str'
        with self.assertRaises(ValueError):
            s1.x = -1
        with self.assertRaises(TypeError):
            s1.y = 'str'
        with self.assertRaises(ValueError):
            s1.y = -1

    def test_Str(self):
        """ Testing the __str__ method """
        tmp = Square.__dict__.get('__str__')
        self.assertIsNotNone(tmp, True)

        s1 = Square(1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")
        self.assertTrue(type(str(s1)) is str)

        s2 = Square(1, 2, 4, 98)
        self.assertEqual(str(s2), "[Square] (98) 2/4 - 1")

    def test_Update(self):
        """ Testing the update method """
        tmp = Square.__dict__.get('update')
        self.assertIsNotNone(tmp, True)

        s1 = Square(1, 1, 1)
        s1.update(3, 4, 5)
        self.assertEqual(str(s1), "[Square] (3) 5/1 - 4")

        s2 = Square(1, 1, 1, 1)
        s2.update(id=2, size=10, x=3, y=4)
        self.assertEqual(str(s2), "[Square] (2) 3/4 - 10")

        s2.update()
        self.assertEqual(str(s2), "[Square] (2) 3/4 - 10")

    def test_ToDictionary(self):
        """ Testing to_dictionary method """
        tmp = Square.__dict__.get('to_dictionary')
        self.assertIsNotNone(tmp, True)

        s1 = Square(1, 2, 3)
        s1_rep = s1.to_dictionary()
        self.assertTrue(type(s1_rep) is dict)
        output_rep = {'id': 1, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s1_rep, output_rep)
