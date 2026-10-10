#!/usr/bin/env python3
"""Serialize and deserialize a custom class with pickle."""
import pickle


class CustomObject:
    """A simple object that can be pickled to and from a file."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Pickle this instance to filename. Return None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load a CustomObject from filename. Return None on failure."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError,
                AttributeError, ImportError, IndexError, TypeError,
                ValueError):
            return None
        if not isinstance(obj, cls):
            return None
        return obj
