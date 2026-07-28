def evenOddChecker(num):
  msg = ''
  if num % 2 == 0:
    msg = 'Even'
  else:
    msg = 'Odd'
  print(f'{num} is {msg}.')

evenOddChecker(234154)
evenOddChecker(1005)