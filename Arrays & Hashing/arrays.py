#Dynamic array

class DynamicArray:
  def __init__(self, capacity):
    self.capacity = capacity
    self.length = 0
    self.arr = [0]*self.capacity

  # get will return the element at index i
  def get(self, i):
    return self.arr[i]

  # set method will set the element at index i 
  def set(self, i , val):
    self.arr[i] = val

  # pushback will push the element to the end of the array
  def pushback(self, val):
    #check if the capacity is full
    if self.length == self.capacity:
      self.resize()
    
    #after resize or if ther is enough space in array
    self.arr[self.length] = val # push at the end
    # increase array length by 1 given we have added new element at the end of the array
    self.length+=1 

  # popback will remove the the element at the end assuming the array is non-empty
  def popback(self):
    if self.length == 0:
      return
    
    if self.length > 0:
      self.length -=1 # just decrease the size by one 
    # given the length is starting from 1 we can return element at index len-1 even we decrease length by 1 incase confused
    return self.arr[self.length]

  # resize the array
  def resize(self):
    # create the double capacity array
    self.capacity = 2 * self.capacity
    new_arr = [0]*self.capacity

    # now insert element from old arr to new_arr
    for i in range(self.length):
      new_arr[i] = self.arr[i]
    self.arr = new_arr

  def get_size(self):
    return self.length

  def get_capacity(self):
    return self.capacity
