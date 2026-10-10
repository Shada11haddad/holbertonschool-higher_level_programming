#!/usr/bin/env python3
"""Serialize and deserialize a dictionary with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary into XML under a <data> root and save it."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)
    tree = ET.ElementTree(root)
    if hasattr(ET, "indent"):
        ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Read XML from filename and return it as a dictionary.

    Values are returned as strings, since XML stores text only.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: (child.text or "") for child in root}
