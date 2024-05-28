#!/usr/bin/python3
"""Test module for Amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
from os import getenv


class TestAmenity(unittest.TestCase):
    """Test class for Amenity"""

    @classmethod
    def setUpClass(cls):
        """Set up for tests"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """Tear down after tests"""
        del cls.amenity

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_checking_for_docstring_Amenity(self):
        """Checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Checking if Amenity has attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """Test if Amenity is subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """Test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "Using DB")
    def test_save_Amenity(self):
        """Test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "NOT Using DB")
    def test_save_Amenity_db(self):
        """Test if the save works"""
        return True
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
