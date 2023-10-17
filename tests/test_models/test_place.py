#!/usr/bin/python3
"""Defines unittests for models for place.py.
Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    p = Place()

    def test_no_args_instantiates(self):
        """Tests the place class instance"""
        self.assertEqual(Place, type(Place()))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is stored in the file"""
        self.assertIn(Place(), models.storage.all().values())

    def testPlace_inheritance(self):
        """ Test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, BaseModel)

    def testHasAttrs(self):
        """ Test if Place has all attributes"""
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))

    def test_Types(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime)
        self.assertIsInstance(self.p.updated_at, datetime)

    def test_2_places(self):
        """ Tests if 2 places has different ids"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_3_places(self):
        """ Tests if 2 places has different ids"""
        p1 = Place()
        p2 = Place()
        p3 = Place()
        self.assertNotEqual(p1.id, p2.id, p3.id)

    def test_2_places_different_created_at(self):
        p1 = Place()
        sleep(0.03)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_2_places_different_updated_at(self):
        p1 = Place()
        sleep(0.04)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)

    def test_args_unused(self):
        p = Place(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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

    def test_save_one(self):
        p = Place()
        sleep(0.04)
        one_updated_at = p.updated_at
        p.save()
        self.assertLess(one_updated_at, p.updated_at)

    def test_save_with_arg(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.save(None)


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        p = Place()
        self.assertTrue(dict, type(p.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        p = Place()
        self.assertIn("id", p.to_dict())
        self.assertIn("created_at", p.to_dict())
        self.assertIn("updated_at", p.to_dict())
        self.assertIn("__class__", p.to_dict())

    def test_to_dict_contains_added_attributes(self):
        p = Place()
        p.middle_name = "Bonny"
        p.my_number = 99
        self.assertEqual("Bonny", p.middle_name)
        self.assertIn("my_number", p.to_dict())


if __name__ == '__main__':
    unittest.main()
