"""
A complete, runnable Python program implementing a CSV parser that handles quoted fields.
"""

class CSVParser:
    """
    A parser for CSV format strings that correctly handles delimiters inside quotes.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the CSV parser.

        Args:
            delimiter (str): The character used to separate fields.
            quotechar (str): The character used to enclose fields containing the delimiter.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parse a single line of CSV.

        Args:
            line (str): A string representing a single line of CSV.

        Returns:
            list: A list of strings representing the parsed fields.
        """
        fields = []
        current_field = []
        in_quotes = False
        i = 0
        
        # Remove trailing newline characters
        line = line.rstrip('\r\n')
        
        while i < len(line):
            char = line[i]
            
            if char == self.quotechar:
                # Handle escaped quotes (double quotechar)
                if in_quotes and i + 1 < len(line) and line[i+1] == self.quotechar:
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    # Toggle quote state
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                # End of a field
                fields.append("".join(current_field))
                current_field = []
            else:
                # Regular character
                current_field.append(char)
            i += 1
            
        # Append the last field
        fields.append("".join(current_field))
        return fields

def run_demo():
    """
    Demonstrates the CSVParser with various input cases.
    """
    parser = CSVParser()
    
    test_cases = [
        'Name,Age,Location',
        'John Doe,30,"New York, NY"',
        '"Smith, Jane",25,London',
        'Bob "The Builder",45,"Construction Site"',
        'Alice,22,"""Wonderland"""'
    ]
    
    print("CSV Parser Demonstration\n" + "="*25)
    for i, test in enumerate(test_cases, 1):
        parsed = parser.parse_line(test)
        print(f"Test {i}: {test}")
        print(f"Parsed: {parsed}\n")

if __name__ == "__main__":
    run_demo()
