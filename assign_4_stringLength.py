''' Write a program that calculates and outputs the length of a given input string without using any built-in string length functions.'''

text = input("Give your string: \n")
print("Using function: ",len(text))

# If I want the same output without len() then
count = 0
for i in text:
    count = count+1
print("Without using function: ",count)