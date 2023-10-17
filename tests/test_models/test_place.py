#!/usr/bin/python3
""" """

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_attributes(self):
        """
        Test the public attributes of Place class.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        """
        Test the inheritance of Place class.
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == '__main__':
    unittest.main()
