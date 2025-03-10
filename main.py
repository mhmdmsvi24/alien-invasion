import pygame
from pygame.sprite import Group

import game_functions as gf
from bullet_info import BulletInfo
from settings import Settings
from ship import CargoShip


def run_game() -> None:
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    screen_rect = screen.get_rect()

    ship = CargoShip(screen)
    bullets = Group()

    bullets_info = BulletInfo(screen, ship.mag_size, ship.bullets_fired)

    while True:
        gf.check_events(settings, screen, ship, bullets, bullets_info)
        ship.update()
        bullets.update()
        gf.clean_bullets(bullets, screen_rect)
        gf.update_screen(settings, screen, ship, bullets, bullets_info)


if __name__ == "__main__":
    run_game()
