import re
text1 = re.match('newton','is conducting the class of natural language processing',flags=re.I)
text2 = re.match('newton','newton is conducting the class of nlp',flags=re.I)
print(text1)
print(text2.group())
