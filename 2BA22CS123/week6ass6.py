import re
s=input("enter the pan number")
k= r'^[A-Z]{5}[0-9]{4}[A-Z]$'
a=re.match(k,s)
if a:
    print("valid")
else:
    print("invalid")