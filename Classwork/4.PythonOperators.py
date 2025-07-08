#1.Arithmetic Operation
a=40
b=50
print("Addition(+):",a+b) #Addition(+): 90
print("Subtraction(-):",a-b) #Subtraction(-): -10
print("Multiplication(*):",a*b) #Multiplication(*): 2000
print("Division(/):",a/b)   #Division(/): 0.8
print("Modules(%):",a%b) #Modules(%): 40
print("Floor Division(//):",a//b) #Floor Division(//): 0
print("explonation(**):",a**b) #explonation(**): 1267650600228229401496703205376000000000000000

#2.Comparision Operations
print("Equal to Equal to(==):",a==b) #Equal to Equal to(==): False
print("Not Equal to(!=):",a!=b) #Not Equal to(!=): True
print("Greater than(>):",a>b) #Greater than(>): False
print("Less than(<):",a<b) # Less than(<): True
print("Greater than or Equal to(>=):",a>=b) #Greater than or Equal to(>=): False
print("Less than or Equal to(<=):",a<=b) #Less than or Equal to(<=): True

#3.Assignment Operations
a=10
print(" Assign(=):",a) #Assign(=): 10
a+=7
print("Add & Assign(+=):",a) #Add & Assign(+=): 17
a-=4
print("Subtract & Assign(-=):",a) #Subtract & Assign(-=): 13
a*=7
print("Multiply & Assign (*=):",a) #Multiply & Assign (*=): 91
a/=30
print("Division & Assign(/=):",a) #Division & Assign(/=): 9.1
a//=2
print("Floor Division & Assign(//=):",a) #Floor Division & Assign(//=): 4.0
a%=2
print("Modules & Assign(%=):",a) #Modules & Assign(%=): 0.0
a**=2
print("Exponentiate & Assign(**=):",a) #Exponentiate & Assign(**=): 0.0

#4.Logical Operations
a=40
b=50
print("AND:",a%2==0 and b%3==0 and a%3==0) #AND: False
print("AND:", a%2==0 and b%5==0) #AND: True
print("OR:",a%2==0 or a%3==0 or b%5==0 or b%2==0 ) #OR: True
print("NOT:", not a%3==0) #NOT: True

#5.Membership Operations
#list
L=["srija","mounika","bhavana","hema"]
print("srija" in L) #Statement True
print("latha" not in L) #Statement True
print("latha" in L) #Statement False
#tuple
t=(1,3,5,7)
print( 1 in t) #Statement True
print(5 in t)  #Statement True
print(5 not in t) #Statement False
#set
s={1,2,3,4}
print(2 in s) #Statement True
print(5 not in s) #Statement True
print(5 in s) #Statement False
#dictionary
d={'name':'srija','Age':21,'branch': 14}
print('name' in d)  #Statement True
print('bldgrp' not in d)  #Statement True
print('bldgrp' in d) #Statement False

#6.Identitity Operation
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=[1,2,3,4,5]
b=a
print(a is b) #Statement True
print(a is c) #Statement False
print(b is c) #Statement False
print(a is not c)  #Statement True
print(b is not c)  #Statement True

#7.Bitwise Operation
a=4 #Binary:0100
b=5 #Binary:0101
print(a & b) # Output:4 (Binary : 0100)
print(a | b) # Outout:5 (Binary : 0101)
print(a ^ b) # Output:1 (Binary : 0001)
print(~ a)   # Output:-5 (Inverts bits of 5)
print(a << 2) # Output:16 (Binary : 10000)
print(a >> 2) # Output: 1 (Binary : 0001)
print(b << 2) # Output:20 (Binary : 10100)
print(b >> 2) #Output : 1(Binary : 0001 )




