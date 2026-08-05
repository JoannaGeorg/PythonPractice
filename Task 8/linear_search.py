def linearSearch(element, nums):
  for i in range(0, len(nums)):
    if nums[i] == element:
      return i
  return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linearSearch(9, nums)

if index >= 0:
  print(f"The element was found at index {index}")
else:
  print("The element was not found in the list.")