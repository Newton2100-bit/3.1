import sys

RED = '\033[91m'
RESET = '\033[0m'

# Color persists across newlines
print(f"{RED}Line 1", file=sys.stderr)
print("Line 2 (still red)", file=sys.stderr)  
print("Line 3 (still red)", f"{RESET}", file=sys.stderr)
print(f"{'\033[36m'}Line 4 (back to normal) probably cyan", file=sys.stderr)
