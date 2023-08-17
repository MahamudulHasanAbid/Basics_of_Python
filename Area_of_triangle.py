# A program to find Are of a triangle.

a = float(input("First arm of a triangle in cm:"))
b = float(input("Second arm of a triangle in cm:"))
c = float(input("Third arm of a triangle in cm:"))
perimeter = a+b+c
print("The perimeter of this triangle is : %0.3f cm ." %perimeter)
semi_peri = (a+b+c)/2
area_of_triangle = (semi_peri*(semi_peri-a)*(semi_peri-b)*(semi_peri-c)) ** 0.5 
print("The area of the given triangle is: %0.4f cm." %area_of_triangle)



