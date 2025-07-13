#converting from int
a=22
print(type(a)) #<class 'int'>
print(float(a)) #22.0
print(type(float(a))) #<class 'float'>
print(str(a)) #'22'
print(type(str(a))) #<class 'str'>
print(bool(a)) #True (Non-Zero ints are True)
print(type(bool(a))) #<class 'bool'>
print(complex(a)) #(22+0j)
print(type(complex(a))) #<class 'complex'>
#int is a single value..
#we can not convert single to multiple/iteratable values like list,set,tuple,dict
#print(set(a)) #typeError:'int' object is not iterable 
#print(type(set(a))) #typeError:'int' object is not iterable 

#converting from float
b= 23.1
print(type(b)) #<class 'float'>
print(int(b)) #23
print(type(int(b))) #<class 'int'>
print(str(b)) #'23.1'
print(type(str(b))) #<class 'str'>
print(bool(b)) #True (Non-Zero ints are True)
print(type(bool(b))) #<class 'bool'>
print(complex(b)) #(23.1+0j)
print(type(complex(b))) #<class 'complex'>
#float is a single value..
#we can not convert single to multiple/iteratable values like list,set,tuple,dict
#print(set(a)) #typeError:'float' object is not iterable 
#print(type(set(a))) #typeError:'float' object is not iterable 

#converting from string
c= "srija"
print(type(c)) #<class 'str'>
#if want to convert str in int or float the values should be in numeric ex: for int 1,2,3.. for float 1.0, 2,0...
c1='2' 
print(int(c1)) #2
print(type(int(c1))) #<class 'int'>
c2='2.3'
print(float(c2)) #2.3
print(type(float(c2))) #<class 'float'>
c3='24+5j'
print(complex(c3)) #(24+5j)
print(type(complex(c3))) #<class 'complex'>
c4='sri'
print(bool(c4)) #True(Non-Zero ints are True)
print(type(bool(c4))) #<class 'bool'>
c= "srija"
print(list(c)) #['s', 'r', 'i', 'j', 'a']
print(type(list(c))) #<class 'list'>
c= "srija"
print(tuple(c)) #('s', 'r', 'i', 'j', 'a')
print(type(tuple(c))) #<class 'tuple'>
c= "srija"
print(set(c)) #{'r', 'a', 'i', 'j', 's'}
print(type(set(c))) #<class 'set'>
c= "srija"
#print(dic(c))
#print(type(dic(c))) #Needs Key-value pair structure

#converting to list
l=[1,2,3,4]
print(type(l)) #<class 'list'>
#we can not convert multiple/iterables to single values like int,float,complex
#print(int(l)) #typeError: 'int' object is not iterable 
#print(type(int(l))) #typeError: 'int' object is not iterable
print(tuple(l)) #(1, 2, 3, 4)
print(type(tuple(l))) #<class 'tuple'>
print(bool(l)) #True(Non-Zero ints are True)
print(type(bool(l))) #<class 'bool'>
print(set(l)) #{1, 2, 3, 4}
print(type(set(l))) #<class 'set'>
#print(dic(1))
#print(type(dic(1))) #TypeError: cannot convert dictionary update sequence element in to a sequence

#converting to tuple
t=(1,2,3,4)
print(type(t)) #<class 'tuple'>
print(list(t)) #[1, 2, 3, 4]
print(type(list(t))) #<class 'list'>
print(bool(t)) #True(Non-Zero ints are True)
print(type(bool(t))) #<class 'bool'>
print(set(t)) #{1, 2, 3, 4}
print(type(set(t))) #<class 'set'>
#print(dic(t))
#print(type(dic(t))) #TypeError: cannot convert dictionary update sequence element in to a sequence

#converting to set
s={1,2,3,4}
print(type(s)) #<class 'set'>
print(bool(s)) #True(Non-Zero ints are True)
print(type(bool(s))) #<class 'bool'>
print(tuple(s)) #(1, 2, 3, 4)
print(type(tuple(s))) #<class 'tuple'>
print(list(s)) #[1, 2, 3, 4]
print(type(list(s))) #<class 'list'>
#print(dic(s))
#print(type(dic(s))) #TypeError: cannot convert dictionary update sequence element in to a sequence

#converting to Dictionary
d={2:3,4:5,6:7,8:9}
print(type(d)) #<class 'dict'>
print(bool(d)) #True(Non-Zero ints are True)
print(type(bool(d))) #<class 'bool'>
print(list(d)) #[2, 4, 6, 8]
print(type(list(d))) #<class 'list'>
print(tuple(d)) #(2, 4, 6, 8)
print(type(tuple(d))) #<class 'tuple'>
print(set(d)) #{8, 2, 4, 6}
print(type(set(d))) #<class 'set'>










