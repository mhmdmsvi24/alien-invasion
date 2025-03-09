import sys

import pygame

from bullet import Bullet
from graphics.bullet_rounds import BulletRounds


def ship_keydown(ship, event) -> None:
    if event.key == pygame.K_w:
        ship.moving_top = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_s:
        ship.moving_bottom = True
    elif event.key == pygame.K_d:
        ship.moving_right = True


def ship_keyup(ship):
    ship.moving_top = False
    ship.moving_left = False
    ship.moving_bottom = False
    ship.moving_right = False


def ship_mousedown(ship, settings, screen, bullets, bullet_graphic):
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)
    bullet_graphic.mag = ship.mag_size - len(bullets.sprites())


def check_events(settings, screen, ship, bullets, bullet_graphic):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Ship controls w,a,s,d
        elif event.type == pygame.KEYDOWN:
            ship_keydown(ship, event)
        elif event.type == pygame.KEYUP and event.key in [
            pygame.K_w,
            pygame.K_a,
            pygame.K_s,
            pygame.K_d,
        ]:
            ship_keyup(ship)
        # ship mouse events for attacks, etc
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ship_mousedown(ship, settings, screen, bullets, bullet_graphic)


# Every thing that need to be displayed
def update_screen(settings, screen, ship, bullets, bullet_graphic):
    bg_image = pygame.image.load(settings.bg_image)

    # scales bg image to fit window
    bg_image = pygame.transform.scale(
        bg_image, (settings.screen_width, settings.screen_height)
    )

    screen.blit(bg_image, (0, 0))

    # graphics
    ship.blitme()
    bullet_graphic.blitme()

    # Redraw all bullets infront of the ship
    for bullet in bullets.sprites():
        if len(bullets.sprites()) <= ship.mag_size:
            bullet.draw_bullet()
        else:
            print("Insuficient rounds")

    pygame.display.flip()
