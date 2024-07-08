#common characters between two strings
s1=input('enter string 1:')
s2=input('enter string 2:')
count=0
common=[]
for i in s1:
    if i in s2:
       if i not in common and i!=' ':
           common.append(i)
           count+=1
print('number of common characters=',count)
print('common characters:',end='')
for i in common:print(i,end='')