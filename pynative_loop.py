#Exercise 1. Print first 10 natural numbers using while loop 
i=1
while(i<10):
    print(i)
    i = i+1

# Exercise 2. Display numbers from -10 to -1 using for loop
i=-10
while(i<=-1):
    print(i)
    i= i+1
# OR
for i in range(-10, 0):
    print(i)

# Exercise 3. Display a message “Done” after successful execution of for loop
for i in range(0,5):
    print(i)
else:
    print("Done!")

# Exercise 4. Calculate the sum of all numbers from 1 to N
# Practice Problem: Write a program that accepts a number from the user and 
# calculates the sum of all numbers from 1 up to that number.
n = int(float(input("Give you number. I will execute the calculation: ")))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)
# res = sum(range(1, n+1))
# print(res)

# Exercise 4. Print multiplication table of a given number
n= int(input("Which multiplication table you wanna see: "))
print(f"\n Multiplication table for {n}:")
for i in range(1, 11):
    mul = n* i
    print(f" {n} * {i} = {mul}")

# Using while loop
# i=1
# while(i<11):
#     mul = n*i
#     print(f'{n} * {i} = {mul}')
#     i=i+1

# Exercise 6: Calculate the cube of all numbers from 1 to a given number.
n = int(input("Enter the number for the cube operation: "))

if n==0:
    print("Zero is always a zero")
else:
    for i in range(1, n+1):
        cube= pow(i,3) # i**3
        print(f" Cube of {i} is {cube}")

# Exercise 7. Display numbers from a list using a loop
# Practice Problem: Given a list of numbers, iterate through it and 
# print numbers that satisfy these conditions:
 # The number must be divisible by five.
 # If the number is greater than 150, skip it and move to the next.
 # If the number is greater than 500, stop the loop entirely.

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>500:
        break
    if i> 150:
        continue
    if i%5 == 0:
        print(i)

# Exercise 8. Count occurrences of a specific element in a list
# Practice Problem: Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

list1 = [10,20,30,40,10,80,10,20,30,80]
target = 30 
# print(f"{target} is {list1.count(30)} times in the list.")
count = 0
for i in list1:
    if i == target:
        count += 1

print(f"{target} appears {count} times in the list.")

# Exercise 9. Print elements from a list present at odd index positions
# Practice Problem: Given a Python list, use a loop to print only the elements 
   # that are located at odd index positions (index 1, 3, 5, etc.).

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for key, value in enumerate(my_list):
    if key % 2!=0:
        print(value, end=" ")
# Or we can do this...
# for i in range(1, len(my_list), 2):
#     print(my_list[i], end = " ")

# Exercise 10. print list in reverse order.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(my_list[::-1])
for i in reversed(my_list):
    print(i, end=" ")

# Exercise 11. Reverse a string using a for loop (no slicing)

# string= 'python'
# val= len(string)
# new_str = '' 
# for i in range(val-1, -1, -1):
#     new_str += string[i]
# print(new_str)

original_str = 'Python'
rev_str = ''
for i in original_str:
    rev_str = i+rev_str #prepending.

print(f"Original string: {original_str}")
print(f"Original string: {rev_str}")

# Exercise 12: Count vowels and consonants in a sentence(ignore spacces and special characters)
sen= "Hey I am an old monk. Trying to reach the sky."
vowel_list = 'aeiou'
vowel= 0
consonant=0

for i in sen.lower():
    if i.isalpha():
        if i in vowel_list:
            vowel += 1
        else:
            consonant += 1

print(f"Vowel is total: {vowel}")
print(f"Consonant is total: {consonant}")

# Exercise 13. Count total number of digits in a number(while loop)

num = 986876932681135
# count = 0
# for i in str(num):
#     # print(i, end=' ')
#     count += 1
# print(count)

count = 0
while num != 0:
    num = num //10
    count += 1
print(count)

# Exercise 14. Reverse an integer number using while loop
num = 12345
rev_num = 0
while num > 0:
    digit = num%10
    rev_num= (rev_num * 10) + digit
    num = num // 10
