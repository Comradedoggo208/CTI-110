'''
Teofilo Serpa
10/28/24
P3Lab1
This program allows the user to enter a money (float) value with two places after the decimal.
'''
# Get value from user
change = float(input("Enter amount of money: $"))

print(f"Change Amount: {change}")

# Convert value to integer
change = round(change * 100)

print(f"Change Amount: {change}")


if change == 0:
    print("No Change Due")
# Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_Quarters = change // 25
change = change - (num_Quarters * 25)

num_Dimes = change // 10
change = change - (num_Dimes * 10)

num_Nickles = change // 5
change = change - (num_Nickles * 5)

num_pennies = change


if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_Quarters > 0:
    if num_Quarters == 1:
        print(f"{num_Quarters} Quarter")
    else:
        print(f"{num_Quarters} Quarters")

if num_Dimes > 0:
    if num_Dimes == 1:
        print(f"{num_Dimes} Dime")
    else:
        print(f"{num_Dimes} Dimes")
        
if num_Nickles > 0:
    if num_Nickles == 1:
        print(f"{num_Nickles} Nickle")
    else:
        print(f"{num_Nickles} Nickles")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Pennie")
    else:
        print(f"{num_pennies} Pennies")
        
