#!usr/bin/python3
"""Module test_console"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_Console(unittest.TestCase):
    """Class to test the console"""
    @classmethod
    def setUpClass(self):
        """Sets a Class for testing"""
        self.console_1 = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Test to delete the class created"""
        del self.console_1

    def test_do_create(self):
        """Testing do_create in the console"""
        with patch('sys.stdout', new=StringIO()) as mock:
            self.console_1.onecmd("create State numb=1")
            self.assertTrue(len(mock.getvalue()) >= 1)
        with patch('sys.stdout', new=StringIO()) as mock_2:
            self.console_1.onecmd("Show state" + mock.getvalue())
            self.assertFalse("numb" in mock_2.getvalue())
         with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            us = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            st = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            ct = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            rv = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            am = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())
