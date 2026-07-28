def positiveNegativeZeroChecker(num):
  msg = ''
  if num > 0:
    msg = 'Positive'
  elif num < 0:
    msg = 'Negative'
  else:
    msg = 'Zero'
  print(f'{num} is {msg}')

positiveNegativeZeroChecker(23)
positiveNegativeZeroChecker(-23)
positiveNegativeZeroChecker(0)
