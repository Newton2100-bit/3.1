import re
text3 = 'natural learning processing'
text5 = re.sub(r'\bcat\b', 'dog', 'cat in the cathedral')  # Replaces whole word 'cat'
text4 = re.sub(r'learning','language',text3)
print(text4,'\n',text5)

