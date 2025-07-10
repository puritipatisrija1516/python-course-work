items=["shoes","smartwatch","phone","laptop","airpods","toycars"]
print('welcome to Amazon Store'.center(50,'*'))
search_input=input("Enter the item:").lower()
if search_input in items:
    print(f"{searchinput} found.buy now!!!")
else:
    print(f"out of the stock.stock is ready inform you!!")
      


#weekend budget plan
amount= int(input("Enter the amount you can spend for weekend:"))
if amount>20000:
    print("Trip to Goa")
elif amount>15000:
    print("go for shopping")  
elif amount>10000:
    print(" go for arunachallam")  
elif amount>5000:
    print("cafe/dinner")   
elif amount>2000:
    print("maintancess")
elif amount>500:
    print("Go for movie")
elif amount>100:
    print("go for street food")  
else:
    print("save the money and sleep")                     