a=int(input())
print(a)
j=0
d=a
while(d>0):
  b=d%10
  j+=b*b
  d=d//10
print(j)
