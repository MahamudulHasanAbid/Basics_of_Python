'''A program to run the countdown using recursive function.'''
def countdown(starting_val):
    print(f"Starting the countdown{starting_val}")

    if(starting_val-1)>0:
        countdown(starting_val-1)

countdown(5)

print('\n')

'''Sum of a sequence'''

def sum(n):
    if n>0:
        return n + sum(n-3)
    return 0
print(f"Total is : {sum(10)}")

