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

# Exercise 12:  Write a Python program to create a Vehicle class with a class attribute color = "White" that is shared by all instances.
#  Create two vehicle objects and demonstrate that both share the same default color,
# then show that changing the class attribute updates all instances that have not overridden it.

class Vehicle:
    color = 'White'

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    # def show_data(self):
    #     print(f"{self.name}- Color:{self.color}, speed:{self.speed}")

vehicle_1 = Vehicle("Tesla", 200)
vehicle_2 = Vehicle("Audi", 220)

print(f"{vehicle_1.name}- Color:{vehicle_1.color}, speed:{vehicle_1.speed}")
print(f"{vehicle_2.name}- Color:{vehicle_2.color}, speed:{vehicle_2.speed}")

Vehicle.color = "Red"

print(f"{vehicle_1.name}- Color:{vehicle_1.color}, speed:{vehicle_1.speed}")
print(f"{vehicle_2.name}- Color:{vehicle_2.color}, speed:{vehicle_2.speed}")

# Exercise 13:Write a Python program to create a Vehicle parent class with name and max_speed attributes and a display() method. 
# Then create a Bus child class that inherits everything from Vehicle without adding anything new, 
# and confirm that an instance of Bus can access the parent’s method.

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name} Max Speed:{self.max_speed}")
    
class Bus(Vehicle):
    pass

volvo = Bus("School Bus", "250")
volvo.display()

# Exercise 14: Write a Python program where a Vehicle parent class has a seating_capacity() method that accepts a capacity argument. 
# Create a Bus child class that overrides this method to provide a default seating capacity of 50, using super() to call the parent’s version internally

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        print(f"{self.name} has the maximum capacity of {capacity}")

class Bus(Vehicle):
    def seating_capacity(self):
        return super().seating_capacity(50)

bus1 = Bus("School Bus", 80)

bus1.seating_capacity()

# Exercise 15:  Write a Python program that creates a Vehicle parent class with a base fare, 
# then extends a Taxi child class that adds a 10% maintenance fee on top of the base fare using super().

class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintanance_fee = base_fare * 0.1

    def total_fare(self):
        total = self.base_fare + self.maintanance_fee
        return total
taxi = Taxi(500)

print(f"Total fare with maintanance fee: {taxi.total_fare()}")

#Exercise 16: Write a Python program that defines an Animal base class with a speak() method, 
# then overrides it in Dog and Cat subclasses to return their respective sounds.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Mewao"

dog = Dog("Dog")
cat = Cat("Cat")

print(f"{dog.name} sound: {dog.speak()}")
print(f"{cat.name} sound: {cat.speak()}")

#Exercise 17: Write a Python program that defines an Employee base class,
#  then creates FullTimeEmployee and PartTimeEmployee subclasses,
#  each implementing different pay calculation logic.

