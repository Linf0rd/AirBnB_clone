#!/usr/bin/python3
"""
Defines unittests for models/engine/file_storage.py
"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import json
import os


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after each test.
        """
        self.storage.reload()

    def test_all(self):
        """
        Test the 'all' method of FileStorage..
        """
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objs)
        self.assertEqual(all_objs["BaseModel.{}".format(obj.id)], obj)

    def test_new(self):
        """
        Test the 'new' method of FileStorage.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """
        Test the save() method.
        """
        obj = BaseModel()
        self.storage.new(obj)
        with patch(
                'models.engine.file_storage.open', create=True) as mock_file:
            self.storage.save()
            mock_file.assert_called_once_with
            (self.storage._FileStorage__file_path, 'w')

    def test_reload(self):
        """
        Test the reload() method.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objs)
        self.assertEqual(
                all_objs["BaseModel.{}".format(obj.id)].to_dict(),
                obj.to_dict()
        )

    def test_reload_file_not_found(self):
        """
        Test the reload() method when the file is not found.
        """
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.storage.reload()
            self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
