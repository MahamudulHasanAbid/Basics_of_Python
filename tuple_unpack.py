# Tuple Unpacking
# When we create a tuple we normally assign values to it = Packing

# we are also allowed to extract the values back into variables. This is called "unpacking"

fruits = ('apple', 'banana', 'mango', 'orange', 'pineapple')

# (red, green, yellow, orange, blue) = fruits

# (red, green, *blue) = fruits #Using * for Variable-Length Unpacking

(red, *_, blue) = fruits # Ignoring values.
print(red)
# print(green)
print(blue)

# Unpacking in loops

nums = [(1,2), (2,3), (4,5)]

for x,y in nums:
    print(f"{x} {y}")

# .items(), enumerate(), zip(). All these have the unpacking behavior.

stock = {"apples": 10, "bananas": 24, "mangos": 15}

for fruit, count in stock.items():
    print(f"{fruit} = {count}")

# ----------------------------

fruits = ["apple", "banana", "mango"]

for index, fruits in enumerate(fruits):
    print(f"{index} no. position = {fruits}")
# -----------------------------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name} scores {score} and grade is: {grade}")
  
# Exercise 12. Swap two elements at given indices
list6 = [1,2,3,5,4,6]

list6[3], list6[4] = list6[4], list6[3] # tuple unpacking
print(list6)
