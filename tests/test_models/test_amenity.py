#!/usr/bin/python3
"""Module: test_amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test_amenity Class"""

    def __init__(self, *args, **kwargs):
        """initializing instances"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test 2 name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
