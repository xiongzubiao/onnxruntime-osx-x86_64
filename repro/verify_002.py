"""
JSON Pretty-Printer Module

This module provides a simple implementation of a JSON pretty-printer 
that can handle nested dictionaries and lists.
"""

import json

class JSONPrettyPrinter:
    """
    A class to handle pretty-printing of JSON-like data structures.
    """

    def __init__(self, indent=4):
        """
        Initialize the pretty-printer with a specific indentation level.

        Args:
            indent (int): Number of spaces for indentation.
        """
        self.indent = indent

    def format(self, data):
        """
        Format the given data into a pretty-printed string.

        Args:
            data (dict|list): The data structure to format.

        Returns:
            str: The pretty-printed string representation.
        """
        return json.dumps(data, indent=self.indent)

def pretty_print_json(data, indent=4):
    """
    A helper function to pretty-print JSON data.

    Args:
        data (dict|list): The data to print.
        indent (int): Indentation level.
    """
    printer = JSONPrettyPrinter(indent=indent)
    print(printer.format(data))

if __name__ == "__main__":
    # Demonstration data
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "is_developer": True,
        "skills": ["Python", "Machine Learning", "ONNX"],
        "address": {
            "street": "123 Main St",
            "city": "Tech City",
            "zip": "12345"
        },
        "projects": [
            {"id": 1, "name": "Project A", "status": "Completed"},
            {"id": 2, "name": "Project B", "status": "In Progress"}
        ]
    }

    print("Original Data:")
    print(sample_data)
    print("\nPretty-Printed Data:")
    pretty_print_json(sample_data)
