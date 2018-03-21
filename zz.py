def comp(p1,p2):
    count=0
    if len(p1)<len(p2):
        n=len(p1)
    else:
        n=len(p2)
    for a in range(0,n):
        if p1[a]==p2[a]:
            count+=1
        else:
            break
    return p1[:count]
num=input("enter the no of string:")
l=[]
for x in range(0,num):
    l.append(raw_input())
for x in range(0,num-1):
    
    l[x+1]=comp(l[x],l[x+1])
print l.pop()
