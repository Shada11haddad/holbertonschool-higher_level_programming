#!/usr/bin/env python3
"""Basic serialization module: dict <-> JSON file."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to filename.

    If the file already exists, it is replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
