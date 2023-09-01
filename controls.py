import keyboard
import pygame

from controller import Controller

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

        controller = Controller()

        while not escapePressed:
            if keyboard.is_pressed('up'):
                if not upPressed:
                    upPressed = True
                    controller.walk_forward()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
                    count += 1
                    if count > 3:
                        controller.enemy_appears()
            else:
                upPressed = False

            if keyboard.is_pressed('down'):
                if not downPressed:
                    downPressed = True
                    controller.walk_backward()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                downPressed = False

            if keyboard.is_pressed('left'):
                if not leftPressed:
                    leftPressed = True
                    controller.walk_left()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                leftPressed = False

            if keyboard.is_pressed('right'):
                if not rightPressed:
                    rightPressed = True
                    controller.walk_right()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                rightPressed = False

            if keyboard.is_pressed('space'):
                if not spacePressed:
                    spacePressed = True
                    controller.jump()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                spacePressed = False

            if keyboard.is_pressed('shift'):
                if not shiftPressed:
                    shiftPressed = True
                    controller.menu()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                shiftPressed = False

            if keyboard.is_pressed('a'):
                if not aPressed:
                    aPressed = True
                    controller.swing()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                aPressed = False

            if keyboard.is_pressed('b'):
                if not bButtonPressed:
                    bButtonPressed = True
                    controller.block()
                    # Delay of 100 milliseconds (10 frames at 60 FPS)
                    clock.tick(10)
            else:
                bButtonPressed = False

            clock.tick(60)  # Limit the frame rate to 60 FPS
