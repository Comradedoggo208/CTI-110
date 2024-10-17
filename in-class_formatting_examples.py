# formatting examples

rent = 5000
phone = 25.87314
internet = 43.751
elec = 75.84601
gas = "Not Applicable"
total = rent+phone+internet+elec

print(f"{'BILLS':<20}{'Amount'}")
print("+-"*18)
print(f"{'Rent:':<20}${rent:,.2f}")
print(f"{'Phone:':<20}${phone:,.2f}")
print(f"{'Internet:':<20}${internet:,.2f}")
print(f"{'Electricity:':<20}${elec:,.2f}")
print(f"{'Gas:':<20}{gas}")
print(f"{'Total Bill:':<20}${total:,.2f}")
