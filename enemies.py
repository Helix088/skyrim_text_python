# import urllib.request
import random
from inventory import Inventory

# word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
# response = urllib.request.urlopen(word_url)
# long_txt = response.read().decode()
# words = long_txt.splitlines()
# upper_words = [word for word in words if word[0].isupper()]
# name_words = [word for word in upper_words if not word.isupper()]

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
        self.enemyGold = 0
        self.inv = Inventory

    def add_enemy(self):
        self.set_enemy_name()
        self.set_enemy_gender()
        self.set_enemy_race()
        self.set_enemy_age()
        self.add_enemy_inventory()

    def display_enemy_info(self):
        print("Name:", self.get_enemy_name())
        print("Gender:", self.get_enemy_gender())
        print("Race:", self.get_enemy_race())
        print("Age:", self.get_enemy_age())
        self.inv.display_enemy_inventory()
        print()

    def add_inventory(self):
        self.inv = Inventory()
        self.inv.get_inventory()
        return self.inv

    # def rand_name():
    #     rand_name = ' '.join(
    #         [name_words[random.randint(0, len(name_words)-1)] for i in range(2)])
    #     return rand_name

    def set_name(self):
        # for n in range(10):
        #     self.enemyName = self.rand_name()
        self.enemyName = "Bob"

    def get_name(self) -> str:
        return self.enemyName

    def set_race(self):
        self.enemyRace = random.choice(races)

    def get_race(self) -> str:
        return self.enemyRace

    def set_gender(self):
        self.enemyGender = random.choice(gender)

    def get_gender(self) -> str:
        return self.enemyGender

    def set_age(self):
        self.enemyAge = random.randint(18, 1000)

    def get_age(self) -> int:
        return self.enemyAge

    def set_gold(self) -> int:
        self.enemyGold = random.randint(10, 500)

    def get_gold(self) -> int:
        return self.enemyGold
