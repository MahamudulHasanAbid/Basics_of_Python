# age = input("Enter your age: ")
# if int(age) >= 18:
#     ticket_price = 20
# else:
#     ticket_price = 5

# print(f"You have to pay {ticket_price} taka.")

age = input("Enter your age:")
ticket_price = 20 if int(age) >=18 else 5 #ternary operator

print(f"You have to pay the amount of {ticket_price}")


