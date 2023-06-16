from tkinter import Canvas
from game import Game
from player import Player
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import winsound
import time
import keyboard
import time
import os

player = Player()
game = Game()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        super().__init__()

        self.mouse_over = False

        default_image = create_surface_with_text(
            text, font_size, bg_rgb, text_rgb)

        highlighted_image = create_surface_with_text(
            text, font_size * 1.2, bg_rgb, text_rgb)

        self.images = [default_image, highlighted_image]
        self.rects = [default_image.get_rect(
            center=center_position), highlighted_image.get_rect(center=center_position)]

    @property
    def current_image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def current_rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        if self.current_rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.current_image, self.current_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
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
    
    while True:
        if keyboard.is_pressed('enter'):
            break

    winsound.PlaySound(None, winsound.SND_PURGE)
    # game.loading_screen()
    # game.intro()
    game.start()
    game.play()

    escapePressed = False
    shiftPressed = False
    upPressed = False
    downPressed = False
    leftPressed = False
    rightPressed = False
    aPressed = False
    bPressed = False
    spacePressed = False
    cv = Canvas()
    count = 0

    while not escapePressed:
        if keyboard.is_pressed('up'):
            if not upPressed:
                upPressed = True
                game.walk_forward()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
                count += 1
                if count > 3:
                    game.enemy_appears()
        else:
            upPressed = False

        if keyboard.is_pressed('down'):
            if not downPressed:
                downPressed = True
                game.walk_backward()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            downPressed = False

        if keyboard.is_pressed('left'):
            if not leftPressed:
                leftPressed = True
                game.walk_left()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            leftPressed = False

        if keyboard.is_pressed('right'):
            if not rightPressed:
                rightPressed = True
                game.walk_right()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            rightPressed = False

        if keyboard.is_pressed('space'):
            if not spacePressed:
                spacePressed = True
                game.jump()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            spacePressed = False

        if keyboard.is_pressed('shift'):
            if not shiftPressed:
                shiftPressed = True
                game.menu()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            shiftPressed = False

        if keyboard.is_pressed('a'):
            if not aPressed:
                aPressed = True
                game.swing()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            aPressed = False

        if keyboard.is_pressed('b'):
            if not bButtonPressed:
                bButtonPressed = True
                game.block()
                clock.tick(10)  # Delay of 100 milliseconds (10 frames at 60 FPS)
        else:
            bButtonPressed = False

        clock.tick(60)  # Limit the frame rate to 60 FPS

    winsound.PlaySound(None, winsound.SND_PURGE)

main()