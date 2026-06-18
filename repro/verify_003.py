"""
CSV Parser Module

This module provides a basic implementation of a CSV parser that correctly handles
fields containing commas, provided those fields are enclosed in double quotes.
"""

import io

class SimpleCSVParser:
    """
    A simple CSV parser that can handle quoted fields.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with specific delimiter and quote character.

        Args:
            delimiter (str): The character used to separate fields.
            quotechar (str): The character used to enclose fields containing the delimiter.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_row(self, line):
        """
        Parses a single line of CSV text.

        Args:
            line (str): A single line of CSV content.

        Returns:
            list: A list of strings representing the fields in the row.
        """
        fields = []
        current_field = []
        in_quotes = False
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if char == self.quotechar:
                # Handle escaped quotes (double quotechar)
                if in_quotes and i + 1 < len(line) and line[i+1] == self.quotechar:
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                fields.append("".join(current_field))
                current_field = []
            elif char in ('\r', '\n') and not in_quotes:
                # End of line characters
                break
            else:
                current_field.append(char)
            i += 1
            
        fields.append("".join(current_field))
        return fields

def run_demo():
    """
    Demonstrates the SimpleCSVParser with various edge cases.
    """
    parser = SimpleCSVParser()
    
    test_cases = [
        'name,age,city',
        '"Doe, John",30,New York',
        'Alice,"""Wonderland""",UK',
        'Plain Field,"Field with , comma",Simple'
    ]
    
    print("Starting CSV Parser Demo...\n")
    for row in test_cases:
        parsed = parser.parse_row(row)
        print(f"Original: {row}")
        print(f"Parsed:   {parsed}\n")

if __name__ == "__main__":
    run_demo()
