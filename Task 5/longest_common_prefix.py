def longestCommonPrefix(strs):
  if not strs:
    return ""
  longest = strs[0]
  for word in strs:
    if longest == word:
      continue
    else:
      for i in range(0, len(longest)):
        if i > len(word)-1 or longest[i] != word[i]:
          longest = longest[:i]
          break
  return longest

word_list = ["flower", "flow", "flowing"]
print(f"\nGiven the list: {word_list}")
print(f"The Longest common prefix = {longestCommonPrefix(word_list)}")
