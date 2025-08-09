import sys

class ColoredError:
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    @staticmethod
    def error(message):
        print(f"{ColoredError.RED}{ColoredError.BOLD}ERROR: {message}{ColoredError.RESET}", 
              file=sys.stderr)
    
    @staticmethod
    def warning(message):
        print(f"\033[93m{ColoredError.BOLD}WARNING: {message}{ColoredError.RESET}", 
              file=sys.stderr)

# Usage
ColoredError.error("Something went wrong!")
ColoredError.warning("This is a warning!")
