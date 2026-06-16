"""
A simple JSON pretty-printer module.
This module provides a class and functions to format nested dictionaries and lists 
into a human-readable JSON-like string.
"""

import json

class JSONFormatter:
    """
    A class used to format JSON-like objects (dicts and lists).
    """

    def __init__(self, indent=4):
        """
        Initializes the formatter with a specific indentation level.
        
        Args:
            indent (int): The number of spaces for each indentation level.
        """
        self.indent = indent

    def format(self, data):
        """
        Formats a dictionary or list into a pretty-printed string.
        
        Args:
            data (dict|list): The data to be formatted.
            
        Returns:
            str: The pretty-printed string.
        """
        return json.dumps(data, indent=self.indent)

def pretty_print(data, indent=4):
    """
    Convenience function to pretty print a dictionary or list.
    
    Args:
        data (dict|list): The data to print.
        indent (int): Indentation level.
    """
    formatter = JSONFormatter(indent=indent)
    print(formatter.format(data))

if __name__ == "__main__":
    # Demo data
    sample_data = {
        "name": "MemoryBox",
        "version": "1.0.0",
        "features": ["Memories", "Documents", "Connectors"],
        "metadata": {
            "author": "Xiong Zubiao",
            "active": True,
            "stats": {
                "users": 1000,
                "uptime": "99.9%"
            }
        },
        "tags": [None, 1, 2.5]
    }

    print("--- Original Data ---")
    print(sample_data)
    print("\n--- Pretty Printed Data ---")
    pretty_print(sample_data)
