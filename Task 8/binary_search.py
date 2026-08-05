def binarySearch(target, nums):
  first = 0
  last = len(nums) - 1
  while first <= last:
    mid = (first + last) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      last = mid - 1
    else:
      first = mid + 1
  return -1

nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 17, 20, 21, 22, 24, 25, 27, 28, 32, 45]
e = 45
index = binarySearch(e, nums)

if index >= 0:
  print(f'The element {e} was found at index {index}')
else:
  print(f'The element {e} was not in the list')

