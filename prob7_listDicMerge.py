'''Problem 7: Given a list of dictionaries, merge them into a single dictionary.
   - Guideline: Iterate through the list and use the same techniques as in Problem 3 to merge dictionaries.'''
list_dic=[
    {'Name':'Mahmud Hasan','Id':330},
    {'Class':'11','Game': 'Cricket'}]

dic = {}

for i in list_dic:
    dic.update(i)
print(dic)



    
