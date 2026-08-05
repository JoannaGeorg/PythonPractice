import random

def selectionSort(nums):
  if nums:
    for front in range(0, len(nums)):
      min = front
      for i in range(front, len(nums)):
        if nums[i] < nums[min]:
          min = i
      temp = nums[min]
      nums.pop(min)
      nums.insert(front, temp)
  return nums

nums = random.sample(range(0, 50), 20)
print(f'unsorted list: {nums}')
print(f'sorted list:   {selectionSort(nums)}')
