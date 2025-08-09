import sys
import time

RED = '\033[91m'      # ✅ Fixed: correct escape sequence
GREEN = '\033[92m'
RESET = '\033[0m'

# Color persists across newlines and function calls
def demonstrate_persistence():
    print(f"{RED}", end="", file=sys.stderr)
    print("Red line 1", file=sys.stderr)
    print("Red line 2", file=sys.stderr)
    time.sleep(1)
    print("Still red after sleep", file=sys.stderr)  # ✅ Fixed: consistent color description
    print(f"{RESET}", end="", file=sys.stderr)       # ✅ Fixed: reset after red text
    print()  # Empty line for spacing
    
    # ✅ Fixed: proper f-string formatting and removed curly braces around time.ctime()
    print(f'The time is {GREEN}{time.ctime(time.time())}.{RESET}', file=sys.stderr)

demonstrate_persistence()

# Additional demonstration of the fixes
print("\n=== Additional Examples ===")
print(f"{RED}This is red{RESET}", file=sys.stderr)
print(f"{GREEN}This is green{RESET}", file=sys.stderr)
print("This is normal", file=sys.stderr)
