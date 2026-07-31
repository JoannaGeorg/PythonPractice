def romanToInteger(s):
  num = 0
  for i in range(0, len(s)):
    if s[i] == 'M':
      num += 1000
    elif s[i] == 'D':
      num += 500
    elif s[i] == 'C':
      pre = 1
      if i < (len(s) - 1):
        if s[i+1] == 'M' or s[i+1] == 'D':
          pre = -1
      num = num + pre * 100
    elif s[i] == 'L':
      num += 50
    elif s[i] == 'X':
      pre = 1
      if i < (len(s) - 1):
        if s[i+1] == 'L' or s[i+1] == 'C':
          pre = -1
      num = num + pre * 10
    elif s[i] == 'V':
      num += 5
    elif s[i] == 'I':
      pre = 1
      if i < (len(s) - 1):
        if s[i+1] == 'X' or s[i+1] == 'V':
            pre = -1
      num = num + pre * 1

  return num

roman = "MCMXCIV"
print(f"{roman} = {romanToInteger(roman)}")
