#!/usr/bin/python3
"""Defines unittests model for city.py.
Unittest classes:
    TestCityInstantiation
    TestCitySave
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models.base_model import BaseModel

class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    c = City()

    def testCity_instantiates(self):
        self.assertEqual(City, type(self.c))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is stored in the file"""
        self.assertIn(City(), models.storage.all().values())

    def testCity_inheritance(self):
        """ Test if City is a subclass of BaseModel"""
        self.assertIsInstance(self.c, BaseModel)

    def testHasAttrs(self):
        """ Test if City has all the attributes"""
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime)
        self.assertIsInstance(self.c.updated_at, datetime)

    def test_places_2(self):
        """ Tests if 2 cities have different ids"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_places_3(self):
        """ Tests if 3 cities have different ids"""
        c1 = City()
        c2 = City()
        c3 = City()
        self.assertNotEqual(c1.id, c2.id, c3.id)

    def testArgs_unused(self):
        c = City(None)
        self.assertNotIn(None, c.__dict__.values())


class TestCitySave(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_save_1(self):
        c = City()
        sleep(0.04)
        one_updated_at = c.updated_at
        c.save()
        self.assertLess(one_updated_at, c.updated_at)

    def test_save_with_arg(self):
        c = City()
        with self.assertRaises(TypeError):
            c.save(None)


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        c = City()
        self.assertTrue(dict, type(c.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        c = City()
        self.assertIn("id", c.to_dict())
        self.assertIn("created_at", c.to_dict())
        self.assertIn("updated_at", c.to_dict())
        self.assertIn("__class__", c.to_dict())

    def test_to_dict_with_arg(self):
        c = City()
        with self.assertRaises(TypeError):
            c.to_dict(None)


if __name__ == '__main__':
    unittest.main()
