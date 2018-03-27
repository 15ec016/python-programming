def main():
    list=[]
    h,k=input().split(" ")
    h=int(n)
    k=int(k)
    for i in range(0,h):
        z=int(input())
        list.append(str(z))

    final=(list[-k:]+list[:-k])
    print( ' '.join(final))
if __name__ == '__main__':
    main()
