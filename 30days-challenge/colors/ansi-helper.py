import sys

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def error_print(message):
    print(f"{Colors.RED}{message}{Colors.RESET}", file=sys.stderr)

def warning_print(message):
    print(f"{Colors.YELLOW}{message}{Colors.RESET}", file=sys.stderr)

# Usage
error_print("This is a red error!")
warning_print("This is a yellow warning!")
