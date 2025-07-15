import random

random.seed(42)
print('_____USING A RANDOM SEED VALUE _______')
data = [i for i in range(2,100) if i % 3 == 0]
for i in data:
    print(f'Our random data is {random.randint(1,10)}')

print('____END OF OUR SEEDED PROGRAM_________')   


