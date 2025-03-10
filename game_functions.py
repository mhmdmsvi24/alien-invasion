import sys

import pygame

from bullet import Bullet


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


def clean_bullets(bullets, screen_rect):
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.right > screen_rect.right:
            bullets.remove(bullet)


def fire_bullets(ship, settings, screen, bullets, bullets_info):
    """Manages the number of bullets shot based on the ships available ammunation"""
    if ship.bullets_fired < ship.mag_size:
        ship.bullets_fired += 1
        print(ship.bullets_fired, ship.mag_size)
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

        bullets_left = ship.mag_size - ship.bullets_fired
        bullets_info.update(bullets_left)


def ship_mousedown(ship, settings, screen, bullets, bullets_info):
    fire_bullets(ship, settings, screen, bullets, bullets_info)


def check_events(settings, screen, ship, bullets, bullets_info):
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
            ship_mousedown(ship, settings, screen, bullets, bullets_info)


def update_screen(settings, screen, ship, bullets, bullets_info):
    """Everything that needs to be updated on each FPS"""
    screen.blit(settings.bg_image, (0, 0))

    # graphics
    ship.blitme()
    bullets_info.blitme()

    # Redraw all bullets infront of the ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()
