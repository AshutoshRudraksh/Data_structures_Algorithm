class PrefixSum:
  def __init__(self,nums):
    self.prefix=[]
    total = 0
    for n in nums:
      total += n
      self.prefix.append(total)
  def rangeSum(self, left, right):
    PreRight = self.prefix[right]
    PreLeft = self.prefix[left-1] if left>0 else 0
    return PreRight - PreLeft