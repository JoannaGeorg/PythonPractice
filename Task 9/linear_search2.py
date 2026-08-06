def linearSearch(target, num_list):
  """
  This function uses linear search to find a specific number in a list of numbers.
  """
  for index in range(0, len(num_list)):
    if num_list[index] == target:
      return index
  return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linearSearch(9, nums)

if index >= 0:
  print(f"The element was found at index {index}")
else:
  print("The element was not found in the list.")