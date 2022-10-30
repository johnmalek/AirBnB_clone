#!/usr/bin/python3
"""
Test class for place class
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    class for testing Place class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_Place(self):
        """
        Test that place.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """
        Test that test_place.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up method for place class
        """
        self.P = Place()

    def tearDown(self):
        """initialized method for place
        """
        self.P = None

    def test_type(self):
        """test method for type testing of place
        """
        self.assertIsInstance(self.P, Place)
        self.assertEqual(type(self.P), Place)
        self.assertEqual(issubclass(self.P.__class__, Place), True)
        self.assertEqual(isinstance(self.P, Place), True)
