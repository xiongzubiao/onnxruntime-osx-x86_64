"""
CSV Parser Repro Script (verify_027.py)
This module provides a simple CSV parser that correctly handles quoted fields,
including cases where the delimiter or quote character is embedded within a field.
"""

class CSVParser:
    """
    A parser for CSV format that handles quoted fields and basic escapes.
    """
    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser.
        :param delimiter: The character used to separate fields (default: ',').
        :param quotechar: The character used to quote fields (default: '"').
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse(self, text):
        """
        Parses a multi-line CSV string into a list of lists.
        """
        lines = text.strip().splitlines()
        return [self.parse_line(line) for line in lines]

    def parse_line(self, line):
        """
        Parses a single line of CSV text.
        """
        fields = []
        current_field = []
        in_quotes = False
        i = 0
        while i < len(line):
            char = line[i]
            if char == self.quotechar:
                # Handle escaped quotes (e.g., "")
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

def run_demo():
    """
    Demonstrates the CSVParser with various edge cases.
    """
    parser = CSVParser()
    csv_data = (
        'Name,Occupation,"Location, City"\n'
        'John Doe,Engineer,"New York, NY"\n'
        '"Jane ""The Brain"" Smith",Scientist,"San Francisco, CA"'
    )
    
    print("Input CSV Data:")
    print("---------------")
    print(csv_data)
    print("\nParsed Rows:")
    print("------------")
    rows = parser.parse(csv_data)
    for row in rows:
        print(row)

if __name__ == '__main__':
    run_demo()
