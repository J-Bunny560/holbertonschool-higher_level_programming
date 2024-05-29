#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Create the root element
    root = ET.Element("data")

    # Iterate through the dictionary items
    for key, value in dictionary.items():
        # Create a child element for each key-value pair
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    # Create an ElementTree object
    tree = ET.ElementTree(root)

    # Write the tree to the file
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Initialize an empty dictionary
    dictionary = {}

    # Iterate through the XML elements to reconstruct the dictionary
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary

