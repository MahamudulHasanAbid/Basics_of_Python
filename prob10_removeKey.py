'''Problem 10: Write a program that removes a key from a dictionary.
    - Guideline: Use the `pop()` method or the `del` statement to remove a key from the dictionary.
'''

dic = {
    'Brand':'Ford',
    'Model':'Mustang Ecoboost',
    'Year' :'2012'
}
# del dic['Year']
# print(dic)

dic.pop('Year')
print(dic)
