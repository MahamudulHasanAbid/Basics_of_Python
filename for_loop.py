# for item in string(5):
#     print(item*2)

# A single charecter traverse through.
# word=['cat','dog','cow']
# letter=[]
# for a_word in word:
#     for a_letter in a_word:
#         letter.append(a_letter)
# print(letter)

# square = [i*i for i in range(1,11) if i%2!=0]
# print(square)

# print([ch.upper() for ch in 'comprehension' if ch  in 'aeiou'])
# print([ch.upper() for ch in 'comprehension'])

#Test 
word_list = ['cat', 'dog', 'rabbit']
letter_list=[ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)
unique = []
[unique.append(i) for i in letter_list if i not in unique]
print(unique)
