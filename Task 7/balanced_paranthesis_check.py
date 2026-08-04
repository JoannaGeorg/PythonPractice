def validParenthesis(s):
  parse_par = []
  for char in s:
    if not parse_par:
      if char == ')' or char == '}' or char == ']':
        return False
    if char == '(' or char == '{' or char == '[':
      parse_par.append(char)
    elif char == ')':
      if '(' == parse_par[-1]:
        parse_par.pop()
      else:
        return False
    elif char == '}':
      if '{' == parse_par[-1]:
        parse_par.pop()
      else:
        return False
    elif char == ']':
      if '[' == parse_par[-1]:
        parse_par.pop()
      else:
        return False
  if parse_par:
    return False
  return True


print(validParenthesis("(this is a (valid [test]))"))
print(validParenthesis("(this is an (invalid} [test]))"))