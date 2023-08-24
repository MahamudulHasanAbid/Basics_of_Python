inp1 = input("Enter your first string: ")
inp2 = input("Enter your second string: ")

result = inp1+" "+inp2
print(result)

# Using .join()

output = " ".join([inp1,inp2])
print(output)

# Using .format() or fstring

print(f"{inp1} {inp2}")

