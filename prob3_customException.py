class NegativeValueError(Exception):
    pass
while True:
    try:
        x = int(input("Enter a positive integer: "))
        if x<0:
            raise NegativeValueError("No negative value is allowed.")

        print(x)
        break
    except NegativeValueError as nv:
        print(nv)
    except ValueError :
        print("Your input is not an Integer. ")



       