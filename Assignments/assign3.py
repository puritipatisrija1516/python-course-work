questions=[
    "1.what is the output of:print(type((1,)))?"
    "2.which function returns the absolute value of a number?"
    "3.what does the 'in' keywoed do in python?"
    "4.which of these is a valid variable name?"
    "5.what is the output of:print(bool(''))?"
    "6.which keyword is used to exit a loop"
    "7.which is the default return value of a function with no return statement?"
    "8.what is the output of:print(10 % 3)?"
    "9.which method is used to remove the last item from a list?"
    "10.which data type is returned by the input() function?"
    "11.which statement is used to skip the current iteration in a loop?"
    "12.what is the output of:print(5 // 2)?"
    "13.what is the output of:print(len({'a':1.'b':2}))?"
    "14.which operator is used for exponentiation in python?"
    "15.which function gives the largest number in a list?"
    "16.which built-in data type is unordered and mutable?"
    "17.what is the output of:print(type(3.0))?"
    "18.which method is used to change all letters in a string to uppercase?"
    "19.which of these is not a python data type?"
    "20.which keyword is used to define on anonymous function? "
]

#options
options=[
    {"a": "<class 'tuple'>", "b": "<class 'int'>", "c": "<class 'list'>", "d": "<class 'set'>"},
    {"a": "max()", "b": "abs()", "c": "sum()", "d": "round()"},
    {"a": "Imports a module", "b": "Checks membership", "c": "Initializes a loop", "d": "Defines a variable"},
    {"a": "2value", "b": "value_2", "c": "value-2", "d": "value 2"},
    {"a": "True", "b": "False", "c": "None", "d": "Error"},
    {"a": "continue", "b": "break", "c": "pass", "d": "stop"},
    {"a": "0", "b": "None", "c": "False", "d": "Empty string"},
    {"a": "3", "b": "1", "c": "0", "d": "10"},
    {"a": "remove()", "b": "pop()", "c": "delete()", "d": "discard()"},
    {"a": "int", "b": "str", "c": "float", "d": "bool"},
    {"a": "break", "b": "skip", "c": "continue", "d": "pass"},
    {"a": "2", "b": "2.5", "c": "3", "d": "Error"},
    {"a": "1", "b": "2", "c": "3", "d": "Error"},
    {"a": "^", "b": "", "c": "//", "d": "pow"},
    {"a": "max()", "b": "min()", "c": "sum()", "d": "largest()"},
    {"a": "list", "b": "set", "c": "tuple", "d": "dict"},
    {"a": "<class 'float'>", "b": "<class 'int'>", "c": "<class 'decimal'>", "d": "<class 'double'>"},
    {"a": "upper()", "b": "uppercase()", "c": "toUpper()", "d": "capitalize()"},
    {"a": "list", "b": "tuple", "c": "array", "d": "dict"},
    {"a": "func", "b": "def", "c": "lambda", "d": "anon"},

]

#correct options
answers=['a','b','b','b','b','b','b','b','b','b','c','a','b','b','a','b','a','a','c','c']

#Quiz
def quiz_game():
    score = 0
    print("welcome to the python interview Quiz\n")

    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)
        ans=input("your answer (a/b/c/d):").strip().lower()

        if ans== answers[i]:
            print("correct!\n")
            score += 1
        else:
            print("wrong! correct answer is:",answers[i],"\n")

    print("Final score:",score,"/",len(questions))
    if score >= 15:
        print("Excellent! You're ready.")
    elif score >=10:
        print("Good work,revise more.")
    else:
        print("keep learning, you'll improve.")

 #Run it
    quiz_game()                               
