# def sec_try(name, age):
#     print(name,"\n",str(age))
# sec_try("Abid",25)
# sec_try("Abdullah",5)
# sec_try("Meherima",1.5)

# def calculation(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b 
#     return add, sub, mul, div
# add,sub,mul,div = calculation(42,8)
# print(add)
# print(sub)
# print(mul)
# print(div)


# def outer(a,b):
#     def inner(a,b):
#         return a+b
#     return inner(a,b)+5
# print(outer(9,3))

'''Non keyword and Keyword argument = Variable length of argument'''
# Nonkeyword argument: *args or *anything
# def Hello(*call):
#     for i in call:
#         print(i)
# Hello("This is a *args practice part.","What else can be done","Practice and practice more"," 42 is the serial")

# # Keyword argument: **args or **anything
# def intro(**info):
#     for i,j in info.items():
#         print(f"{i} == {j}") #i=key,j=value
# intro(Name = 'Mahamudul Hasan',ID = "CSE3033",Dept = "Science", passing_year=2023)


# def basic(fname,lname):
#     return f"Hello {fname} you are {lname}"
# ans = basic('abid','failure')

# print(ans)


# number = int(input("Enter the number: "))

# count = 0

# init_val1, init_val2 = 0,1

# if number<=init_val1:
#     print("Wrong Input")
# elif number==init_val2:
#     print(f"You get {init_val1}")
# else:
#     while count<number:
#         print(init_val1)
#         change_val=init_val1+init_val2
#         init_val1 = init_val2
#         init_val2 = change_val

#         count += 1


'''Recursive Function...'''
# def countdown(start):
#     print(start)

#     if (start-1)>=0:
#         countdown(start-1)
    
# countdown(19)


# def info(*args):
#     for i in args:
#         print(i)
# info([2,3], 'abid', 23)


# def calculation(a,b):

#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add, sub, mul, div 

# addi, subt, multi, divi = calculation(40,10)
# print(f"{addi}, {subt}, {multi}, {divi}")


# def outer(a,b):
#     def inner(c,d):
#         return c+d
#     calc= inner(a,b)+5
#     return calc
# res = outer(3,5)
# print(res)

# def countdown(n):
#     if n>0:
#         return n + countdown(n-1)
#     else:
#         return 0
# show = countdown  
# res = show(10)
# print(f"sum of 10 number  is {res}")


def shownum(n):
    if n<31:
        return [n] + shownum(n+2)
    else:
        return []
res =shownum(4)
print(res)
# Or we can write the whole code in one line
print(list(range(4,31,2)))