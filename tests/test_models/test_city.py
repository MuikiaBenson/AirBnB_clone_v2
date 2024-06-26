#!/usr/bin/python3
"""Test module for City"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8
from os import getenv


class TestCity(unittest.TestCase):
    """Test class for City"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""

        from models.state import State
        cls.state = State()
        cls.state.name = "California"
        cls.state.save()
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = cls.state.id

    @classmethod
    def tearDownClass(cls):
        """Tear down after the test"""
        from models import storage

        storage.delete(cls.city)
        storage.delete(cls.state)
        del cls.city
        del cls.state

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_checking_for_docstring_City(self):
        """Checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Checking if City has attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Test if City is subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """Test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """Test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
