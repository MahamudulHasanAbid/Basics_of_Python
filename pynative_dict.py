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

# Exercise 18: Dictionary Comprehension.
# Write a Python program to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line

sqr_num = {i:i*i for i in range(1,11)}
print(sqr_num)

# Exercise 19: Filter Dictionary
# keep only students scores greater than 60

scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

passed_scores = {i:j for i,j in scores.items() if j>60}
print(passed_scores)

# Exercise 20: Key of Minimum Value

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

low_val = min(stock, key = stock.get)
# low_val = min(dict.items(stock), key= lambda i: i[1])
print(low_val) 

# Exercise 21: Key of Maximum Value

scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}

top_scorer = max(scores, key=scores.get)
# top_score = max(dict.items(scores), key = lambda i: i[-1])
top_score = max(scores.values())

all_top = {i:j for i,j in scores.items() if j==top_score}
print(top_scorer)
print(top_score)
print(all_top)

#Exercise 22: List of Tuples to Dictionary
# Problem Statement: Write a Python program to convert a list of key-value tuples into a dictionary without using any loops.

pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]

dict_paris = dict(pairs)
print(dict_paris)

# Exercise 23: Find Common Keys

d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"b": 20, "c": 30, "d": 40}

# common= set(d1).intersection(set(d2))
common = d1.keys() & d2.keys()
print(common)
print(type(common))

# Exercise 25: Dictionary Intersection

d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"a": 1, "b": 99, "c": 3}

common = d1.keys() & d2.keys()

common_val = {i:d1[i] for i in common if d1[i] == d2[i]}
print(common_val)

# Exercise 26: Word Count

text = "the cat sat on the mat the cat"
counter_dict ={}
for i in text.lower().split():
    counter_dict[i] = counter_dict.get(i, 0) + 1

print(counter_dict)

# Remove NONE values

data = {"name": "Alice", "age": None, "city": "Paris", "score": None}

clean_data = {i:j for i,j in data.items() if j is not None}

print(clean_data)

# Exercise 28: Sort Dictionary by Keys

data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}

sort_data = dict(sorted(data.items()))

print(sort_data)

# Exercise 29: Sort Dictionary by Values

scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

sort_dict = dict(sorted(scores.items(), key= lambda i:i[1], reverse= True))

print(sort_dict)

# Exercise 30: Unique Values Check:

data = {"a": 1, "b": 2, "c": 3, "d": 2}

unique_data = set(data.values())

res = len(data) == len(unique_data)

print(res)

# Exercise 31: Check for Subset

main = {"a": 1, "b": 2, "c": 3, "d": 4}
subset = {"a": 1, "c": 3}

is_subset = subset.items() <= main.items()

print(res)

# Exercise 32: Sort Dictionary by Value Length

words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

print(words.items())
sor_words = dict(sorted(words.items(), key = lambda i: len(i[1])))
print(sor_words)

# Exercise 33: Key with Longest List

data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}

item = max(data.items(), key= lambda i: len(i[1]))[0]
print(item)

# Exercise 34: Convert Dictionary to JSON
import json

person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}

res = json.dumps(person, indent=4)
print(res)

# Exercise 35: Invert Dictionary
# Problem Statement: Write a Python program to invert a dictionary by swapping its keys and values, so each original value becomes a key and each original key becomes the corresponding value.

original = {"a": 1, "b": 2, "c": 3}

swap = {i:j for j,i in original.items()} # values must be unique
print(swap)

# Exercise 36: Invert Dictionary with duplicates

original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

invert_dic = {}
for i,j in original.items():
     invert_dic.setdefault(j,[]).append(i)

print(invert_dic)

# Exercise 37: Flatten Nested Dictionary
nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}

