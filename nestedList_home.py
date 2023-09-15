nestedList = [[2,3,4,5],[9,2,4,2,9]]

# Access the 4th element of the 2nd list

print("Element in 4th position of 2nd element is: ",nestedList[1][3])
nestedList[1][3]=8
print(nestedList)

# retrive the elements from inner list

for i in nestedList:
    print(f"list is : {i} and elements are :")
    for index,value in enumerate(i,0):
        print(f"element {index} is: {value}")