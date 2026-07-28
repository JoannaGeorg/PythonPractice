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

  return grade

def listGradeCalculator(mark_list):
  total = 0
  avg = None
  for marks in mark_list:
    total += marks
    grade = gradeCalculator(marks)
    msg = None
    if grade == 'F':
      msg = 'FAIL'
    else:
      msg = 'PASS'
    print(f'{marks}: grade {grade} => {msg}!')
  avg = total / (len(mark_list))
  print(f'\nTotal: {total}\nAverage marks: {avg}')


student_marks = [23, 45.5, 67, 89, 86, 69, 100, 97, 92, 74, 61]
listGradeCalculator(mark_list=student_marks)