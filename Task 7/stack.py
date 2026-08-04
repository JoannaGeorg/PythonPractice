class Stack:
  def __init__(self):
    self.stack = []

  #push
  def push(self, val):
    self.stack.append(val)

  #pop
  def pop(self):
    self.stack.pop()

  #peek
  def peek(self):
    return self.stack[-1]

  def isEmpty(self):
    if self.stack:
      return False
    else:
      return True

  def size(self):
    return len(self.stack)

  def __repr__(self):
    return f'{self.stack}'


nums = Stack()

print(nums)
print(nums.isEmpty())

nums.push(2)
nums.push(8)
nums.push(8)

print(nums)

nums.pop()

print(nums)

nums.push(6)

print(nums.peek())
print(nums)
