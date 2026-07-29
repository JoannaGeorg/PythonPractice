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
        student.printStudent()
        return
    print("Student not in the system")

  def getAverage(self):
    total = 0
    for student in self.students:
      total += student.marks
    return total / len(self.students)


class_a = StudentManagement()
print("STUDENT MANAGEMENT PROGRAM")

cont = True
while cont:
  op = input("\n1. Add a Student\n2. Print the list of Students\n3. Search for a Student\n4. Get the Average Marks\nPlease Enter the index of the function to perform: ")
  if op == '1':
    name = input("\nEnter the name of the student: ")
    marks = float(input("Enter the marks of the student: "))
    class_a.addStudent(name, marks)
  elif op == '2':
    class_a.viewStudents()
  elif op == '3':
    name = input("\nEnter the name of the student: ")
    class_a.searchStudent(name)
  elif op == '4':
    print(f"\nThe average of the class = {class_a.getAverage()}")
  else:
    print('\nInvalid Input\n')
  if input("\nWould you like to continue? Type 'n' to exit: ") == 'n':
    print("Goodbye.")
    cont = False