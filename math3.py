from math import tan, pi

n = int(input("Number of sides: "))
l = int(input("The length of a side: "))

a = round(n*(l**2)/(4*tan(pi/n)))

print("The area of the polygon is:", a)