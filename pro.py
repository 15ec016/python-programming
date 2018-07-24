z=int(input())
list=[]
for i in range(0,z):
    y=int(input())
    list.append(y)
count=0
for i in list:
    for x in list:
        if i==x:
            count+=2
    if count==2:
print(i)
