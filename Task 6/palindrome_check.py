def palindromeCheck(word):
  rev_word = word[::-1]
  if word == rev_word:
    return True
  return False

word = 'plannalp'
if palindromeCheck(word):
  print(f"{word} is a palindrome")
else:
  print(f'{word} is NOT a palindrome')