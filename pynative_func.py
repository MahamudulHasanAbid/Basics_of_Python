'''
Table of contents
Exercise 1: Create a function in Python
Exercise 2: Create a function with variable length of arguments
Exercise 3: Return multiple values from a function
Exercise 4: Create a function with a default argument
Exercise 5: Create an inner function
Exercise 6: Create a recursive function
Exercise 7: Assign a different name to function and call it through the new name
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Exercise 9: Find the largest item from list
Exercise 10: Call Function using both positional and keyword arguments
Exercise 11: Create a function with keyword arguments
Exercise 12: Modifies global variable
Exercise 13: Write a recursive function to calculate the factorial
Exercise 14: Create a lambda function that squares a given number
Exercise 15: Use a lambda with the filter() function to get all even numbers from a list
Exercise 16: Use a lambda with the map() function to double each element in a list
Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element
Exercise 18: Create Higher-Order Function
'''

#2. Write a program to create a function func1() that accepts 
# a variable number  of arguments and prints each of their values.

def func1(*args):
    for i in args:
        print(i)

func1(20,40,60)

# Write a function calculation() that accepts two variables and calculates 
# both their addition and subtraction. The function should 
# then return both the sum and the difference in a single return statement.

def calculation(a,b):
    add = a+b
    sub = a-b

    return add, sub

res = calculation(40,10)
print(res)

#Write a program to create a function show_employee() with the following specifications:
# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000

def showEmployee(name, salary=9000):
    return f'name:{name} salary: {salary}'

output1 = showEmployee("Jessa")
output2 = showEmployee("Jhon", 20000)
print(output1)
print(output2)

# Create a program with nested functions to perform an addition calculation as follows:

# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def outer(a,b):
    def inner(a,b):
        return a+b
    add = inner(a,b)
    return add+5
result = outer(5,5)
print(result)




# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself repeatedly.

def sum(n):
    return n + sum(n-1) if n>0 else 0
res = sum(10)
print(res)

# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. 
# Call this function using both positional and keyword arguments.

def describe_pet(animal_type, pet_name):
    return f'animal type:{animal_type} pet_name: {pet_name}'

posarg = describe_pet('Cat', 'Don')
print(posarg)

keyarg = describe_pet(
    animal_type='Dog',
    pet_name= 'Puppy'
)
print(keyarg)

# Create a function print_info(**kwargs) that accepts keyword arguments and prints the key-value pairs. 
# Call it with different keyword arguments

def print_info(**kwargs):
    return f"Name: {kwargs['name']}, Age: {kwargs['age']}"

res = print_info(name='bob', age=12)
print(res)

#Flexible version

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
res = print_info(name='bob', age=12)

# Write a recursive function to calculate the factorial of a non-negative integer.
def fact(n):
    if n<0:
        return "Factorial is not for negative numbers."
    return n * fact(n-1) if n>0 else 1
res = fact(3)
print(res)
# Exercise 14: Create a lambda function that squares a given number
   #lambda arguments: expression
square = lambda x: x**2
num = 5
square_number = square(num)
print(f"The square of {num} is {square_number}")

# Exercise 15: Use a lambda with the filter() function to get all even numbers from a list
num=[1,2,3,4,5,6]

even= list(filter(lambda c: c%2 == 0, num))
print(f'even numbers: {even}')

# Exercise 16: Use a lambda with the map() function to double each element in a list
num = [1,2,3,4,5,6]
double = list(map(lambda x:x*2, num))
print(double)

# Exercise 17: Use a lambda with the sorted() function 
# to sort a list of tuples 
# based on the second element
tup_list = [('Apple',5), ('Banana',2), ('date',1), ('Guava', 3), ('Pinapple', 4)]
srt = list(sorted(tup_list, key = lambda x: x[1] ))
print(srt)
# Exercise 18: Create Higher-Order Function
# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, 
# and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
# The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.
# A higher-order function:
#  Takes a function as input
#  Calls that function

def apply_operation(func,x, y):
    return func(x,y)
def add(x,y):
    return x+y
sum = apply_operation(add,2,3)
print(sum)

sub = lambda x,y: x-y
res_sub = apply_operation(sub,3,2) # sub = func
print(res_sub)

mul = lambda x,y: x*y
res_mul= apply_operation(mul,2,2) # mul = func
print(res_mul)

