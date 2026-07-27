#creating
my_dict = {'key': 'value', 'mamamoo': 'moomoo'}
print(my_dict)

#calling a dict by its key
print(f'using key: {my_dict["key"]}\nusing mamamoo: {my_dict["mamamoo"]}')

#flexible datatypes
my_dict = {
  'num': 123,
  'list': [12, 32, 45],
  'str_list': ['shane', 'illya']
}
print(f"key str_list: {my_dict['str_list']}")
print(f"fist element of str_list: {my_dict['str_list'][0]}")

#Create keys by assignment
my_dict['water'] = 'H2O'
print(my_dict)

#nesting dictionaries
print('\n nesting dictionaries')
nest_dict = {
  'key1': {'nestkey': my_dict}
}
print(nest_dict)
print(f'\nusing key1: {nest_dict["key1"]}\nwith nestkey: {nest_dict["key1"]["nestkey"]}')

#Dictionary methods
print("\nMethods:")

#return all keys
print(my_dict.keys())

#return all values
print(my_dict.values())

#Tuples
print("\n\nTUPLES")
#contructing
tup = (1, 2, 3)
print(tup)

#check length
print(f'length: {len(tup)}')

#indexing
print(f'Index 1: {tup[1]}')

#slicing just like in lists
print(f"sliced 1 onwards: {tup[1:]}")

#Tuple methods
print('\nTuple methods')

#find the idex of a value
print(f"index of value 3: {tup.index(3)}")

#Count the number of times a value has appeared
print(f'Count of 2: {tup.count(2)}')

#Tuples are immutable - they cannot be changed through assigning nor can they grow
#used only when imutability is required.