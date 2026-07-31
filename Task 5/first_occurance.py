def needleInHaystack(haystack, needle):
  for i in range(0, len(haystack)):
    if haystack[i] == needle[0]:
      j = len(needle)
      if haystack[i:i+j] == needle:
        return i
  return None

h = 'buttonless'
l = 'lesin'
index = needleInHaystack(h, l)

print(f"\nThe haystack: {h}\nThe needle: {l}")
if index:
  print(f"\nThe first occurance starts at index {index}\n")
else:
  print("\nNot Found.\n")