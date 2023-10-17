#!/usr/bin/python3
""" """

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_attributes(self):
        """
        Test the public attributes of Amenity class.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """
        Test the inheritance of Amenity class.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
