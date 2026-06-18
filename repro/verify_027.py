"""
A complete, runnable Python program implementing a custom CSV parser.
This parser handles basic CSV structures, including fields containing
commas enclosed in double quotes and escaped double quotes.
"""

import io

class CSVParser:
    """
    A simple CSV parser that can handle quoted fields and escaped quotes.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with specific delimiter and quote character.

        Args:
            delimiter (str): The character used to separate fields.
            quotechar (str): The character used to enclose fields containing special characters.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parse a single line of CSV text into a list of fields.

        Args:
            line (str): A single line of CSV data.

        Returns:
            list: A list of strings representing the parsed fields.
        """
        fields = []
        current_field = io.StringIO()
        in_quotes = False
        i = 0
        n = len(line.rstrip('\r\n'))

        while i < n:
            char = line[i]

            if char == self.quotechar:
                if in_quotes and i + 1 < n and line[i+1] == self.quotechar:
                    # Handle escaped quote (e.g., "")
                    current_field.write(self.quotechar)
                    i += 1
                else:
                    # Toggle quote state
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                # End of field
                fields.append(current_field.getvalue())
                current_field = io.StringIO()
            else:
                # Regular character
                current_field.write(char)
            i += 1

        fields.append(current_field.getvalue())
        return fields

def run_demo():
    """
    Demonstrates the CSVParser with various edge cases.
    """
    parser = CSVParser()
    test_cases = [
        'plain,simple,fields',
        '"quoted field","another, field",regular',
        '"field with ""escaped"" quotes",normal,"comma, here"',
        'empty,,field',
    ]

    print("Starting CSV Parser Demo...")
    print("-" * 30)

    for i, test_str in enumerate(test_cases, 1):
        parsed = parser.parse_line(test_str)
        print(f"Test Case {i}:")
        print(f"  Input : {test_str}")
        print(f"  Output: {parsed}")
        print("-" * 30)

if __name__ == '__main__':
    run_demo()
