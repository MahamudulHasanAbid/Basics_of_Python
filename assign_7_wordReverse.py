'''Create a program that takes a sentence as input and reverses the order of the words in the sentence.
'''
sentence = input("Enter text: \n")

# if " " in sentence:
#    seperate = sentence.split()
#    i = []
#    for i in seperate:
#       seperate = [i]+seperate
#       result=" ".join(seperate)
# print(result)  # Output is repeating. But why?

if " " in sentence:
   seperate = sentence.split()
   reverse = seperate[::-1]
   result=" ".join(reverse)
   print(result)