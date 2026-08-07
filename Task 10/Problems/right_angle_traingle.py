def createTriangle(length):
  if length <= 0:
    print("Invalid Length provided :(")
  elif length == 1:
    print("*")
  else:
    triangle_line = "*"
    for i in range(1, length+1):
      print(triangle_line)
      triangle_line += " *"

createTriangle(10)
