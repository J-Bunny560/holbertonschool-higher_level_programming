#!/usr/bin/python3
""" script that adds all arguments to a Python list"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
finally:
    for arg in sys.argv[1:]:
        items.append(arg)
    save_to_json_file(items, "add_item.json")
