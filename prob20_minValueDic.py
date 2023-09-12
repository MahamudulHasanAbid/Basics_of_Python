'''Problem 20: Write a program that finds the key with the minimum value in a dictionary.
    - Guideline: Use the `min()` function with a custom key function or a list comprehension to find the key with the minimum value.'''

dic = {
    'a':2,
    'n':9,
    'b':1,
    'k':7
}
def min_value(dic):
    for i in dic:
        if not dic:
            return None
        else:
            return min(dic,key = lambda i:dic[i])
        
result = min_value(dic)
print(result)