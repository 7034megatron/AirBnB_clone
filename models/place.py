#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): The ID of the city the place is located in.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of IDs of amenities available in the place.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of Place.

        Args:
            *args (any): Not used.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
