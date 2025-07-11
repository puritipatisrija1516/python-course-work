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


#Negative and positive
name=input("enter the name:")
vowels='AEIOUaeiou'

if name[0] in vowels:
    print("covid +ve. Take Care")
else:
    print("congrats!!!Your Safe")   

#Booking seats
Seats={
 'L1':True,
 'L2':True,
 'U1':True,
 'U2':False,  
       }  
   
print(seats.keys())
seatid=input("enter the seat number:")
if seatid in seats:
    if seats[seatid]:
        print("seat is avaliable. you can book")
    else:
        print("seat is not avaliable.  pick other one ")
else:
    print("choose the seat number properly")

#positive & Negitive num
num=int(input("enter the number:"))
if num>0:
    print("positive number")
elif num<0:
    print("Negitive number")  
else:
    print("zero")  

#Even or Odd
num=int(input("enter the number:"))  

if num%2==0:
    print(f'{num} is odd number')
else:
    print(f'{num} is Odd number') 

#leap year
year=int(input("enter the year:"))  

if year%400==0 or year%4==0 and year%100!=0:
    print(f'{year} is leap year')
else:
    print(f'year is not leap year')    