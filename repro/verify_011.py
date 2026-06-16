"""
A simple CSV parser module that handles quoted fields.

This module provides functionality to parse CSV strings and files,
including support for fields that contain commas or escaped quotes, 
provided they are enclosed in double quotes.
"""

import io

class CSVParser:
    """
    A class to parse CSV data.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with a delimiter and quote character.

        Args:
            delimiter (str): The character separating fields.
            quotechar (str): The character used for quoting fields.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parses a single line of CSV text.

        Args:
            line (str): A single line of CSV.

        Returns:
            list: A list of field strings.
        """
        fields = []
        current_field = []
        in_quotes = False
        
        # Strip newline characters from the end
        line = line.rstrip('\r\n')
        
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
            else:
                current_field.append(char)
            i += 1
            
        fields.append("".join(current_field))
        return fields

    def parse(self, data):
        """
        Parses multi-line CSV data.

        Args:
            data (str): The full CSV content.

        Returns:
            list: A list of lists representing the rows.
        """
        rows = []
        f = io.StringIO(data)
        for line in f:
            if line.strip():
                rows.append(self.parse_line(line))
        return rows

def run_demo():
    """
    Demonstrates the CSVParser with various test cases.
    """
    csv_data = """Name,Age,City
"John Doe",30,"New York, NY"
"Jane ""Expert"" Smith",25,San Francisco
Simple,Field,Value
"""
    print("Parsing CSV Data:")
    print("-" * 20)
    print(csv_data)
    print("-" * 20)
    
    parser = CSVParser()
    rows = parser.parse(csv_data)
    
    for i, row in enumerate(rows):
        print(f"Row {i}: {row}")

if __name__ == "__main__":
    run_demo()
