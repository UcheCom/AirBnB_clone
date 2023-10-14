#!/usr/bin/python3
""" Defines the user class that inherits from the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ class user inherits from the BaseModel.

    Attributes:
        email: string - The email of the user.
        password: string - The password of the user.
        first_name: string - The first name of the user.
        last_name: string - The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