class Employee:
    def __init__(self, name):
        self.name = name
     
    def calculate_pay(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary/12

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked * 24
    

ft = FullTimeEmployee("Asadullah", 400000)
pt = PartTimeEmployee("Mizan", 400, 9)

print(f"{ft.name} get {ft.calculate_pay():.2f} BDT per month.")
print(f"{pt.name} get {pt.calculate_pay():.2f} BDT per month.")

# Exercise 18. Write a Python program that defines a Shape base class with an area() method, 
# then implements it in Circle, Square, and Triangle subclasses using the appropriate geometric formulas.

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(7)
square = Square(4)
triangle = Triangle(6, 8)

print(f"Circle area: {circle.area()}")
print(f"Square area: {square.area()}")
print(f"Triangle area: {triangle.area()}")

# Exercise 19:  Write a Python program that defines a Media base class, then creates Book, Magazine, and DVD subclasses, 
# each with type-specific attributes and a describe() method.

class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def show(self):
        return f"{self.title} - Rs.{self.price}"
class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author
    def show(self):
        return f"{self.title} by {self.author} -RS{self.price}"

class Magazine(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author
    def show(self):
        return f"{self.title} by {self.author} -RS{self.price}"

class DVD(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author
    
    def show(self):
        return f"{self.title} by {self.author} -RS{self.price}"

items=[
    Book("Hath a khori", 100, "Hakim"),
    Magazine("Hath a khori", 200, "Hasim"),
    DVD("Vice city", 300, "Moron")
]

for item in items:
    print(item.show())

# Exercise 20. Write a Python program that creates an Order class with a total amount, 
# then creates a DiscountedOrder subclass that applies a 10% discount to the total.

class Order:
    def __init__(self, item, total_amount):
        self.item = item
        self.total_amount = total_amount

    def final_amount(self):
        return self.total_amount

class DiscountedOrder(Order):
    def __init__(self, item, total_amount):
        super().__init__(item, total_amount)


    def final_amount(self):
        final_amount = self.total_amount * 0.9
        return final_amount 
    
price = DiscountedOrder('Orange',220)

print(f"Price:{price.total_amount} \nAfter Discount:{price.final_amount():.2f}")

# Exercise 21.  Write a Python program that defines a Vehicle base class 
# and creates Bike, Truck, and Bus subclasses, 
# each defining a unique max_speed attribute and a describe() method.

class Vehicle:
    def __init__(self,name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def describe(self):
        return "Some Text"

        
class Bike(Vehicle):
    def __init__(self,name, max_speed):
        super().__init__(name, max_speed)
    def describe(self):
        return f"{self.name} has max speed: {self.max_speed}"
    
class Truck(Vehicle):
    def __init__(self,name, max_speed):
        super().__init__(name, max_speed)
    def describe(self):
        return f"{self.name} has max speed: {self.max_speed}"
    
class Bus(Vehicle):
    def __init__(self,name, max_speed):
        super().__init__(name, max_speed)
    def describe(self):
        return f"{self.name} has max speed: {self.max_speed}"
    
bike = Bike("Yamaha", 180)
truck = Truck("Mahindra", 80)
bus = Bus("Volvo", 280)

print(bike.describe())
print(truck.describe())
print(bus.describe())

#Exercise 22: Write a Python program that creates objects from multiple classes 
# and uses the built-in type() function  to identify which class each object belongs to.
class Dog:
    pass
class Cat:
    pass
class Vehicle:
    pass

d = Dog()
c = Cat()
v = Vehicle()

objects = {'d':d, 'c':c,'v':v}

for name,object in objects.items():
    print(f"{name} is of type:{type(object)}")

### Exercise 23: Write a Python program that uses isinstance() to check whether an object is an instance of a given class,
#  and issubclass() to check whether one class is a subclass of another.

class Animal:
    pass    
class Dog(Animal):
    pass
d = Dog()
# isinstance(obj, ClassName), issubclass(ChildClass, ParentClass)

print("Is d an instance of Dog?", isinstance(d, Dog))
print("Is d an instance of Animal?", isinstance(d, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))

# Exercise 24: Write a Python program that creates a Vector class representing a 2D vector, 
# and implements the __add__ dunder method so that two Vector objects can be added using the + operator.

# operator overloading, a powerful OOP feature that lets your custom classes behave like built-in types.

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2,5)
v2 = Vector(4,3)

result = v1 + v2
print(result)

# Exercise 25: Write a Python program that creates a Cart class that stores a list of items,
#  and implements __len__ so that calling len(cart) returns the number of items currently in the cart.

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)
    
cart = Cart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Mango")

print(f"Length of cart items: {len(cart)}")

# Exercise 26: Write a Python program that creates a BankAccount class where the balance is stored as a private attribute __balance, 
# and exposed safely through a @property getter and a setter that validates the value before updating it.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount<0:
            print(f"Balance can not be negative.\n Invalid Balance...")
        else:
            self.__balance = amount
        
    def deposit(self, amount):
        self.balance = self.__balance + amount
    
account = BankAccount(1000)
print("Current balance:", account.balance)

account.deposit(500)
print("Current balance:", account.balance)

account.balance = -200

# Exercise 27: Write a Python program that creates a Multiplier class which stores a factor, 
# and implements __call__ so that an instance of the class can be invoked directly like a function 
# to multiply a given number by that factor.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    
triple = Multiplier(10)

print(triple(3))

# Exercise 28: Write a Python program that creates a Passenger class and a Flight class. 
# The Flight class should manage a list of Passenger objects 
# and block further bookings when the seat capacity is reached.

class Passenger:
    def __init__(self, p_id):
        self.p_id = p_id
class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_passanger = []
    
    def book_passanger(self, passanger):
        self.passanger = passanger
        if len(self.current_passanger)>= self.capacity:
            print("Block further Booking")
        else:
            self.current_passanger.append(passanger)

psngr = Flight(4)
psngr.book_passanger('A012')
print(f"{psngr}")

