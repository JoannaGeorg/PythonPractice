def lastWordLength(sentence):
  words = sentence.split()
  return len(words[-1])

s = "Inheritance of Wills is the main theme of One Piece"
print(lastWordLength(s))
