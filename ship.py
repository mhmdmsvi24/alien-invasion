import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen

        # ship image
        self.image = pygame.image.load("images/space-ship-small.bmp")
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        bullet_rect = pygame.Rect(0, 0, 50, 50)
        pygame.draw.rect(screen, (255, 0, 0), bullet_rect)

        # ship position
        self.rect.centery = float(self.screen_rect.centery)
        self.rect.left = float(self.screen_rect.left)

        # ship speed
        self.movement_speed = 0

        # movments
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

        # attacking mechanism
        self.mag_size = 50

    def update(self):
        """Updates the ship position based on movement flags for continous movment"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.movement_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.movement_speed
        elif self.moving_top and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.movement_speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.movement_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class CargoShip(Ship):
    def __init__(self, screen):
        super().__init__(screen)
        self.movement_speed = 2.5
        self.image = pygame.image.load("images/space-ship-small.bmp")
