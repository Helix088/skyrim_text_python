from inventory import Inventory

class Player:
    def __init__(self):
        self.playerName = ""
        self.playerGender = ""
        self.playerRace = ""
        self.playerAge = 0
        self.playerGold = 0
        self.playerLevel = 0
        self.playerXp = 0
        self.playerHealth = 0
        self.playerStamina = 0
        self.playerMagicka = 0
        self.inv = Inventory

    def menu(self):
        pass

    def add_player(self):
        self.set_name()
        self.set_gender()
        self.set_race()
        self.set_age()
        self.set_level()
        self.set_xp()
        self.set_health()
        self.set_stamina()
        self.set_magicka()
        print()
        self.add_inventory()

    def display_info(self):
        print("Name:", self.get_name())
        print("Gender:", self.get_gender())
        print("Race:", self.get_race())
        print("Age:", self.get_age())
        print("Level:", self.get_level())
        print("Health: ", self.get_)
        print("Stamina: ", self.get_)
        print("Magicka: ", self.get_)
        self.inv.display_inventory()
        print()

    def display_player_inventory(self):
        print("Name: ", self.get_name())
        print("Level: ", self.get_level())
        print("Gold: ", self.get_gold())
        self.inv.display_inventory()

    def add_inventory(self):
        self.inv = Inventory()
        self.inv.get_inventory()
        return self.inv

    def set_name(self):
        self.playerName = input("What is your character's name: ")

    def get_name(self) -> str:
        return self.playerName

    def set_race(self):
        race = input("What is your character's race you can choose: "
                     "\n(Wood Elf, High Elf, Dark Elf, Orc, Redguard, Breton, Nord, Imperial, Khajiit, or Argonian)\n")
        races = [
            "Wood Elf", "High Elf", "Dark Elf", "Orc", "Redguard",
            "Breton", "Nord", "Imperial", "Khajiit", "Argonian"
        ]
        while race not in races:
            race = input("What is your character's race you can choose: "
                         "\n(Wood Elf, High Elf, Dark Elf, Orc, Redguard, Breton, Nord, Imperial, Khajiit, or Argonian)\n")
        self.playerRace = race

    def get_race(self) -> str:
        return self.playerRace

    def set_gender(self):
        gender = input("Are you a male (type 'M') or female: (type 'F')\n")
        while gender not in ("M", "F"):
            gender = input("Are you a male (type 'M') or female: (type 'F')\n")
        self.playerGender = "Male" if gender == "M" else "Female"

    def get_gender(self) -> str:
        return self.playerGender

    def set_age(self):
        while True:
            try:
                age = int(input("What is your character's age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid age (an integer).")
        self.playerAge = age

    def get_age(self) -> int:
        return self.playerAge
    
    def set_level(self) -> int:
        self.playerLevel = 0

    def get_level(self) -> int:
        return self.playerLevel
    
    def set_xp(self) -> int:
        self.playerXp = 0

    def get_xp(self) -> int:
        return self.playerXp
    
    def set_health(self) -> int:
        self.playerHealth = 100

    def get_health(self) -> int:
        return self.playerHealth

    def set_stamina(self) -> int:
        self.playerStamina = 100

    def get_stamina(self) -> int:
        self.playerStamina

    def set_magicka(self) -> int:
        self.playerMagicka = 100

    def get_magicka(self) -> int:
        self.playerMagicka

    def get_gold(self) -> int:
        return self.playerGold

    def add_gold(self, gold) -> int:
        gold = input("You fold _ gold!")
        found_gold = bool
        gold += self.playerGold
        return self.playerGold

    def subtract_gold(self, gold) -> int:
        gold = input("How much gold would you like to spend?")
        gold -= self.playerGold
        return self.playerGold