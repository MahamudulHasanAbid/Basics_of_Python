num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))

if (num1>num2) and (num1>num3):
    print("Largest number is : %.2f" %num1)
elif(num2>num1) and (num2>num3):
    print("Largest number is : %.2f" %num2)
else:
    print("Largest number is then: %.2f" %num3)
