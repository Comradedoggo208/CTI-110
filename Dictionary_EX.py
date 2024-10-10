#in-class Example of a dictionary

# Make the dictionary
sakura_blossom = {"sakura_color":"pink", "Cost":24.85, "max_height": 15, "is_perennial":True}

# get a value out for the dictionary
print(f"${sakura_blossom['Cost']:.2f}")

# get another value from the dictionary
print(f"is the sakura blossom perennial? {sakura_blossom['is_perennial']}")
print()
# get color without f-string
print(sakura_blossom['sakura_color'])
print()
# add key value pair 
sakura_blossom['water_needed'] = "20 oz per week"
print()
# print entire dictionary
print(sakura_blossom)
print()
# add key value pair
sakura_blossom.update({"branch_color":"dark brown", "sunlight needed":10})
print()
# print entire dictionary
print(sakura_blossom)
print()
# remove a value from the dictionary
del sakura_blossom['branch_color']
print()
# print entire dictionary
print(sakura_blossom)
print()
# print out all keys in dictionary
print(sakura_blossom.keys())
print()
# ask user for a key for the dict
answer = input("Input a key from the dictionary: ")
print()
# give the value accociated with the users answer
print(f"the value for {answer} is {sakura_blossom[answer]}")
