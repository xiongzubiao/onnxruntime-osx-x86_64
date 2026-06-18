"""
JSON Pretty Printer Module

This module provides functionality to format and print nested Python 
dictionaries and lists in a human-readable JSON-like format.
"""

import json

class JSONPrettyPrinter:
    """
    A class used to represent a JSON Pretty Printer.

    Attributes:
        indent (int): The number of spaces for indentation.
    """

    def __init__(self, indent=4):
        """
        Initializes the JSONPrettyPrinter with a specific indentation.

        Args:
            indent (int): The number of spaces for indentation (default is 4).
        """
        self.indent = indent

    def format(self, data):
        """
        Formats a Python object (dict or list) into a pretty-printed string.

        Args:
            data (dict or list): The nested object to be formatted.

        Returns:
            str: The pretty-printed JSON string.
        """
        return json.dumps(data, indent=self.indent)

def print_json(data, indent=4):
    """
    Convenience function to print a Python object as formatted JSON.

    Args:
        data (dict or list): The nested object to be printed.
        indent (int): The number of spaces for indentation (default is 4).
    """
    printer = JSONPrettyPrinter(indent=indent)
    print(printer.format(data))

if __name__ == "__main__":
    # Demonstration of the JSON Pretty Printer
    sample_data = {
        "user": "developer",
        "active": True,
        "profile": {
            "name": "Zubiao Xiong",
            "roles": ["Admin", "Developer", "Maintainer"],
            "metadata": {
                "id": 12345,
                "tags": ["onnx", "runtime", "osx"]
            }
        },
        "repositories": [
            {"name": "onnxruntime-osx-x86_64", "branch": "master"},
            {"name": "test-repo", "branch": "main"}
        ]
    }

    print("Pretty-printing sample nested data:")
    print_json(sample_data)
