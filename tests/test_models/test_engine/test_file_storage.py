#!/usr/bin/python3
"""Test module for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for FileStorage'''

    @classmethod
    def setUpClass(cls):
        """Set up for tests"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """Tear down after tests"""
        del cls.user

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Test PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_all(self):
        """Test if all works in FileStorage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """Test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        Test reload
        """
        self.storage.save()
        root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_all_method(self):
        '''Test all method'''
        fs = FileStorage()
        new_state = State()
        fs.new(new_state)
        fs.save()
        self.assertIn(new_state, fs.all(State).values())

    def test_all_no_specification(self):
        '''Test all when no class is passed'''
        return True
        fs = FileStorage()
        new_state1 = State()
        fs.new(new_state1)
        fs.save()
        new_user1 = User()
        fs.new(new_user1)
        fs.save()
        self.assertEqual(8, len(fs.all()))

    def test_delete_method(self):
        '''Test delete method'''
        fs = FileStorage()
        new_state = State()
        fs.new(new_state)
        fs.save()
        self.assertIn(new_state, fs.all(State).values())
        fs.delete(new_state)
        self.assertNotIn(new_state, fs.all(State).values())

if __name__ == "__main__":
    unittest.main()
