#!/usr/bin/python3
""" """

import unittest
from models.state import State
from models.base_model import BaseModel
import models
import os


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_attributes(self):
        """
        Test the public attributes of State class.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """
        Test the inheritance of State class.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
