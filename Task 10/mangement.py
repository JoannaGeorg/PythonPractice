from student import Student

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
      print(student)

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
