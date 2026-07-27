#assigning a list
my_list = [1, 2, 3]

#get the length of the string
print(f"List length: {len(my_list)}")

#indexing
print(f"Element at index 1: {my_list[1]}")

#slicing
print(my_list[1:])

#concatenating a list without editing the lists
print(my_list + [5, 6, 7])

#Ressign to use the '+' to permenantly add the elements of another list
my_list = my_list + [5, 6, 7]
print(my_list)

#double the list
print(my_list * 2)

#BASIC LIST METHODS
print("\nTesting Basic list methods.")

#append
my_list.append(8)
print(my_list)

#pop at idex
print(my_list.pop(3))
print(my_list)

#reversing a list - permanently
my_list.reverse()
print(my_list)

#sort - alphabetically or for numbers ascending order
my_list.sort()
print(my_list)

print("\nNested lists.")
#nested lists
nest_list = [my_list, [3, 5, 6, 7, 8, 9], [12, 3, 4, 5, 2, 6]]
print(nest_list)

#first item of nested list
print(nest_list[1])

#3rd item of 2nd list
print(nest_list[1][2])

#List comprehension
print("\nList Comprehension")
first_col = [row[0] for row in nest_list]
print(f"The first column of the nested list: {first_col}")