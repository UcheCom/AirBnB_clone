#!/usr/bin/python3
"""Defines class model for place."""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class inherits from the BaseModel.
    Attributes:
        city_id(str): The City id.
        user_id(str): The User id.
        name(str): The name of the State.
        description(str): The description of the Place.
        number_rooms(int): The number of rooms.
        number_bathrooms(int): The number of bathrooms.
        max_guest(int): The maximum number of  guest.
        price_by_night(int): The price by night of the place.
        latitude(float): The latitude of the place.
        longitude(float): The longitude of the place.
        amenity_ids(list): The list of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
