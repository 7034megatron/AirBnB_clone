#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of Amenity.

        Args:
            *args (any): Not used.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
