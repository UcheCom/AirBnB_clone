#!/usr/bin/python3
""" Module defines the parent class for other classes.
"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """ This defines the base class for the HBNB
    console project.
    """

    def __init__(self):
        """ Initializes the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints the string representation of the
        Base class instance.
        """
        c_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(c_name, self.id, self.__dict__))

    def save(self):
        """ This updates the updated_at with the
        current date.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        o_dict = self.__dict__.copy()
        o_dict['__class__'] = self.__class__.__name__
        o_dict['created_at'] = self.created_at.isoformat()
        o_dict['updated_at'] = self.updated_at.isoformat()
        return (o_dict)
