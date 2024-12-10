'''
Teofilo A Serpa
P5HW
create a video game using python code
'''

import random


# Base class for all characters
class Character:
    def __init__(self, name, health, attack_power, special_move):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_move = special_move
        self.shield_active = False

    def attack(self, target):
        if target.shield_active:
            damage = self.attack_power // 2
            print(f"{target.name} shields the attack, reducing damage to {damage}!")
            target.health -= damage
            target.shield_active = False
        else:
            print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
            target.health -= self.attack_power

    def shield(self):
        self.shield_active = True
        print(f"{self.name} activates their shield! Incoming damage will be halved.")

    def use_special_move(self, target, all_characters=None):
        print(f"{self.name} uses {self.special_move['name']}!")
        if self.special_move['name'] == "Random Power!":
            if all_characters:
                move = random.choice([
                    char.special_move for char in all_characters if char.special_move["name"] != "Random Power!"
                ])
                if move:
                    print(f"Random Power triggered {move['name']}!")
                    if "self_heal" in move:
                        self.health += move["self_heal"]
                        print(f"{self.name} heals for {move['self_heal']} health!")
                    if "damage" in move:
                        if target.shield_active:
                            damage = move["damage"] // 2
                            print(f"{target.name} shields the random move, reducing damage to {damage}!")
                            target.health -= damage
                            target.shield_active = False
                        else:
                            print(f"{move['damage']} damage dealt to {target.name}!")
                            target.health -= move["damage"]
                else:
                    print("Random Power! did nothing this time.")
            else:
                print("Random Power! did nothing this time.")
        elif self.special_move.get("self_heal"):
            self.health += self.special_move["self_heal"]
            print(f"{self.name} heals for {self.special_move['self_heal']} health!")
        elif self.special_move.get("damage"):
            if target.shield_active:
                damage = self.special_move["damage"] // 2
                print(f"{target.name} shields the special move, reducing damage to {damage}!")
                target.health -= damage
                target.shield_active = False
            else:
                target.health -= self.special_move["damage"]
                print(f"{self.special_move['damage']} damage dealt to {target.name}!")

    def is_defeated(self):
        return self.health <= 0

#Pre-determined class
class Warrior(Character):
    def __init__(self):
        super().__init__(
            name="Warrior",
            health=150,
            attack_power=20,
            special_move={"name": "Berserker Rage", "damage": 55}
        )


class Dark_Heart(Character):
    def __init__(self):
        super().__init__(
            name="Dark_Heart",
            health=160,
            attack_power=20,
            special_move={"name": "Darkness Grap", "damage": 65}
        )

class Gun_Messia(Character):
    def __init__(self):
        super().__init__(
            name="Gun_Messia",
            health=125,
            attack_power=25,
            special_move={"name": "Deus Ex Machina", "damage": 75}
        )

class Laid_Back_Vampire(Character):
    def __init__(self):
        super().__init__(
            name="Laid_Back_Vampire",
            health=200,
            attack_power=20,
            special_move={"name": "Last Horizon", "damage": 75}
        )

class Mechanical_Nightmare(Character):
    def __init__(self):
        super().__init__(
            name="Mechanical_Nightmare",
            health=175,
            attack_power=20,
            special_move={"name": "Error_2bf", "damage": 67}
        )

class Dragon_like_Warrior(Character):
    def __init__(self):
        super().__init__(
            name="Dragon_like_Warrior",
            health=195,
            attack_power=20,
            special_move={"name": "DRAGON INSTALL", "damage": 75}
        )

class Yoyo_slinging_bounty_hunter(Character):
    def __init__(self):
        super().__init__(
            name="Yoyo_slinging_bounty_hunter",
            health=175,
            attack_power=20,
            special_move={"name": "Attack of the killer machine", "damage": 75}
        )


# Game logic
def create_custom_character():
    name = input("Enter your character's name: ")
    while True:
        try:
            health = int(input("Enter your character's health (max 250): "))
            if 1 <= health <= 250:
                break
            else:
                print("Health must be between 1 and 250.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            attack_power = int(input("Enter your character's attack power (max 75): "))
            if 1 <= attack_power <= 75:
                break
            else:
                print("Attack power must be between 1 and 75.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"{name}'s special move is 'Random Power!'")
    return Character(
        name=name,
        health=health,
        attack_power=attack_power,
        special_move={"name": "Random Power!"}
    )

# Boss class
class DarkOverlord(Character):
    def __init__(self):
        super().__init__(
            name="Dark Overlord",
            health=300,
            attack_power=25,
            special_move={"name": "Abyssal Fury", "damage": 70}
        )
        self.attacks = {
            "Shadow Strike": 30,
            "Dark Flame": 40,
            "Soul Drain": 35,
            "Abyssal Blast": 50,
            "Doom Wave": 60
        }

    def random_attack(self, target):
        attack, damage = random.choice(list(self.attacks.items()))
        if target.shield_active:
            damage //= 2
            print(f"{self.name} uses {attack}! {target.name} shields, reducing damage to {damage}!")
            target.shield_active = False
        else:
            print(f"{self.name} uses {attack}! It deals {damage} damage!")
        target.health -= damage

def maybe_spawn_boss():
    if random.randint(1, 100) <= 50:  # 50% chance
        print("The Dark Overlord has appeared!")
        return DarkOverlord()
    return None


def choose_character():
    print("Choose your character:")
    print("1. Warrior")
    print("2. Dark_Heart")
    print("3. Gun_Messia")
    print("4. Laid_Back_Vampire")
    print("5. Mechanical_Nightmare")
    print("6. Dragon_like_Warrior")
    print("7.Yoyo_slinging_bounty_hunter")
    print("8. Create a Custom Character")

    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        return Warrior()
    elif choice == 2:
        return Dark_Heart()
    elif choice == 3:
        return Gun_Messia()
    elif choice == 4:
        return Laid_Back_Vampire()
    elif choice == 5:
        return Mechanical_Nightmare()
    elif choice == 6:
        return Dragon_like_Warrior()
    elif choice == 7:
        return Yoyo_slinging_bounty_hunter()
    elif choice == 8:
        return create_custom_character()
    else:
        print("Invalid choice. Please try again.")
        return choose_character()






def game ():
    Rematch = "YES!"
    print("Welcome to my wonderful Turn Based Fighting game!")
    player = choose_character()
    print(f"You have chosen the {player.name}!")

    while Rematch == "YES!":
        boss = maybe_spawn_boss()

        while boss and not boss.is_defeated() and not player.is_defeated():
            print(f"\n{player.name} Health: {player.health} | {boss.name} Health: {boss.health}")
            action = input("Choose your action (attack/shield/special): ").strip().lower()
                
            if action == "attack":
                    player.attack(boss)
            elif action == "shield":
                    player.shield()
            elif action == "special":
                    player.use_special_move(boss, all_characters=[player, boss])
            else:
                print("Invalid action. Try again.")
                continue

            if boss.is_defeated():
                print(f"You have defeated the {boss.name}!")
                break

            boss.random_attack(player)
            if player.is_defeated():
                print(f"You were defeated by the {boss.name}...")

        if not boss:
            print("You venture forth, but no boss appears. The journey continues!")
        Rematch = input("Would you like to Rematch?('YES! or NO!'): ")
    print("Thank you soo much for-a playing my game-a!")



#call ze man
if __name__ == "__main__":
    game()
