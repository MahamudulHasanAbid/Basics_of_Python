'''Write a program that takes a string as input and calculates the count of vowels and consonants in the string.'''
text = input("Enter text: ")
vowel = 'aeiouAEIOU'
v_count = 0
c_count = 0

for i in text:
    if i in vowel:
        v_count += 1
    else:
        c_count +=1

print(f"Number of vowels in text is: {v_count}")
print(f"Number of consonant in text is: {c_count}")



    
    
