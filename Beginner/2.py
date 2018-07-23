n =int(input("Enter the num:\n"))
k=int(input("Enter the digit to remove:\n"))
m= int(str(n)[:-k])
print(m)
def smallest(lst):
    for i,n in enumerate(lst):
        if n != '0':
            tmp = lst.pop(i)
            break
    return str(tmp) + ''.join(lst)
if __name__ == '__main__':
    lst = list(str(m))
    lst.sort()
    print ("smallest num combination is:\n",smallest(lst))
