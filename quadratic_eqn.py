# A program to find quadratic equation. ax^2+bx+c=0

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

quadratic_eqn1 = (-b - (b**2 - 4*a*c) ** 0.5)/(2*a)
quadratic_eqn2 = (-b + (b**2 - 4*a*c) ** 0.5)/(2*a)

print("The result of this value: {0} and {1} " .format(quadratic_eqn1,quadratic_eqn2) ) 
