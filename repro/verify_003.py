"""
A simple CSV parser module that handles quoted fields.
"""

import io

class CSVParser:
    """
    A parser for comma-separated values (CSV) that supports quoted fields.
    """

    def __init__(self, delimiter=',', quotechar='"'):
        """
        Initialize the parser with specific delimiter and quote character.
        """
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line):
        """
        Parse a single line of CSV text.
        
        Args:
            line (str): The CSV line to parse.
            
        Returns:
            list: A list of fields.
        """
        result = []
        field = []
        in_quotes = False
        i = 0
        while i < len(line):
            char = line[i]
            if char == self.quotechar:
                if in_quotes and i + 1 < len(line) and line[i+1] == self.quotechar:
                    # Escaped quote
                    field.append(self.quotechar)
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                result.append("".join(field).strip())
                field = []
            elif char in ('\n', '\r') and not in_quotes:
                break
            else:
                field.append(char)
            i += 1
        result.append("".join(field).strip())
        return result

def parse_csv(data):
    """
    Parse a multiline CSV string into a list of lists.
    """
    parser = CSVParser()
    lines = data.strip().splitlines()
    return [parser.parse_line(line) for line in lines]

if __name__ == "__main__":
    # Demonstration
    csv_data = 'name,age,city\n"Doe, John",30,"New York"\n"Jane ""Queen"" Smith",25,London'
    print("Parsing CSV data:")
    print(csv_data)
    print("\nResult:")
    parsed = parse_csv(csv_data)
    for row in parsed:
        print(row)
