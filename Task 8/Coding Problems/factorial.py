import random

def factorial(num):
  if num == 0 or num == 1:
    return 1
  return num * factorial(num-1)

num = random.choice(range(0, 30))
print(f'{num}! = {factorial(num)}')
