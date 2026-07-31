def raiseReversePower(num):
  str_num = str(num)
  str_num = str_num[::-1]
  rev = int(str_num)
  return num ** rev

print(raiseReversePower(20))
