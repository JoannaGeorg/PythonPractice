def numberGuess():
  input('\nThink of a number between 1 and 100\n')
  start = 0
  end = 100
  found = False
  while not found:
    if start == end:
      print(f'Number is {start}')
      found = True
    num = int((start + end) / 2)
    res = input(f'\nIs the number {num}? (y/n) ')
    if res == 'y':
      print("The number was found")
      found = True
    else:
      is_less = input('\nIs the number less? (y/n) ')
      if is_less == 'y':
        end = num
      else:
        start = num

numberGuess()
