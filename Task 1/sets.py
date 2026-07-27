#an unordered collection of unique elements

#construction
x = set()
print(x)

#add to sets using add() method
x.add(1)
print(x)
x.add(2)
print(x)

#will not add the same values
x.add(2)
print(f"tryed to add 2 again: {x}")

#creating a list will reoccurring values and printing it cast as a set
my_list = [2, 4, 5, 2, 4, 6, 3, 4, 5, 7, 9, 4]
print(set(my_list))

#Booleans
print('\nBOOLEANS\n')

#setting variable true or false
a = True
print(type(a))

#Using comparision for boolenas
print(23 < 5)

#Using None as a placeholder when you dont want to reassign just yet
b = None
print(b)