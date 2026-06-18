"""
A module for pretty-printing JSON-like nested dictionaries and lists.

This module provides a class and functions to format complex data structures
into a human-readable string representation.
"""

import json

class JSONPrettyPrinter:
    """
    A class to handle the pretty-printing of JSON data.
    """

    def __init__(self, indent=4):
        """
        Initialize the pretty-printer with a specific indentation level.

        Args:
            indent (int): The number of spaces to use for indentation.
        """
        self.indent = indent

    def format(self, data):
        """
        Format the given data into a pretty-printed string.

        Args:
            data (dict | list): The nested structure to format.

        Returns:
            str: The formatted string.
        """
        return json.dumps(data, indent=self.indent)

def pretty_print_json(data, indent=4):
    """
    Convenience function to pretty-print JSON data.

    Args:
        data (dict | list): The nested structure to format.
        indent (int): Indentation level.
    """
    printer = JSONPrettyPrinter(indent=indent)
    print(printer.format(data))

if __name__ == "__main__":
    # Demonstration of the JSONPrettyPrinter
    sample_data = {
        "project": "JSON Pretty Printer",
        "version": 1.0,
        "features": ["nested dicts", "lists", "docstrings"],
        "author": {
            "name": "Assistant",
            "role": "Coding Assistant"
        },
        "active": True
    }

    print("--- Demonstrating JSON Pretty Printing ---")
    pretty_print_json(sample_data)
