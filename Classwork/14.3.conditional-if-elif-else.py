#if and elif and else statements
#weekend budget plan
amount= int(input("Enter the amount you can spend for weekend:"))
if amount>=20000:
    print("Trip to Goa") #Trip to Goa #if 20000 or more
elif amount>=15000:
    print("go for shopping") #go for shopping # if 15000 or more
elif amount>=10000:
    print(" go for arunachallam")  # go for arunachallam  #if 10000 or more
elif amount>=5000:
    print("cafe/dinner")  #cafe/dinner #if 5000 or more
elif amount>=2000:
    print("maintanance..") #maintanance.. #if 2000 or more
elif amount>=500:
    print("Go for movie") #Go for movie  #if 500 or more
elif amount>=100:
    print("go for street food")  #go for street food  #if 100 or more
else:
    print("save the money and sleep")   #save the money and sleep 