import randomname
import random
from inventory import Inventory

races = [
    "Wood Elf", "High Elf", "Dark Elf", "Orc", "Redguard",
    "Breton", "Nord", "Imperial", "Khajiit", "Argonian"
]

gender = ["Male", "Female"]

class Enemy:
    def __init__(self):
        self.enemyName = ""
        self.enemyGender = ""
        self.enemyRace = ""
        self.enemyAge = 0
        self.enemyLevel = 0
        self.enemyGold = 0
        self.enemyHealth = 0
        self.enemyStamina = 0
        self.enemyMagicka = 0
        self.inv = Inventory

    def add_enemy(self):
        self.set_enemy_name()
        self.set_enemy_gender()
        self.set_enemy_race()
        self.set_enemy_age()
        self.set_enemy_level()
        self.add_enemy_inventory()
        self.set_enemy_health()
        self.set_enemy_stamina()
        self.set_enemy_magicka()

    def display_enemy_info(self):
        print("Name:", self.get_enemy_name())
        print("Gender:", self.get_enemy_gender())
        print("Race:", self.get_enemy_race())
        print("Age:", self.get_enemy_age())
        print("Health:", self.get_enemy_health())
        print("Stamina:", self.get_enemy_stamina())
        print("Magicka:", self.get_enemy_magicka())
        self.inv.display_inventory()
        print()

    def add_enemy_inventory(self):
        self.inv = Inventory()
        self.inv.get_inventory()
        return self.inv

    def set_enemy_name(self) -> str:
        self.enemyName = randomname.get_name()

    def get_enemy_name(self) -> str:
        return self.enemyName

    def set_enemy_race(self) -> str:
        self.enemyRace = random.choice(races)

    def get_enemy_race(self) -> str:
        return self.enemyRace

    def set_enemy_gender(self) -> str:
        self.enemyGender = random.choice(gender)

    def get_enemy_gender(self) -> str:
        return self.enemyGender

    def set_enemy_age(self) -> int:
        self.enemyAge = random.randint(18, 1000)

    def get_enemy_age(self) -> int:
        return self.enemyAge
    
    def set_enemy_level(self) -> int:
        self.enemyLevel = 0

    def get_enemy_level(self) -> int:
        return self.enemyLevel
    
    def set_enemy_health(self) -> int:
        self.enemyHealth = 100
    
    def get_enemy_health(self) -> int:
        return self.enemyHealth
    
    def set_enemy_stamina(self) -> int:
        self.enemyStamina = 100

    def get_enemy_stamina(self) -> int:
        return self.enemyStamina
    
    def set_enemy_magicka(self) -> int:
        self.enemyMagicka = 100

    def get_enemy_magicka(self) -> int:
        return self.enemyMagicka

    def set_enemy_gold(self) -> int:
        self.enemyGold = random.randint(10, 500)

    def get_enemy_gold(self) -> int:
        return self.enemyGold
