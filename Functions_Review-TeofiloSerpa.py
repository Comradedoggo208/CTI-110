# review

import random

def death_calculator(name, age):

    avg_lifespan = 80
    approx_years = avg_lifespan - age
    print(f"using the avg lifespan {avg_lifespan}, {name} has {approx_years} years left to PARTY!")
    pos_death = ["chocked on grape-fruit", "attacked by crow", "bunny pushed them down stairs", "sneezed too hard"]
    cause = random.choice(pos_death)
    return cause


def main():
    cause = death_calculator(input("enter your name: "), int(input("how old are you: ")))

    print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
    print(f"Cause of death: {cause}")
    print()
    print("GAME OVER!")

#call da main
if __name__ == "__main__":
    main()

    
