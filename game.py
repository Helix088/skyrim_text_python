import time
import os
import msvcrt
import winsound
import dialogue
import player
from dialogue import Dialogue
from player import Player
from enemies import Enemy


class Game:
    def __init__(self):
        self.dialogue = Dialogue()
        self.player = Player()
        self.enemies = Enemy()

    def title_screen(self):
        os.system("CLS")
        print("Music about to start, please turn down volume to accommodate".center(120))
        time.sleep(4.5)
        os.system("CLS")
        winsound.PlaySound("8-bit-skyrim.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
        print("Bethesda Softworks".center(120))
        time.sleep(3.5)
        os.system("CLS")
        print("The Elder Scrolls V: Skyrim".center(120))
        time.sleep(3.5)
        print("Text Edition".center(120))
        time.sleep(3.5)
        print("Music By: Joe Jeremiah".center(120))
        time.sleep(3.5)

    def loading_screen(self):
        os.system("CLS")
        print("Helpful Tip: Did you know that if you need to breath, you should inhale.".center(120))
        print("Loading...".center(120))
        time.sleep(5)
        os.system("CLS")

    def intro(self):
        print("Bethesda Softworks".center(120))
        time.sleep(3.5)
        os.system("CLS")
        print("The Elder Scrolls V".center(120))
        time.sleep(3.5)
        os.system("CLS")
        print("Skyrim: Text Edition".center(120))
        time.sleep(3.5)
        os.system("CLS")

    def start(self):
        # self.dialogue.opening_scene()
        print("Once you press 'Enter' the dialogue will disappear.")
        print("Press 'Enter' to continue...")
        while True:
            if msvcrt.getch() == b'\r':
                break
        os.system("CLS")
        self.player.add_player()
        self.player.display_info()

    def play(self):
        print("What would you like to do?")
        print("Press the UP ARROW key to walk.")
        print("Press the DOWN ARROW key to walk.")
        print("Press the LEFT ARROW key to walk.")
        print("Press the RIGHT ARROW key to walk.")
        print("Press the SPACEBAR to jump.")
        print("Press the LEFT MOUSE button to swing your weapon.")
        print("Press the RIGHT MOUSE button to block with your weapon.")
        print("Press the SHIFT key to open your inventory.")
        print("Press the ESC key to leave the game.")
        print()

    def enemy_appears(self):
        print("An enemy appears!")
        self.enemies.add_enemy()
        self.enemies.display_enemy_info()


    def enter_room(self):
        print("You see a door!")
        enter_door = input("Will you open it? (Type Y or N)")
        if (enter_door == "Y" or "y"):
            print("You enter the room.")
            time(3)
            os.system("CLS")
            self.loading_screen()
        else:
            print("You do not enter the room.")
    
    def exit_room(self):
        print("You return to the door")
        exit_door = input("Would you like to exit? (Type Y or N)")
        if (exit_door == "Y" or 'y'):
            print("You exit the room.")
            time(3)
            os.system("CLS")
            self.loading_screen()
        else:
            print("You do not exit the room.")

    def menu(self):
        choice = ''
        print("Menu:")
        print("Type '0'. Resume")
        print("Type '1'. Inventory")
        print("Type '2'. Controls")
        while choice != '0':
            choice = input()
            print()
            if choice == '1':
                self.player.display_player_inventory()
            elif choice == '2':
                self.play()

    def walk_forward(self):
        print("You walk forwards.")
        print()

    def walk_backward(self):
        print("You walk backwards.")
        print()

    def walk_left(self):
        print("You walk left.")
        print()

    def walk_right(self):
        print("You walk right.")
        print()

    def swing(self):
        print("You swing your weapon!")
        print()

    def block(self):
        print("You block with your weapon!")
        print()

    def jump(self):
        print("You jump!")
        print()
