import sys
from colorama import Fore, Style, init

# Initialize colorama (especially important on Windows)
init()

def red_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}", file=sys.stderr)

# Usage
red_error("This is a red error message")
