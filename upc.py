word=list(input())
for i in range(len(word)):
    if word[i].islower():
        wor[i]=word[i].upper()
    else:
        word[i]=word[i].lower()
print("".join(str(x) for x in word))
