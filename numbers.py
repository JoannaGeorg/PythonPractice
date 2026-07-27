# Adding two numbers
while True:
  num1 = float(input("\nEnter a number: "))
  num2 = float(input("Enter another number: "))

  print("\n{} + {} = {}".format(num1, num2, num1+num2))

  if input("Go again? (y/n): ") == 'n':
    break