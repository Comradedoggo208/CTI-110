'''
Teofilo Serpa
10/08/2024
P2LAB1
Using pythons math library
'''
#import math library
import math

print(f"the value of pi is {math.pi:.2f}")

radius = float(input("What is the radius of said circle? "))
print()
diameter = 2*radius
print(f"The diameter of this circle is {diameter:.1f}")
print()
circum = 2*math.pi*radius
print(f"The circumference of this circle is {circum:.2f}")
print()
area = math.pi*math.pow(radius,2)
print(f"The Area of this circle is {area:.3f}")
