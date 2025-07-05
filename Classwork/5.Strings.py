#string
Name="srijs"
print(type(Name)) #Output: <class 'str'>

#1.String Operations
#Concatenation(+)
fname='Puritipati'
lname='Srija' 
print(fname+lname)  #Output: <class 'str'>  (PuritipatiSrija)

#Repetition(*)
name="Manasa"
print("Manasa"*6) #Output: (ManasaManasaManasaManasaManasaManasa)

#Indexing
text="munibhargav"
print(text[3]) #Output:(i)
print(text[0]) #Output:(m)
print(text[-1]) #Output:(v)
print(text[-4]) #Output:(r)

#Slicing
name="Maheshwari"
print(name[0:6]) #Output: Mahesh
print(name[:8])  #Output: Maheshwa
print(name[3:])  #Output: eshwari 
print(name[:])   #Output: Maheshwari

#Membership
name='srija'
print('sri' in name) #Output: True
print('sri' not in name) #Output: False
print('mahi' in name)    #Output: False
print('mahi' not in name) #Output: True

#2.String Functions
#len()
name="srija"
print(len(name)) #Output: 5

#max() and min()
name="chinnuXYZ"
print(max("chinnuXYZ")) #Output: u
print(min("chinnuXYZ")) #Output: X

#Sorted()
name="chinnu"
print(sorted("chinnu")) #Output:['c', 'h', 'i', 'n', 'n', 'u']

#chr() and ord()
X=('A')
print(ord(X)) #Output: 65
x=('a')
print(ord(x)) #Output: 97
x=('@')
print(ord(x))  #Output: 64
#chr()
print(chr(97)) #Output: a
print(chr(45)) #Output: -
print(chr(81)) #Output: Q








