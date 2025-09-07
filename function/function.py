#python function:
#syntax:
#def function_name():
def my_function():
    print("Hello")
#calling a function:
my_function()
#Arguments:
#funtion with parameters:
def add_numbers(a,b):
    Sum=a+b
    return Sum
#Calling the function:
result = add_numbers(10,20)
print(result)
#return value:
def my_function(x):
    return 5*x
print(my_function(2))
print(my_function(3))
print(my_function(4))
#Function with default parameters:
def greet_person(name="world"):
    print("hello",name)
#calling the function without argument:
greet_person()
#calling the function with an argument:
greet_person("Alice")




