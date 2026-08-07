class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def __repr__(self):
    return f'Name: {self.name} Marks: {self.marks}'

