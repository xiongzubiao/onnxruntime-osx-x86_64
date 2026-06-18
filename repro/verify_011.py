"""
A simple CSV parser module that handles quoted fields.
This module provides a basic implementation for parsing CSV lines according to common standards,
specifically focusing on fields that may contain commas or other characters enclosed in double quotes.
"""

class SimpleCSVParser:
    """
    A class to parse CSV data, handling quoted fields.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with specific delimiter and quote character.

        Args:
            delimiter (str): The character used to separate fields. Defaults to ','.
            quotechar (str): The character used to enclose fields containing the delimiter. Defaults to '"'.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parses a single line of CSV text.

        Args:
            line (str): A single line from a CSV file.

        Returns:
            list: A list of strings representing the parsed fields.
        """
        fields = []
        current_field = []
        in_quotes = False
        
        # Strip trailing newline characters
        line = line.rstrip('\r\n')
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if char == self.quotechar:
                if in_quotes and i + 1 < len(line) and line[i+1] == self.quotechar:
                    # Handle escaped quotes (e.g., "")
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    # Toggle quote mode
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                # Field separator found outside of quotes
                fields.append("".join(current_field))
                current_field = []
            else:
                # Regular character
                current_field.append(char)
            i += 1
            
        fields.append("".join(current_field))
        return fields

def parse_csv_string(csv_data):
    """
    Parses a multi-line CSV string.

    Args:
        csv_data (str): The CSV data as a string.

    Returns:
        list of list: A list of rows, where each row is a list of fields.
    """
    parser = SimpleCSVParser()
    results = []
    # Use splitlines to handle different newline formats
    for line in csv_data.strip().splitlines():
        if line.strip():
            results.append(parser.parse_line(line))
    return results

if __name__ == '__main__':
    # Demonstration data with quoted fields containing commas
    demo_data = """Name,Occupation,Location
"Smith, John",Engineer,"New York, NY"
"Doe, Jane",Scientist,"San Francisco, CA"
"Brown, Bob", "Teacher", London
"""
    print("Parsing demo CSV data...")
    parsed_rows = parse_csv_string(demo_data)
    
    for row in parsed_rows:
        print(f"Row: {row}")

    # Specific check for quoted content
    test_line = '"Result: OK",200,"Success, move on"'
    parser = SimpleCSVParser()
    parsed_test = parser.parse_line(test_line)
    print(f"\\nTest line: {test_line}")
    print(f"Parsed: {parsed_test}")
