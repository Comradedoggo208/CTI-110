'''
teo serpa
11/26/24
P5HW
Create a game with functions
'''

def create_Character():


    name = input("Enter Character's name!: ")
    Hp = int(input(f"Enter {name}'s Hp Stat: "))
    inventory = []
    weapon = ["fists", "metal pipe"]
    strength = int(input(f"what is {name}'s strength Stat: "))


    character = {
        "Name":name,
        "Hitpoints":Hp,
        "items":inventory,
        "Weapons":weapon,
        "Stronk":strength,
        }
    return character
        
    




def main():
    print("CHOOSE YOUR FIGHTER")
    print()
    # call create character
    char_select = create_Character()
    print(char_select)



#call ze man
if __name__ == "__main__":
    main()
