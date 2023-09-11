try:
    with open("data.txt","r") as file:
        access = file.read()
        print(" File content:\n",access)
except FileNotFoundError as fnf:
    print("Your file is not in the directory")
except IOError as io:
    print(io)