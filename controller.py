import time

class Controller:
    def __init__(self, game, player):
        self.game = game
        self.player = player

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
