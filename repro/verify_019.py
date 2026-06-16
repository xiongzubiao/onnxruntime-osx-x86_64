"""
A simple CSV parser that handles quoted fields.
This module provides functionality to parse a CSV string into a list of lists.
"""

class CSVParser:
    """
    A class to parse CSV data with support for quoted fields.
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

    def parse(self, text):
        """
        Parse a CSV string into a list of records.

        Args:
            text (str): The CSV string to parse.

        Returns:
            list: A list of lists, where each inner list represents a row.
        """
        result = []
        row = []
        current_field = []
        in_quotes = False
        
        i = 0
        while i < len(text):
            char = text[i]
            
            if char == self.quotechar:
                if in_quotes and i + 1 < len(text) and text[i+1] == self.quotechar:
                    # Handle escaped quotes (e.g., "")
                    current_field.append(self.quotechar)
                    i += 1
                else:
                    # Toggle quote state
                    in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                # End of field
                row.append("".join(current_field))
                current_field = []
            elif char == '\n' and not in_quotes:
                # End of row
                row.append("".join(current_field))
                result.append(row)
                row = []
                current_field = []
            elif char == '\r' and not in_quotes:
                # Skip carriage returns
                pass
            else:
                current_field.append(char)
            i += 1
            
        # Append last field/row if text doesn't end with a newline
        if current_field or row:
            row.append("".join(current_field))
            result.append(row)
            
        return result

def parse_csv(data):
    """
    Convenience function to parse CSV data using default settings.

    Args:
        data (str): The CSV string to parse.

    Returns:
        list: The parsed CSV data.
    """
    parser = CSVParser()
    return parser.parse(data)

if __name__ == "__main__":
    # Demonstration of the CSV parser
    csv_input = (
        'name,age,location\n'
        '"Doe, John",30,"New York, NY"\n'
        'Jane Smith,25,"San Francisco"\n'
        '"Bob ""The Builder"" Smith",40,London'
    )
    
    print("--- Original CSV Input ---")
    print(csv_input)
    print("\n--- Parsed Output ---")
    
    records = parse_csv(csv_input)
    for record in records:
        print(record)
