#!/usr/bin/python3
"""Defines class model for review."""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from the BaseModel.
    Attributes:
        place_id(str): The Place id.
        user_id(str): The User id.
        text(str): Message text.
    """

    place_id = ""
    user_id = ""
    text = ""
