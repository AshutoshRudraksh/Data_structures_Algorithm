# defination of a binary tree node
class TreeNode:
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

# time and space O(n)

def inorder(root):
  stack = []
  curr = root 

  while curr or stack:
    # go all the way to the left and the left nodes to the stack
    if curr:
      stack.append(curr)
      curr = curr.left 
    # if no left subtree unstack and print the nodes and the right subtree
    else:
      curr = stack.pop()
      print(curr.val)
      curr = curr.right


def preorder(root):
  #create stack
  stack = []
  curr = root
  # given there is node in stack or given node at the hand
  while curr or stack:
    # check for node and print the value
    if curr:
      print(curr.val)
      # if there is right child add it to the stack
      if curr.right:
        stack.append(curr.right)
      # go exploring the left subtree for that right child
      curr = curr.left 
    # if there is no current node to explore search pop if some node in stack
    else:
      curr = stack.pop()

   
def postorder(root):
  # add the root node in the stack
  stack = [root]
  # mark is as not visited
  visited = [False]
  while stack:
    curr, visited = stack.pop(), visited.pop()
    if curr:
      if visited:
        print(curr.val)
      else:
        stack.append(curr)
        visited.append(True)
        stack.append(curr.right)
        visited.append(False)
        stack.append(curr.left)
        visited.append(False)
