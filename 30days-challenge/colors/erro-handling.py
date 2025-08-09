import sys

class StyledOutput:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    @staticmethod
    def error(message):
        print(f"{StyledOutput.RED}{StyledOutput.BOLD}ERROR: {message}{StyledOutput.RESET}", 
              file=sys.stderr)
    
    @staticmethod
    def warning(message):
        print(f"{StyledOutput.YELLOW}WARNING: {message}{StyledOutput.RESET}", 
              file=sys.stderr)

def get_double():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            StyledOutput.error("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            StyledOutput.error("Operation cancelled by user")
            sys.exit(1)

# Usage
try:
    number = get_double()
    print(f"You entered: {number}")
except Exception as e:
    StyledOutput.error(f"Unexpected error: {e}")
