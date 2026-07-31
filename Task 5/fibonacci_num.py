def fibonacciNumber(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fibonacciNumber(num - 1) + fibonacciNumber(num - 2)


print(fibonacciNumber(0))
print(fibonacciNumber(1))
print(fibonacciNumber(5))
print(fibonacciNumber(10))

