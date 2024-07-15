f=open('file.txt', 'r')
f2= open('vowel.txt', 'w')
vowels = 'aeiouAEIOU'
for i in f:
    if i[0] in vowels:
        f2.write(i)
