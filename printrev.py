def reverse(i):
  str = ""
  for r in i:
    str = r + str
  return str
i = raw_input()
print (reverse(i))
