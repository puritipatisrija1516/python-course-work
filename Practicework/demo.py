n=int(input("Enter the Size:"))
for row in range(n):
    for spc in range(row):
        print(' ',end='')
    for col in range(n-row):
        print("*",end='')
    print()

n=int(input("Enter the Size:"))
for row in range(n):
    print(' '*row,end='')
    print("*"*(n-row),end='')
    print()   

n=int(input("Enter the size:"))
for row in range(n):
    if row<=n//2:
        print('*'*(row+1),end=' ')
    else:
        print('*'*(n-row),end=' ')
    print() 

n=int(input("Enter the Size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end='')
        else:
            print("*",end='')
    print()    



 

