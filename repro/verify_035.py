"""
Module for parsing CSV data with support for quoted fields.

This module provides a CSVParser class that can handle standard CSV formats,
including fields enclosed in double quotes that may contain commas or newlines.
"""

import io


class CSVParser:
    """
    A simple CSV parser that handles quoted fields.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with specific delimiter and quote character.

        Args:
            delimiter (str): The character used to separate fields.
            quotechar (str): The character used to enclose fields.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parse a single line of CSV text.

        Args:
            line (str): A single CSV line.

        Returns:
            list: A list of parsed fields.
        """
        fields = []
        current_field = []
        in_quotes = False
        i = 0
        while i < len(line):
            char = line[i]

            if char == self.quotechar:
                if in_quotes and i + 1 < len(line) and line[i + 1] == self.quotechar:
                    # Handle escaped quotes ("")
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    # Toggle quote mode
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                # Field separator
                fields.append(''.join(current_field).strip())
                current_field = []
            elif char in ('\r', '\n') and not in_quotes:
                # End of line
                break
            else:
                current_field.append(char)
            i += 1

        fields.append(''.join(current_field).strip())
        return fields

    def parse_string(self, text):
        """
        Parse a multi-line CSV string.

        Args:
            text (str): The CSV content.

        Returns:
            list: A list of rows, where each row is a list of fields.
        """
        result = []
        lines = text.splitlines()
        for line in lines:
            if line.strip():
                result.append(self.parse_line(line))
        return result


def main():
    """
    Demonstration of the CSVParser functionality.
    """
    csv_data = [
        'Name,Age,Location',
        'John Doe,30,"New York, NY"',
        '"Doe, Jane",25,London',
        'Bob "The Builder" Smith,45,Construction Site'
    ]
    csv_text = '\\n'.join(csv_data)

    print("--- Original CSV Data ---")
    print(csv_text)
    print("\\n--- Parsed Results ---")

    parser = CSVParser()
    parsed_rows = parser.parse_string(csv_text)

    for row in parsed_rows:
        print(row)


if __name__ == "__main__":
    main()
