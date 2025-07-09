import re
text = re.search('Newton','This class of natural language processing is being conducted by dr.newton',flags=re.I)
print(text)
print(text.group())
