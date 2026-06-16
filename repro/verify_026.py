"""
A module to pretty-print JSON-like structures (nested dicts and lists).
"""

import json

class JSONPrettyPrinter:
    """
    A class to handle the pretty-printing logic for nested dictionaries and lists.
    """

    def __init__(self, indent=4):
        """
        Initialize the pretty printer with a specific indentation.

        Args:
            indent (int): Number of spaces for indentation.
        """
        self.indent = indent

    def format(self, data):
        """
        Format the provided data into a pretty-printed string.

        Args:
            data (dict|list): The JSON-compatible data structure.

        Returns:
            str: Pretty-printed string.
        """
        return json.dumps(data, indent=self.indent)

def pretty_print(data, indent=4):
    """
    A helper function to quickly pretty-print a data structure.

    Args:
        data (dict|list): The JSON-compatible data structure.
        indent (int): Number of spaces for indentation.
    """
    printer = JSONPrettyPrinter(indent=indent)
    print(printer.format(data))

if __name__ == '__main__':
    # Demonstration of the JSONPrettyPrinter
    sample_data = {
        "name": "MemoryBox",
        "version": "1.0.0",
        "features": ["memory", "search", "connectors"],
        "metadata": {
            "author": "xiongzubiao",
            "active": True,
            "tags": None
        }
    }

    print("Pretty-printing sample data:")
    pretty_print(sample_data)
