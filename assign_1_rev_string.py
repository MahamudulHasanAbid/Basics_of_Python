''' A program that takes a string as input and outputs the reverse of the input string.'''

take = input("Write down something: \n")
rev = take[::-1]
print(rev)

# Another way using slice()
reve = take[slice(None,None,-1)]
print(reve)


#Way using for loop
output = " "
for i in take:
    output = i+output
print(output)

reverse= "".join(reversed(take))
print(reverse)
