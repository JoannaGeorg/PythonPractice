#initializing an array
arr = [1, 2, 3, 4, 5, 6, 7]

#traversal
print("arr:")
for num in arr:
  print(num)

#Insertion
arr.insert(3, 'insert')
print(arr)

#Deletion
#using index
arr.pop(3)
print(arr)
#using element
arr.remove(4)
print(arr)