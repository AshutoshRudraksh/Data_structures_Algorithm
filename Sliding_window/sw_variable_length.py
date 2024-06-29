# variation 3
# sliding window variable size
def longestSubarray(nums):
  length = 0
  L = 0

  for R in range(len(nums)):
    if nums[R] != nums[L]:
      L=R
    length = max(length, R-L+1)
  return length
