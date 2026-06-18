"""
JSON Pretty-Printer Module

This module provides a utility class to pretty-print nested Python dictionaries
and lists in a JSON-like format.
"""

import json

class JSONPrettyPrinter:
    """
    A class used to represent a JSON Pretty-Printer.

    Attributes
    ----------
    indent : int
        the number of spaces to use for indentation (default is 4)
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
        Formats the input data into a pretty-printed JSON string.

        Parameters
        ----------
        data : dict or list
            The nested data structure to format.

        Returns
        -------
        str
            The pretty-printed JSON string.
        """
        return json.dumps(data, indent=self.indent)

    def print(self, data):
        """
        Prints the formatted JSON string to the console.

        Parameters
        ----------
        data : dict or list
            The nested data structure to print.
        """
        print(self.format(data))

if __name__ == "__main__":
    # Demonstration of the JSONPrettyPrinter class
    printer = JSONPrettyPrinter(indent=2)

    sample_data = {
        "name": "MemoryBox",
        "version": "1.0.0",
        "features": ["Memories", "Documents", "Connectors"],
        "metadata": {
            "author": "xiongzubiao",
            "active": True,
            "stats": {
                "users": 1000,
                "uptime": "99.9%"
            }
        }
    }

    print("Pretty-printing sample data:")
    printer.print(sample_data)
