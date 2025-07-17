#for (ifelse)   
products=['cycle','watch','laptop','mobile','mouse']
items=input("Enter the items:").split() 

for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print(f"{i} is not available")    