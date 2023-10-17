#!/usr/bin/python3
""" """

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_attributes(self):
        """
        Test the public attributes of Review class.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """
        Test the inheritance of Review class.
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == '__main__':
    unittest.main()
