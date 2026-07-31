def addBinary(b1, b2):
  b1 = b1[::-1]
  b2 = b2[::-1]
  ans = ''
  length = len(b1) if len(b1) < len(b2) else len(b2)
  carry = '0'
  for i in range(0, length):
    if b1[i] == '0' and b2[i] == '0' and carry == '0':
      ans += '0'
    elif b1[i] == '0' and b2[i] == '0' and carry == '1':
      ans += '1'
      carry = '0'
    elif b1[i] == '0' and b2[i] == '1' and carry == '0':
      ans += '1'
    elif b1[i] == '0' and b2[i] == '1' and carry == '1':
      ans += '0'
    elif b1[i] == '1' and b2[i] == '0' and carry == '0':
      ans += '1'
    elif b1[i] == '1' and b2[i] == '0' and carry == '1':
      ans += '0'
    elif b1[i] == '1' and b2[i] == '1' and carry == '0':
      ans += '0'
      carry = '1'
    elif b1[i] == '1' and b2[i] == '1' and carry == '1':
      ans += '1'

  if len(b1) > length:
    i = length
    while carry == '1' and i < len(b1):
      if b1[i] == '0':
        ans += '1'
        carry = '0'
      elif b1[i] == '1':
        ans += '0'
      i += 1
    if i < len(b1):
      ans += b1[i:]
  elif len(b2) > length:
    i = length
    while carry == '1' and i < len(b2):
      if b2[i] == '0':
        ans += '1'
        carry = '0'
      elif b2[i] == '1':
        ans += '0'
      i += 1
    if i < len(b2):
      ans += b2[i:]
  if carry == '1':
    ans += '1'

  return ans[::-1]


print(addBinary('1001', '1011'))
