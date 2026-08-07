def checkMarksInput():
  while True:
    try:
      marks = float(input("Enter Marks between 0 and 100: "))
      if marks >= 0 and marks <= 100:
        return marks
      else:
        input('\nInvalid Marks\n')
    except ValueError:
      input("\nPlease Enter a valid number for the Marks.\n")
      
