"""
JSON Pretty Printer Module

This module provides a simple implementation of a JSON-like pretty printer
for nested dictionaries and lists in Python.
"""

import json

class JSONPrettyPrinter:
    """
    A class used to represent a JSON Pretty Printer.
    """

    def __init__(self, indent=4):
        """
        Parameters
        ----------
        indent : int, optional
            The number of spaces for indentation (default is 4)
        """
        self.indent = indent

    def format(self, data):
        """
        Formats a dictionary or list into a pretty-printed string.

        Parameters
        ----------
        data : dict or list
            The data to be pretty-printed.

        Returns
        -------
        str
            The pretty-printed string representation of the data.
        """
        return json.dumps(data, indent=self.indent)

def print_json_demo(data):
    """
    Prints a demonstration of the JSONPrettyPrinter class.

    Parameters
    ----------
    data : dict or list
        The data to be pretty-printed and displayed.
    """
    printer = JSONPrettyPrinter(indent=2)
    pretty_data = printer.format(data)
    print("Pretty Printed JSON:")
    print(pretty_data)

if __name__ == "__main__":
    # Demonstration data: nested dictionary and list
    demo_data = {
        "name": "MemoryBox",
        "version": "1.0.0",
        "features": ["Memories", "Documents", "Connectors"],
        "metadata": {
            "author": "Zubiao",
            "active": True,
            "tags": ["AI", "Knowledge Management"]
        }
    }

    # Execute the demo
    print_json_demo(demo_data)
