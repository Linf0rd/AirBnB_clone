#!/usr/bin/python3
""""
Test cases
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of BaseModel instance attributes.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, prev_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
                model_dict['created_at'], model.created_at.isoformat()
        )
        self.assertEqual(
                model_dict['updated_at'], model.updated_at.isoformat()
        )
