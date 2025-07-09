import re

# Using different methods
text = "Contact: john@email.com or jane@email.com"
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Different approaches
emails1 = re.findall(pattern, text)
print(emails1)
emails2 = [m.group() for m in re.finditer(pattern, text)]
compiled = re.compile(pattern)
emails3 = compiled.findall(text)
