# find the middle if a linked list with two pointers
# time O(n), space O(1)

def middleofList(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow 

# determine if linked list contains a cycle
def hasCycle(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: # this is were we detect cycle
      return True
  return False

# determince the cycle and return the head of the cycle
def cycleStart(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break
  
  if not fast or not fast.next:
    return None
  
  slow2 = head # this is were you start with second pointer 
  while slow != slow2: # and when slow2 and slow meet that's were the head of cycle is
    slow = slow.next
    slow2 = slow2.next
  return slow
