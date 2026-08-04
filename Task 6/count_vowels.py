def countVowels(s):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  num_vowels = 0
  for char in s:
    if char in vowels:
      num_vowels += 1
  return num_vowels

words = "Nico Robin"
print(f"There are {countVowels(words)} vowels in {words}")
