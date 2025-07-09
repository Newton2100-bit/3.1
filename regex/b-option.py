import re

text = "The cat cathes cats in the catalog"

# WITHOUT \b - matches partial words
pattern1 = r"cat"
matches1 = re.findall(pattern1, text)
print(matches1)  # ['cat', 'cat', 'cat', 'cat'] - matches inside words

# WITH \b - matches whole words only
pattern2 = r"\bcat\b"
matches2 = re.findall(pattern2, text)
print(matches2)  # ['cat'] - only matches the standalone word
