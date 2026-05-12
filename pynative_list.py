# Exercise 1. Perform Basic List Operations
# Practice Problem: Write a script to perform the following three operations on given list
# Access the third element of a list
# List Length: Print the total number of items
# Check if the list is empty

numbers = [10,20,30,40,50]

print(f"Third element: {numbers[2]}")

print(len(numbers))

is_empty = len(numbers) == 0
print(f"Is the list empty?{is_empty}")

is_empty = bool(numbers) == False
print(is_empty)

# Exercise 2. Perform list manipulation
# Practice Problem: Take a given list and modify it through five specific actions:
# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.

numbers = [10,20,30,40,50]

numbers[1]= 200
print(numbers)

numbers.append(600)
print(numbers)

numbers.remove(600)
print(numbers)

numbers.pop(0)
print(numbers)

# Exercise 3. Sum and Average of All Numbers in a List
# Practice Problem: Calculate the total sum of all integers in a list 
# and find the arithmetic mean (average).

num= [10,20,30,40,50]

total = sum(num)
avg = total/len(num)
print(total)
print(avg)

# Exercise 4. Find Maximum and Minimum from List
# Practice Problem: Identify the largest and smallest numerical values within a provided list.

data=[54,12,29,11,30,31,13,23]

max_val = max(data)
min_val = min(data)
print(f"Maximum: {max_val}\nMinimum: {min_val}")

# Exercise 5. Calculate the Product of All Elements
# Practice Problem: Multiply every number in a list together to find the total product.

num_list = [2,3,4,1,5,8]
mul = 1
for i in num_list:
    mul *= i
print(f"Total Product: {mul}")

# Exercise 6. Count Even and Odd numbers.
num_list = [2,3,4,1,5,8,7]
odd = 0
even = 0
for i in num_list:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print(f" Odd number: {odd}")
print(f" Even number: {even}")

# Reverse a list:
num_list = [2,3,4,1,5,8]
print(num_list[::-1])

# Or we can do this:

rev_list=[]
for i in reversed(num_list):
    rev_list.append(i)
print(rev_list)

# Sort a list of numbers
num_list = [2,3,4,1,5,8]

num_list.sort()
print(num_list)
# Or
num_list.sort(reverse= True)
print(num_list)
# Or
# sorted() create a new list.
srt_list_d = sorted(num_list, reverse=True)
print(srt_list_d)
srt_list_a = sorted(num_list)
print(srt_list_a)

# Exercise 9. Create a copy of a list

list_1 = [1,2,3,4,5]
list_2 = list_1.copy() #shallow copy
list_2.append(6)

print(list_1)
print(list_2)

# Exercise 10. Combine two lists

list_a= [1,2,3,4,5]
list_b= [6,7,8,9,10]
com_list = list_a + list_b
print(com_list)

# Exercise 11. List slicing: Extract Middle Elements
# Practice Problem: Given a list, extract a 'slice' containing the middle three elements.

