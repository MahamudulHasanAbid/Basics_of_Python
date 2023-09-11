try:
    a = int(input("1st Integer: "))
    b = int(input("2nd Integer:"))
    result = a/b
except ValueError as ve:
    print("You can not skip any value/input in Decimal system.")
except ZeroDivisionError as zd:
    print("Zero can not be a divisor. ")
else:
    
    print(result)
