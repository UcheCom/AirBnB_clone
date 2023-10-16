#!/usr/bin/python3
"""Defines unittests model for state.py.
Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
from models.state import State
import models


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    st = State()

    def testState_class(self):
        """Tests if an instance of the State is an instance of
        State class"""
        self.assertEqual(State, type(self.st))

    def test_no_args_instantiates(self):
        """Tests for no argument"""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """ Tests if a new instance is stored in the file"""
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Tests if the str id is public"""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        """Tests the created_at instance"""
        self.assertEqual(datetime, type(State().created_at))

    def testState_inheritance(self):
        """ Tests if State is a subclass of BaseModel"""
        self.assertIsInstance(self.st, BaseModel)

    def testHasAttributes(self):
        """Tests if the State has all the attributes"""
        self.assertTrue(hasattr(self.st, 'name'))
        self.assertTrue(hasattr(self.st, 'id'))
        self.assertTrue(hasattr(self.st, 'created_at'))
        self.assertTrue(hasattr(self.st, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.st.name, str)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime)
        self.assertIsInstance(self.st.updated_at, datetime)

    def test_2_state_unique_ids(self):
        """Tests if 2 places have different ids"""
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_3_state_unique_ids(self):
        """Tests if 3 places have different ids"""
        st1 = State()
        st2 = State()
        st3 = State()
        self.assertNotEqual(st1.id, st2.id, st3.id)

    def test_2_states_different_created_at(self):
        st1 = State()
        sleep(0.04)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_2_states_different_updated_at(self):
        st1 = State()
        sleep(0.04)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_args_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    class TestState_save(unittest.TestCase):
        """Unittests for testing save method of the State class."""

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

    def test_one_save(self):
        st = State()
        sleep(0.03)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    def test_save_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updates_file(self):
        st = State()
        st.save()
        st_id = "State." + st.id
        with open("file.json") as f:
            self.assertIn(st_id, f.read())

    class TestState_to_dict(unittest.TestCase):
        """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)


if __name__ == '__main__':
    unittest.main()
