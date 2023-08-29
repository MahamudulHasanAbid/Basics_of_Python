'''2. Password Strength Checker:
   As a cybersecurity analyst, you need to evaluate the strength of user passwords. Write a Python program that takes a list of passwords as input and checks their strength based on certain criteria (e.g., length, presence of uppercase letters, numbers, and special characters).

   Guidelines:
   - Create a list that contains several passwords.
   - Use a loop to iterate over the list of passwords.
   - Within the loop, check each password against the defined criteria.
   - Assign a strength score to each password based on the criteria.
   - After the loop, print the strength score for each password.
'''

pass_list =[]
score = 2

special_char= '''`!@#$%^&*()_+~=-|'"\;:.,[]{}'''
list_size = int(input("Input the list size: "))
for i in range(list_size):
    password = input("Enter password: ")
    pass_list.append(password)
    criteria = True

    if len(password)>14:
        criteria = False
        print("You exceded the length size.")
        score=0
    if any(char.isupper() for char in password):
        criteria = False
        print("Upper case later should not use in password.")
        score = 0
    if any(char.isdigit() for char in password):
        criteria = False
        print("It is not good to include digits in password.")
        score = 0
    if any(char in special_char for char in password):
        criteria = False
        print("No special charecter is allowed.")
        score=0
    if " " in password:
        criteria= False
        print("No space is allowed.")
        score=0
    
    if criteria:
        score = 5
        print(f"\nPassword is :{password}\nscore: {score}")
    else:
        print("\nPassword doesn't meet criteria.")
    
if criteria:
    print(f"A correct password list is: {pass_list}")   




