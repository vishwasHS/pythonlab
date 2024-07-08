s=input('enter a string')
L=list(s)
for i in range(len(L)):
    if L[i]>='A'and L[i]<='Z':
        L[i]=L[i].lower()
s1=''.join(L)
print(s1)
    