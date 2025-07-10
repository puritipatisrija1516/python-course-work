#1.sets
# Creating a set with elements
my_set = {1, 2, 3, 4}
# Set with duplicate elements
set = {1, 2, 2, 3, 4}
print(set) # Output: {1, 2, 3, 4}

#2.Operations on sets
#membership Testing
set = {1, 2, 3, 4}
print(3 in set) # Output: True
print(5 not in set) # Output: True

#union()or union (|) method
s1={1,2,3}
s2={3,4,5}
result=s1|s2
print(result) # Output:{1, 2, 3, 4, 5}

#(Intersection or &)
set1= {2,3,4}
set2= {4,5,6}
result= set1 & set2
print(result) #{4}

#( difference or "-")
s1={2,4,6}
s2={6,8,9}
result= s1 - s2
print(result) #{2,4}

#(symmetric Difference or ^)
s1={1,3,5}
s2={5,7,9}
result= s1 ^ s2
print(result) #{1, 3, 7, 9}

#Subset (<= or issubset() method)
a1={1,2}
a2={1,2,3}
print(a1 <= a2) #True

#Superset (>= or issuperset() method)
a1={1,2,3}
a2={1,2}
print(a1 >= a2) #True

#Disjoint Sets (isdisjoint() method)
a1={1,2,3} 
a2={4,5,6}
print(a1.isdisjoint(a2)) #True

#3.Sets Methods
b1= {1,2,3,4}
b2={5,6,7,8}
#add
b1.add(5)
print(b1) #{1, 2, 3, 4, 5}
#remove
b1.remove(5)
print(b1) #{1, 2, 3, 4}
#Discard
b1.discard(2)
print(b1) # {1, 3, 4}
#pop
b1.pop()
print(b1) #{3, 4}
#clear
b2.clear()
print(b2) #set()
#update
b1= {1,2,3,4}
b2={5,6,7,8}
b1.update(b2)
print(b1) #{1, 2, 3, 4, 5, 6, 7, 8}

#intersection_update
names1= {'abhu','chinnu','nani','mouli'}
names2={'mouli','srija','mahi','deepika'}
names1.intersection_update(names2)
print(names1)  #{'mouli'}

#difference_update
names1= {'abhu','chinnu','nani','mouli'}
names2={'mouli','srija','mahi','deepika'}
names1.difference_update(names2)
print(names1) #{'abhu', 'chinnu', 'nani'}

#symmetric_difference_update
names1= {'abhu','chinnu','nani','mouli'}
names2={'mouli','srija','mahi','deepika'}
names1.symmetric_difference_update(names2)
print(names1)
# {'deepika', 'abhu', 'mahi', 'chinnu', 'nani', 'srija'} 

#copy()
fruits={'banana','cherry','mango'}
animals={'lion','tiger','cat'}
food=fruits.copy()
print(food) #{'mango', 'banana', 'cherry'}

#Functions for set
c1={3,5,7}
#len
print(len(c1))
print(c1) #3
#max
print(max(c1))
print(c1) #7
#min
print(min(c1))
print(c1) #3
#sum
c3={1,2,3,4}
print(sum(c3))
print(c3) #10
#sorted
c4={'classwork'}
print(sorted(c4))
print(c1) #['classwork']
#set
l=[1,2,3]
print(set(l)) #{1,2,3}
print(l)

# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen)
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)



