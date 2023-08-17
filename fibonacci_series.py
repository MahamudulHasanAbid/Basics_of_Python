number=int(input("Input the last value you want to iterate the fibonacci series:"))

init_value1, init_value2=0,1

count=0

if number<=0:
    print("Enter a valid number to perform the fibonacci series")
elif number==1:
    print("You get" ,init_value1)
else:
    while count<number:
        print(init_value1)
        
        change_value=init_value1+init_value2
        init_value1 = init_value2
        init_value2 = change_value
        count += 1
        
        

