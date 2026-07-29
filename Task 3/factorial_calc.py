def factorial(num):
  result = 1
  for i in range(2, num+1):
    result *= i
  return result

num = 13
print(f'{num}!: {factorial(num)}')
