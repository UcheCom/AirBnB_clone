#!/usr/bin/python3
""" This is the unit test module for test_base_model class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from time import sleep

class TestBaseModel(unittest.TestCase):
    """ Test case for base model"""

    my_model = BaseModel()

    def tests_Attributes(self):
        """ This test the attributes of the class"""
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        my_model_json = self.my_model.to_dict()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

        self.assertEqual(self.my_model.id, my_model_json['id'])
        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])

    def tests_Save(self):
        """ This tests the save method """
        my_model = BaseModel()
        sleep(0.1)
        updated_at_1 = my_model.updated_at
        my_model.save()
        self.assertLess(updated_at_1, my_model.updated_at)

    def test_to_dict_type(self):
        """ Tests the dictionary type"""
        my_model = BaseModel()
        self.assertTrue(dict, type(my_model.to_dict()))

    if __name__ == "__main__":
        unittest.main()
