import time
import os
import msvcrt
import winsound
import dialogue
import player
from dialogue import Dialogue
from player import Player


class Game:
    def __init__(self):
        self.dialogue = Dialogue()
        self.player = Player()

    def title_screen(self):
        print("This contains sound, please adjust your headset accordingly".center(90))
        os.system("CLS")
        winsound.PlaySound("8-bit-skyrim.wav",
                           winsound.SND_ASYNC | winsound.SND_LOOP)
        print("Bethesda Softworks".center(72))
        os.system("CLS")
        print("The Elder Scrolls V: Skyrim".center(76))
        os.system("CLS")
        print("Text Edition".center(67))
        os.system("CLS")
        print("Music By: Joe Jeremiah".center(74))

    def loading_screen(self):
        print("Helpful Tip: Did you know that if you need to breath, you should inhale.".center(100))
        print("Loading...".center(67))
        os.system("CLS")

    def intro(self):
        print("Bethesda Softworks".center(72))
        os.system("CLS")
        print("The Elder Scrolls V".center(73))
        os.system("CLS")
        print("Skyrim: Text Edition".center(74))
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

    def menu(self):
        choice = ''
        print("Menu:")
        print("0. Resume")
        print("1. Inventory")
        print("2. Controls")
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
