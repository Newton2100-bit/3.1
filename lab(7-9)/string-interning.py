a = 'hello world'
b = 'hello world'

print('Is a the same as b',a is b)
x = 'hel' + 'lo'
y = 'hel' + 'lo'

print('Having runtime created strings',x is y)

c = 'newton'
d = c
d= 'mwaura newton is my name'
print(c)

data = {'name':'Newton','age':21,'course':'cs'}
keys = data.keys()
print('Old keys',keys)

data.update({'happy':'yes','year':'third'})
print(keys)



