"""
JSON Pretty-Printer Module

This module provides functionality to format nested Python dictionaries and lists
into a human-readable JSON-like string format.
"""

import json

class JSONPrettyPrinter:
    """
    A class used to represent a JSON Pretty-Printer.

    Attributes
    ----------
    indent : int
        The number of spaces to use for indentation (default is 4).
    """

    def __init__(self, indent=4):
        """
        Parameters
        ----------
        indent : int, optional
            The number of spaces for indentation (default is 4).
        """
        self.indent = indent

    def format(self, data):
        """
        Formats a Python object (dict or list) into a pretty-printed string.

        Parameters
        ----------
        data : dict or list
            The data to be formatted.

        Returns
        -------
        str
            The pretty-printed string representation of the data.
        """
        return json.dumps(data, indent=self.indent)

def print_pretty_json(data, indent=4):
    """
    Helper function to print data in a pretty JSON format.

    Parameters
    ----------
    data : dict or list
        The data to be printed.
    indent : int, optional
        The number of spaces for indentation (default is 4).
    """
    printer = JSONPrettyPrinter(indent=indent)
    print(printer.format(data))

if __name__ == "__main__":
    # Demonstration of the JSONPrettyPrinter
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "is_developer": True,
        "skills": ["Python", "Machine Learning", "ONNX"],
        "address": {
            "city": "Seattle",
            "zip": "98101"
        },
        "projects": [
            {"id": 1, "name": "Project Alpha", "status": "Completed"},
            {"id": 2, "name": "Project Beta", "status": "In Progress"}
        ]
    }

    print("Pretty Printing Nested Data:")
    print_pretty_json(sample_data)
