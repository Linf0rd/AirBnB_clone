#!/usr/bin/python3
""" """

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for User class.
    """

    def test_email_default_value(self):
        """
        Test the default value of email attribute.
        """
        user = User()
        self.assertEqual(user.email, "")

    def test_password_default_value(self):
        """
        Test the default value of password attribute.
        """
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_default_value(self):
        """
        Test the default value of first_name attribute.
        """
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_default_value(self):
        """
        Test the default value of last_name attribute.
        """
        user = User()
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
