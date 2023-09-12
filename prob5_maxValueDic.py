'''Problem 5: Given a dictionary, find the key with the maximum value.
   - Guideline: Use the `max()` function with a custom key function or a list comprehension to find the key with the maximum value.'''
def max_value(space):
    if not space:
        return None
    return max(dic,key = lambda i: dic[i]) #For each key 'i' get value associated with that key in dictionary. Lambda returns a value of dictionary

dic = {'a':2,'b':7,'c':1,'d':9}

max_key = max_value(dic)
print(max_key)


