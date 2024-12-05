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

    def use_special_move(self, target):
        print(f"{self.name} uses {self.special_move['name']}!")
        if self.special_move.get("self_heal"):
            self.health += self.special_move["self_heal"]
            print(f"{self.name} heals for {self.special_move['self_heal']} health!")
        if self.special_move.get("damage"):
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


# Specific player classes
class Warrior(Character):
    def __init__(self):
        super().__init__(
            name="Warrior",
            health=150,
            attack_power=20,
            special_move={"name": "Berserker Rage", "damage": 50}
        )


class Mage(Character):
    def __init__(self):
        super().__init__(
            name="Mage",
            health=100,
            attack_power=25,
            special_move={"name": "Fireball", "damage": 60}
        )


class Rogue(Character):
    def __init__(self):
        super().__init__(
            name="Rogue",
            health=120,
            attack_power=30,
            special_move={"name": "Poison Strike", "damage": 40}
        )


class Paladin(Character):
    def __init__(self):
        super().__init__(
            name="Paladin",
            health=200,
            attack_power=15,
            special_move={"name": "Holy Light", "self_heal": 50}
        )


class Archer(Character):
    def __init__(self):
        super().__init__(
            name="Archer",
            health=110,
            attack_power=20,
            special_move={"name": "Piercing Arrow", "damage": 45}
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
            damage = damage // 2
            print(f"{self.name} uses {attack}! {target.name} shields, reducing damage to {damage}!")
            target.shield_active = False
        else:
            print(f"{self.name} uses {attack}! It deals {damage} damage!")
        target.health -= damage


# Game logic
def choose_class():
    classes = [Warrior(), Mage(), Rogue(), Paladin(), Archer()]
    print("Choose your class:")
    for i, cls in enumerate(classes):
        print(f"{i + 1}. {cls.name}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return classes[choice]


def maybe_spawn_boss():
    if random.randint(1, 100) <= 30:  # 30% chance
        print("The Dark Overlord has appeared!")
        return DarkOverlord()
    return None


def game():
    print("Welcome to the game!")
    player = choose_class()
    print(f"You have chosen the {player.name}!")
    
    boss = maybe_spawn_boss()

    while boss and not boss.is_defeated() and not player.is_defeated():
        print(f"\n{player.name} Health: {player.health} | {boss.name} Health: {boss.health}")
        action = input("Choose your action (attack/shield/special): ").strip().lower()
        
        if action == "attack":
            player.attack(boss)
        elif action == "shield":
            player.shield()
        elif action == "special":
            player.use_special_move(boss)
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


# Run the game
if __name__ == "__main__":
    game()
