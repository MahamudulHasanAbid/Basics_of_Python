'''Problem 8: Create a dictionary of words as keys and their lengths as values from a list of words.
   - Guideline: Use a loop to iterate through the list of words and add key-value pairs to the dictionary.'''

dic_list = ['Universe','IT','Institute']
dic={}

for i in dic_list:
    dic[i]=len(i)

print(dic)




