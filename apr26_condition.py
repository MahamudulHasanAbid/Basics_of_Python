
''' age = input('Enter your age: ')
if int(age) >=18:
    print("You are eligible for Vote.")
else:
    print("Not eligible for voting.") 
    
#Ternary operator = Alternate to if...else

age = int(input("Enter your age: "))

ticket_price = 20 if age>=18 else 5

print(f'The ticket price is ${ticket_price}')
'''


# While loop
# command = ''

# while command.lower() != 'quit':
#     command = input('>')
#     print(f'echo: {command}')

# print('hello world')

for x in range(5):
    for y in range(5):
        if y>1:
            break
    print(f"({x}, {y})")
