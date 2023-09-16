mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in mat:
    print(row)

print("---------------------")
# Using list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
for row in matrix:
    print(row)   
