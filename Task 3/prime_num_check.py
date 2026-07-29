def primeNumberCheck(num):
  """
  This function checks if the number is a prime number.
  Returns: bool
  """
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

print(primeNumberCheck(97))