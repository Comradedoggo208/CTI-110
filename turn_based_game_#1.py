import random

class Character:
    def __init__(self, name, health, attack, special):
        self.name = name
        self.health = health
        self.attack = attack
        self.special = special

    def perform_action(self, target):
        if self.health <= 0:
            print(f"{self.name} is out of health and can't perform actions!")
            return
        print(f"\n{self.name}'s turn!")
        print(f"1. Attack ({self.attack} damage)")
        print(f"2. Special: {self.special['description']}")
        choice = input("Choose an action (1 or 2): ")
        if choice == "1":
            self.basic_attack(target)
        elif choice == "2":
            self.special_action(target)
        else:
            print("Invalid choice. Turn skipped.")

    def basic_attack(self, target):
        if target.health <= 0:
            print(f"{target.name} is already defeated!")
            return
        target.health -= self.attack
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")

    def special_action(self, target):
        if target.health <= 0:
            print(f"{target.name} is already defeated!")
            return
        action = self.special["action"]
        action(self, target)

    def is_alive(self):
        return self.health > 0


class Boss(Character):
    def __init__(self, name, health, special_attacks):
        super().__init__(name, health, 0, None)
        self.special_attacks = special_attacks

    def perform_action(self, target):
        if self.health <= 0:
            print(f"{self.name} is defeated and can't act!")
            return
        print(f"\n{self.name}'s turn!")
        attack = random.choice(self.special_attacks)
        attack["action"](self, target)


def heal(self, target):
    heal_amount = 15
    self.health += heal_amount
    print(f"{self.name} heals for {heal_amount} health!")


def strong_attack(self, target):
    damage = 25
    target.health -= damage
    print(f"{self.name} performs a strong attack on {target.name} for {damage} damage!")


def shield(self, target):
    shield_amount = 10
    self.health += shield_amount
    print(f"{self.name} raises a shield, gaining {shield_amount} health!")


def firestorm(self, target):
    damage = 30
    target.health -= damage
    print(f"{self.name} casts Firestorm on {target.name}, dealing {damage} damage!")


def lightning_bolt(self, target):
    damage = 20
    target.health -= damage
    print(f"{self.name} strikes {target.name} with Lightning Bolt, dealing {damage} damage!")


def earthquake(self, target):
    damage = 25
    target.health -= damage
    print(f"{self.name} shakes the ground with Earthquake, dealing {damage} damage!")


def dark_blast(self, target):
    damage = 35
    target.health -= damage
    print(f"{self.name} unleashes a Dark Blast on {target.name}, dealing {damage} damage!")


# Create characters
characters = [
    Character("Warrior", 100, 20, {"description": "Strong Attack (25 damage)", "action": strong_attack}),
    Character("Mage", 80, 15, {"description": "Heal self (15 health)", "action": heal}),
    Character("Archer", 90, 18, {"description": "Strong Attack (25 damage)", "action": strong_attack}),
    Character("Paladin", 110, 12, {"description": "Shield self (10 health)", "action": shield}),
    Character("Rogue", 85, 22, {"description": "Strong Attack (25 damage)", "action": strong_attack}),
]

boss = Boss("Dark Overlord", 200, [
    {"description": "Firestorm (30 damage)", "action": firestorm},
    {"description": "Lightning Bolt (20 damage)", "action": lightning_bolt},
    {"description": "Earthquake (25 damage)", "action": earthquake},
    {"description": "Dark Blast (35 damage)", "action": dark_blast},
])

# Game loop
player_character = None
while player_character is None:
    print("Choose your character:")
    for i, character in enumerate(characters):
        print(f"{i + 1}. {character.name} (Health: {character.health}, Attack: {character.attack})")
    choice = input("Enter the number of your choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(characters):
        player_character = characters[int(choice) - 1]
    else:
        print("Invalid choice. Try again.")

# Decide the enemy (random chance for the boss)
if random.choice([True, False]):
    enemy_character = boss
    print(f"\nA boss has appeared! You will fight against {enemy_character.name}!")
else:
    enemy_character = random.choice([c for c in characters if c != player_character])
    print(f"\nYou will fight against {enemy_character.name}!")

# Battle loop
while player_character.is_alive() and enemy_character.is_alive():
    player_character.perform_action(enemy_character)
    print(f"\nStatus Update: {player_character.name} (Health: {player_character.health}), {enemy_character.name} (Health: {enemy_character.health})")
    
    if not enemy_character.is_alive():
        print(f"{enemy_character.name} is defeated! You win!")
        break
    
    enemy_character.perform_action(player_character)
    print(f"\nStatus Update: {player_character.name} (Health: {player_character.health}), {enemy_character.name} (Health: {enemy_character.health})")
    
    if not player_character.is_alive():
        print(f"{player_character.name} is defeated! You lose!")
