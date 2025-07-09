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

#3.String Case conversion methods
#uppercase()
name="srija"
print(name.upper()) #Output:SRIJA
#Lowercase()
name="CHINNU"
print(name.lower()) #Output: chinnu
#capitalize()
name="deepika"
print(name.capitalize()) #Output: Deepika
#title()
name= "string methods"
print(name.title()) #Output: String Methods
#swapcase()
name="aBcDeFgHiJ"
print(name.swapcase()) #Output:AbCdEfGhIj
#casefold()
name= 'ß'
print(name.casefold()) #Output: ss

#4.Alignment & Formating Method
#center()
name= 'srija'
print(name.center(20,'*')) #Output: *******srija********
name= "mahi"
print(name.center(30,"-")) #Output: -------------mahi-------------
#ljust()
name="chinnu"
print(name.ljust(10,"^"))  #Output: chinnu^^^^
#rjust()
name="strings"
print(name.rjust(20,"_")) #Output: _____________strings
#Zfill()
a="789"
print(a.zfill(6)) #Output: 000789

#5.Search & Find Methods
#find()
name="prabas"
print(name.find("a"))  #Output: -1
name="swetha"
print(name.find("s"))  #Output: 0
#rfind()
name="abcdabcdabcd"
print(name.rfind("d")) #Output: 11
#index()
name="python"
print(name.index("t")) #Output: 2
print(name.index("o")) #Output: 4
#rindex()
name="abcabcabcabc"
print(name.rindex("c")) #Output: 11
print(name.rindex("a")) #Output: 9
#count()
name="pythoncourse"
print(name.count("o")) #Output: 2

#6.String Testing Methods
#starstwith()
name="21G21A04G0"
print(name.startswith("21")) #Output: True
name="DS15"
print(name.startswith("DS")) #Output: True
name="ABC123"
print(name.startswith("123")) #Output: False
#endswith()
name="Kumar"
print(name.endswith("ar")) #Output: True
name="srija"
print(name.endswith("sri"))  #Output: False
#isalpha()
name="Hello"
print(name.isalpha())  #Output: True
name="ABC123"
print(name.isalpha())   #Output: False
#isalnum()
name="abc"
print(name.isalnum()) #Output: True
name="abc123"
print(name.isalnum()) #Output: True
name="@123"
print(name.isalnum()) #Output: False
#islower()
name="srija"
print(name.islower()) #Output: True
name="SRIJA"
print(name.islower()) #Output: False
#isupper()
name="YOUR FAV COLOUR"
print(name.isupper())  #Output: True
name="your fav colour"
print(name.isupper())  #Output: False
#isspace()
name="        "
print(name.isspace())  #Output: True
#istitle()
name="print hello"
print(name.istitle())  #Output: False
name="Print Hello"
print(name.istitle())  #Output: True
#isidentifier()
name="pythhon1"
print(name.isidentifier())   #Output:True
name="@python"
print(name.isidentifier())  #Output:  False

#7.Replace & Modify Methods
#replace()
name="muni bhargthv"
print(name.replace("th","a"))  #Output: muni bhargav
#translate()
name="abc"
print(name.translate(str.maketrans("a","x")))  #Output: xbc
#maketrans()
name="python"
print(name.maketrans("th","#$")) #Output: {116: 35, 104: 36}

#8.splitting & Joining Methods
#split()
name="x,y,z"
print(name.split(",")) #Output: ['x', 'y', 'z']
#rsplit()
name='u,v,x,y,z'
print(name.rsplit(",",1)) #Output: ['u,v,x,y', 'z']
#splitlines()
name="srija\npuritipati"
print(name.splitlines()) #Output:['srija', 'puritipati']
#join()
name="muni bhargav"
print(",".join(name))  #Output: m,u,n,i, ,b,h,a,r,g,a,v
#partition()
name= "python-course"
print(name.partition("-"))    #Output: ('python', '-', 'course')
#rpartition()
name="python-course"
print(name.rpartition(","))  #Output: ('', '', 'python-course')
print(name.rpartition("-")) #Output: ('python', '-', 'course')

#9.whitespace & Trimming Methods
#strip()
name= " Lakshmi "
print(name.strip()) #Output:  Lakshmi
#lstrip()
name="-----lakshmi"
print(name.lstrip("-")) #Output:lakshmi
#rstrip()
name="lakshmi-----"
print(name.rstrip("-")) #Output:lakshmi

#10. & Decoding Methods
#encode()
name="mouli"
print(name.encode()) #Output:b'mouli'
#decode()
name=b'mouli'
print(name.decode())  #Output: mouli





















