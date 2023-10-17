#!/usr/bin/python3
"""Defines unittests model for amenity.py.
Unittest classes:
    TestAmenityInstance
    TestAmenitySave
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityInstance(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    a = Amenity()

    def testAmenity_class(self):
        self.assertEqual(Amenity, type(self.a))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is store in the file"""
        self.assertIn(Amenity(), models.storage.all().values())

    def testAmenity_inheritance(self):
        """ Test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, BaseModel)

    def testHasAttrs(self):
        """ Test if Amenity has all attributes"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime)
        self.assertIsInstance(self.a.updated_at, datetime)

    def testAmenities_2_unique_ids(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def testAmenities_3_unique_ids(self):
        a1 = Amenity()
        a2 = Amenity()
        a3 = Amenity()
        self.assertNotEqual(a1.id, a2.id, a3.id)

    def test_two_amenities_different_created_at(self):
        a1 = Amenity()
        sleep(0.04)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_two_amenities_different_updated_at(self):
        a1 = Amenity()
        sleep(0.05)
        a2 = Amenity()
        self.assertLess(a1.updated_at, a2.updated_at)

    def test_args_unused(self):
        a = Amenity(None)
        self.assertNotIn(None, a.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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

    def testSave_one(self):
        a = Amenity()
        sleep(0.04)
        one_updated_at = a.updated_at
        a.save()
        self.assertLess(one_updated_at, a.updated_at)

    def testSave_with_arg(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.save(None)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        a = Amenity()
        self.assertTrue(dict, type(a.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        a = Amenity()
        self.assertIn("id", a.to_dict())
        self.assertIn("created_at", a.to_dict())
        self.assertIn("updated_at", a.to_dict())
        self.assertIn("__class__", a.to_dict())

    def test_to_dict_with_arg(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.to_dict(None)


if __name__ == '__main__':
    unittest.main()
