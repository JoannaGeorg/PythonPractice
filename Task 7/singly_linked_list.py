class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __repr__(self):
    return f'[val: {self.val}; next: {self.next}]'

class SinglyLinkedList:
  def __init__(self, head=Node()):
    self.head = head

  def __repr__(self):
    return f'head: {self.head}'

node = Node(4)
node.next = Node(5)

linked_list = SinglyLinkedList(node)

print(linked_list)
