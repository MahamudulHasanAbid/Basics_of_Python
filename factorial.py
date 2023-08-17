number=int(input("Enter the number to perform operation: "))

factorial = 1
if number<0:
    print("Factorial can not be performed on negative number.")
elif number == 0:
    print("Factorial of zero is 1.")
else:
    for i in range(1,number+1):
        factorial *= i
    print(f"The factorial of {number} is equal {factorial}" )
        