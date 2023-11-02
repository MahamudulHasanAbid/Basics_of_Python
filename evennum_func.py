def even_num(listOfnum):
    listing=[]
    for i in listOfnum:
        if i%2==0:
          listing.append(i)
    return listing
even= even_num([2,3,4,6,5,3,7,10])

print(even)

