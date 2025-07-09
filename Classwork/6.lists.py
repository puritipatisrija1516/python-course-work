#1.list
my_list=[1,2,3,4]
print(type(my_list)) #Output: <class 'list'>
#2.emptylist[]
my_list=[]
my_list2= list() #Output: <class 'list'>

#list with Elements
int=[1,2,3]  #Output: [1, 2, 3]
fruits=["mango","banana","orange"] #Output: ['mango', 'banana', 'orange']
mixed=[10,3.5,"banana",3+2j] #Output: [10, 3.5, 'banana', (3+2j)]
print(int,fruits,mixed)

#List with Nested list
nested_list=[[1,2,3],['a','b','c']]
print(nested_list)  #Output: [[1, 2, 3], ['a', 'b', 'c']]

#list using list() constructor
t_l=list((1,2,3)) #Converting tuple to list
s_l=list("python")
print(s_l) #Output:  ['p', 'y', 't', 'h', 'o', 'n']

#3.Accesing Elements in a List
#Using Indexing
list=("deepika", "Raji","mahi")
print(list[0]) #Output: deepika
print(list[1]) #Output: Raji
print(list[2])  #Output: mahi

#Using slicing
num=[10,20,30,40,50]
print(num[1:3]) #Output: [20, 30]
print(num[0:2]) #Output: [10, 20]
print(num[0:]) #Output: [10, 20, 30, 40, 50]
print(num[:4]) #Output: [10, 20, 30, 40]
print(num[:]) #Output: [10, 20, 30, 40, 50]

#4.Modifying lists
#changing elements
num=[1,2,3,4,5]
num[3]=50
print(num) #Output:[1, 2, 3, 50, 5]
 
#5.adding elements
#append()
num=[10,20,30,40,50]
num.append(60)
print(num) #Output: [10, 20, 30, 40, 50, 60]
#insert()
num=[20,40,60,80]
num.insert(2,100)
print(num)   #Output:[20, 40, 100, 60, 80]
#extend()
num=[10,30,50]
num.extend([70,90,20])
print(num)   #Output: [10, 30, 50, 70, 90, 20]

#6.Removing elements
#remove()
num=[10,20,30,40,50,60]
num.remove(60)
print(num) #Output: [10, 20, 30, 40, 50]
#pop()
num.pop(2)
print(num) #Output: [10, 20, 40, 50]
num.pop()
print(num)  #Output: [10, 20, 40]
#delete()
num=[10,20,30,40,50,60]
del num[5]
print(num)  #Output: [10, 20, 30, 40, 50]
#clear()
num.clear()
print(num)  #Output: []

#7.List Methods
l=[22,33,44,55,66,22,33]
print(l.count(22)) #Output: 2
print(l.index(55)) #Output: 3
l.sort()
print(l) #Output: [22, 22, 33, 33, 44, 55, 66]
l.reverse()
print(l)  #Output: [66, 55, 44, 33, 33, 22, 22]
l1=l.copy()
print(l1)  #Output: [66, 55, 44, 33, 33, 22, 22]

m=[20,30,40,50,60]
m.sort() #sorting
print(m) #[20,30,40,50,60]
print(sorted(m)) #sorted[20,30,40,50,60]
print(len(m)) #5
print(min(m)) #20
print(max(m)) #60
print(sum(m)) #200
print(any(m)) #True ,else is present
print(all(m)) #True ,else is present