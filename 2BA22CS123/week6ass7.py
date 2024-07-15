import re
s=input("enter passport number")
k=r'[A-Z]{1}[1-9]{1}[0-9]{1}\s{0,1}[0-9]{4}[A-Z]{1}$'
a=re.search(k,s)
if a:
    print("valid")
else:
    print("invalid")