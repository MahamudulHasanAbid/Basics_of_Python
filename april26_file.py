# with open(r"C:\Users\User\Desktop\help.txt",  "rt") as file:
#     for i in file:
#         print(i)

'''Create a new file and write to that extsting file. '''
# f = open ("myfile.txt", "x")

with open ("myfile.txt", "a") as f:
    f.write("File has content now.")

with open("myfile.txt", "r") as fl:
    content = fl.read()
    print(content)
