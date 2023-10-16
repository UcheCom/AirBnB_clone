#!/usr/bin/python3
"""Defines class model for state."""

from models.base_model import BaseModel


class State(BaseModel):
    """This class inherits from the BaseModel.
    Attribute:
        name(str): The name of the State
    """

    name = ""
