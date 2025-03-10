import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = "images/space-bg.jpeg"

        self.bg_image = pygame.image.load(self.bg_image)

        # scales bg image to fit window
        self.bg_image = pygame.transform.scale(
            self.bg_image, (self.screen_width, self.screen_height)
        )

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 8
        self.bullet_height = 3
        self.bullet_color = (237, 213, 0)
