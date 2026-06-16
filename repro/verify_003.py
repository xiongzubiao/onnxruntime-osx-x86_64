"""
CSV Parser Module
================

This module provides a simple implementation of a CSV (Comma-Separated Values)
parser that correctly handles quoted fields, including those containing
delimiters or escaped quotes.
"""

from typing import List

class CSVParser:
    """
    A parser for CSV data that handles quoted fields.
    """

    def __init__(self, delimiter: str = ','):
        """
        Initialize the parser.

        :param delimiter: The character used to separate fields.
        """
        self.delimiter = delimiter

    def parse_line(self, line: str) -> List[str]:
        """
        Parses a single line of CSV text.

        :param line: A string representing a single line of CSV data.
        :return: A list of strings representing the fields in the line.
        """
        fields = []
        current_field = []
        in_quotes = False
        i = 0
        while i < len(line):
            char = line[i]
            if char == '"':
                if in_quotes and i + 1 < len(line) and line[i+1] == '"':
                    # Escaped quote
                    current_field.append('"')
                    i += 1
                else:
                    # Toggle quote state
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                fields.append("".join(current_field))
                current_field = []
            elif char in ('\\n', '\\r') and not in_quotes:
                break
            else:
                current_field.append(char)
            i += 1
        
        fields.append("".join(current_field))
        return fields

    def parse(self, data: str) -> List[List[str]]:
        """
        Parses multiple lines of CSV data.

        :param data: The CSV data as a string.
        :return: A list of rows, where each row is a list of fields.
        """
        rows = []
        # Simple line splitting for the demo
        for line in data.splitlines():
            if line.strip():
                rows.append(self.parse_line(line))
        return rows

def run_demo():
    """
    Demonstrates the CSVParser with a sample CSV string.
    """
    csv_data = (
        'Name,Occupation,"Location, City"\\n'
        'Alice,Engineer,"New York, NY"\\n'
        'Bob,"Writer, Editor","San Francisco, CA"\\n'
        '"Charlie ""The Great""","Magician",London'
    )

    print("Input CSV Data:")
    print(csv_data)
    print("-" * 20)

    parser = CSVParser()
    parsed_rows = parser.parse(csv_data)

    print("Parsed Rows:")
    for row in parsed_rows:
        print(row)

if __name__ == '__main__':
    run_demo()
