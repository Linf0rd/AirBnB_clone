#!/usr/bin/python3
"""
Class BaseModel
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all other classes in the project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'
                                )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """
        Updates the updated_at attribute with the current
        datetime and saves the object.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
