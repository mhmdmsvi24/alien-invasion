import pygame # type: ignore

from settings import Settings
from ship import CargoShip
import game_functions as gf


def run_game() -> None:
    pygame.init()

    setting = Settings()

    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = CargoShip(screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(setting, screen, ship)

if __name__ == "__main__":
    run_game()
