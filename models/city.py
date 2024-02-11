#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of City.

        Args:
            *args (any): Not used.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
