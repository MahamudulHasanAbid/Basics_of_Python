'''Problem 6: Write a program to find the sum of all values in a dictionary.
   - Guideline: Use a loop to iterate through the dictionary's values and add them up.'''
dic = {'a':2,'b':7,'c':1,'d':9}

def sumOfDic(space):
    sum = 0
    for i in space:
        sum = sum+ space[i]
    return sum

add = sumOfDic(dic)
print(add)