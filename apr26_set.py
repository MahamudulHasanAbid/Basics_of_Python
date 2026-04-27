skills = set()
if not skills:
    print('Empty sets are falsy')

size =len(skills)
print(size)

charecters = set('letter')
print(charecters)
print(len(charecters))

fruits = {'apple', 'banana', 'orange'}
print('banana' not in fruits)

# add item
fruits.add("mango")
print(fruits)

tropical = {'pineapple', 'papaya'}
fruits.update(tropical)
print(fruits)

# remove item
fruits.remove("apple")
print(fruits)

# Set comprehension

tags = {'Django', 'Pandas', 'Numpy'}

lowercase_tags = set()

for i in tags:
    lowercase_tags.add(i.lower())

print(lowercase_tags)

low_tags = set(map(lambda x: x.lower(), tags))
print(low_tags)

# using comprehension
lower_tag = {i.lower() for i in tags}

print(lower_tag)
