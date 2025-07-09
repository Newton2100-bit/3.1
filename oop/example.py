print("This runs ALWAYS (import or direct run)")

def helper():
    print("Function defined (runs on definition, not call)")

if __name__ == "__main__":
    print("This runs ONLY when executed directly")
    helper()
else:
    print("This runs ONLY when imported")
