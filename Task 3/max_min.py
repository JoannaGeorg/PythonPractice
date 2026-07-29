def maxMinFinder(nums):
  if not nums:
      return None
  
  maximum = nums[0]
  minimum = nums[0]
  
  for num in nums:
    if num > maximum:
      maximum = num
    elif num < minimum:
      minimum = num
  return (maximum, minimum)

nums = [4, 76, 4, 6, 0, 87, 57]
max_num, min_num = maxMinFinder(nums) or (None, None)
print(f'{max_num} {min_num}')
