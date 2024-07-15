f=open("t.txt","r")
f1=open("t3.txt","w")
lines = f.readlines()

filtered_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
f1.writelines(filtered_lines)

print("Lines at even indices from month.txt have been deleted and remaining lines saved in k.txt.")
