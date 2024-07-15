n = int(input("enter the number of lines"))
unique_words = []
f=open("t.txt","r")
f1=open("t3.txt","w")
for i in range(n):
    words = f.readline().split()
    for word in words:
         if word not in unique_words:
             unique_words.append(word)

unique_words.sort()
for word in unique_words:
    f1.write(word + '\n')

print("Unique words from the first", n, "lines of t.txt have been written to t3.txt.")
