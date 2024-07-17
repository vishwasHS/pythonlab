mlist=eval(input("enter the list:"))
n=int(input("enter the value of n:"))
result=[mlist[i:i+n]for i in range (0,len(mlist),n)]
print(result)
