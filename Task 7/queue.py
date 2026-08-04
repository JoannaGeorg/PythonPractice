class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, val):
    self.queue.append(val)

  def dequeue(self):
    return self.queue.pop(0)

  def peek(self):
    return self.queue[0]

  def isEmpty(self):
    if self.queue:
      return False
    else:
      return True

  def size(self):
    return len(self.queue)

  def __repr__(self):
    return f'{self.queue}'


q = Queue()

print(q.isEmpty())

q.enqueue(4)
q.enqueue(7)
print(q)
print(q.dequeue())

q.enqueue(6)
q.enqueue(10)
print(q)

print(q.peek())
print(q.isEmpty())
