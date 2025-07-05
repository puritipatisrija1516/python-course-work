#Numeric data type
a=10
print(type(a)) # Output: <class int> 
a=10.342
print(type(a)) # Output: <class float>
a=3+3j
print(type(a)) # Output: <class complex>

#string datatype
name="srija"
print(type(name))  # Output: <class 'str'>  
name='''puritipatisrija'''
print(type(name))   # Output: <class 'str'>  

#tuple
t=tuple()
a=(2,3,4,5) #Output:() (2, 3, 4, 5)     
print(t,a)
print(type(t)) #Output: <class 'tuple'>  
print(type(a)) #Output: <class 'tuple'>  

#set
s=set()
a={1,1,1,2,2,3,3,4}
print(s,a)  #Output: set() {1, 2, 3, 4}
print(type(s))  #Output: <class 'set'>
print(type(a))  #Output:  <class 'set'>

#frozenset
s=frozenset({1,2,3})
print(type(s)) #Output: <class 'frozenset'>

#Dictionary
a={'name':'srija','age':21,'weight':45}
print(type(a)) #Output: <class 'dict'>

#boolean
status=True
status=False
print(type(status)) #Output: <class 'bool'>

#null
randomvar=None
print(type(randomvar)) #Output: <class 'NoneType'>

