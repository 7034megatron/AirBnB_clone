#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): The ID of the place the review is for.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of Review.

        Args:
            *args (any): Not used.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
