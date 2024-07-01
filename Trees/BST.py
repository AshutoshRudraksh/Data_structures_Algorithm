class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# insert and removing is in O(logN) time
def searchBST(root,target):\
  # if no root 
  if not root:
    return False
  # if the target lies in right side
  if target > root.val:
    return searchBST(root.right, target)
  #if the target lies on the left side
  elif target < root.val:
    return searchBST(root.left, target)
  # target found
  else:
    return True

  

def insert(root, val):
  # if no node insert one
  if not root:
    return TreeNode(val)
  # if the val greater than root node then it will go on the right side of the tree
  if val > root.val:
    root.right = insert(root.right, val)
  # if the val greater than root node then it will go on the right side of the tree
  elif val < root.val:
    root.left = insert(root.left, val)
  return root


# BST remove
def minVal(root):
  # it is like traversing the linked list
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr

def remove(root, val):
  # if no node return Null
  if not root:
    return None
  # for left
  if val < root.val:
    root.left = remove(root.left, val)
  # for right
  elif val > root.val:
    root.right = remove(root.right, val)
  # found the target 
  else:
    # return the left or right if has if it has only one leaf node
    if not root.left:
      return root.right
    elif not root.right:
      return root.left
    # else find the min on the right subtree of that node
    else:
      minNode = minVal(root.right) # store that min node in temp
      root.val = minNode.val   # replace the root node's value by the temp minNode val
      root.right = remove(root.right, minNode.val ) # remove the minNode since we assigned it as root node now
  return root


