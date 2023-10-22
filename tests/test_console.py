#!/usr/bin/python3
"""
Defines unittests for console.py
"""

import os
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Unit tests for the console.py module.
    """

    def setUp(self):
        """
        Set up the console instance before each test.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up after each test.
        """
        pass

    def test_quit(self):
        """
        Test if the quit command exits the program.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """
        Test if the EOF command exits the program.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_help(self):
        """
        Test if the help command displays the help message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):",
                          f.getvalue())

    def test_empty_line(self):
        """
        Test if an empty line does nothing.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_BaseModel(self):
        """
        Test if the create command creates an instance of BaseModel.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(f.getvalue().strip().isalnum())

    def test_BaseModel_all(self):
        """
        Test if the BaseModel.all() command prints all BaseModel instances.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")

    def test_Review_all(self):
        """
        Test if the Review.all() command prints all Review instances.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.all()")

    def test_BaseModel_count(self):
        """
        Test if the BaseModel.count() command prints
        the count of BaseModel instances.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")

    def test_User_count(self):
        """
        Test if the User.count() command prints the count of User instances.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")

    def test_BaseModel_show(self):
        """
        Test if the BaseModel.show() command prints the
        string representation of a BaseModel instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show(\"id\")")

    def test_User_show(self):
        """
        Test if the User.show() command prints the
        string representation of a User instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show(\"id\")")

    def test_BaseModel_destroy(self):
        """
        Test if the BaseModel.destroy() command deletes a BaseModel instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.destroy(\"id\")")

    def test_User_destroy(self):
        """
        Test if the User.destroy() command deletes a User instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.destroy(\"id\")")

    def test_BaseModel_update(self):
        """
        Test if the BaseModel.update() command updates a BaseModel instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.update(\"id\", \"attribute_name\", "
                                "\"string_value\")")

    def test_User_update(self):
        """
        Test if the User.update() command updates a User instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update(\"id\", \"attribute_name\", "
                                "\"string_value\")")


if __name__ == '__main__':
    unittest.main()