print(rev_num)

# for i in str(num):
#     rev_num = i+ rev_num
# revd_num=int(rev_num)
# print(revd_num)

#Exercise 15. Find largest and smallest digit in a number
num = 19384
smallest = 9
largest = 0

while num>0:
    digit = num%10
    if digit >= largest:
        largest = digit
    if digit <= smallest:
        smallest = digit
    num = num//10

print("Largest digit:", largest)
print("Smallest digit:", smallest)

#Exercise 16. Check If a number palindrome or not
num = int(input("Validate your number if it is a palindrome: "))
temp = num
rev_num = 0
while num>0:
    digit = num%10
    rev_num = (rev_num*10) + digit
    num = num // 10
if rev_num == temp:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

#Exercise 17. Find factorial of a number 
num = int(input("Input your number: "))
fact=1
if num<0:
    print("For negative number, there is no factorial value")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact *= i

print(f"The factorial of {num} is {fact}")

#Exercise 18. "Collatz Conjecture"- A sequence that eventually reach 1
# Start with any integer. If it is even then divide it by 2,If odd then multiply by 3 and add 1

num= int(input("Enter a number: "))
print(num, end="")
while num != 1:
    if num%2 == 0:
        num = num//2
    else:
        num = (num*3)+1
    print(f", {num}", end ="")

#Exercise 19. "Armstrong Number"- 153 = 1^3+5^3+3^3
num= int(input("Enter a number: "))
total = 0
power= len(str(num))
for i in str(num):
    total += int(i) ** power
if total == num:
    print("Armstrong Number")
else:
    print("Normal Number.")

#Exercise 20. Print right-angled triangle number pattern using a loop.

line = int(input("Enter how many line we would like to have: "))

