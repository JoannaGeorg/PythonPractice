from mangement import StudentManagement
from error_handling import checkMarksInput

classA = StudentManagement()
print("STUDENT MANAGEMENT PROGRAM")

cont = True
while cont:
  input("\nPress Enter to Continue.")
  option = input("\n1. Add a Student\n2. Print the list of Students\n3. Search for a Student\n4. Get the Average Marks\n5. Get Grade of a Student\n6. Update Student Information\n7. Delete a Student\n\nE to Exit\n\nPlease Enter the index of the function to perform: ")
  if option == '1':
    name = input("\nEnter the name of the student: ")
    marks = checkMarksInput()
    classA.addStudent(name, marks)
  elif option == '2':
    classA.viewStudents()
  elif option == '3':
    name = input("\nEnter the name of the student: ")
    student = classA.searchStudent(name)
    if student:
      print(student)
  elif option == '4':
    print(f"\nThe average of the class = {classA.getAverage()}")
  elif option == '5':
    name = input("\nEnter the name of the student: ")
    grade = classA.getGrade(name)
    if grade:
      print(f"{name} => Grade: {grade}")
  elif option == '6':
    name = input("\nEnter the name of the student: ")
    classA.updateStudent(name)
  elif option == '7':
    name = input("\nEnter the name of the student: ")
    classA.deleteStudent(name)
  elif option == 'E' or option == 'e':
    print("Goodbye.")
    cont = False
  else:
    print('\nInvalid Input\n')
  
