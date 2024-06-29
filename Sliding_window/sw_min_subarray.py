# variation 4
# subarray of minmum size
def shortestSubarray(nums, target):
  L, total = 0, 0 
  # the another way to set the length is len(nums) + 1
  length = float('inf') # length of array set to infinity 

  for R in range(len(nums)):
    total += nums[R]
    while total >= target: 
      length = min(length, R-L+1) # get the minimum subarray until this point
      total -= nums[L] # substract the left element value from sum
      # shift the left pointer by one
      L+=1
  return 0 if length == float("inf") else length
