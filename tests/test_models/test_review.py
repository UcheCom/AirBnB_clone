#!/usr/bin/python3
"""Defines the unittest model for review.py
Unittest classes:
    TestReviewInstance
    TestReviewSave
    TestReview_to_dict
"""

import os
import models
import unittest
from models.review import Review
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestReviewInstance(unittest.TestCase):
    """Unittests for testing instances of the Review class"""

    r = Review()

    def TestReviewClass(self):
        self.assertEqual(Review, type(self.r))

    def test_instance_store_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def testReview_inheritance(self):
        self.assertIsInstance(self.r, BaseModel)

    def testHasAttrs(self):
        """ Test if Review has all attributes"""
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime)
        self.assertIsInstance(self.r.updated_at, datetime)

    def test_reviews_2_unique(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_reviews_3_unique_ids(self):
        r1 = Review()
        r2 = Review()
        r3 = Review()
        self.assertNotEqual(r1.id, r2.id, r3.id)

    def test_two_reviews_different_created_at(self):
        r1 = Review()
        sleep(0.05)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_two_reviews_different_updated_at(self):
        r1 = Review()
        sleep(0.04)
        r2 = Review()
        self.assertLess(r1.updated_at, r2.updated_at)

    def test_args_unused(self):
        r = Review(None)
        self.assertNotIn(None, r.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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
        r = Review()
        sleep(0.05)
        one_updated_at = r.updated_at
        r.save()
        self.assertLess(one_updated_at, r.updated_at)

    def test_save_with_arg(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.save(None)


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        r = Review()
        self.assertTrue(dict, type(r.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        r = Review()
        self.assertIn("id", r.to_dict())
        self.assertIn("created_at", r.to_dict())
        self.assertIn("updated_at", r.to_dict())
        self.assertIn("__class__", r.to_dict())


if __name__ == '__main__':
    unittest.main()
