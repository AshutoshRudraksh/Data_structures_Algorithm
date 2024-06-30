class ListNode:
  def __init__(self, val):
    self.val = val #node value
    self.next = None # node Pointer

#Implementation of singly Linked List
class LinkedList:
  def __init__(self):
    #create a dummy node so that removing node from the start will be easy
    self.head = ListNode(-1) # dummy node
    self.tail = self.head # head &  tail pointing to the same node

  # insert new node at the end
  def insertEnd(self, val): 
    self.tail.next = ListNode(val) # tail-> newnode
    self.tail = self.tail.next # tail = newnode

  # remove node at the ith index
  def remove(self, index):
    i = 0 
    curr = self.head
    while i<index and curr: # setting i<index will help to get the node before to grab the one we need to delete
      curr = curr.next
      i+=1
    #remove the node 
    if curr and curr.next:
      # check if you at the end of the LinkedList 
      if curr.next == self.tail:
        self.tail = curr
      curr.next = curr.next.next

  def print(self):
    curr = self.head
    while curr:
      print(curr.val, " -> ", end="")
      curr = curr.next
    print()
