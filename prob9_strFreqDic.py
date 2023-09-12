'''Problem 9: Write a function to find the frequency of each character in a given string and store it in a dictionary.
   - Guideline: Use a loop to iterate through the string, counting each character's frequency using a dictionary.'''

Topic = "Learning python dictionary and Function topic"

def char_frequency(string):
    dic={}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic
result = char_frequency(Topic)
print(result)