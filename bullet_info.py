import pygame


class BulletInfo:
    def __init__(self, screen, mag, bullets_fired):
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load("images/bullet.png"), (50, 50)
        )

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.left = self.screen_rect.left + 5
        self.rect.bottom = self.screen_rect.bottom - 5

        self.mag = mag
        self.bullets_fired = bullets_fired
        self.bullets_left = self.mag - self.bullets_fired

        self.font = pygame.font.Font(None, 30)
        self.text_color = (255, 255, 255)

        self.text_position = self.rect.right + 5
        self.text_y_position = self.rect.centery - 5

    def update(self, bullets_left):
        self.bullets_left = bullets_left

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        bullet_text = self.font.render(f"{self.bullets_left}", True, self.text_color)
        self.screen.blit(bullet_text, (self.text_position, self.text_y_position))
