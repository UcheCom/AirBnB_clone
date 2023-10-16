#!/usr/bin/python3
"""Defines class model for amenity."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherits from the BaseModel.
    Attribute:
        name(str): The name of the Amenity.
    """

    name = ""
