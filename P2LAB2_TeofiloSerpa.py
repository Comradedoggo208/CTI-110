'''
Teofilo Serpa
10/10/24
P2LAB2
i will be writing a program that creates my own dictionary based on already set values
'''
# make said dictionary
Car_mpg = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Sliverado":26}

# print the keys
print(Car_mpg.keys())
print()
# ask the user what car they want to see the mpg
Vehical = input("What car are ya picking!?: ")
print()
# display the mpg for the car
print(f"the {Vehical} gets {Car_mpg[Vehical]} mpg")
print()
# ask the user how many miles will they drive
miles = float(input(f"how far (in miles) are you planning to go in the {Vehical}?: "))
print()
# calculate the gallons how much gass they will use on their drive
gas_needed = miles / Car_mpg[Vehical]
print(f"{gas_needed:.2f} gallon(s) of gass are needed to drive the {Vehical} {miles} miles")
