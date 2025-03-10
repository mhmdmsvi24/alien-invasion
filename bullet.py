import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """bullets class to manage ship attack system"""

    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

        self.x = float(self.rect.x)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Update bullet position on screen based on ship position"""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
