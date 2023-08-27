info = "hello, Universe IT! get ready 123 2.0"

# 1. len()
print(f"\nLength of the string: {len(info)}")
#2. capitalize()
cap= info.capitalize()
print(f"\nCapitalized form is :{cap}")

#3. upper()
up= info.upper()
print(f"\nUpper case formation: {up}")
#4. lower()
print("\nlower case formation: %s"%(info.lower()))

#5. isupper()
print("\nReturns True if follow the title.\n {}".format(info.isupper()))
#6. islower()
print(f"Returns true if follow the title.\n {info.islower()}")
#7. title()
title = info.title()
print(f"Each word's first charecter would be capital: {title}")

#8. count()
count = info.count("0")
print(f"\ncount anything what I want as count = o. \n {count}")

#9. find()
find = info.find("IT")
print(f"\nIndex of \'IT\':{find}")

#10. replace()
replace = info.replace("123","OneTwoThree")
print(f"\n Modified string: {replace}")

#11. split()
split = info.split("!")
print(f"Split string: {split}")

#12. join()
join = " ".join(split)
print(f"After joining: {join}")
