"""
JSON Pretty-Printer Module

This module provides a simple utility to pretty-print nested dictionaries and lists
into a human-readable JSON format.
"""

import json

class PrettyPrinter:
    """
    A class used to represent a JSON Pretty-Printer.
    """

    def __init__(self, indent=4):
        """
        Parameters
        ----------
        indent : int, optional
            The number of spaces to use for indentation (default is 4).
        """
        self.indent = indent

    def format(self, data):
        """
        Formats a dictionary or list into a pretty-printed string.

        Parameters
        ----------
        data : dict or list
            The data structure to format.

        Returns
        -------
        str
            The formatted JSON string.
        """
        return json.dumps(data, indent=self.indent, sort_keys=True)

def print_json(data, indent=4):
    """
    Utility function to print formatted JSON data.

    Parameters
    ----------
    data : dict or list
        The data to be printed.
    indent : int, optional
        Indentation size (default 4).
    """
    pp = PrettyPrinter(indent=indent)
    print(pp.format(data))

if __name__ == '__main__':
    # Demonstration of the JSON Pretty-Printer
    sample_data = {
        "name": "MemoryBox",
        "version": "1.0.0",
        "features": ["memory", "documents", "connectors"],
        "metadata": {
            "author": "Zubiao",
            "active": True,
            "tags": None
        }
    }
    
    print("Original data (printed normally):")
    print(sample_data)
    print("\nPretty-printed data:")
    print_json(sample_data)