for i in range(1, line+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')

# Exercise 21. Print the decrising pattern

for i in range(5,0,-1):
    for j in range(i, 0,-1):
        print(j, end=' ')
    print('')

# Exercise 22. Print the alternate numbers from 1 to 20 (Pattern)
for i in range(1,21,2):
    print(i, end=' ')

#Exercise 23. Alphabet  Pattern.
ascii_val= 65
for i in range(6):
    letter = chr(ascii_val+i)
    for j in range(i+1):
        print(letter, end=' ')
    print('')

# Exercise 24. Print a hollow square pattern
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')

# Exercise 25. Print pyramid pattern of stars
for i in range(1,6):
    for j in range(i):
        print('*', end=' ')
    print()
for k in range(4,0,-1):
    for l in range(k):
        print('*', end=' ')
    print()

# Full pyramid
rows= 5
for i in range(1,rows+1):
    # for space
    for j in range(rows-i):
        print(" ", end=' ')
    
    # for star
    for k in range(2*i-1):
        print("* ", end=' ')
    
    print()

# Exercise 26. Print full multiplication table(1 to 10)
for i in range(1,11):
    for j in range(1,11):
        print(f'{i*j}', end=' ')
    print(end='\n...\n')

# Exercise 27. Each element is the sum of all previous from a list.
num=[1,2,3,4]
print(f"Original list: {num}")
current_sum = 0
cumulative_list = []
for i in num:
    current_sum += i
    cumulative_list.append(current_sum)

print(f"Cumulative Sum: {cumulative_list}")

# Exercise 28. Dictionary filter: Extract pairs where value exceeds a threshold.
# Practice Problem: Given a dictionary of student scores, create a new dictionary 
# that only includes students who scored above a certain threshold (e.g., 75).

scores = {"Alice":85, "Bob": 70, "Charlie":95, "David": 60}
threshold = 75
Passing_std = {}
for i,j in scores.items():
    if j>=75:
        Passing_std[i] = j
print(f"Passing Students: {Passing_std}")

# Exercise 29. Find common elements (Intersection) using loop
# Practice Problem: Given two lists, find the elements that appear in both. Do not use Python’s built-in set().intersection() method.
list_a = [1,2,3,4,5]
list_b = [4,5,6,7,8]

common_list = []

for i in list_a:
    if i in list_b:
        common_list.append(i)
print(common_list)

# Exercise 30. Remove duplicates without set 
# Practice Problem: Write a program to remove all duplicate values from a list using a loop, 
# maintaining the original order of elements.

n_list = list(map(int, input("Enter your choice of numbers: \n").split()))
print(n_list)
res = set(n_list)
Unique_list = list(res)
print(Unique_list)
# another way to deal with the problem.

num=[1,2,3,3,2,5,6]
print(num)
unique_lst=[]
for i in num:
    if i not in unique_lst:
        unique_lst.append(i)

print(unique_lst)

# Exercise 31. Even/Odd segregation: Move evens to front, odds to back
num = [1,2,3,4,5,6]
odd=[]
even=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.extend(odd) #new_list = even + odd
print(f"Segregated List: {even}") # print(new_list)

# Exercise 32. List Rotation: Rotate elements left by k positions
# Practice Problem: Given a list and an integer k, rotate the list to the left by k positions.
# For example, if k=2, the first two elements move to the end of the list.

nums= [1,2,3,4,5]
k=2
part=nums[k:]
print(part)
rotated = nums[k:] + nums[:k]
print(rotated)

# Exercise 33. Word frequency counter
# Practice Problem: Write a program to count the frequency 
# of each word in a given string.
text= "apple banana mango orange palm guava"
words =  text.split() #change the text into the list.
print(words)

freq = {} 

for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Exercise 34: Display fibonacci series up to 10 terms
# Practice Problem: Write a program to display the Fibonacci sequence up to 10 terms. 
# The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
n_terms = 10
num1 = 0
num2 = 1
for i in range(10):
    print(num1, end=' ')
    res = num1+num2
    num1=num2
    num2=res

# Exercise 35: Perfect number check
# Practice Problem: Write a program to check if a number is a “Perfect Number.” 
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).
# For example, 6 is perfect because 1 + 2 + 3 = 6
num = int(input("Enter a positive number: "))
divisor_sum = 0
for i in range(1,(num//2)+1):
    if num%i == 0:
        divisor_sum += i
    else:
        pass
if divisor_sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    
# Exercise 36. Binary to decimal using loop
binary_str = '10101'
decimal= 0
rev_string= binary_str[::-1]
for i in range(len(rev_string)):
    if rev_string[i] == '1':
        decimal += 2**i

print(f"Decimal of {binary_str} is : {decimal}")

# Exercise 37. Display all prime numbers within a range.
start = 25
end = 50

for i in range(start,end+1):
    is_prime = True
    for j in range(2, i):
        if i%j == 0:
            is_prime = False
            break

    if is_prime and i>1:
        print(i, end=' ')

# Exercise 38. Find the sum of the series up to n terms
# Practice Problem: Write a program to calculate the sum of the series 2 + 22 + 222 + 2222 + …. up to N terms. 
# For example, if n=5, the series is 2 + 22 + 222 + 2222 + 22222.
n= 5
start = 2
sum = 0
for i in range(0, n):
    sum += start
    start = (start*10) + 2
print(sum)

# Exercise 39. Flatten a nested list using loops
# Practice Problem: Given a nested list (a list containing other lists), 
# write a program to “flatten” it into a single list containing all the individual elements

nested_list = [[10,20],[30,40],[50,60]]
flattened = []

for i in nested_list:
    for j in i:
        flattened.append(j)
print(flattened)

# Exercise 40. Nested list search(2D matrix coordinates)
# Practice Problem: Given a 2D list (matrix), 
# find the row and column index of a target value.

matrix=[[10,20],[30,40],[50,60]]
target = 60

for r_indx, row in enumerate(max):
    for c_indx, col in enumerate(row):
        if col == target:
            print(f"Target {target} found at row {r_indx} and column {c_indx}")
