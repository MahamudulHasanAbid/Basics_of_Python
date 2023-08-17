# A program to convert all the possibilities of temperature.......


print("************************************************************")
print('''.......................................................
Type 'c' for Celcius as an input.
Type'f' for fahrenheit as an input.
Type 'k' for kelvin as an input.
.............................................................''')


inp = input("Type 'c' or 'f' or 'k' as you want to take the input type:")

if inp == 'c' :
    cel = float(input("Enter the value of celcius for change it to fahrenheit and kalvin:"))
    fah = (9 * cel)/5 +32
    kal = cel + 273
    print("%0.3f Celcius is %0.3f fahrenheit and %0.3f kalvin" %(cel,fah,kal))
    print("\n************************************************************")

elif inp == 'f':
    fah = float(input("Enter the value of fahrenheit for change it to celcius and kalvin:"))
    cel = (5*(fah-32))/9
    kal = (5*(fah-32))/9 + 273
    print("%0.3f fahrenheit is %0.3f Celcius and %0.3f kalvin" %(fah,cel,kal))
    print("\n************************************************************")

elif inp == 'k':
    kal = float(input("Enter the value of kalvin for change it to fahrenheit and celcius:"))
    fah = ((9*(kal-273))/5)+32
    cel = kal-273
    print("%0.3f kalvin is %0.3f fahrenheit and %0.3f celcius" %(kal,fah,cel))
    print("\n************************************************************")
else:
    print("\n Unknown input...\n\n")
