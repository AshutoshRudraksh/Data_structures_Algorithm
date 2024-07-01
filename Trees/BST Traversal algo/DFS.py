class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

#increasing order
def inorder(root):
  if not root:
    return 
  inorder(root.left) # left
  print(root.val, end="") # print the root.val
  inorder(root.right) # right


#decreasing order
def decreasingOrder(root):
  if not root:
    return
  decreasingOrder(root.right)
  print(root.val)
  decreasingOrder(root.left)

#preorder: print the root node then left tree and then the right tree
def preorder(root): 
  if not root:
    return
  print(root.val, end="") # print the root node
  preorder(root.left) # go to the left subtree 
  preorder(root.right) # then go to the right subtree



#postorder: print the left tree and then the right tree and then root node
def postorder(root):
  if not root:
    return
  postorder(root.left) # print the left subtree
  postorder(root.right) # print the root node
  print(root.val, end="") # print the right subtree

