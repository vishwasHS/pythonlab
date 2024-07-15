f=open("file1.txt","r")
f1=open("key.txt","w")
words = f.read().split(" ")
df={}
for word in words:
    if word in df:
        df[word] += 1
    else:
        df[word] = 1


for word, freq in df.items():
      f1.write(f"{word}: {freq}\n")

print("Word frequencies have been counted and saved in key.txt.")    