#string input
name= input("Enter your full name:")
print(name) #Enter your full name: puritipati srija
            #puritipati srija
#Integer Input
item=int(input("Enter the number of items:"))
print(item) #24

#Float Input
discount=float(input("Enter the number of discount:"))
print(discount) #3.0

#Input as list (space-separated)
names= input("Enter employee names(space_separated):").split()
print(names) #Enter employee names(space_separated): srija manasa mounika
              #Out:['srija', 'manasa', 'mounika']

#Input as List (comma-separated)   
task=input("Enter task name(comma-separated): ") .split(',') 
print(task)   #Enter task name(comma-separated): #cash,credit,debit
           #['cash', 'credit', 'debit']   
           
#list of integers
marks=list(map(int,input("Enter the marks:").split() )) 
print(marks)  #Enter Marks: 75 89 90 95
              #Out:[75, 89, 90, 95]

#list of Floats
Weights= list(map(float,input("Enter Weights:").split())) 
print(Weights)  #Enter Weights:45.6 67.8 89.3
                  #Out: [45.6, 67.8, 89.3]   

#Tuple Input 
dimensions = tuple(map(int, input("Enter length, width, height:").split())) 
print(dimensions)   #Enter length, width, height:10 20 30
                      #Out:(10, 20, 30)  

#set Input
selected_image = set(map(int, input("Enter selected image IDs:").split()))
print(selected_image) #Enter selected image IDs:201 202 203 204 205
                        #{201, 202, 203, 204, 205}

#Dictionary Input using eval()
profile = eval(input("Enter user profile as a dictionary:"))
print(profile) #Enter user profile as a dictionary:{'name':'mouli','age':75,'role':'admin'}
                 #{'name': 'mouli', 'age': 75, 'role': 'admin'}

#Multiple Inputs with Unpacking
username, password = input("Enter username and password:").split()
print("username:",username)
print("password:",password)    #Enter username and password:user123 password#1516
                               #username: user123
                               #password: password#1516 

#only use eval() when input is trusted.                                            