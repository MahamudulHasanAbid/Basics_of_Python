'''Develop a Python program for a shopping application. The program should take the total purchase amount as input and apply discounts based on the following conditions:
10% discount for purchases above $100
20% discount for purchases above $200
30% discount for purchases above $300
No discount for purchases below $100'''

# purchage_list=[]
# total_purchage =0
# product = int(input("How many products: "))
# for i in range(1,product+1):
#     purchages = int(input(f"Product {i} is : $"))
#     purchage_list.append(purchages)
#     total_purchage += purchages

total_purchage = int(input("Total purchage : $"))

if(total_purchage>300):
    print(f"payment is: {total_purchage}")
    after_discount = total_purchage-(total_purchage*0.3)
    print(f"30% discount for purchases above $300\nAfter 30% discount payment is: {after_discount}")

elif(total_purchage>200):
        print(f"payment is: {total_purchage}")
        after_discount = total_purchage-(total_purchage*0.2)
        print(f"20% discount for purchases above $200\nAfter 20% discount payment is: {after_discount}")


elif(total_purchage>100):
    print(f"payment is: {total_purchage}")
    after_discount = total_purchage -(total_purchage*0.1)
    print(f"10% discount for purchases above $100\nAfter 10% discount payment is: {after_discount}")

else:
    print("No discount for purchases below $100")