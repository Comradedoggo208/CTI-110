# Teofilo Serpa
# 9/26/24
# P2HW1
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
print("Your Travel Expenses")
print(f"{'Expenses':<25}{'Amount'}")
print("+-"*18)
print(f"{'Destination:':<25}{des}")
print(f"{'Starting budget:':<25}${budget:,.2f}")
print(f"{'Gas/fuel:':<25}${gas:,.2f}")
print(f"{'Accomidation:':<25}${accom:,.2f}")
print(f"{'Food Spending:':<25}${food:,.2f}")
print("+-"*18)
print()
Final = budget-gas-accom-food
print(f"{'Final Balance:':<25}${Final:,.2f}")
