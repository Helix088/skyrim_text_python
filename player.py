from inventory import Inventory

class Player:
    def __init__(self):
        self.playerName = ""
        self.playerGender = ""
        self.playerRace = ""
        self.playerAge = 0
        self.playerGold = 0
        self.inv = Inventory

    def menu(self):
        pass

    def add_player(self):
        self.set_name()
        self.set_gender()
        self.set_race()
        self.set_age()
        print()
        self.add_inventory()

    def display_info(self):
        print("Name:", self.get_name())
        print("Gender:", self.get_gender())
        print("Race:", self.get_race())
        print("Age:", self.get_age())
        self.inv.display_inventory()
        print()

    def display_player_inventory(self):
        print("Name:", self.get_name())
        print("Gold:", self.get_gold())
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

    def get_gold(self) -> int:
        return self.playerGold

    def add_gold(self) -> int:
        return 0

    def subtract_gold(self) -> int:
        return 0

# class Player:
#     def __init__(self):
#         self.playerName = ""
#         self.playerGender = ""
#         self.playerRace = ""
#         self.playerAge = 0
#         self.playerGold = 0
#         self.inv = None

#     def __init__(self, playerName, playerGender, playerRace, playerAge, inv):
#         self.playerName = playerName
#         self.playerAge = playerAge
#         self.playerRace = playerRace
#         self.inv = inv

#     def menu(self):
#         pass

#     def add_player(self):
#         self.set_name()
#         self.set_gender()
#         self.set_race()
#         self.set_age()
#         print()
#         self.add_inventory()

#     def display_info(self):
#         print("Name: ", self.get_name())
#         print("Gender: ", self.get_gender())
#         print("Race: ", self.get_race())
#         print("Age: ", self.get_age())
#         self.inv.display_inventory()
#         print()

#     def display_player_inventory(self):
#         print("Name: ", self.get_name())
#         print("Gold: ", self.get_gold())
#         self.inv.display_inventory()

#     def add_inventory(self):
#         self.inv = Inventory()
#         self.inv.get_inventory()
#         return self.inv

#     def set_name(self):
#         print("What is your character's name: ")
#         self.playerName = input()
#         return self.playerName
    
#     def get_name(self):
#         return self.playerName
    
#     def set_race(self):
#         race = ""
#         print("What is your character's race you can choose: ")
#         print("(Wood Elf, High Elf, Dark Elf, Orc, Redguard, Breton, Nord, Imperial, Khajiit, or Argonian)")
#         input(race)
#         if (race == "Wood Elf"):
#             playerRace = "Wood Elf"
#         elif (race == "High Elf"):
#             playerRace = "High Elf"
#         elif (race == "Dark Elf"):
#             playerRace = "Dark Elf"
#         elif (race == "Orc"):
#             playerRace = "Orc"
#         elif (race == "Redguard"):
#             playerRace = "Redguard"
#         elif (race == "Breton"):
#             playerRace = "Breton"
#         elif (race == "Nord"):
#             playerRace = "Nord"
#         elif (race == "Imperial"):
#             playerRace = "Imperial"
#         elif (race == "Khajiit"):
#             playerRace = "Khajiit"
#         elif (race == "Argonian"):
#             playerRace = "Argonian"
#         else:
#             print("What is your character's race you can choose: ")
#             print("(Wood Elf, High Elf, Dark Elf, Orc, Redguard, Breton, Nord, Imperial, Khajiit, or Argonian)")
#             input(race)
#         return playerRace

#     def get_race(self):
#         return self.playerRace
    
#     def set_gender(self): 
#         gender = ""
#         print("Are you a male (type 'M') or female: (type 'F')")
#         input(gender)
#         if (gender == "M"): 
#             self.playerGender = "Male"
#         elif (gender == "F"): 
#             self.playerGender = "Female"
#         else: 
#             print("Are you a male (type 'M') or female: (type 'F')")
#             input(gender)
#         return self.playerGender
    


# def get_gender(self): 
#     return self.playerGender


# def set_age(self): 
#     print("What is your character's age: ")
#     input(self.playerAge)
    
#     return self.playerAge


# def get_age(self):

#     return self.playerAge


# def get_gold(self): 
#     return self.playerGold


# def add_gold():

#     return 0


# def subtract_gold():

#     return 0

