# Teofilo Serpa
# 9/26/24
# P1HW1
# create a program that does some basic math on numbers that are entered.

print("this program calculates your own travel expenses for you!")
print()
budget = int(input("What is your budget?: "))
print()
des = input("Where are ya headed?(Destintation): ")
print()
gas = int(input("what do you think you'll spend on gas?: "))
print()
accom = int(input(" are you planning to stay anywhere? (Accomidation): "))
print()
food = int(input("are you gonna be ordering out? (Food): "))
print()
print("-----Your Travel Expenses-----")
print("Destination:", des)
print("Your initial budget:", budget)
print()
print("Gas/Fuel:", gas)
print("Accomidation:",accom)
print("Food Spending:", food)
print()
Final = budget-gas-accom-food
print("Final Balance:", Final)
