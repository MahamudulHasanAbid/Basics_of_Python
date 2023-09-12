'''Problem 3: Write a program to merge two dictionaries.
   - Guideline: Use the `update()` method or dictionary unpacking (`{**dict1, **dict2}`) to merge two dictionaries.
'''

dic1 = {
    'Brand':'Ford',
    'Model':'Mustang Ecoboost',
    'Year' :2013
}
dic2 = {
    'Milage': 25,
    'color' : ['red','blue','green']
}

# dic1.update(dic2)
# print(dic1)

merge_dic = {**dic1, **dic2}
print(merge_dic)


