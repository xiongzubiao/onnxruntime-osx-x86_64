"""
JSON Pretty-Printer Module

This module provides a class and utility functions for formatting nested
dictionaries and lists into a human-readable JSON-like string.
"""

import json

class JSONPrettyPrinter:
    """
    A class to handle the pretty-printing of nested data structures.
    """

    def __init__(self, indent=4):
        """
        Initialize the printer with a specific indentation level.

        Args:
            indent (int): The number of spaces to use for each indentation level.
        """
        self.indent = indent

    def format(self, data):
        """
        Convert a Python object into a pretty-printed JSON string.

        Args:
            data (dict|list|str|int|float|bool|None): The data to format.

        Returns:
            str: The formatted string.
        """
        return json.dumps(data, indent=self.indent)

def pretty_print(data, indent=4):
    """
    A helper function to quickly print data to the console.

    Args:
        data (dict|list|str|int|float|bool|None): The data to print.
        indent (int): The indentation level.
    """
    printer = JSONPrettyPrinter(indent=indent)
    print(printer.format(data))

if __name__ == "__main__":
    # Demonstration of the JSONPrettyPrinter
    sample_data = {
        "user": "developer",
        "active": True,
        "roles": ["admin", "contributor"],
        "metadata": {
            "last_login": "2026-06-17",
            "session_id": 12345,
            "tags": None
        },
        "items": [
            {"id": 1, "name": "item_a"},
            {"id": 2, "name": "item_b", "extra": [1, 2, 3]}
        ]
    }

    print("--- Original Data ---")
    print(sample_data)
    print("\n--- Pretty-Printed Data ---")
    pretty_print(sample_data)
