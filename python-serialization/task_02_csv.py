#!/usr/bin/env python3
"""Convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read csv_filename and write its rows as JSON to data.json.

    Return True on success, False if the conversion fails.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
            data = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except (OSError, csv.Error):
        return False
