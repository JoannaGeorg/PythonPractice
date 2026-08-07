def countDigits(num):
  digit_num = 0
  while num >= 1:
    num = num // 10
    digit_num += 1
  return digit_num

print(countDigits(178))
