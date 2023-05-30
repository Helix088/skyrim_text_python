from game import Game
from player import Player
import winsound
import time
import keyboard

player = Player()
game = Game()

print("Press 'Enter' to start a new game...")
while True:
    if keyboard.is_pressed('enter'):
        break

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

while not escapePressed:
    if keyboard.is_pressed('esc'):
        escapePressed = True
    if keyboard.is_pressed('up'):
        if not upPressed:
            upPressed = True
            game.walk_forward()
            time.sleep(0.2)
    else:
        upPressed = False
    if keyboard.is_pressed('down'):
        if not downPressed:
            downPressed = True
            game.walk_backward()
            time.sleep(0.2)
    else:
        downPressed = False
    if keyboard.is_pressed('left'):
        if not leftPressed:
            leftPressed = True
            game.walk_left()
            time.sleep(0.2)
    else:
        leftPressed = False
    if keyboard.is_pressed('right'):
        if not rightPressed:
            rightPressed = True
            game.walk_right()
            time.sleep(0.2)
    else:
        rightPressed = False
    if keyboard.is_pressed('space'):
        if not spacePressed:
            spacePressed = True
            game.jump()
            time.sleep(0.2)
    else:
        spacePressed = False
    if keyboard.is_pressed('shift'):
        if not shiftPressed:
            shiftPressed = True
            game.menu()
            time.sleep(0.2)
    else:
        shiftPressed = False
    if keyboard.is_pressed('a'):
        if not aPressed:
            aPressed = True
            game.swing()
            time.sleep(0.2)
    else:
        aPressed = False
    if keyboard.is_pressed('b'):
        if not bButtonPressed:
            bButtonPressed = True
            game.block()
            time.sleep(0.2)
    else:
        bButtonPressed = False

winsound.PlaySound(None, winsound.SND_PURGE)
