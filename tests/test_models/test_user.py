#!/usr/bin/python3
"""Defines the unittest module for user.py"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test case for the User class"""

    def setUp(self):
        """Set up for all tests"""
        self.user = User()

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_attributes(self):
        """Test if User has the required attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """Test if User's to_dict method returns
        a dictionary with the correct attributes
        """
        # Call the to_dict method on the user instance
        # and assign it to user_dict
        user_dict = self.user.to_dict()
        # Check if user_dict is a dictionary
        self.assertIsInstance(user_dict, dict)
        # Check if user_dict has the correct class name
        self.assertEqual(user_dict["__class__"], "User")
        # Check if user_dict has the same id as the user instance
        self.assertEqual(user_dict["id"], self.user.id)
        # Check if user_dict has the same created_at
        # as the user instance in ISO format
        self.assertEqual(
            user_dict["created_at"],
            self.user.created_at.isoformat()
            )
        # Check if user_dict has the same updated_at
        # as the user instance in ISO format
        self.assertEqual(
            user_dict["updated_at"],
            self.user.updated_at.isoformat()
            )

    def test_init_kwargs(self):
        """Test if User's __init__ method
        with keyword arguments works correctly"""
        # Create a dictionary of attributes and values
        kwargs = {
                "id": "5678",
                "email": "bob@mail.com",
                "password": "1234",
                "first_name": "Bob",
                "last_name": "Smith"
            }
        # Create an instance of User with kwargs
        user = User(**kwargs)
        # Check if the user has the same attributes and values as kwargs
        for key, value in kwargs.items():
            self.assertEqual(getattr(user, key), value)


if __name__ == "__main__":
    unittest.main()
