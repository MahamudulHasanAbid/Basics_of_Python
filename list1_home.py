# Lists are ordered,changeable,duplicate values, heterogenous
# li=['Abdullah',5,17.4,[3,4,7],'Meherima','Ayesa','Amena','Abdullah','Hamim','Sohan','Acia',5]
# print(li)
# print(len(li))
# print(li[-10:])
# for item in range(5,len(li)):
#     print(li[item])
# li.insert(9,['Alomgir','popi'])
# print(li)
# li.insert(7,"Manik,Lakhi")
# print(li)

# li.extend([5,6,7])
# print(li)
# li[0] = 'Sequence'
# print(li)
# li.remove([3,4,7])
# print(li)

# del li[0:3]
# print(li)
# li.clear()
# print(li)

l = list(('Hasan',24,65.9))
print(l)
print(len(l))
# for retriving data or print only elements: 
print("Retriving elements from list :")
for i,j in enumerate(l, 0):
    print(f"element {i} is : {j}")

# list2 = list()
# print(list2)
# print(len(list2))
var = "James Bond"

print(var[2::-1])