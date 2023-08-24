'''Build a program that takes a main string and a search string as inputs and checks if the search string is present within the main string.'''

main_string = input("Enter text as input: ")
search_string = input("Enter text for search: ")

if search_string in main_string:
    print(f"Yes. It is in the main string and is at {main_string.index(search_string)}")
else: 
    print("Yor search is not valid.")