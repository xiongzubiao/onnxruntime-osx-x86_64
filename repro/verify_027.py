"""
A simple CSV parser that handles quoted fields.

This module provides a parser that can split a CSV line into its constituent fields,
correctly handling cases where commas are enclosed within double quotes.
"""

import io

class SimpleCSVParser:
    """
    A parser for CSV data that handles quoted fields.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with a delimiter and quote character.

        Args:
            delimiter (str): The character used to separate fields.
            quotechar (str): The character used to enclose fields containing the delimiter.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parse a single line of CSV data.

        Args:
            line (str): The CSV line to parse.

        Returns:
            list: A list of fields extracted from the line.
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
                # Handle escaped quotes (double quotes)
                if in_quotes and i + 1 < len(line) and line[i+1] == self.quotechar:
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                fields.append(''.join(current_field))
                current_field = []
            else:
                current_field.append(char)
            i += 1
            
        fields.append(''.join(current_field))
        return fields

    def parse_stream(self, stream):
        """
        Parse an iterable stream of CSV lines.

        Args:
            stream (iterable): An iterable (like a file object) yielding CSV lines.

        Yields:
            list: Parsed fields for each line.
        """
        for line in stream:
            yield self.parse_line(line)

def main():
    """
    Demonstration of the SimpleCSVParser.
    """
    csv_data = [
        'Name,Age,Location',
        'John Doe,30,"New York, NY"',
        '"Smith, Jane",25,Los Angeles',
        'Bob "The Builder",40,London'
    ]
    
    parser = SimpleCSVParser()
    
    print("Parsing CSV strings:")
    for line in csv_data:
        parsed = parser.parse_line(line)
        print(f"Original: {line}")
        print(f"Parsed:   {parsed}")
        print("-" * 20)

    # Example with a file-like object
    print("\nParsing from a stream:")
    stream = io.StringIO("\\n".join(csv_data))
    for fields in parser.parse_stream(stream):
        print(fields)

if __name__ == "__main__":
    main()
