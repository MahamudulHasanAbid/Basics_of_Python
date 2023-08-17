low_bound = int(input("Value for start the table: "))
up_bound = int(input("Value for end the table:"))

for i in range(low_bound, up_bound+1):
    print("Multiplication Table of {0} : ".format(i))
    for j in range(1,13):
        result = i*j
        print("%5d X %2d = %3d" %(i,j,result))