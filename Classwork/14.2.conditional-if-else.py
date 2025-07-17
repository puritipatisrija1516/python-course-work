items=["shoes","smartwatch","phone","laptop","airpods","toycars"]
print('welcome to Amazon Store'.center(50,'*'))
search_input=input("Enter the item:")
if search_input in items:
    print(f"{search_input} found.buy now!!!") #Enter the item:shoes
                                             #shoes found.buy now!!!
else:
    print(f"{search_input}out of the stock now.we will notify you!!") #earphonesout of the stock now.we will notify you!!