def gcdOfTwo(a, b):
  len = None
  if a < b:
    len = a
  else:
    len = b

  for i in range(2, len+1):
    if a % i == 0 and b % i == 0:
      return i

  return 0

x = gcdOfTwo(21, 56)
if x:
  print(x)
else:
  print("No GCD found")
