"""
JSON Pretty-Printer Module

This module provides functionality to format and print nested Python 
dictionaries and lists into a human-readable JSON-like string format.
"""

import json

class JSONFormatter:
    """
    A class to handle formatting of nested data structures.
    """
    def __init__(self, indent_size=4):
        """
        Initialize the formatter with a specific indentation size.
        
        Args:
            indent_size (int): Number of spaces for each indentation level.
        """
        self.indent_size = indent_size

    def format(self, data):
        """
        Format a nested dictionary or list into a pretty string.
        
        Args:
            data (dict|list): The data structure to format.
            
        Returns:
            str: The formatted string representation.
        """
        return json.dumps(data, indent=self.indent_size)

def pretty_print_json(data, indent=4):
    """
    Utility function to directly print formatted JSON data.
    
    Args:
        data (dict|list): The data structure to print.
        indent (int): Indentation size.
    """
    formatter = JSONFormatter(indent_size=indent)
    print(formatter.format(data))

if __name__ == "__main__":
    # Demonstration of the JSON Pretty-Printer
    sample_data = {
        "project": "Pretty Printer",
        "version": 1.0,
        "features": [
            "nested dictionaries",
            "lists",
            "custom indentation"
        ],
        "metadata": {
            "author": "GitHub Assistant",
            "date": "2026-06-15",
            "tags": ["python", "json", "formatter"]
        },
        "active": True
    }

    print("Original Data Representation:")
    print(sample_data)
    
    print("\nPretty Printed JSON:")
    pretty_print_json(sample_data)
