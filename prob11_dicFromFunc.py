'''Problem 11: Write a function that returns a dictionary containing the squares of numbers from 1 to n.
    - Guideline: Use a loop to generate the key-value pairs for the squares.'''

import math
def dic(space):
    dic_f = {}
    for i in range(space):
        key = f'value {i+1}'
        dic_f[key] = math.pow(i+1,2)
    return dic_f
n = 5
result = dic(n)
print(result)
