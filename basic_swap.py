# A program to swap two numbers or values

a = input("Input the first value: ")
b = input("Input the second value: ")
print("Before swapping the values are : {0} and {1}" .format(a,b))

temp = a
a = b
b = temp

print("After swapping the values are : {0} and {1}" .format(a,b))

# ---------------------------------------------------------------------------
# Another way to construct same problem

x = input("Input the first value: ")
y = input("Input the second value: ")

print("Before swapping the values are : {0} and {1}" .format(x,y))

x,y = y,x

print("After swapping the values are : {0} and {1}" .format(x,y))