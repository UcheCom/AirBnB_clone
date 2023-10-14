#!/usr/bin/python3
""" This is the unit test module for test_file_storage class
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import models
import os


class TestFileStorage(unittest.TestCase):
    """ Test case for file storage"""

    def setUp(self):
        """ Set up for all tests """
        self.storage = FileStorage()

    def tearDown(self):
        """ Remove file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """ Test all method """
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        storage.save()
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertIn("BaseModel." + obj.id, objs)

    def test_new(self):
        """ Test new method """
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        self.assertIn("BaseModel." + obj.id, storage.all())

    def test_save(self):
        """ Test save method """
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + obj.id, f.read())

    def test_reload(self):
        """ Test reload method """
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        storage.save()
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertIn("BaseModel." + obj.id, objs)


if __name__ == "__main__":
    unittest.main()
