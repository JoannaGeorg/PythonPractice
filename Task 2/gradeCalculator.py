def gradeCalculator(marks):
  grade = None
  if marks >= 90:
    grade = 'A'
  elif marks >= 80:
    grade = 'B'
  elif marks >= 70:
    grade = 'C'
  elif marks >= 60:
    grade = 'D'
  elif marks >= 50:
    grade = 'E'
  else:
    grade = 'F'

  print(f"Marks: {marks} => Grade: {grade}")

gradeCalculator(93)
gradeCalculator(68)
gradeCalculator(43)
gradeCalculator(85)
