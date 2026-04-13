# A Tuple is a special type of list that can not be changed.
# value can't be changed = immutable.
# Tuple = immutable list.
rgb = ('red', 'green', 'blue')
print(rgb[1])
print(rgb[2])

# Define tuple with a single element.
numbers= (3,)  # A trailing comma is must.
print(type(numbers))

# List
# Accessing elements to the list
numbers = [1,2,3,4,5,6]
print(numbers[3])
print(numbers[-3])

# Modifying, adding, and removing elements 
# list[index] = new value

numbers = [1,2,3,4,5]
numbers[1] = 9 #To change an element.
print(numbers)

numbers[4] = numbers[4]* 3 #To change an element.
print(numbers)

numbers.append(7) #To add an element to the last index.
print(numbers)

numbers.insert(2, 55) #To add an element to the dynamic index.
print(numbers)

del numbers[0] #To delete an element.
print(numbers) 

numbers.pop() #To delete an element to the last index.
print(numbers) 

numbers.pop(1) #To delete an element to the dynamic index.
print(numbers)

numbers.remove(15) #To delete an element by the element.
print(numbers)

# Sort Elements.
guests = ['Mb','Jd', 'Pk']
guests.sort()
print(guests)
guests.sort(reverse=True)
print(guests)

sorted_guests = sorted(guests, reverse = True) # returns a new list
print(sorted_guests)

# sort() = changes
# sorted() = copies

#Slice from a list
# sub_list = list[begin: end: step]

nums = [0,1,2,3,4,5,6,7,8,9]
slice_num = nums[1:5]
print(slice_num)

nFirst = nums[:3]
print(nFirst)

nLast = nums[5:]
print(nLast)
nth_element = nums[::3]
print(nth_element)

reverse_list = nums[::-1]
print(reverse_list)

nums[0:2] = ['A', 'B']
print(nums)

del nums[0:2]
print(nums)

# The enumerate() function returns a tuple that contains the current index and element of the list.
cities = ['Dhaka','Chittagong', 'Rajsahi', 'Rangpur','Barishal','Sylhet','Khulna', 'Mymensingh']
for i in enumerate(cities):
    print(i)

for i,j in enumerate(cities):
    print(f"{i}: {j}") #unpacking the tuple

# Use the iter() function to get an iterator from an iterable object and the next() function to get the next element from the iterable object.

# List Comprehension
nums = [1,2,3,4,5,6,7]

sqr_num = [i**2 for i in nums]
print(sqr_num)

sqr_map = list(map(lambda x: x**2, nums))
