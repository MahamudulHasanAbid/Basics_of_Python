number = [2,1,3,4,7,9,8]
print(number)
# print(type(number))
number.sort()
print(number)
number.sort(reverse=True)
print(number)

companies = [
    ('Google', 2019, 134.89),
    ('Apple', 2019, 290.32),
    ('Facebook', 2018, 80.8)
]
print(companies)
print(companies[2])
print("..............................")
# def sort_key(company):
#     return company[2]
# companies.sort(key = sort_key, reverse=True)

companies.sort(key = lambda company:company[2], reverse=True)
print(companies)
print("...............................")
new_sort = sorted(companies)
print(companies)
print(new_sort)