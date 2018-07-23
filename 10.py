def stair():
	s=0
	l=[]
	m=int(input())
	for i in range(m):
		l.append(int(input()))
	for i in l:
		s+=(m-i)
	print(s)
  
try:
  stair()
except:
  print('invalid')
  p
