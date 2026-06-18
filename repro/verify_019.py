"""
repro/verify_019.py

A complete, runnable Python program implementing a CSV parser that handles quoted fields.
This script demonstrates basic CSV parsing logic without relying on the built-in 'csv' module.
"""

class CSVParser:
    """
    A class to parse CSV data from a string or file-like object.
    Supports basic quoted field handling.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the CSV parser with custom delimiter and quote character.

        Args:
            delimiter (str): The character separating fields.
            quotechar (str): The character used to enclose fields containing delimiters.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parses a single line of CSV text.

        Args:
            line (str): A single CSV-formatted line.

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
                # Handle double quotes as an escaped quote
                if in_quotes and i + 1 < len(line) and line[i+1] == self.quotechar:
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                fields.append("".join(current_field))
                current_field = []
            elif char in ('\r', '\n') and not in_quotes:
                # End of record
                break
            else:
                current_field.append(char)
            i += 1
            
        fields.append("".join(current_field))
        return fields

    def parse_text(self, text):
        """
        Parses multi-line CSV text.

        Args:
            text (str): The CSV text to parse.

        Returns:
            list: A list of lists, where each inner list represents a row.
        """
        rows = []
        for line in text.strip().splitlines():
            if line:
                rows.append(self.parse_line(line))
        return rows

def run_demo():
    """
    Runs a demonstration of the CSVParser with quoted fields and delimiters.
    """
    csv_data = """Name,Occupation,"Location, Country"
"Doe, John",Engineer,"New York, USA"
Jane Smith,"Data Scientist","London, ""UK"""
"Bob ""The Builder""",Construction,Unknown
"""
    
    print("--- CSV Data ---")
    print(csv_data)
    
    parser = CSVParser()
    parsed_rows = parser.parse_text(csv_data)
    
    print("\n--- Parsed Results ---")
    for row in parsed_rows:
        print(row)

if __name__ == '__main__':
    run_demo()
