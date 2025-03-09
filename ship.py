import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen

        # ship image
        self.image = pygame.image.load("images/space-ship-small.bmp")
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        # ship position
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # ship speed
        self.movement_speed = 5.0

        # movments
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False


    def update(self):
        """Updates the shop pos based on movement flags for continous movment"""
        if self.moving_right:
            self.rect.x += self.movement_speed
        elif self.moving_left:
            self.rect.x -= self.movement_speed
        elif self.moving_top:
            self.rect.y -= self.movement_speed
        elif self.moving_bottom:
            self.rect.y += self.movement_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class CargoShip(Ship):
    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load("images/space-ship-small.bmp")

