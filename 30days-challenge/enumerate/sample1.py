scores = [90, 34, 56, 67, 78, 32, 32]

for i in enumerate(scores, 5):
    print(i)
print(f"\033[4;36mTHE STUDENTS SCORED\033[0m")
for i,item in enumerate(scores,5):
    print(f'{i} : {item}')
