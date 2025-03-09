class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = "images/space-bg.jpeg"

        # Bullet settings
        self.bullet_speed_factor = 8
        self.bullet_width = 6
        self.bullet_height = 3
        self.bullet_color = (237, 213, 0)
