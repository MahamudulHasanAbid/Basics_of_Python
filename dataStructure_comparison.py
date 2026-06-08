'''Creating and Adding'''
# LIST (Duplicates allowed, ordered)
lists = [1, 2]
lists.append(3)         # [1, 2, 3]
lists.extend([4, 5])    # [1, 2, 3, 4, 5]

# SET (Unique elements only, unordered)
sets = {1, 2}
sets.add(3)             # {1, 2, 3}
sets.update([4, 5])     # {1, 2, 3, 4, 5}

# DICTIONARY (Key-Value pairs)
dicts = {'a': 1, 'b': 2}
dicts['c'] = 3          # {'a': 1, 'b': 2, 'c': 3}
dicts.update({'d': 4})  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

'''Updating and Modifying'''
# LIST
lists = [10, 20, 30]
lists[1] = 99           # [10, 99, 30] (Changes index 1)

# SET
sets = {10, 20, 30}
# Sets are unindexed. To "change" 20 to 99, you remove and add:
sets.remove(20)
sets.add(99)            # {10, 30, 99}

# DICTIONARY
dicts = {'a': 10, 'b': 20}
dicts['b'] = 99

'''Deleting and Removing'''
# LIST
lists = ['a', 'b', 'c', 'b']
lists.remove('b')       # ['a', 'c', 'b'] (Removes ONLY the first 'b')
popped = lists.pop(1)   # Removes and returns index 1 ('c')
del lists[0]            # Removes index 0

# SET
sets = {'a', 'b', 'c'}
sets.remove('b')        # {'a', 'c'} (Raises KeyError if 'b' doesn't exist)
sets.discard('z')       # Safe removal. Does nothing if 'z' is missing
popped = sets.pop()     # Removes and returns a random/arbitrary element

# DICTIONARY
dicts = {'a': 1, 'b': 2, 'c': 3}
del dicts['a']          # {'b': 2, 'c': 3}
val = dicts.pop('b')

'''Itering and looping'''
# LIST
for item in lists:
    print(item)

# SET
for item in sets:
    print(item)

# DICTIONARY
for key in dicts:          # Loops through keys
    print(key, dicts[key])

for key, val in dicts.items(): # Loops through both simultaneously
    print(key, val)

# Checking if an item exists (if x in collection) is incredibly fast O(1) for Sets and Dictionaries 
# because they use hash tables behind the scenes. 
# For a List, Python has to scan the whole line O(n), which gets sluggish if your list has millions of items!

