import keyboard
import pygame

from game import Game

class Controls:
    def __init__(self):
        super().__init__()

    def controlFunc():
        escapePressed = False
        shiftPressed = False
        upPressed = False
        downPressed = False
        leftPressed = False
        rightPressed = False
        aPressed = False
        bPressed = False
        spacePressed = False
        count = 0

        clock = pygame.time.Clock()

        game = Game()

        while not escapePressed:
            if keyboard.is_pressed('up'):
                if not upPressed:
                    upPressed = True
                    game.walk_forward()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
                    count += 1
                    if count > 3:
                        game.enemy_appears()
            else:
                upPressed = False

            if keyboard.is_pressed('down'):
                if not downPressed:
                    downPressed = True
                    game.walk_backward()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                downPressed = False

            if keyboard.is_pressed('left'):
                if not leftPressed:
                    leftPressed = True
                    game.walk_left()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                leftPressed = False

            if keyboard.is_pressed('right'):
                if not rightPressed:
                    rightPressed = True
                    game.walk_right()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                rightPressed = False

            if keyboard.is_pressed('space'):
                if not spacePressed:
                    spacePressed = True
                    game.jump()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                spacePressed = False

            if keyboard.is_pressed('shift'):
                if not shiftPressed:
                    shiftPressed = True
                    game.menu()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                shiftPressed = False

            if keyboard.is_pressed('a'):
                if not aPressed:
                    aPressed = True
                    game.swing()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                aPressed = False

            if keyboard.is_pressed('b'):
                if not bButtonPressed:
                    bButtonPressed = True
                    game.block()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                bButtonPressed = False

            clock.tick(60)  # Limit the frame rate to 60 FPS
