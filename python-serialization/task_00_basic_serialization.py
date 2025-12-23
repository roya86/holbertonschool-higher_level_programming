#!/usr/bin/env python3
"""
Basic serialization module:
- Serialize a Python dictionary to a JSON file
- Deserialize a JSON file back to a Python dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file into a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
