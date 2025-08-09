# In your renamed file (not rich.py)
from rich.console import Console
import sys

console = Console(stderr=True)

def rich_error(message):
    console.print(f"[bold red]ERROR: {message}[/bold red]")

# Usage
rich_error("This is a styled error message")
