# variation Target sum (Shrinking window)
def targetSum(nums, target):
  L, R = 0, len(nums)-1
  while L<R:
    total = nums[L] + nums[R]
    if total > target:
      R-=1
    elif total < target:
      L+=1
    else:
      return [L,R]