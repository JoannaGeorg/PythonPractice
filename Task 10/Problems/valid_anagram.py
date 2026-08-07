def validAnagram(sentence, target):
  for char in target:
    if char not in sentence:
      return False
    elif target.count(char) > sentence.count(char):
      return False
  return True

sentence = "Obsession is not equal to love"
target = 'essential'

print(f"The Sentence: {sentence}\nThe Result: {target}\n\nThe Result is an Anagram: {validAnagram(sentence, target)}")
