#!/usr/bin/python3
"""Module: test_state"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test_state Class"""

    def __init__(self, *args, **kwargs):
        """init instances"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test name 3"""
        new = self.value()
        self.assertEqual(type(new.name), str)
