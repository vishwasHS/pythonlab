s=input('enter a string')
L=list(s)
for i in range(len(L)):
    if L[i]>='a'and L[i]<='z':
        L[i]=L[i].upper()
s1=''.join(L)
print(s1)
    