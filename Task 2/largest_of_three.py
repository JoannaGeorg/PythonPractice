def largestOfThree(a, b, c):
  largest = a
  if largest < b:
    largest = b
  if largest < c:
    largest = c
  print(f'{largest} is the largest of [{a}, {b}, {c}]')

largestOfThree(3, 6, 8)
largestOfThree(54, 45, 32)
largestOfThree(4, 7, 2)
