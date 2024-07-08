s=input("enter binary digit").split(",")
div=[]
for i in s:
    dec=int(i,2)
    print(dec)
    if dec%5==0:
        div.append(i)
print("divisible by 5 are",div)