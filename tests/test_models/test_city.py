#!/usr/bin/python3
""" """

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_attributes(self):
        """
        Test the public attributes of City class.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        """
        Test the inheritance of City class.
        """
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
