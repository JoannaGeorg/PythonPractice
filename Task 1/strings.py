#string
s = 'This is a string.'

#Splitting the string at whitespace
print(s.split())

#Splitting at i
print(s.split('i'))

#indexing
print(s[3])

#concatenation
print(s + ' This was added to it!')

#slicing
print(s[:5])
print(s[5:10])
#reversing the string using slicing
print(s[::-1])

#length of string
print(len(s))