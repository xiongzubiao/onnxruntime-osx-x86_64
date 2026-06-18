"""
JSON Pretty-Printer Module

This module provides a utility class and functions to format and print
nested Python dictionaries and lists in a human-readable JSON-like format.
"""

import json

class JSONPrettyPrinter:
    """
    A class to handle the pretty-printing of nested data structures.
    """

    def __init__(self, indent_size=4):
        """
        Initialize the pretty-printer.

        Args:
            indent_size (int): The number of spaces per indentation level.
        """
        self.indent_size = indent_size

    def format(self, data):
        """
        Format the given data into a pretty-printed string.

        Args:
            data (dict|list): The data structure to format.

        Returns:
            str: The formatted string representation of the data.
        """
        return json.dumps(data, indent=self.indent_size)

def pretty_print(data, indent=4):
    """
    A convenience function to print data directly to the console.

    Args:
        data (dict|list): The data structure to print.
        indent (int): The number of spaces per indentation level.
    """
    printer = JSONPrettyPrinter(indent_size=indent)
    print(printer.format(data))

if __name__ == "__main__":
    # Demonstration of the JSONPrettyPrinter
    sample_data = {
        "project": "onnxruntime-osx-x86_64",
        "status": "verified",
        "nested_items": [
            {"id": 1, "name": "item_one", "tags": ["repro", "verify"]},
            {"id": 2, "name": "item_two", "active": True}
        ],
        "metadata": {
            "version": "1.0.0",
            "author": "Assistant",
            "timestamp": "2026-06-17"
        }
    }

    print("--- Formatted Data Demo ---")
    pretty_print(sample_data)
