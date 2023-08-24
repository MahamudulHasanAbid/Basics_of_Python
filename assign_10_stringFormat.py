'''Develop a program that takes a list of names and their corresponding ages as input and outputs a formatted string that presents the names and ages in a visually appealing way.'''

num = int(input("Enter number of people: "))
info = []
for i in range(num):
    name = input("Name: ")
    age = input("age: ")
    info.append((name,age))
for name,age in info:
    print(f"{name} is {age}")