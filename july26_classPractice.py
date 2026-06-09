# Creating a class
class failure:
    x = 5
print(failure)

# Creating an Object
class mycls:
    x = 6
obj1 = mycls()
print(obj1.x)

# Delete Objects
class todel:
    x = 6

obj2 = todel()
print(obj2.x)

del obj2
print(obj2)

# __init__() method in python

class Person:
    def __init__(self, name, age):
        self.nm = name
        self.ag = age

obj1 = Person("Hitler", 189)
print(obj1.nm)
print(obj1.ag)

'''__init__() method will run automatically and no need to call it further.'''

# self parameter links the method to the specific object.
class person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)
o1= person("groot")
o2 = person("Ragnar")

o1.printname()
o2.printname()

# Accessing properties with self
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.model} {self.brand}")

o1 = Car("Toyota", "CHR", 2022)
o2 = Car("Hundai", "Creta", 2021)

o1.display_info()
o2.display_info()

# Calling method with self

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return "Hello, " + self.name
    def welcome(self):
        msg = self.greet()
        print(msg + "! Welcome to the website...")

o3 = Person("Jacky")
o3.welcome()
        
