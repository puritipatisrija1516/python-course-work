#printing Text
print("Hello, World!") #Output:Hello, World!
#printing multiple items
name = "sri"
age = 20
print("Name:", name, "Age:", age) #Name: sri Age: 20
#Using sep to change the separator
print("2024","02","07",sep="-") #2024-02-07
#Using end to control line Endings
print("sri", end=" ") #sri course!
print("course!")      #sri
print("sri\ncourse")  #course

print("Name:\tsri") #Name:   sri
#Output Formatting
#1 Using commas (simple print Method)
name = "sri"
age = 20
score = 97.5
#using commas
print("Name:",name, "Age:", age, "score:", score) #Name: sri Age: 20 score: 97.5
#Using modulo operator(% Formatting)
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score)) #Name: sri | Age: 20 | Score: 97.50
#Using f-strings
print(f"Name: {name} | Age: {age} | score: {score:.2f}") #Name: sri | Age: 20 | score: 97.50
#Using str.format()
print("Name: {} | Age: {} | score: {:.1f}".format(name, age, score)) #Name: sri | Age: 20 | score: 97.5

