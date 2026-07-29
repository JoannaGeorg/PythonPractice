def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def calculator():
  operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
  }

  run_calc = True
  result = None
  while run_calc:
    if not result:
      result = float(input("Enter the first number: "))
    op = input("Enter the operator: ")
    num2 = float(input("Enter the next number: "))
    result = operation[op](result, num2)
    print(f'Current Result = {result}')
    if input('Done? (y/n) :') != 'n':
      run_calc = False

  return result

print("CALCULATOR\n")
result = calculator()
print(f"\nResult = {result}")
