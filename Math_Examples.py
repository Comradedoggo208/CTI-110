# in class examlpes of math equations

# import random library for use in the program
import random



'''
# have user give us info for side one and two
side_1 = float(input("Give me a value for side one: "))
print()
side_2 = float(input("Give me a value for side two: "))
'''

# Generate random values for side one and side two
side_1 = random.randint(7,140)
side_2 = random.randint(1,100)

print()
print()
# use the 2 values to calculate the hypotenuse
hypotenuse = (side_1**2)+(side_2**2)
# show the user the end result
print(f"The hypotenuse of this right triangle with the sides of {side_1} and {side_2} is {hypotenuse}")
