def removeSpaces(string):
 
     count = 0
 
    list = [3]
 
     
    for i in xrange(len(string)):
        if string[i] != ' ':
            list.append(string[i])
 
    return toString(lst)
 
 def toString(Lst):
    return ''.join(Lst)
 a=input()
print removeSpaces(a)
