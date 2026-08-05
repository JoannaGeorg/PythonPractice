import random

def bubbleSort(nums):
  if not nums:
    return nums
  for last in range(len(nums)-1, 0, -1):
    for i in range(0, last):
      if nums[i] > nums[i+1]:
        temp = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = temp
  return nums

nums = random.sample(range(0, 50), 20)
print(f'unsorted list: {nums}')
print(f'sorted list: {bubbleSort(nums)}')

