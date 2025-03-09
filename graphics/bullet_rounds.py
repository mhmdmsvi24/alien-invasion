import pygame


class BulletRounds:
    def __init__(self, screen, mag):
        self.screen = screen
        self.images = [
            pygame.transform.scale(pygame.image.load("images/bullet.png"), (50, 50))
            for _ in range(3)
        ]

        # Creates 3 seperate images for 3 bullet icons representing number of bullets left
        self.rects = [image.get_rect() for image in self.images]
        self.screen_rect = screen.get_rect()

        # Position bullets in a row at the bottom-left of the screen
        spacing = -35  # Space between bullets
        start_x = self.screen_rect.left + 5  # Offset from the left
        start_y = self.screen_rect.bottom - 50  # Offset from the bottom

        # number of bullets left
        self.mag = mag

        for i, rect in enumerate(self.rects):
            rect.topleft = (start_x + i * (rect.width + spacing), start_y)

        # Font setup for text
        self.font = pygame.font.Font(None, 36)  # Default font, size 36
        self.text_color = (255, 255, 255)  # White color

        # Positioning the text near bullets
        self.text_position = (
            start_x + 3 * (self.rects[0].width + spacing) + 35,
            start_y + 15,
        )

    def blitme(self):
        # Blit each bullet at its rect position
        for image, rect in zip(self.images, self.rects):
            self.screen.blit(image, rect)
            # pygame.draw.rect(self.screen, (255, 0, 0), rect, 2)

        # Render and draw text
        bullet_text = self.font.render(f"{self.mag}", True, self.text_color)
        self.screen.blit(bullet_text, self.text_position)
