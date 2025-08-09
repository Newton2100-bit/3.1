import sys

# ANSI color codes
RED = '\033[91m'
RESET = '\033[0m'

def eprint_red(*args, **kwargs):
    print(f"{RED}", end="", file=sys.stderr)
    print(*args, file=sys.stderr, **kwargs)
    print(f"{RESET}", end="", file=sys.stderr)

# Usage
eprint_red("This is a red error message")
