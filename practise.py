def my_func(x,y=[]):
    y.append(x)
    return y
print(my_func(1))
print(my_func(9))
print(my_func(5))