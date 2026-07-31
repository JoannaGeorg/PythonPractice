def removeElement(nums, val):
  fin_nums = []
  for i in range(0, len(nums)):
    if nums[i] == val:
      fin_nums.append(i)
    i += 1
  
  times = 0
  for i in fin_nums:
    i -= times
    nums.pop(i)
    times += 1

  return nums

num_list = [1, 2, 4, 6, 2, 5, 3, 1, 3, 6, 2]
print(removeElement(num_list, 3))