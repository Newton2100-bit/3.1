# # web browser import import webbrowser webbrowser.open('www.youtube.com') Multiline , doc strings and using the \ option # negative -1 slicing print(0 == -0) # Reversing in python data = [23, 45, 67] print(data[::-1]) data.reverse() print(data) # The in operator # The find method in strings that are iterables print('Youtube'.find('You')) print('Youtube'.find('no')) if 'no' in 'Youtube': print('we have the no in the command') else: print("not found kindly.") print('no' in 'Youtube.') # The id function data = {'Newton' : 21} print(id(data)) # working of assignmens of objects data = 23 data2 = data print(f"Is data equal to data2 : {id(data) == id(data2)} ") data2 = 100
# print(f"Is data equal to data2 : {id(data) == id(data2)} ")
#
# print(f"data = {id(data)} data2 = {id(data2)}")
# print(f"data = {data} data2 = {data2}")

# primitive = 23
# print(id(primitive))
# primitive = 100
# print(id(primitive))
# data = [3, 2, 1]
# print(id(data))
# data.reverse()
#

# # The copy method in python
# languages = ['c++', 'go', 'python', 'java']
# learning1 = languages.copy()
# print('learning1', id(learning1))
# learning2 = languages[::]
# print('learning2',id(learning2))
# learning3 = languages
# print('learning3',id(learning3))
# print('laguages',id(languages))


# tech = ['c++', 'go', 'python', ['html','css','pics']]
# learning = tech.copy()
# print('These performs a shallow cop by the fact that w ehave the nested part being aliased.')
# print(learning) 
# value = 'yes' if id(learning[-1][-1]) == id(tech[-1][-1]) else 'No'
# print(f'Is it really true {value}.')

# # Sample Solutions.
# from copy import deepcopy
# tech = ['c++', 'go', 'python',['html', 'css', 'pics']]
# learning = deepcopy(tech)
# print(tech)
# value = 'yes' if id(learning[-1][-1]) == id(tech[-1][-1]) else 'No'
# print('These performs a shallow cop by the fact that w ehave the nested part being aliased.')
# print(f'Is it really true {value}.')

# # Not operator
# name = 'Newton'
# age = 25
# favourite_lang = ['c++', 'python']
# msg = name + str(age) + favourite_lang[0] + favourite_lang[1]# + value for value in favourite_lang
# print(msg)
*x, y = 23, 45, 67
print(tuple(x))
print(y)
