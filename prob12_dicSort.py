'''Problem 12: Write a program to sort a dictionary by its values.
    - Guideline: Use the `sorted()` function with a custom key function to sort the dictionary items by values.
'''

dic = {'Mahmud':28,'Mabin':22,'Abid':19,'Abed':25}

dic_sort = sorted(dic.items(),key =lambda i:i[1])
print(dic_sort)
sort_dic = {i[0]:i[1] for i in dic_sort}

print(sort_dic)

