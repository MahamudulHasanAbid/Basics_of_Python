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

for i in sen:
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

#Exercise 15. Find largest and smallest digit in a number
num = 19384
smallest = 0
largest = 9

while num>0:
    digit = num%10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    num = num//10

print("Largest digit:", largest)
print("Smallest digit:", smallest)