list_num= [1,2,3,4,5,6,7,8]
middle= (len(list_num)//2)-1
res = list_num[middle: middle+3 ]
print(res)

# Exercise 12.Swap two elements at given indices
# Practice Problem: Write a script to swap the positions of two elements 
# in a list based on their indices.
list_num=[1,2,3,4,5,6]

# temp = list_num[0]
# list_num[0]=list_num[2]
# list_num[2] = temp
# print(list_num)

# Pythonic way... Tuple unpacking

list_num[0], list_num[2] = list_num[2], list_num[0]
print(list_num)

# Exercise 13. Access Nested Lists (Simple Indexing)
# Practice Problem: Given a “list of lists,” 
# access a specific item hidden inside the inner list.

Nested_List = [[1, 2], [3, 4, 5], [6, 7]]

# goal = 5
# for row_indx, row in enumerate(Nested_List):
#     for col_indx, col in enumerate(row):
#         if col == goal:
#             print(f"found the accessed value at row{row_indx} column{col_indx}")
value = Nested_List[1][2]
print(f"Accessed value: {value}")

# Exercise 14. Check if List Contains a Specific Item
list_c= ['apple', 'banana', 'mango']

checker = input('Enter your fruits to check:')

if checker in list_c:
    print('Yes, It is in the list.')
else:
    print('No, It is not in the list')


# Find the longest string in the list

list_c= ['apple', 'banana', 'mango',  'water melon','pomegranate']

long_str = max(list_c, key = len)
print(long_str)

# Exercise 16. Turn Every Item of a List into its Square (List Comprehension)
list1= [1,2,3,4,5]
print(f"Original list: {list1}")
list_com=[i*i for i in list1]
print(f"After square operation: {list_com}")

# Exercise 17. Count occurrences of an item. No looping
numlist=[10,20,10,40,50,60]
target = 10

counter = numlist.count(10)
print(f"{target} is {counter} times in the list.")


#Exercise 18. Remove All Occurrences of a Specific Item
# wrong way to this:
rmv = numlist.remove(10)
print(numlist)
# Because remove only delete the first occurance.
# proper way:
nw_list=[i for i in numlist if i != target]
print(nw_list)

# Exercise 19. Remove Empty Strings from a List of Strings(strip())

name = ["Mike", "Tyson", "Hitler", "Zengish","", "Zoro", " "]

cleaned_names = [i for i in name if i.strip()]
print(f"Cleaned List: {cleaned_names}")

# Or
cln_names = list(filter(None, name))
print(cln_names)

# Exercise 20. Remove duplicates from a list. (dict.fromkeys())

duplicates = [12, 12, 22, 21, 22, 10, 11]

rem_duplicates = list(dict.fromkeys(duplicates)) #Preserves order
print(f"Unique list: {rem_duplicates}")

# or
rmvd_list = set(duplicates) #No ordering
res_list = list(rmvd_list)
print(res_list)
print(rmvd_list)

# Exercise 21. List comprehension for filtering numbers

data = [1,2,3,4,5,6,7,8,9,10]

even = [i for i in data if i%2 == 0]
print(even)

# Exercise 22. Concatenate Two lists Index-wise (zip())

a= ["Py", "is", "aweso"]
b= ["thon", " ", "me"]

res =[i+j for i,j in zip(a,b)]
print(res)

# Exercise 23. Iterate Both lists simultaneously. zip() is the Safe Parallel Iterator.
c= [10,20,30]
d= [100, 200, 300]
res = [ [i, j] for i,j in zip(c,d)]
print(res)

# or
for i,j in zip(c,d):
    print(f"{i} {j}")

# Exercise 24. Add New Item After a Specified Item
lst= [10,20,30,40]
target = 20
new_val = 43

# Find the target
index =  lst.index(target)

lst.insert(index+1, new_val)
print(lst)

# Exercise 25. Replace List’s Item with New Value if Found
# Practice Problem: Find the first occurrence of a specific value in a list and replace it with a new value.

talika = [5,10, 20 ,15,25]
find = 20
replace = 200

if find in talika:
    index = talika.index(find)
    talika[index] = replace
print(talika)

# Exercise 26. Find the second largest number in the list.
lst = [12, 35, 1, 12, 34, 1,35]

desc= sorted(set(lst), reverse=True)
print(desc)
if len(lst) < 2:
    print("There is no second value.")
else:
    print(f" Second largets {desc[1]}")

# Exercise 27. Find the most frequent element
# Practice Problem: Create a script that identifies the “Mode” of a list—the element 
# that appears most frequently. If there is a tie, 
# returning one of the top elements is sufficient for this exercise.
list5 =  [1, 3, 3, 2, 1, 1, 4, 3, 3]
count = 0
frequency={}
for rw_indx, rw in enumerate(list5):
    if rw in frequency:
        frequency[rw] += 1 
    else:
        frequency[rw] = 1
mode = max(frequency, key = frequency.get)
print(f"{mode} is the most frequent element in the list.")

# Or we can do this:
def find_mode(lst):
    frequency = {}

    for i in lst:
        frequency[i] = frequency.get(i, 0)+1
    
    mode = max(frequency, key = frequency.get)
    return mode

list5 =  [1, 3, 3, 2, 1, 1, 4, 3, 3]
res = find_mode(list5)
print(f"Mode of the list: {res}")

# Exercise 28. Extract Every Nth Element from a List
def extrct_nth(lst, n):
    nth_lst= lst[::n]

    return nth_lst

my_list = ['a','b','c','d','e','f','g','h','i','j','k',]
n_val = 3

res = extrct_nth(my_list, n_val)
print(res)

# Exercise 29. Check if list is palindrome
def pal_checker(lst):
    rev = lst[::-1]
    if lst == rev:
        return True
    else:
        False

pal_list = [1,2,3,2,1]
res = pal_checker(pal_list)

print(f"Is palindrome? {pal_checker}")

# Or we can do this:
def pal_checker(lst):
    return lst == lst[::-1]

pal_list1 = [1,2,3,2,1]
pal_list2 = [1,2,3,4,5]

print(f"{pal_list1} is palindrome? {pal_checker(pal_list1)}")
print(f"{pal_list2} is palindrome? {pal_checker(pal_list2)}")

# Exercise 30. Find All Common Elements Between Three Lists

lis_a = [1,5,10,20]
lis_b = [6,7,20,80,100]
lis_c = [3, 4,15,20,30,70,80]

common = set(lis_a).intersection(lis_b,lis_c)
print(list(common))

# Or we can do this 
def common_checker(l1,l2,l3):
    common = set(l1) & set(l2) & set(l3)

    return list(common)

lis_a = [1,5,10,20]
lis_b = [6,7,20,80,100]
lis_c = [3, 4,15,20,30,70,80]

result = common_checker(lis_a, lis_b, lis_c)

print(result)

# Exercise 31. Filter Strings by Length in a List
# Practice Problem: Write a function that takes a list of strings and an integer k. 
# The function should return a new list containing only the strings 
# that have a length greater than or equal to k.

fruits = ["apple","banana","Chery","Pomegranate","Watermelon","pineapple"]
length = 6
def func(lst, k):
    update_list = [i for i in lst if len(i)>= k]

    return update_list

res = func(fruits, length)
print(res)

# Exercise 32. Check if List is Sorted. (all() for checking all are true)
# Practice Problem: Create a function that determines if a list of numbers is sorted 
# in non-decreasing (ascending) order. Return True if it is, and False otherwise.

def sort_checker(lst):
    return lst == sorted(lst)

list_d = [10, 20, 30, 40, 25]

res = sort_checker(list_d)

print(f" Is Sorted: {res}")

# Or we can do this:
def sort_checker(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1) )

nums1 = [10, 20, 30, 40]
nums2 = [10, 20, 30, 25, 40]

print(f" Is Sorted: {sort_checker(nums1)}")
print(f" Is Sorted: {sort_checker(nums2)}")
