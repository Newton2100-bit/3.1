# Check if any item in list1 exists in list2
list1 = [1, 2, 3]
list2 = [3, 4, 5]

found = False
for item in list1:
    if item in list2:
        found = True
        break

# Or more pythonically:
found = any(item in list2 for item in list1)
