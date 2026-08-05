import random

def harmonicSeries(num):
  if num <= 1:
    return 1
  return (1 / num) + harmonicSeries(num-1)

num = random.choice(range(0, 20))
print(f'The harmonic series of {num} is {harmonicSeries(num)}')
