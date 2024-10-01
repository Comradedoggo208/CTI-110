# this program creates a recipt based on user input
# Get item name from user
# get quantity from user
# get price from user
# do those steps 3 times
# calculate the subtotal
item_1 = input("Please Insert item name here: ")
quant_1 = int(input(f"Please enter the quantity of {item_1}: "))
price_1 = float(input(f"Please enter the price of {item_1}: "))
print()
item_2 = input("Please insert item name here: ")
quant_2 = int(input(f"Please enter the quantity of {item_2}: "))
price_2 = float(input(f"Please enetr the pric eof {item_2}: "))
print()
item3 = input("Please Insert item name here: ")
quant3 = int(input(f"Please enter the quantity of {item3}: "))
price3 = float(input(f"Please enter the price of {item3}: "))
print()
print()
print("thanks for shopping at Big Al's")
print("-"*20)
print()
item = "ITEM"
quantity = "QUANTITY"
item_total = "ITEM TOTAL"
print(f"{item:<20}{quantity:<15}{item_total}")
print()
print(f"{item_1:<20}{quant_1:<15}${price_1 * quant_1:.2f}\n")
print(f"{item_2:<20}{quant_2:<15}${price_2 * quant_2:.2f}\n")
print(f"{item3:<20}{quant3:<15}${price3 * quant3:.2f}\n")
print()
subtotal = (price_1 * quant_1)+(price_2 * quant_2)+(price3 * quant3)
print(f"Your Subtotal: ${subtotal:.2f}")
print()
tax = subtotal * 0.07
print(f"Taxation: ${tax:.2f}")
print()
end_total = subtotal + tax
print(f"Gross Total: ${end_total:.2f}")



              
