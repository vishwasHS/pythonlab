s=input('enter the string')
print(s)
size=len(s)
l=list(s)
for i in range(len(l)):
    if l[i]>='a' and l[i]<='z':
       l[i]=l[i].upper()
    elif l[i]>='A' and l[i]<='Z':
        l[i]=l[i].lower()
s1=''.join(l)
print(s1)
        
 