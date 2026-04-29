# stocks = {
#     'AAPL': 121,
#     'AMZN': 3380,
#     'MSFT': 219
# }

# new_stocks = {}
# print(type(new_stocks))
# for i,j in stocks.items():
#     new_stocks[i] = j*1.02

# print(new_stocks)

# new_stock = {i: round(j*1.04,2) for(i,j) in stocks.items()}
# print(new_stock)

'''Access Dictionary Items'''
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car["model"]
print(x)

y = car.get("brand")
print(y)

z = car.keys()
print(z)
a = car.values()
print(a)
b = car.items()
print(b)
print(type(b))

'''Change Dictionary Items'''
fruits = {
    "Name": "Mango",
    "Color": "Yellow",
    "Origin":"Bangladesh"
}

x = fruits["Origin"] = "India"

print(fruits)
y = fruits.update({"Color": "Red"})
print(fruits)

'''Add Dictionary Items'''
adval= fruits["Sciname"] = "Mangifera Indica"
print(fruits)

'''Removing Dictionary Items'''
remval = fruits.pop("Sciname")
# del fruits["Sciname"]
print(fruits)

remlast = fruits.popitem()
print(fruits)

fruits.clear()
print(fruits)

# del fruits #No longer exist this dictionary

'''Nested Dictionaries'''
Familymember = {
    "Father":{
        "Name":"M. Dan",
        "Year": 1966
    },
    "Mother":{
        "Name": "Mrs. Lily",
        "Year": 1975       
    },
    "Son1":{
        "Name": "M. Mad",
        "Year": 1997,
        "Wife":"Mrs. Olive",
        "Child1": {
            "Name": "Waterlily",
            "Year": 2021
        },
        "Child2":{
            "Name": "Laalu",
            "Year": 2025

        }
    },
    "Son2":{
        "Name": "M. Madmax",
        "Year": 2017
    }
}
print(Familymember)
