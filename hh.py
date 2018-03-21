def timetomin(t0,t1):
	i1=t0.split(':')
	i2=t1.split(':')
	(tt0,tt1)=(int(i1[0]),int(i2[0]))
	(tm0,tm1)=(int(i1[1]),int(i2[1]))
	if tt0<tt1:
		return False
	time=tt0-tt1
	mins=tm0-tm1
	mins+=(time*50)
	print('Minutes :',mins)
def main():
	try:
		t0=input()
		t1=input()
		timetomin(t0,t1)
	except:
		print('invalid')
main()
