import time
import os
import msvcrt
import winsound
import pygame
import pygame.freetype
from dialogue import Dialogue
from player import Player
from enemies import Enemy
from ui import UIElement
from controls import Controls

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        self.dialogue = Dialogue()
        self.player = Player()
        self.enemies = Enemy()
        self.controls = Controls()

    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        uielement = UIElement(center_position=(
            600, 800), font_size=30.0, bg_rgb=BLACK, text_rgb=WHITE, text="Press 'Enter' to start a new game...")

        winsound.PlaySound("8-bit-skyrim.wav",
                        winsound.SND_ASYNC | winsound.SND_LOOP)

        running = True
        while running:
            screen.fill(BLACK)
            mouse_pos = pygame.mouse.get_pos()
            uielement.update(mouse_pos)
            uielement.draw(screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False

        winsound.PlaySound(None, winsound.SND_PURGE)

        pygame.quit()
        self.loading_screen()
        self.intro()
        self.start()
        self.play()
        self.controls.controlFunc()

        winsound.PlaySound(None, winsound.SND_PURGE)
        

    def intro(self):
        screen = pygame.display.set_mode((800, 600))
        uielement = UIElement(center_position=(
            200, 200), font_size=30, bg_rgb=WHITE, text_rgb=None, text="Music about to start, please turn down volume to accommodate")
        # print(
        #     "Music about to start, please turn down volume to accommodate".center(120))
        time.sleep(4.5)
        os.system("CLS")
        winsound.PlaySound("8-bit-skyrim.wav",
                           winsound.SND_ASYNC | winsound.SND_LOOP)
        # print("Bethesda Softworks".center(120))
        time.sleep(3.5)
        os.system("CLS")
        uielement = UIElement(center_position=(
            200, 200), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Bethesda Softworks")
        screen.fill(BLACK)
        # print("The Elder Scrolls V: Skyrim".center(120))
        uielement = UIElement(center_position=(
            300, 300), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="THE ELDER SCROLLS V: SKYRIM")
        screen.fill(BLACK)
        time.sleep(3.5)
        # print("Text Edition".center(120))
        uielement = UIElement(center_position=(
            400, 400), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="TEXT EDITION")
        screen.fill(BLACK)
        time.sleep(3.5)
        # print("Music By: Joe Jeremiah".center(120))
        uielement = UIElement(center_position=(
            500, 500), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Music By: Joe Jeremiah")
        screen.fill(BLACK)
        time.sleep(3.5)

        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press 'Enter' to start a new game...")
        pygame.display.flip()
        os.system("CLS")
        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)

    def loading_screen(self):
        os.system("CLS")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Helpful Tip: Did you know that if you need to breath, you should inhale.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Loading...")
        time.sleep(5)
        os.system("CLS")

    def start(self):
        self.dialogue.opening_scene()
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Once you press 'Enter' the dialogue will disappear.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press 'Enter' to continue...")
        while True:
            if msvcrt.getch() == b'\r':
                break
        os.system("CLS")
        self.player.add_player()
        self.player.display_info()

    def play(self):
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="What would you like to do?")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the UP ARROW key to walk.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the DOWN ARROW key to walk.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the LEFT ARROW key to walk.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the RIGHT ARROW key to walk.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the SPACEBAR to jump.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the LEFT MOUSE button to swing your weapon.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the RIGHT MOUSE button to block with your weapon.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the SHIFT key to open your inventory.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Press the ESC key to leave the game.")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="")
        

    def enemy_appears(self):
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="An enemy appears!")
        self.enemies.add_enemy()
        self.enemies.display_enemy_info()

    def enemy_killed(self):
        if(self.enemies.enemyHealth == 0):
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Enemy has been killed!")
            xp = self.player.set_xp()
            xp += 20
        return xp

    def level_up(self):
        if(self.player.playerXp == (self.player.playerLevel * 100)):
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Level up!")
            level = self.player.set_level()
            level += 1
        return level

    def enter_room(self):
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="You see a door!")
        enter_door = input(uielement=UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Will you open it? (Type Y or N)"))
        if (enter_door == "Y" or "y"):
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="You enter the room.")
            time(3)
            os.system("CLS")
            self.loading_screen()
        else:
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="You do not enter the room.")
    
    def exit_room(self):
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="You return to the door")
        exit_door = input(uielement=UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Would you like to exit? (Type Y or N)"))
        if (exit_door == "Y" or 'y'):
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="You exit the room.")
            time(3)
            os.system("CLS")
            self.loading_screen()
        else:
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="You do not exit the room.")

    def menu(self):
        choice = ''
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Menu:")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Type '0'. Resume")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Type '1'. Inventory")
        uielement = UIElement(center_position=(
            600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="Type '2'. Controls")
        while choice != '0':
            choice = input()
            uielement = UIElement(center_position=(
                600, 800), font_size=30, bg_rgb=BLACK, text_rgb=WHITE, text="")
            if choice == '1':
                self.player.display_player_inventory()
            elif choice == '2':
                self.play()

    