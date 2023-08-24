'''A program that determines whether a given string is a palindrome or not'''

given = input("\nEnter a string : \n")
temp=given
reverse=given[::-1]
print(reverse)

if reverse==temp:
    print("This is palindrome.")
else:
    print("This is not a palindrom.")

