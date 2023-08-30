import pygame
import os
import time
import winsound
from pygame.sprite import Sprite


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.font.SysFont("Courier", font_size, bold=True)
    surface = font.render(text, True, text_rgb, bg_rgb)
    return surface


class UIElement(pygame.sprite.Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        super().__init__()

        self.mouse_over = False

        font_size = int(font_size)  # Convert font_size to an integer

        default_image = create_surface_with_text(
            text, font_size, bg_rgb, text_rgb)
        highlighted_image = create_surface_with_text(
            text, int(font_size * 1.2), bg_rgb, text_rgb)  # Convert the calculated size to an integer

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
