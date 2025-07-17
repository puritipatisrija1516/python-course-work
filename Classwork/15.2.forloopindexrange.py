#range and for (if)
s='manasa mounika bhavana hema srija'.lower()
n= len(s)
ch=input().lower()
for i in range(n):
    if s[i]==ch:
        print(ch,i)
        

