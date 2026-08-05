import random

def listSum(nums):
  """
  This function sums the numbers in a list using recursion.
  """
  if not nums:
    return 0
  if len(nums) == 1:
    return nums[0]
  return nums[0] + listSum(nums[1:])

nums = random.sample(range(1, 30), 5)
print(f'Sum of {nums} = {listSum(nums)}')