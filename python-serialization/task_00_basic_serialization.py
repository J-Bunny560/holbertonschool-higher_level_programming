#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a json file
    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output json filr
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"The data has been serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """
    Load and deserialize a json file to a python dictionary
    Args:
        filename (str): The filename of the input json file
    Returns:
        dict: The deserialized Python dictionary
    """
    with open(filename, 'r') as f:
        return json.load(f)
