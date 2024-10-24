# using if else statements

num1 = 1

num2 = 20
'''
if num1 == num2:
    print(f"{num1} and {num2} are equal")

elif num1 > num2:
    print(f"{num1} is greater than {num2}")

else:
    print(f"{num1} is NOT greater than {num2}")
'''
# Get age from user
'''
Age = int(input("Enter your age: "))

if Age > 65:
    life_stage = "Senior"

elif Age > 17:
    life_stage = "Adult"

elif Age > 13:
    life_stage = "Teen"

elif Age > 4:
    life_stage = "Child"

elif Age > 0:
    life_stage = "Baby/Toddler"



print(f"You are {Age} years old and you are a {life_stage}")
'''

age = int(input("Enter your age: "))

if age >= 0 and age <=5:
    life_stage = "Baby/Toddler"

if age >= 6 and age <=12:
    life_stage = "Child"

if age >= 13 and age <=17:
    life_stage = "Teen"

if age >= 18 and age <=65:
    life_stage = "Adult"

if age >= 65:
    life_stage = "Senior")
