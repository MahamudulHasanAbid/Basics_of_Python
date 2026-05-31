# def sec_try(name, age):
#     print(name,"\n",str(age))
# sec_try("Abid",25)
# sec_try("Abdullah",5)
# sec_try("Meherima",1.5)

# def calculation(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b 
#     return add, sub, mul, div
# add,sub,mul,div = calculation(42,8)
# print(add)
# print(sub)
# print(mul)
# print(div)


# def outer(a,b):
#     def inner(a,b):
#         return a+b
#     return inner(a,b)+5
# print(outer(9,3))

'''Non keyword and Keyword argument = Variable length of argument'''
# Nonkeyword argument: *args or *anything
def Hello(*call):
    for i in call:
        print(i)
Hello("This is a *args practice part.","What else can be done","Practice and practice more"," 42 is the serial")

# Keyword argument: **args or **anything
# def intro(**info):
#     for i,j in info.items():
#         print(f"{i} == {j}") #i=key,j=value
# intro(Name = 'Mahamudul Hasan',ID = "CSE3033",Dept = "Science", passing_year=2023)

# Write a recursive function to calculate the factorial.
def factorecur(n):
    if n<0:
        return f"There is no factorial for negative number."
    return n* factorecur(n-1) if n>0 else 1

factres= factorecur(5)
print(factres)

# Exercise 14(pynative): Create a lambda function that squares a given number
#lambda arguments: expression
num = 4
square = lambda n: n**2

sqr_res = square(num)
print(sqr_res)

# Exercise 15(pynative):Use a lambda with the filter() function to get all even numbers from a list

num = [1,2,3,4,5,6]

even =list(filter(lambda x: x%2==0, num)) 
print(type(even))
print(even)

# Exercise 17(pynative): Use a lambda with the sorted() function to sort a list of tuples
# based on the second element.

tup_list = [('Apple', 5), ('Banana', 2), ('date', 1), ('Guava',3)]

srt = list(sorted(tup_list, key = lambda x: x[1]))

print(srt)

# Exercise 16(pynative): Use a lambda with the map() function to double each element in a list
num = [1,2,3,4,5,6]

doub_list = list(map(lambda x: x*2, num))

print(doub_list)

# Exercise 18(pynative): Create higher-Order function
# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, 
# and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
# The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.
# A higher-order function:
#  Takes a function as input
#  Calls that function

def apply_operation(func, x, y):
    return func(x,y)

def addition(x,y):
    return x+y

sum= apply_operation(addition, 3,2)
print(sum) 

def subtraction(x,y):
    return x-y
minus= apply_operation(subtraction, 3,2)
print(minus)

mul = lambda x,y: x*y
multiplication = apply_operation(mul, 3,2)
print(multiplication)

div = lambda x,y: x/y
division = apply_operation(div, 3,2)
print(division)
