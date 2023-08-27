age = int(input("Age is: "))
if(age<=0):
    print("Invalid Input")
elif(age<13):
    print('child')
elif(13<=age<=19):
    print('Teen')
elif(20<=age<=65):
    print('Adult')
elif(age>65):
    print("Senior")