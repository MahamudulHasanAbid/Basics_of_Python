'''Dictionary is the most important Data structure in Python'''

# Exercise 1: Basic Dictionary Operations
# Problem Statement: Write a Python program to add a new key-value pair to a dictionary, modify an existing value, 
# and access a specific key.

student = {"name": "Alice", "age": 20, "grade": "B"}

student.update({"city": "New york"})
student["age"] = 21
print(student)
name = student.get("name")
print(f"Name: {name}")

# Exercise 2: Dictionary Operations
# Problem Statement: Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, 
# and check whether a given key exists.

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

car.pop("color")
print(car)

x = car.items()
print(x)

y = "color" in car
z = "brand" in car

print(f"Color exist: {y}")
print(f"Brand exist: {z}")

# Exercise 3: Dictionary from Two Lists

keys = ["name", "age", "city"] 
values = ["Bob", 25, "London"]

info = dict(zip(keys, values))
print(info)

# Exercise 4: Clear Dictionary
# Problem Statement: Write a Python program to remove all items from a dictionary 
# while keeping the dictionary object itself intact.

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

inventory.clear()
print(inventory)

# Exercise 5: Merge Dictionaries
# Problem Statement: Write a Python program to combine two dictionaries into a single dictionary.
# If both dictionaries share a key, the value from the second dictionary should take precedence.

dict1 = {"a": 1, "b": 2} 
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)
# Or we can do this
merged = dict1 | dict2
print(merged)

# Exercise 6: Access Nested Dictionary
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}

# city = person["address"]["city"]
# print(city)

city = person.get("address", {}).get("city")
print(city)

# Exercise 7: Access ‘history’ Key From a Nested Dictionary

student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

history_grade = student["grades"]["history"]
print(f"History grade: {history_grade}")

# Exercise 8: Initialize Dictionary with Default Values
# Problem Statement: Write a Python program to create a dictionary from a list of keys,
#  assigning the same default value to every key.

keys = ["math", "science", "english", "history", "science"] 
default = 0

# dict_keys = dict.fromkeys(keys,default)
# print(dict_keys)
# or we can do this:
dict_keys = {i: default for i in keys} # it gives each key its own independent list.
print(dict_keys)

# Exercise 9: Rename a Key of Dictionary
employee = {"fname": "John", "age": 30, "dept": "Engineering"}

# employee["first name"] = employee.pop("fname")
# print(employee)

# Or this can be done in a better way:
up_employee = {("first name" if i == "fname" else i):j for i,j in employee.items()}
print(up_employee)

# Exercise 10: Delete a List of Keys

product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}

remove_keys = ["stock", "warehouse"]

final_product = {i:j for i,j in product.items() if i not in remove_keys}

print(final_product)

# Exercise 11: Check Value Existence
# Problem Statement: Write a Python program to verify whether a specific value is present anywhere in a dictionary.

roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}

def checker(dict,j):
    return j in dict.values()
     
checker1 = checker(roles, "editor")
checker2 = checker(roles, "manager")

print(checker1)
print(checker2)

# Exercise 12: Sum All Values
expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}

# total = sum(expenses.values())
# print(total)
total = 0
for i in expenses.values():
    total += i
print(total)

# Exercise 13: Extract Subset of Keys
# Problem Statement: Write a Python program to create a new dictionary
# containing only a specified subset of keys from an existing dictionary.

user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}

extract = ["id", "username", "email"]

base_user = {i:j for i,j in user.items() if i in extract}

print(base_user)

# Exercise 14. Map two lists

attributes = ["brand", "model", "year", "color"]
details = ["Honda", "Civic", 2023, "silver"]

# new_list = []

# for i in zip(attributes, details):
#     new_list.append(i)
# print(type(new_list))
# print(dict(new_list))

new_list = dict(zip(attributes, details))
print(new_list)

# Exercise 15: Count Character Frequencies
text = "hello world how is every wonder."

text_freq = {}
for i in text:
    text_freq[i] = text_freq.get(i, 0) + 1

print(text_freq)

# Exercise 16: Modify Nested Dictionary
# Change the city to munich

company = {
    "name": "TechCorp",
    "location": {"city":"Berlin", "Country": "Germany"}
}

company["location"]["city"] = "Munich"
print(company)

# Exercise 17: Update Deeply Nested key
# Update Students to 35

data = {
    "school": {
        "department": {
            "class": {
                "teacher": "Mr. Smith",
                "students": 30
            }
        }
    }
}

data["school"]["department"]["class"]["students"] = 35
print(data)


