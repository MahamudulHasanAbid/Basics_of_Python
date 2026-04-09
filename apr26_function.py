'''def fun_name():
    print(hi)
    '''

#calling a function

def greet():
    print('hi')
greet()

#Passing information in a function

def greet(name):
    print(f'hi {name}. How is going?')
greet('Mahamud') # here Mahamud is an argument

#Returning a function for reusability

def greet(name):
    return f"Hi {name}"
greeting = greet('Jhon')
print(greeting)

def sum(a,b):
    return a+b
total = sum(10,20)
print(total)

#Keword arguments (make function calls more readable)

def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(
    price = 100,
    discount = 0.1
)

print(f'{net_price: .2f}')

#using **kwargs
def get_net_price(**kwargs):
    return kwargs['price'] * (1-kwargs['discount'])

net_price = get_net_price(
    price =100,
    discount = 0.1
)
print(f'{net_price: .2f}')

'''Recursive Function = When a function call itself.(trees, graphs, binary search)
A recursive function needs to have a condition to stop calling itself.
    def fn():
        #...
        if condition:
            #stop calling itself
        else:
            fn()
        #...    

Before call → going down
After call → coming back up
'''

def count_down(start):
    print(start)
    next = start-1
    if next>0:
        count_down(next)
count_down(3)

#print 1 to 100
def sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
result = sum(100)
print(result)

#Using recursion
def sum(n):
    if n>0:
        return n+ sum(n-1)
    return 0
result = sum(100)
print(result)

#Ternary operator
def sum(n):
    return n+ sum(n-1) if n>0 else 0

result = sum(100)
print(result)
55
'''
Python lambda expressions allow you to define anonymous functions.
Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.
A lambda expression typically contains one or more arguments, but it can have only one expression.

syntax: lambda parameters: expression

'''
