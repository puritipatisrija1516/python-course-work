email,pwd='xyz@gmail.com','xyz@123'
max_attempts=5

while max_attempts>0:
    useremail=input("Enter the email:")
    password=input("Enter the password:")
    if useremail==email and pwd==password:
        print("Login successful")
        break
    else:
        print("invalid login")
        max_attempts-=1
else:
    print("try after some time!")        
