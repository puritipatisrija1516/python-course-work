#Dictionary
#1.dictionary example
d_name={"name": "srija","age":"21","course":"python"}
print(type(d_name)) #<class 'dict'>

#2.Dictionary Operators
#Accessing values
d={"name":"srija","age":21,"course":"python"}
print(d["name"]) #Output: srija
print(d.get("age"))  #Output: 21

#Differenc Between dict[key] and dict.get(key)
d={"name":"srija","age":21,"city":"Nellore"}
print(d.get("course", "Not available")) #Output:Not available

#Adding and Updating Items
d={"name":"srija","age":21,"city":"Nellore"}
d["course"]="python"
print(d) 
#Output: 'name': 'srija', 'age': 21, 'city': 'Nellore', 'course': 'python'}

#3.Removing Items from a Dictionary
#Using pop()
details={"name":"srija","age":21,"branch":"ece","course":"python"}
age=details.pop("age")
print(age)
print(details)
#{'name': 'srija', 'branch': 'ece', 'course': 'python'} 

#Using del()
del details["course"]
print(details) #Output: {'name': 'srija', 'branch': 'ece'}

#Using popitems
details.popitem()
print(details) #Output: {'name': 'srija'}

#Using Clear()
details.clear()
print(details) #Output:{}

#dict.update
d={"name":"srija","branch":"ece","course":"python"}
d.update({"age":21})
print(d)
#Output:{'name': 'srija', 'branch': 'ece', 'course': 'python', 'age': 21}

#4.Functions for Dictionaries
#len()
d={"name":"srija","branch":"ece","course":"python"}
print(len(d)) #3
#max()
print(max(d)) #name
#min()
print(min(d)) #branch
#sorted()
print(sorted(d)) #['branch', 'course', 'name']

#6.Nested Dictionaries
students = {
"srija": {"age": 21, "course": "CS"},
"mahi": {"age": 22, "course": "Math"}
}
print(students["srija"]["course"]) # Output: CS
print(students["mahi"]["course"]) #Output: Math

