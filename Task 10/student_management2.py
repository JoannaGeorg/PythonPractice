from student import Student
from mangement import StudentManagement


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
      print(student)
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
  
