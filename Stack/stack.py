# Implementing a stack is trivial using a dynamic array
# which we implemented earlier
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, val):
    self.stack.append(val)
  
  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def size(self):
    return self.stack.size()
