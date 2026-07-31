class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def printStudent(self):
    print(f'Name: {self.name} Marks: {self.marks}')


class StudentManagement:
  def __init__(self):
    self.students = []

  def addStudent(self, name, marks):
    if name in [student.name for student in self.students]:
      print("Student is already in the system")
      return
    self.students.append(Student(name, marks))

  def viewStudents(self):
    print("\nClass Students:")
    for student in self.students:
      student.printStudent()

  def searchStudent(self, name):
    for student in self.students:
      if name == student.name:
        return student
    print("Student not in the system")

  def getAverage(self):
    total = 0
    for student in self.students:
      total += student.marks
    return total / len(self.students)

  def calculateGrade(self, marks):
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

  def getGrade(self, name):
    student = self.searchStudent(name)
    if student:
      grade = self.calculateGrade(student.marks)
      return grade
    return None

  def updateStudent(self, name):
    student = self.searchStudent(name)
    if not student:
      return
    new_name = input("Enter the updated name of the student, or skip: ")
    if new_name and new_name != 'skip':
      student.name = new_name
    new_marks = input("Enter the new marks, or skip: ")
    if new_marks and new_marks != 'skip':
      student.marks = int(new_marks)
    student.printStudent()

  def deleteStudent(self, name):
    student = self.searchStudent(name)
    if not student:
      return
    self.students.remove(student)
    print("Removed")



class_a = StudentManagement()
print("STUDENT MANAGEMENT PROGRAM")

cont = True
while cont:
  input("\nPress Enter to Continue.")
  op = input("\n1. Add a Student\n2. Print the list of Students\n3. Search for a Student\n4. Get the Average Marks\n5. Get Grade of a Student\n6. Update Student Information\n7. Delete a Student\n\nE to Exit\n\nPlease Enter the index of the function to perform: ")
  if op == '1':
    name = input("\nEnter the name of the student: ")
    marks = float(input("Enter the marks of the student: "))
    class_a.addStudent(name, marks)
  elif op == '2':
    class_a.viewStudents()
  elif op == '3':
    name = input("\nEnter the name of the student: ")
    student = class_a.searchStudent(name)
    if student:
      student.printStudent()
  elif op == '4':
    print(f"\nThe average of the class = {class_a.getAverage()}")
  elif op == '5':
    name = input("\nEnter the name of the student: ")
    grade = class_a.getGrade(name)
    if grade:
      print(f"{name} => Grade: {grade}")
  elif op == '6':
    name = input("\nEnter the name of the student: ")
    class_a.updateStudent(name)
  elif op == '7':
    name = input("\nEnter the name of the student: ")
    class_a.deleteStudent(name)
  elif op == 'E' or op == 'e':
    print("Goodbye.")
    cont = False
  else:
    print('\nInvalid Input\n')
  
