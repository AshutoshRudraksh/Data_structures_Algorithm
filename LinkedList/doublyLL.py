class ListNode:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None
  
class DoublyLL:
  def __init__(self):
    self.head = ListNode(-1)
    self.tail = self.head
    self.head.next = self.tail
    self.tail.prev = self.head

  def insertFront(self, val):
    newNode = ListNode(val)
    newNode.prev = self.head
    newNode.next = self.head.next

    self.head.next.prev = newNode
    self.head.next = newNode

  def insertEnd(self, val):
    newNode = ListNode(val)
    newNode.next = self.tail # newNode -> tail
    newNode.prev = self.tail.prev #  lastnode <-newNode

    self.tail.prev.next = newNode #lastNode -> newNode
    self.tail.prev = newNode # tail pointer -> newNode 

  def removeFront(self):
    self.head.next.next.prev = self.head # head <- (node0) <- node1 
    self.head.next = self.head.next.next # head -> (node0) -> node
  
  def removeEnd(self):
    self.tail.prev.prev.next = self.tail # node3 -> (node0) ->tail
    self.tail.prev = self.tail.prev.prev # node3 <- (node0) <-tail

  def print(self):
    curr = self.head.next
    while curr!=self.tail:
      print(curr.val, " -> ", end="")
      curr=curr.next
    print()

