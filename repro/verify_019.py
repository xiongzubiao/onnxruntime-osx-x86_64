"""
A simple CSV parser module that handles quoted fields and escaped quotes.

This module provides a CSVParser class to parse CSV data from strings or files,
correctly handling fields that contain commas, newlines, or escaped double quotes.
"""

import io
from typing import List, Iterator


class CSVParser:
    """
    A parser for Comma-Separated Values (CSV) data.
    
    Attributes:
        delimiter (str): The character used to separate fields.
        quotechar (str): The character used to quote fields containing special characters.
    """

    def __init__(self, delimiter: str = ',', quotechar: str = '"'):
        """
        Initializes the CSVParser with a delimiter and quote character.

        Args:
            delimiter (str): The field separator. Defaults to ','.
            quotechar (str): The quoting character. Defaults to '"'.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line: str) -> List[str]:
        """
        Parses a single line of CSV text into a list of fields.

        Args:
            line (str): The CSV line to parse.

        Returns:
            List[str]: A list of field values.
        """
        fields = []
        current_field = []
        in_quotes = False
        i = 0
        
        while i < len(line):
            char = line[i]
            
            if in_quotes:
                if char == self.quotechar:
                    # Check for escaped quote (double quotechar)
                    if i + 1 < len(line) and line[i + 1] == self.quotechar:
                        current_field.append(self.quotechar)
                        i += 1
                    else:
                        in_quotes = False
                else:
                    current_field.append(char)
            else:
                if char == self.quotechar:
                    in_quotes = True
                elif char == self.delimiter:
                    fields.append(''.join(current_field))
                    current_field = []
                elif char in ('\r', '\n'):
                    # Ignore trailing newlines
                    break
                else:
                    current_field.append(char)
            i += 1
            
        fields.append(''.join(current_field))
        return fields

    def parse_stream(self, stream: Iterator[str]) -> List[List[str]]:
        """
        Parses a stream of CSV lines.

        Args:
            stream (Iterator[str]): An iterator providing CSV lines.

        Returns:
            List[List[str]]: A list of parsed rows.
        """
        return [self.parse_line(line) for line in stream]


def demo():
    """
    Demonstrates the functionality of the CSVParser.
    """
    csv_data = [
        'Name,Age,Location',
        '"Doe, John",30,"New York, NY"',
        'Jane Smith,25,London',
        '"The ""Great"" Gatsby",1925,"Long Island"'
    ]
    
    parser = CSVParser()
    print("Parsing CSV Data:")
    print("-" * 20)
    
    for line in csv_data:
        parsed_row = parser.parse_line(line)
        print(f"Original: {line}")
        print(f"Parsed  : {parsed_row}")
        print("-" * 20)


if __name__ == '__main__':
    demo()
