from collections import deque
# Breadth First Search

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def bfs(root):
  # create the data structure
  queue = deque()

  #check for the root node and insert the root node  in queue
  if root:
    queue.append(root)

  # now keep track of each level going down
  level = 0
  while len(queue)>0: # still there is node in the queue to explore
    # print the level at which you are
    print("level: ", level)
    # explore each node on that level
    for i in range(len(queue)):
      node = queue.popleft() # popleft mean get the one in the front of the queue
      print(node.val)
      # check if that node has children
      if node.left:
        #if the left child exists then add to the exploration queue
        queue.append(node.left)
      elif node.right:
        # if the right child exists then add to the exploration queue
        queue.append(node.right)
    #after the loop ends that means you have explored each node on that particular level
    level+=1 # go to the next level
    