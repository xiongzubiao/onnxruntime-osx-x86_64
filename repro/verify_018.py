"""
JSON Pretty-Printer Module

This module provides a utility to format and print nested dictionary and list 
structures in a human-readable JSON-like format.
"""

import json
from typing import Any, Union

class JSONFormatter:
    """
    A class to handle the formatting of JSON-compatible Python objects.
    """

    def __init__(self, indent: int = 4):
        """
        Initialize the formatter.

        Args:
            indent (int): The number of spaces for each indentation level.
        """
        self.indent = indent

    def format(self, data: Union[dict, list]) -> str:
        """
        Convert a Python object (dict or list) into a pretty-printed string.

        Args:
            data (Union[dict, list]): The data to format.

        Returns:
            str: The formatted string.
        """
        return json.dumps(data, indent=self.indent)

def pretty_print(data: Any) -> None:
    """
    Print the given data in a pretty format to the console.

    Args:
        data (Any): The data to print.
    """
    formatter = JSONFormatter()
    print(formatter.format(data))

if __name__ == "__main__":
    # Demonstration of the JSON pretty-printer
    sample_data = {
        "name": "MemoryBox Repro",
        "version": "1.0.0",
        "features": [
            "GitHub Integration",
            "Memory Retrieval",
            "Tool Calling"
        ],
        "metadata": {
            "author": "Assistant",
            "timestamp": "2026-06-17",
            "active": True
        },
        "nested_list": [
            {"id": 1, "status": "ok"},
            {"id": 2, "status": "pending"}
        ]
    }

    print("--- Original Data ---")
    print(sample_data)
    
    print("\n--- Pretty Printed Data ---")
    pretty_print(sample_data)
