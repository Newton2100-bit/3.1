import sys
import time

RED = '\033[36m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Color persists across newlines and function calls
def demonstrate_persistence():
    print(f"{RED}", file=sys.stderr)
    print("Red line 1", file=sys.stderr)
    print("Red line 2", file=sys.stderr)
    time.sleep(1)
    print("Still cyan after sleep", file=sys.stderr)
    print('The time is',  f"{RESET}",f"{GREEN}", {time.ctime(time.time())}, '.', f"{RESET}", file = sys.stderr) 
    print(f'This is normal tesxt good bye👋.')

demonstrate_persistence()
