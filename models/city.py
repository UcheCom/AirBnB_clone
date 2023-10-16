#!/usr/bin/python3
"""Defines class model for city."""

from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from the BaseModel.
    Attributes:
        state_id(str): The State id.
        name(str): The name of the City
    """

    state_id = ""
    name = ""
