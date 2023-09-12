def checker(key):
    for i in dic1:
        if i == key:
         print("key is in the dictionary")
         return True 
    print("Key is not in the dictionary") 
    return False
dic1 = {
    'Brand':'Ford',
    'Model':'Mustang Ecoboost',
    'Year' :'2012'
}
checker('ear')



