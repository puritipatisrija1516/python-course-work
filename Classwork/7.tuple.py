#Tuple
#Empty Tuple
empty_tuple=()
# single-element Tuple(note the trailing comma)
single_tuple=(5,)
#multi-element Tuple
my_tuple=(1,"apple",3.5)
#Without parentheses (implicit tuple creation)
implicit_tuple=  1,2,3
print(empty_tuple,single_tuple,my_tuple) #Output:() (5,) (1, 'apple', 3.5)

#accessing tuple
t=(10,20,30,40)
print(t[0]) #10
print(t[-1]) #40

#slicing
t=(10,20,30,40,50)
print(t[1:4]) #(20, 30, 40)
print(t[-2:]) #(40, 50)
print(t[:-1]) #(10, 20, 30, 40)
print(t[0:])  #(10, 20, 30, 40, 50)
print(t[:3])  #(10, 20, 30)

#Operations on tuples
#repetition
tuple=(1,2)
print(tuple*3)  # (1, 2, 1, 2, 1, 2)
#concatination
tuple1=(1,2)
tuple2=(3,4)
print(tuple1+tuple2) #(1, 2, 3, 4)
#membership
tuple=(2,3,4,5,6,7)
print(6 in tuple) #True
print(8 not in tuple) #True
print(8 in tuple) #False
#Tuple Unpacking
tuple=  ("banana","cherry","mango")
tuple1,tuple2,tuple3= tuple
print(tuple1,tuple2,tuple3)  # banana cherry mango

#Tuple Methods
t=(1,2,3,4,5,3)
print(t.count(3)) #2
print(t.index(2)) #1

#Functions for tuple
t=(1,2,3,4,5)
#length og tuple
print(len(t)) #5
#maximum
print(max(t)) #5
#minimum
print(min(t)) #1
#sum of tuple
print(sum(t)) #15
#nested tuple
t=([1,2,3],(1,2,3)) #([1, 2, 3], (1, 2, 3))
print(t)



