# Exercise 1: Define an Empty Vehicle Class
# Exercise 2: Vehicle Class with Instance Attributes
# Exercise 3: Rectangle Class with Area & Perimeter
# Exercise 4: Student Class with Average Grade
# Exercise 5: Product Class with Stock Value Calculator
# Exercise 6: Bank Account with Deposit & Overdraw Protection
# Exercise 7: Light Class with On/Off State Toggle
# Exercise 8: User Class with Password Validation
# Exercise 9: Temperature Class with Unit Converters
# Exercise 10: Notebook Class with Add & Display Notes
# Exercise 11: Coffee Machine with Multi-Resource Tracking
# Exercise 12: Shared Class Attribute Across Instances
# Exercise 13: Bus Subclass Inheriting from Vehicle
# Exercise 14: verride Parent Method Using super()
# Exercise 15: Add Maintenance Fee in Child Class via super()
# Exercise 16: Polymorphism with Dog & Cat speak()
# Exercise 17: Full-Time vs Part-Time Employee Pay Logic
# Exercise 18: Shape Subclasses with Custom area() Methods
# Exercise 19: Media Subclasses with Type-Specific Attributes
# Exercise 20: Discounted Order Subclass with 10% Off
# Exercise 21: Vehicle Class Hierarchy with Bike, Truck & Bus
# Exercise 22: Identify Object’s Class Using type()
# Exercise 23: Type Checking with isinstance() & issubclass()
# Exercise 24: Vector Addition Using add Overloading
# Exercise 25: Cart Length Using len Overloading
# Exercise 26: Private Balance with Property Getter & Setter
# Exercise 27: Callable Object Class Using call
# Exercise 28: Flight Class with Passenger Capacity Check
# Exercise 29: Zoo Class that Feeds All Animals
# Exercise 30: Character Class with Auto Level-Up Logic
# Exercise 31: Playlist Class with Add, Remove & Shuffle

# Exercise 1:

class Vehichle:
    pass
print(Vehichle)

# Exercise 2:Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.

class Vehichle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
toyota = Vehichle(210, 50)
print(f" Toyota has {toyota.max_speed} km/h max speed where mileage is: {toyota.mileage} km/l")

# Exercise 3: Write a Python program to create a Rectangle class with length and width as instance attributes,
#  and two methods: area() that returns the area and perimeter() that returns the perimeter.

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width        

    def area(self):
        rec_area = self.width * self.length
        return rec_area 
    def perimeter(self):
        rec_perimeter = 2*(self.width + self.length)
        return rec_perimeter
    
obj = rectangle(8, 5)

print(f"The area is: {obj.area()} \nThe perimeter is: {obj.perimeter()}")


# Exercise 4: Write a Python program to create a Student class that stores a student’s name and a list of marks. 
# Add a method average() that calculates and returns the average of all marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        return sum(self.marks)/ len(self.marks)

std = Student('Mridul', [45,32,44,31,39])
print(f"Student name: {std.name}.\nAverage mark: {std.avg()}")

# Exercise 5: Write a Python program to create a Product class with three instance attributes: name, price, and quantity. 
# Add a method total_value() that returns the total stock value by multiplying price by quantity.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        total_stock = self.price * self.quantity
        return total_stock
    
prod_info= Product('Oil', 325.23, 193)
print(f"Product name: {prod_info.name} and total costs:{prod_info.total_value():.2f}")
        

# Exercise 6: Bank Account with overdrawn protection
# Write a Python program to create a BankAccount class with a balance attribute and two methods:
#  deposit(amount) that adds funds to the balance, 
# and withdraw(amount) that deducts funds but prevents the balance from going below zero.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"After deposit balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"After withdraw, balance: {self.balance}")
        else:
            print(f"Insufficient fund.")

ac_01 = BankAccount(20000)
print(f"Balance: {ac_01.balance}")
depost = ac_01.deposit(2000)
withdrw = ac_01.withdraw(5000)

#Exercise7: Write a Python program to create a Light class with three methods: turn_on() that switches the light on, 
# turn_off() that switches it off, and status() that reports whether the light is currently on or off.

class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"Light is ON") 

    def turn_off(self):
        self.is_on = False

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current Status: {state}")
    
light = Light()

light.turn_on()
light.status()
light.turn_off()
light.status()

# Exercise 8: Write a Python program to create a User class that stores a username and a password.
#  Add a check_password(input_password) method 
# that returns True if the input matches the stored password, and False otherwise.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def check_password(self, input_password):
        return input_password == self.password

obj1 = User("Nahid", 'pas01234')
print(obj1.check_password('pas01234'))
print(obj1.check_password('pas012'))

# Exercise 9: Write a Python program to create a Temperature class that stores a temperature in Celsius. 
# Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, 
# and to_kelvin() that converts and returns the value in Kelvin.

class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        fahrenheit = (self.celcius * (9/5)) + 32
        print(f" {self.celcius} deg celcius is equal {fahrenheit} deg fahrenheit.")        
    def to_kelvin(self):
        kelvin = self.celcius + 273.15
        print(f" {self.celcius} deg celcius is equal {kelvin} kelvin.") 

obj2 = Temperature(100)

obj2.to_fahrenheit()
obj2.to_kelvin() 

# Exercise 10: Write a Python program to create a Notebook class that maintains an internal list of notes. 
# Add an add_note(note) method that appends a new note to the list, 
# and a show_notes() method that prints all stored notes.

class Notebook:
    def __init__(self):
        self.notes = []
    def add_note(self, note):
        return    self.notes.append(note)
    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i} = {note}")

notebook = Notebook()

notebook.add_note("Purchase home")
notebook.add_note("Launch a business")
notebook.show_notes()

# Exercise 11.  Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). 
# Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, 
# and prints an appropriate message in either case.

class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    
    def make_latte(self):
        water_needed = 200
        coffee_needed = 20
        milk_needed = 150

        if self.water>= water_needed and self.coffee >= coffee_needed and self.milk>=milk_needed:
            self.water -= water_needed
            self.coffee -= coffee_needed
            self.milk -= milk_needed
            print(f"Have your best latte!\nRemaining water:{self.water}\nRemaining coffee:{self.coffee}\nRemaining milk:{self.milk}")
            print("---------------------------------------------------")
        else:
            print(f"Check and fill the ingridients if needed...")

machine = CoffeeMachine(400, 50, 300)

machine.make_latte()
machine.make_latte()
machine.make_latte()
