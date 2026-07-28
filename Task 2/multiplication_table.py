def multiplicationTable(num):
  print(f"\nThe multiplication table of {num}:")
  for x in range(1, 11):
    print(f'\t{num} x {x} = {num * x}')

multiplicationTable(33)
