import collections
class Inventory:
    def __init__(self):
        self.weapons = []
        self.apparel = []
        self.potions = []
        self.scrolls = []
        self.food = []
        self.ingredients = []
        self.books = []
        self.keys = []
        self.miscellaneous = []

    def set_starting_inventory(self):
        self.weapons = []
        self.apparel = ["Prisoner Clothes", "Prisoner Shoes"]
        self.potions = ["Health Potion"]
        self.scrolls = []
        self.food = ["Apple", "Ale"]
        self.ingredients = []
        self.books = []
        self.keys = []
        self.miscellaneous = []

    def get_inventory(self):
        self.set_starting_inventory()

    def display_inventory(self):
        print("Inventory:")
        self.display_weapons()
        self.display_apparel()
        self.display_potions()
        self.display_scrolls()
        self.display_food()
        self.display_ingredients()
        self.display_books()
        self.display_keys()
        self.display_misc()
        print()

    def display_weapons(self):
        print("\tWeapons: ", end="")
        for i in self.weapons:
            print(i + ", ", end="")
        print()

    def display_apparel(self):
        print("\tApparel: ", end="")
        for i in self.apparel:
            print(i + ", ", end="")
        print()

    def display_potions(self):
        print("\tPotions: ", end="")
        for i in self.potions:
            print(i + ", ", end="")
        print()

    def display_scrolls(self):
        print("\tScrolls: ", end="")
        for i in self.scrolls:
            print(i + ", ", end="")
        print()

    def display_food(self):
        print("\tFood: ", end="")
        for i in self.food:
            print(i + ", ", end="")
        print()

    def display_ingredients(self):
        print("\tIngredients: ", end="")
        for i in self.ingredients:
            print(i + ", ", end="")
        print()

    def display_books(self):
        print("\tBooks: ", end="")
        for i in self.books:
            print(i + ", ", end="")
        print()

    def display_keys(self):
        print("\tKeys: ", end="")
        for i in self.keys:
            print(i + ", ", end="")
        print()

    def display_misc(self):
        print("\tMiscellaneous: ", end="")
        for i in self.miscellaneous:
            print(i + ", ", end="")
        print()