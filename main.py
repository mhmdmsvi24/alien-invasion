import pygame  # type: ignore
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import CargoShip


def run_game() -> None:
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = CargoShip(screen)
    bullets = Group()

    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
